#!/bin/bash
# Add source Argument, this does expect the user to have already installed any and all Dependencies
# Check if "source" argument is provided
if [ "$1" = "source" ]; then
    echo "Installing a development release"
    
    # Prompt the user to enter the development release URL
    read -p "Enter the URL of the .zip asset for the development release: " release_url
    
    if [ -z "$release_url" ]; then
        echo "URL cannot be empty."
        exit 1
    fi
    
    # Download and install the specified release.zip using pipx
    pipx install "$release_url"
    
    echo "Installation complete."
    exit 0
fi

# add uninstall argument as we can now handle this aswell since pipx is the ONLY form of install we are using
# Check if "uninstall" argument is provided
if [ "$1" = "uninstall" ]; then
    echo "Uninstalling Streamdeck"
    
    # Uninstall Streamdeck using pipx
    pipx uninstall streamdeck-linux-gui
    
    echo "Uninstallation complete."
    exit 0
fi

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
    # Changed your Python3 install to use the package that SHOULD be available by default on CentOS
    sudo yum -y install openssl-devel bzip2-devel libffi-devel python3-pip
    # Leaving original in the event that someone who uses CentOS cannot install using this method
    # wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz
    # tar xvf Python-3.8.9.tgz
    # cd Python-3.8.9/
    # ./configure --enable-optimizations
    # sudo make altinstall

    # There should no longer be a need for this as the default python3 on my VM had pip3
    # Upgrade pip
    # python3.8 -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Commented in Favor of a unified Command through pipx kept in the venet someone who uses CentOS cannot install using this method
    # Install Stream Deck UI
    # python3.8 -m pip install streamdeck-linux-gui --user
    pip3 install pipx
    pipx install streamdeck-linux-gui

elif [ -f /etc/fedora-release ]; then
    # Installing on Fedora
    echo "Installing on Fedora"

    # Added pipx as this appears to be simply available on Fedora in my VM which will let us use this
    # Install hidapi
    sudo dnf install python3-pip python3-devel hidapi pipx

    # No Need to upgrade pip if we arent using pip
    # Upgrade pip
    # python -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger
    
    # Leaving original in the event that someone who uses Fedora cannot install using this method
    # Install Stream Deck UI
    # python -m pip install streamdeck-linux-gui --user
    pipx install streamdeck-linux-gui

elif [ -f /etc/os-release ] && grep -qi 'opensuse' /etc/os-release; then
    # Installing on openSUSE
    echo "Installing on openSUSE"

    # Install hidapi
    sudo zypper install libhidapi-libusb0 python312-devel kernel-devel python311-evdev python3-pipx
    # No Need to upgrade pip if we arent using pip
    # Upgrade pip
    # python3 -m pip install --upgrade pip

    # Configure access to Elgato devices
    sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules'
    sudo udevadm trigger

    # Leaving original in the event that someone who uses openSUSE cannot install using this method
    # Install Stream Deck UI
    # python3 -m pip install streamdeck-linux-gui --user
    pipx install streamdeck-linux-gui

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
    
    # Leaving original in the event that someone who uses a Debian Based OS cannot install using this method
    # Install Stream Deck UI
    # python3 -m pipx install streamdeck-linux-gui
    pipx install streamdeck-linux-gui

elif [ -f /etc/nixos/configuration.nix ]; then
    # Installing on NixOS
    echo "Installing on NixOS"

    # Install pipx
    nix-env -iA nixos.python38Packages.pipx

    # Add pipx binaries to PATH
    echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
    source ~/.bashrc

    # Configure access to Elgato devices
    echo '# /etc/nixos/udev/streamdeck.rules' | sudo tee /etc/nixos/udev/streamdeck.rules
    echo 'ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", TAG+="uaccess"' | sudo tee -a /etc/nixos/udev/streamdeck.rules

    # Include the udev rule in NixOS configuration
    echo 'services.udev.extraRules = [ "/etc/nixos/udev/streamdeck.rules" ]' | sudo tee -a /etc/nixos/configuration.nix

    # Apply NixOS configuration
    sudo nixos-rebuild switch

    # Install Streamdeck using pipx
    pipx install streamdeck-linux-gui

else
    echo "Unsupported distribution"
    exit 1
fi

echo "Installation complete."
