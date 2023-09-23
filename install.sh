#!/bin/bash

# Check the distribution and version
if [ -f /etc/arch-release ]; then
    # Installing on Arch Linux
    echo "Installing on Arch Linux"

    # Install Dependencies
    sudo pacman -S hidapi qt6-base

    # Set path
    echo 'PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Install Streamdeck
    sudo pacman -S python-pipx
    pipx install streamdeck-linux-gui

elif [ -f /etc/centos-release ]; then
    # Installing on CentOS
    echo "Installing on CentOS"

    # Install hidapi
    sudo yum install epel-release
    sudo yum update
    sudo yum install hidapi

    # Install Python 3.8
    sudo yum -y groupinstall "Development Tools"
    sudo yum -y install openssl-devel bzip2-devel libffi-devel
    wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz
    tar xvf Python-3.8.9.tgz
    cd Python-3.8.9/
    ./configure --enable-optimizations
    sudo make altinstall

    # Upgrade pip
    python3.8 -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Install Stream Deck UI
    python3.8 -m pip install streamdeck-linux-gui --user

elif [ -f /etc/fedora-release ]; then
    # Installing on Fedora
    echo "Installing on Fedora"

    # Install hidapi
    sudo dnf install python3-pip python3-devel hidapi

    # Upgrade pip
    python -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Install Stream Deck UI
    python -m pip install streamdeck-linux-gui --user

elif [ -f /etc/os-release ] && grep -qi 'opensuse' /etc/os-release; then
    # Installing on openSUSE
    echo "Installing on openSUSE"

    # Install hidapi
    sudo zypper install libhidapi-libusb0 python312-devel kernel-devel python311-evdev

    # Upgrade pip
    python3 -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Install Stream Deck UI
    python3 -m pip install streamdeck-linux-gui --user

elif [ -f /etc/debian_version ]; then
    # Installing on Debian or Ubuntu derivatives
    echo "Installing on Debian or Ubuntu derivatives"

    # Install hidapi and pipx
    sudo apt install libhidapi-libusb0 pipx

    # Set path
    echo 'PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Install Stream Deck UI
    python3 -m pipx install streamdeck-linux-gui

else
    echo "Unsupported distribution"
    exit 1
fi

echo "Installation complete."
