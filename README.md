# Multicast-Scoping-iOS-XE

This Python script automates the configuration of Cisco IOS XE switches for multicast routing, including administrative scoping. It connects to the switches via SSH, applies configurations for PIM Sparse Mode, EIGRP, ACLs, and RP settings, and validates the setup.

Features

Configures multicast routing (ip multicast-routing).

Sets up interfaces with IP addresses and unicast/multicast settings.

Enables PIM Sparse Mode on specified interfaces.

Configures a single RP for multicast.

Defines and applies ACLs for administrative scoping.

Saves the running configuration to startup configuration.

Requirements

Python 3.6 or higher.

paramiko library for SSH connections.

Cisco IOS XE devices with SSH access.

Installation

Clone this repository
Install the required Python library
Run the script

Provide the following inputs when prompted:

Management IP of Switch A.

Management IP of Switch B.

SSH username.

SSH password.

The script will:

Connect to each switch.

Apply the configuration commands from the answer sheet.

Save the configurations.

Script Details

Switch A Configuration

Configures interfaces g1/0/1 and g1/0/2.

Sets up EIGRP AS 1 with wildcard masks.

Enables PIM Sparse Mode and sets the RP.

Creates and applies ACL10 for administrative scoping.

Switch B Configuration

Configures interfaces g1/0/1 and g1/0/2.

Sets up EIGRP AS 1 with wildcard masks.

Enables PIM Sparse Mode.

Creates and applies ACL20 for administrative scoping.

Informs of the RP set on Switch A.
Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or fixes.
