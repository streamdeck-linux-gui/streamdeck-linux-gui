# Installing on Arch

This has been tested on:

* Arch with Plasma (July 2023)
* Arch with Cinnamon (October 2023)
* Arch with Gnome (Per every release, thanks to dhtseany)
* Arch with Sway ans wayland

## AUR 

On Arch Linux, its recommended installing from AUR repositorues. there are two AUR packages available:

1. `streamdeck-ui`: This package targets official and stable releases.
2. `streamdeck-ui-git`: This package targets the git repository's master branch. It provides you with the latest updates but may be unstable at times.

The AUR packages install all the necessary dependencies and udev rules, so you do not need to continue further in this document.

## Manual / source install

### Install Dependencies

```bash
sudo pacman -S hidapi qt6-base
```

### Set path

You need to add `~/.local/bin` to your path. Be sure to add this to your `.bashrc` (or equivalent) file, so it automatically sets it for you in the future.

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

### Install Streamdeck

#### From Pypi with pipx

```bash
sudo pacman -S python-pipx
```

```console
pipx install  streamdeck-linux-gui
```

#### From Source

Please make sure you have followed [Install dependencies](#install-dependencies) and [Configure access to Elgato devices](#configure-access-to-elgato-devices) before continuing.

The steps to install from source can be found [here](source.md)


## Launch the Streamdeck UI

Launch with

```bash
streamdeck
```

See [troubleshooting](../troubleshooting.md) for tips if you're stuck.
