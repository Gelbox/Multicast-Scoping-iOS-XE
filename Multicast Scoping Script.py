import paramiko

def configure_switch(switch_ip, username, password, commands):
    """Connect to a switch and apply the given configuration commands."""
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(switch_ip, username=username, password=password)

        # Open shell
        shell = ssh.invoke_shell()
        for command in commands:
            shell.send(command + '\n')
            shell.recv(1024)  # Receive output (optional)

        ssh.close()
        print(f"Configuration applied successfully on {switch_ip}")

    except Exception as e:
        print(f"Failed to configure {switch_ip}: {str(e)}")

# Gather user input
switch_a_ip = input("Enter the management IP for Switch A: ")
switch_b_ip = input("Enter the management IP for Switch B: ")
username = input("Enter the SSH username: ")
password = input("Enter the SSH password: ")

# Configuration commands for Switch A
commands_switch_a = [
    "configure terminal",
    "ip multicast-routing",
    "interface g1/0/1",
    "no switchport",
    "ip address 10.1.12.1 255.255.255.252",
    "no shutdown",
    "interface g1/0/2",
    "no switchport",
    "ip address 10.1.12.5 255.255.255.252",
    "no shutdown",
    "router eigrp 1",
    "network 10.1.12.0 0.0.0.3",
    "network 10.1.12.4 0.0.0.3",
    "interface loopback0",
    "ip address 192.168.1.1 255.255.255.255",
    "router eigrp 1",
    "network 192.168.1.0 0.0.0.0",
    "ip pim rp-address 192.168.1.1",
    "ip access-list extended ACL10",
    "deny ip any 239.192.0.0 0.3.255.255",
    "permit ip any 224.0.0.0 15.255.255.255",
    "interface g1/0/1",
    "ip pim sparse-mode",
    "ip multicast boundary ACL10",
    "exit",
    "end",
    "copy running-config startup-config"
]

# Configuration commands for Switch B
commands_switch_b = [
    "configure terminal",
    "ip multicast-routing",
    "interface g1/0/1",
    "no switchport",
    "ip address 10.1.12.2 255.255.255.252",
    "no shutdown",
    "interface g1/0/2",
    "no switchport",
    "ip address 10.1.12.6 255.255.255.252",
    "no shutdown",
    "router eigrp 1",
    "network 10.1.12.0 0.0.0.3",
    "network 10.1.12.4 0.0.0.3",
    "ip pim rp-address 192.168.1.1",
    "ip access-list extended ACL20",
    "permit ip any 239.135.0.0 0.0.255.255",
    "deny ip any 224.0.0.0 15.255.255.255",
    "interface g1/0/2",
    "ip pim sparse-mode",
    "ip multicast boundary ACL20",
    "exit",
    "end",
    "copy running-config startup-config"
]

# Apply configurations to both switches
configure_switch(switch_a_ip, username, password, commands_switch_a)
configure_switch(switch_b_ip, username, password, commands_switch_b)
