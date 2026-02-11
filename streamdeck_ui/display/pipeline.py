from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from PIL.Image import Image

from streamdeck_ui.display.filter import Filter


class Pipeline:
    def __init__(self) -> None:
        self.filters: List[Tuple[Filter, Optional[Image]]] = []
        self.first_run = True
        self.output_cache: Dict[int, Image] = {}

    def add(self, pipeline_filter: Filter) -> None:
        self.filters.append((pipeline_filter, None))
        self.first_run = True

    def execute(self, time: Fraction) -> Tuple[Optional[Image], int]:
        """
        Executes all the filter in the pipeline and returns the final image, or None if the pipeline did not yield any changes.
        """

        image: Optional[Image] = None
        is_modified = False
        pipeline_hash = 0

        # To avoid flake8 B023 (https://docs.python-guide.org/writing/gotchas/#late-binding-closures), we need to
        # capture the variable going into the lambda. However, as a result of that, we have a lambda that
        # technically takes an argument (with a default) that does not match the signature we declared
        # for the transform() method. There are likely other solutions to avoid the warning this produces,
        # like using functools.partial, but this needs to be investigated.

        for i, (current_filter, cached) in enumerate(self.filters):

            def _get_input(current_image=image, cached_image=cached) -> Image:
                source = current_image if current_image is not None else cached_image
                if source is None:
                    # Pipelines always start with EmptyFilter, but keep this defensive.
                    raise ValueError("No source image available in pipeline")
                return source.copy()

            def _get_output(output_hash: int, current_pipeline_hash=pipeline_hash) -> Optional[Image]:
                return self.output_cache.get(hash((output_hash, current_pipeline_hash)))

            (image, hashcode) = current_filter.transform(
                _get_input,
                _get_output,
                is_modified | self.first_run,
                time,
            )

            pipeline_hash = hash((hashcode, pipeline_hash))

            if not image:
                # Filter indicated that it did NOT change anything, pull up the last
                # cached value for the next step in the pipeline
                image = cached
            else:
                # The filter changed the image, cache it for future use
                # Update tuple with cached image
                self.filters[i] = (current_filter, image)
                is_modified = True

            # Store this image with pipeline hash if we haven't seen it.
            if pipeline_hash not in self.output_cache and image is not None:
                self.output_cache[pipeline_hash] = image

        if self.first_run:
            # Force an update the first time the pipeline runs
            is_modified = True
            self.first_run = False

        return (image if is_modified else None, pipeline_hash)

    def last_result(self) -> Optional[Image]:
        """
        Returns the last known output of the pipeline
        """
        if not self.filters:
            return None
        return self.filters[-1][1]
