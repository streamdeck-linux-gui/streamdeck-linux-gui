from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QSizePolicy, QFormLayout, QComboBox, QHBoxLayout, \
    QRadioButton, QSlider, QVBoxLayout

from streamdeck_ui.plugins import Plugin


class DemoPlugin(Plugin):
    toggled = False

    def __init__(self, serial_number: str, page_id: int, button_id: int):
        super().__init__(serial_number, page_id, button_id)

    def create_ui(self, plugin_form: QWidget):
        # Creates a vertical layout for the plugin_form so that everything stretches nicely
        verticalLayout = QVBoxLayout(plugin_form)
        VolumeControl = QWidget(plugin_form)
        # Adds the volume control to said layout
        verticalLayout.addWidget(VolumeControl)
        VolumeControl.setObjectName(u"VolumeControl")
        VolumeControl.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VolumeControl.sizePolicy().hasHeightForWidth())
        VolumeControl.setSizePolicy(sizePolicy)
        VolumeControl.setMinimumSize(QSize(0, 0))
        self.formLayout = QFormLayout(VolumeControl)
        self.formLayout.setObjectName(u"formLayout")
        self.device_select = QComboBox(VolumeControl)
        self.device_select.setObjectName(u"device_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.device_select.sizePolicy().hasHeightForWidth())
        self.device_select.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.device_select)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.volume_type_set = QRadioButton(VolumeControl)
        self.volume_type_set.setObjectName(u"volume_type_set")
        sizePolicy1.setHeightForWidth(self.volume_type_set.sizePolicy().hasHeightForWidth())
        self.volume_type_set.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.volume_type_set)

        self.volume_type_adjust = QRadioButton(VolumeControl)
        self.volume_type_adjust.setObjectName(u"volume_type_adjust")
        sizePolicy1.setHeightForWidth(self.volume_type_adjust.sizePolicy().hasHeightForWidth())
        self.volume_type_adjust.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.volume_type_adjust)

        self.volume_type_mute = QRadioButton(VolumeControl)
        self.volume_type_mute.setObjectName(u"volume_type_mute")
        sizePolicy1.setHeightForWidth(self.volume_type_mute.sizePolicy().hasHeightForWidth())
        self.volume_type_mute.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.volume_type_mute)

        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_type = QLabel(VolumeControl)
        self.label_type.setObjectName(u"label_type")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_type.sizePolicy().hasHeightForWidth())
        self.label_type.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_type)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_min_val = QLabel(VolumeControl)
        self.label_min_val.setObjectName(u"label_min_val")
        self.label_min_val.setVisible(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_min_val.sizePolicy().hasHeightForWidth())
        self.label_min_val.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_min_val)

        self.volume_slider = QSlider(VolumeControl)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setVisible(False)

        self.horizontalLayout_2.addWidget(self.volume_slider)

        self.label_max_val = QLabel(VolumeControl)
        self.label_max_val.setObjectName(u"label_max_val")
        self.label_max_val.setVisible(False)
        sizePolicy3.setHeightForWidth(self.label_max_val.sizePolicy().hasHeightForWidth())
        self.label_max_val.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_max_val)

        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_volume = QLabel(VolumeControl)
        self.label_volume.setObjectName(u"label_volume")
        self.label_volume.setVisible(False)
        sizePolicy2.setHeightForWidth(self.label_volume.sizePolicy().hasHeightForWidth())
        self.label_volume.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_volume)

        # Retranslate UI
        self.device_select.setPlaceholderText(QCoreApplication.translate("VolumeControl", u"Select Device", None))
        self.volume_type_set.setText(QCoreApplication.translate("VolumeControl", u"Set", None))
        self.volume_type_adjust.setText(QCoreApplication.translate("VolumeControl", u"Adjust", None))
        self.volume_type_mute.setText(QCoreApplication.translate("VolumeControl", u"Mute", None))
        self.label_type.setText(QCoreApplication.translate("VolumeControl", u"Type", None))
        self.label_min_val.setText(QCoreApplication.translate("VolumeControl", u"min", None))
        self.label_max_val.setText(QCoreApplication.translate("VolumeControl", u"max", None))
        self.label_volume.setText(QCoreApplication.translate("VolumeControl", u"Volume", None))
        self.volume_slider.setToolTip(QCoreApplication.translate("VolumeControl", u"Current Volume", None))

        # Connect Value Changes
        self.volume_type_set.toggled.connect(self.type_set_clicked)
        self.volume_type_adjust.toggled.connect(self.type_adjust_clicked)
        self.volume_type_mute.toggled.connect(self.type_mute_clicked)
        self.volume_slider.valueChanged.connect(self.volume_slider_value_change)

        self.populate_device_select()

    def type_set_clicked(self, checked):
        if checked:
            self.label_volume.setVisible(True)
            self.label_volume.setText("Volume:")
            self.label_min_val.setVisible(True)
            self.label_min_val.setText("0")
            self.label_max_val.setVisible(True)
            self.label_max_val.setText("100")
            self.volume_slider.setVisible(True)
            self.volume_slider.setMinimum(0)
            self.volume_slider.setMaximum(100)
            self.volume_slider.setValue(50)

    def type_adjust_clicked(self, checked):
        if checked:
            self.label_volume.setVisible(True)
            self.label_volume.setText("Step Size:")
            self.label_min_val.setVisible(True)
            self.label_min_val.setText("-50")
            self.label_max_val.setVisible(True)
            self.label_max_val.setText("+50")
            self.volume_slider.setVisible(True)
            self.volume_slider.setMinimum(-50)
            self.volume_slider.setMaximum(50)
            self.volume_slider.setValue(0)

    def type_mute_clicked(self, checked):
        if checked:
            self.label_volume.setVisible(False)
            self.label_min_val.setVisible(False)
            self.label_max_val.setVisible(False)
            self.volume_slider.setVisible(False)

    def volume_slider_value_change(self, value):
        self.volume_slider.setToolTip(QCoreApplication.translate("VolumeControl", u""+str(value), None))

    def populate_device_select(self):
        self.device_select.addItem("DEMO DEVICE")
        pass

    def handle_keypress(self, serial_number: str, page: int, button: int):
        if self.toggled:
            self.button_change_icon(serial_number, page, button, "")
        else:
            self.button_change_icon(serial_number, page, button, "/home/gapls/Pictures/2024-01-31_17-39.png")
        self.toggled = not self.toggled

    def handle_change_button_state(self, serial_number: str, page: int, button: int, state: int):
        pass

    @staticmethod
    def initialize_plugin(serial_number: str, page_id: int, button_id: int):
        return DemoPlugin(serial_number, page_id, button_id)