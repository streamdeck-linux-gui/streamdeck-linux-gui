# Installing on Fedora

This has been tested on Fedora 36, 37.

## Install hidapi

```bash
sudo dnf install python3-pip python3-devel hidapi
```

## Upgrade pip

You need to upgrade pip, using pip. In my experience, old versions of pip may fail to properly install some of the required Python dependencies.

```bash
python -m pip install --upgrade pip
```

## Configure access to Elgato devices

The following will create a file called `/etc/udev/rules.d/70-streamdeck.rules` and add the following text to it: `SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", TAG+="uaccess"`. Creating this file adds a udev rule that provides your user with access to USB devices created by Elgato.

```bash
sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
sudo sh -c 'echo "KERNEL==\"uinput\", SUBSYSTEM==\"misc\", TAG+=\"uaccess\"" >> /etc/udev/rules.d/70-streamdeck.rules'
```

For the rule to take immediate effect, run the following command:

```bash
sudo udevadm trigger
```

If the software is having problems later to detect the Stream Deck, you can try unplugging/plugging it back in.

## Install Stream Deck UI

### From Pypi with pip

```bash
python -m pip install streamdeck-linux-gui --user
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
