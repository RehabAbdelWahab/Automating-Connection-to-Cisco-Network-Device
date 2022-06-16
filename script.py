import pwinput
from netmiko import SSHDetect, ConnectHandler


# get device data from the user
IP = input("Device IP: ")
username = input("Username: ")
password = pwinput.pwinput(prompt='Password: ', mask='*')
port = input("Port: ")
secret = pwinput.pwinput(prompt='Enable password: ', mask='*')


# prepare the device template
device= {
"device_type": "autodetect",
"ip": IP,
"username": username ,
"password": password ,
"port" :  int(port),
"secret": secret 
}


# auto detect device type
print("Detecting device type .....")
guesser = SSHDetect(**device)
best_match = guesser.autodetect()
device["device_type"] = best_match


# establish ssh connection 
ssh_connect = ConnectHandler(**device)
print(ssh_connect.find_prompt())
print("Established SSH connection successfully.")

# change to enable mode
ssh_connect.enable()
print("start enable mode successfully.")
cmd_result = ssh_connect.send_command("show run")

# write show run output to file 
print('write "show run" output to file show_run.txt')
with open("show_run.txt", "w") as file1:
    file1.write(cmd_result)


print('"show run" cmd output: ')
print(cmd_result)

# close enable mode
ssh_connect.exit_enable_mode()

# close the whole ssh connection
ssh_connect.disconnect()
print("disconnect successfully.")
