# Installing on Debian and ubuntu derivatives

This has been tested on Debian 12

## Install hidapi and pipx

```bash
sudo apt install libhidapi-libusb0 pipx
```

> Note that for version `2.0.6` and below, you also need to install `libxcb-xinerama0` (include it with apt in the line above).

## Set path

You need to add `~/.local/bin` to your path. Be sure to add this to your `.bashrc` (or equivalent) file so it automatically sets it for you in future.

```ini
PATH=$PATH:$HOME/.local/bin
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

### From Pypi with pipx

```bash
python3 -m pipx install streamdeck-linux-gui
```

### From Source

Please make sure you have followed the steps below untill the **Install Stream Deck UI section** before continuing.

The steps to install from source can be found [here](source.md)

### Launch the Streamdeck UI

Launch with

```bash
streamdeck
```

See [troubleshooting](../troubleshooting.md) for tips if you're stuck.
