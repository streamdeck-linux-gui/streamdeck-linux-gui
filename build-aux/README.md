# Build Flatpak
All commands assume run from this directory, prepend pathing as needed for building from other locations

## Install qt requirements
```
flatpak install --user org.kde.Sdk//5.15-23.08
flatpak install --user org.kde.Platform//5.15-23.08
```
This selects the qt version to base the flatpak off of; as of writing, 5.15 was the latest attached to a known flatpak runtime version (23.08 - see freedesktop for current 'stable' version). For more options, just run the above command without '//5.15-23.08' and and select something else. 

## To Build:
```
flatpak-builder --force-clean build-dir com.streamdeck.linux-gui.json
```

## Run testing:
```
flatpak-builder --run build-dir com.streamdeck.linux-gui.json streamdeck
```

## Build for deployment:
Provides a directory that can be added as a repository (be aware of path)
```
flatpak-builder --repo=repo --force-clean build-dir com.streamdeck.linux-gui.json
```

## Add personal repo
```
flatpak --user remote-add --no-gpg-verify personal repo
```
To delete
```
flatpak --user remote-delete personal
```
Then you can delete the folder that was created (should be called whatever the last argument is in the add command)

## Install from personal repo
```
flatpak --user install personal com.streamdeck.linux-gui
```

## Run installed flatpak
```
flatpak run com.streamdeck.linux-gui
```
To uninstall
```
flatpak uninstall com.streamdeck.linux-gui
```

