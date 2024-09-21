from netmiko import ConnectHandler
user = input("Enter the Username: ")
passwd = input("Enter the pass: ")
cisco_switch = {
    'device_type': 'cisco_ios',
    'host':   input("Enter the ip addr: "),
    'username': user,
    'password': passwd,
    'port': 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}
net_connect = ConnectHandler(**cisco_switch)
print("***||Layman Switch Automation Script||***")
print("What do you you want to do:\n 1-Show VLANs\n 2-Create VLANs\n 3-Delete VLANs\n 4-Rename VLANs\n 5-Assign IP Address to VLAN interface \n 6-show ip address assigned interface\n 7-Assign default-gateway\n 8-Assign Static route\n 9-Test Ping\n 10-To see Switch version\n 11-To see Vlan up or down")
while True:
    option=int(input("Put your Choice here: "))
    #For Showing the VLANs on the Console
    if option==1:
        output=net_connect.send_command('sh vlan br')
        print(output)
    #For Creating New VLAN on the switch
    elif option==2:
        vlan_id=int(input("Enter VLAN id: "))
        commands=[f"vlan {vlan_id}"]
        output=net_connect.send_config_set(commands)
        print("***Operation performed Successfully to see VLANs Press 1***")
    #For Deleting any VLAN form the Switch
    elif option==3:
        vlan_id=int(input("Enter VLAN id: "))
        commands=[f"no vlan {vlan_id}"]
        net_connect.send_config_set(commands)
        print("***Operation performed Successfully to see VLANs Press 1***")
    #For Assigning the name or renaming any VLAN
    elif option==4:
        vlan_id=int(input("Enter VLAN id: "))
        vlan_name=input("Enter VLAN name: ")
        commands=[f'vlan {vlan_id}',f'name {vlan_name}']
        net_connect.send_config_set(commands)
        print("***Operation performed Successfully to see renamed VLANs Press 1***")
    #For Assigning the IP Address to the VLAN virtual Interface
    elif option==5:
        vlan_id=int(input("Enter interface VLAN id: "))
        IP_address=input("Enter ip address: ")
        netmask=input("Enter the vlan subnet mask: ")
        commands=[f'int vlan {vlan_id}',f'ip address {IP_address} {netmask}','no sh']
        net_connect.send_config_set(commands)
        print("***Operation performed Successfully to see interfaces Press 6***")
    #For Seeing all the IP assigned interface
    elif option==6:
        output=net_connect.send_command('sh ip int br | exclude unassigned')
        print(output)
    #For assigning the default gateway to the Switch
    elif option==7:
        default_route=input("Enter the default-route IP: ")
        commands=[f'ip default-gateway {default_route}']
        net_connect.send_config_set(commands)
        print("***Operation performed Successfully***")
    #For assigning a static route on the switch
    elif option==8:
        destination_network=input("Enter the destination Network: ")
        des_mask=input("Enter the destination Mask: ")
        next_hop=input("Enter the next hop IP: ")
        commands=[f'ip route {destination_network} {des_mask} {next_hop}']
        net_connect.send_config_set(commands)
        print("***Operation performed Successfully***")
    #For doing echo Ping request to any IP
    elif option==9:
        ping_ip=input("Enter the IP Address to ping: ")
        commands=[f'do ping {ping_ip}']
        op=net_connect.send_config_set(commands)
        print(f"***Operation performed Successfully***\n {op}")
    #For seeing switch version
    elif option==10:
        output=net_connect.send_command('sh version  | inc Version')
        print(output)
    elif option==11:
        vlan_no=int(input("Enter the Vlan id: "))
        output=net_connect.send_command(f'sh int vlan {vlan_no} | inc line')
        print(output)
    #For exiting out of the program
    elif option==0:
        exit(0)
    else:
        print("Invalid input")




