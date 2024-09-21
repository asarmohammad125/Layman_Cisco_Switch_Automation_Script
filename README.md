# Layman_Cisco_Switch_Automation_Script
This Python script automates basic switch configuration tasks on Cisco switches using the Netmiko library. It allows a user to manage VLANs, configure interfaces, assign IP addresses, set static routes, and test network connectivity directly from the command line interface. 
# Cisco Switch Automation Script

This Python script provides an easy-to-use command-line interface to automate common tasks on Cisco switches. The script uses the Netmiko library to connect to the switch via SSH and execute various network configuration commands.

## Features

- **Show VLANs**: Display a list of VLANs configured on the switch.
- **Create VLANs**: Add new VLANs to the switch.
- **Delete VLANs**: Remove existing VLANs from the switch.
- **Rename VLANs**: Rename an existing VLAN.
- **Assign IP Address to VLAN Interface**: Assign an IP address and subnet mask to a specific VLAN interface.
- **Show IP Assigned Interfaces**: Display all interfaces with assigned IP addresses.
- **Assign Default Gateway**: Set a default gateway for the switch.
- **Assign Static Route**: Configure a static route on the switch.
- **Ping Test**: Test network connectivity to a specified IP address.
- **Show Switch Version**: Display the switch's software version.
- **Check VLAN Status**: Check if a VLAN interface is up or down.

## Requirements

- Python 3.x
- Netmiko library (`pip install netmiko`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/asarmohammad125/Layman_Cisco_Switch_Automation_Script
    ```

2. Install the required Python libraries:
    ```bash
    pip install netmiko
    ```

3. Run the script:
    ```bash
    python switch_automation.py
    ```

## Usage

When you run the script, it will prompt for the following inputs:
- **Username**: Your SSH username for the Cisco switch.
- **Password**: Your SSH password.
- **Switch IP Address**: The IP address of the Cisco switch you want to connect to.

Once connected, the script presents a menu of operations you can perform:

```plaintext
What do you want to do:
 1 - Show VLANs
 2 - Create VLANs
 3 - Delete VLANs
 4 - Rename VLANs
 5 - Assign IP Address to VLAN interface
 6 - Show IP assigned interfaces
 7 - Assign default-gateway
 8 - Assign Static route
 9 - Test Ping
 10 - Show Switch Version
 11 - Check if VLAN is up or down
