# Installing on openSUSE

This has been tested on Tumbleweed.

## Install hidapi

```bash
sudo zypper install libhidapi-libusb0 python312-devel kernel-devel python311-evdev
```

> `python310-devel` and `kernel-devel` are required because pip is going to have to build `evdev`.

## Upgrade pip

You may need to upgrade pip, using pip.

```bash
python3 -m pip install --upgrade pip
```

### Configure access to Elgato devices (udev rules)

The following will create a file called `/etc/udev/rules.d/60-streamdeck.rules` with all the necessary udev rules that provides your user with access to USB devices created by Elgato.

```bash
sudo wget https://raw.githubusercontent.com/streamdeck-linux-gui/streamdeck-linux-gui/main/udev/60-streamdeck.rules -O /etc/udev/rules.d/60-streamdeck.rules
```

alternatively to grabbing the file directly from the repository you can use the following command:

```bash
sh -c "echo -e 'SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", ATTRS{idProduct}==\"0060\", TAG+=\"uaccess\"\\n'\
'SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", ATTRS{idProduct}==\"0063\", TAG+=\"uaccess\"\\n'\
'SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", ATTRS{idProduct}==\"006c\", TAG+=\"uaccess\"\\n'\
'SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", ATTRS{idProduct}==\"006d\", TAG+=\"uaccess\"\\n'\
'SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", ATTRS{idProduct}==\"0080\", TAG+=\"uaccess\"\\n'\
'KERNEL==\"uinput\", SUBSYSTEM==\"misc\", OPTIONS+=\"static_node=uinput\", TAG+=\"uaccess\", GROUP=\"input\", MODE=\"0660\"' > /etc/udev/rules.d/60-streamdeck.rules"
```

For the rule to take immediate effect, run the following command:

```bash
sudo udevadm trigger
```

If the software is having problems later to detect the Stream Deck, you can try unplugging/plugging it back in.

## Install Stream Deck UI

### From Pypi with pip

```bash
python3 -m pip install streamdeck-linux-gui --user
```

### From Source

Please make sure you have followed the steps below untill the **Install Stream Deck UI section** before continuing.

The steps to install from source can be found [here](source.md)

### Launch the Streamdeck UI

Launch with

```bash
streamdeck
```

See [system tray](../troubleshooting.md#no-system-tray-indicator) installation.

See [troubleshooting](../troubleshooting.md) for tips if you're stuck.
