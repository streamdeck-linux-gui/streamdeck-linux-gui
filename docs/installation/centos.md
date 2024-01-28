# Installing on CentOS

This has been tested on CentOS 7, 8.

## Install hidapi

```bash
sudo yum install epel-release
sudo yum update
sudo yum install hidapi
```

> ### Note for CentOS7
>
> If you're having trouble installing hdapi, try installing the epel from the Fedora site as follows:

```bash
sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

> and try the hdapi install again.

## Install python 3.8

CentOS 7/8 ships with Python 3.6. We need to build version 3.8 (or later if you prefer).

```bash
sudo yum -y groupinstall "Development Tools"
sudo yum -y install openssl-devel bzip2-devel libffi-devel
wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz
tar xvf Python-3.8.9.tgz
cd Python-3.8.9/
./configure --enable-optimizations
sudo make altinstall
```

## Upgrade pip

You need to upgrade pip, using pip. In my experience, old versions of pip may fail to properly install some of the required Python dependencies.

```bash
python3.8 -m pip install --upgrade pip
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
python3.8 -m pip install streamdeck-linux-gui --user
```

### From Source

Please make sure you have followed the steps below untill the **Install Stream Deck UI section** before continuing.

The steps to install from source can be found [here](source.md)

### Launch the Streamdeck UI

```bash
streamdeck
```

See [troubleshooting](../troubleshooting.md) for tips if you're stuck.
