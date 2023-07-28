# Installing on Debian
This has been tested on Debian 12 Bookwork

May work for ubuntu and others, not tested yet.

## Install hidapi
``` console
sudo apt install libhidapi-libusb0
```

## Set path
You need to add `~/.local/bin` to your path. Be sure to add this to your `.bashrc` (or equivalent) file so it automatically sets it for you in future.
``` console
PATH=$PATH:$HOME/.local/bin
```

## Configure access to Elgato devices
The following will create a file called `/etc/udev/rules.d/70-streamdeck.rules` and add the following text to it: `SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", TAG+="uaccess"`. Creating this file adds a udev rule that provides your user with access to USB devices created by Elgato.
``` bash
sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
```
For the rule to take immediate effect, run the following command:
``` bash
sudo udevadm trigger
```
If the software is having problems later to detect the Stream Deck, you can try unplugging/plugging it back in.

## Install poetry python virtual environment
```
curl -sSL https://install.python-poetry.org | python3 -
```
## Install Git
```
sudo apt install git
```

## Install Stream Deck Linux UI
Make a directory for the files to be kept in.
```
mkdir streamdeck-linux
```
Pull from github
```
git clone https://github.com/streamdeck-linux-gui/streamdeck-linux-gui.git
```
Enter folder pulled from github
```
cd streamdeck-linux-gui
```
Run Install
```
poetry install
```

Launch with
```
poetry run streamdeck
```
## Known error
Will give error - Due to Debian 12 not having gnome system tray notifications
```
qt.core.qobject.connect: QObject::connect: No such signal QPlatformNativeInterface::systemTrayWindowChanged(QScreen*)
```

See [troubleshooting](../troubleshooting.md) for tips if you're stuck.
