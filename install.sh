#!/bin/bash

# ZENOX Framework v2.0 - Installation Script
# Automated installation for Kali Linux and Debian-based systems

echo "
███████╗███████╗███╗   ██╗ ██████╗ ██╗  ██╗
╚══███╔╝██╔════╝████╗  ██║██╔═══██╗╚██╗██╔╝
  ███╔╝ █████╗  ██╔██╗ ██║██║   ██║ ╚███╔╝ 
 ███╔╝  ██╔══╝  ██║╚██╗██║██║   ██║ ██╔██╗ 
███████╗███████╗██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝

ZENOX Framework v2.0 - Installation Script
"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Functions
print_status() {
    echo -e "${CYAN}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   print_error "This script should not be run as root for security reasons."
   exit 1
fi

# Check OS
print_status "Checking operating system..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    print_success "Linux detected"
else
    print_warning "This script is designed for Linux systems"
fi

# Check Python 3
print_status "Checking Python 3 installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_success "Python 3 found: $PYTHON_VERSION"
else
    print_error "Python 3 not found. Please install Python 3.x"
    exit 1
fi

# Check pip3
print_status "Checking pip3 installation..."
if command -v pip3 &> /dev/null; then
    print_success "pip3 found"
else
    print_error "pip3 not found. Installing pip3..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Check nmap
print_status "Checking nmap installation..."
if command -v nmap &> /dev/null; then
    print_success "nmap found"
else
    print_warning "nmap not found. Installing nmap..."
    sudo apt update && sudo apt install -y nmap
fi

# Install Python dependencies
print_status "Installing Python dependencies..."
if pip3 install -r requirements.txt; then
    print_success "Python dependencies installed successfully"
else
    print_error "Failed to install Python dependencies"
    exit 1
fi

# Make main.py executable
print_status "Setting executable permissions..."
chmod +x main.py
print_success "Permissions set"

# Create symbolic link (optional)
read -p "Do you want to create a system-wide command 'zenox'? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    ZENOX_PATH=$(pwd)/main.py
    sudo ln -sf "$ZENOX_PATH" /usr/local/bin/zenox
    print_success "System command 'zenox' created. You can now run 'zenox' from anywhere."
fi

# Installation complete
print_success "ZENOX Framework v2.0 installation completed!"
echo
print_status "To run ZENOX Framework:"
echo "  1. Navigate to this directory: cd $(pwd)"
echo "  2. Run: python3 main.py"
if [[ -L /usr/local/bin/zenox ]]; then
    echo "  3. Or simply run: zenox (from anywhere)"
fi
echo
print_warning "Remember to use ZENOX Framework only on authorized networks!"
print_warning "Respect local cybersecurity laws and regulations."
echo

