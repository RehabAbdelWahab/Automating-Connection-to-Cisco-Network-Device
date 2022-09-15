from smc import session
from smc.api.exceptions import CreateElementFailed, ElementNotFound
import smc.elements
import smc.core.engine
import smc.core.engines
import smc.policy
from smc.elements.network import Host, Network, AddressRange
from smc.elements.service import TCPService , UDPService
from smc.elements.group import Group
import sys

def get_prefix(mask_value):
    prefix=''
    if mask_value=="255.0.0.0":
        prefix="8"
    elif mask_value=="255.128.0.0":
        prefix="9"
    elif mask_value=="255.192.0.0":
        prefix="10"
    elif mask_value=="255.224.0.0":
        prefix="11"
    elif mask_value=="255.240.0.0":
        prefix="12"
    elif mask_value=="255.248.0.0":
        prefix="13"
    elif mask_value=="255.252.0.0":
        prefix="14"
    elif mask_value=="255.254.0.0":
        prefix="15"
    elif mask_value=="255.255.0.0":
        prefix="16"
    elif mask_value=="255.255.128.0":
        prefix="17"
    elif mask_value=="255.255.192.0":
        prefix="18"
    elif mask_value=="255.255.224.0":
        prefix="19"
    elif mask_value=="255.255.240.0":
        prefix="20"
    elif mask_value=="255.255.248.0":
        prefix="21"
    elif mask_value=="255.255.252.0":
        prefix="22"
    elif mask_value=="255.255.254.0":
        prefix="23"
    elif mask_value=="255.255.255.0":
        prefix="24"
    elif mask_value=="255.255.255.128":
        prefix="25"
    elif mask_value=="255.255.255.192":
        prefix="26"
    elif mask_value=="255.255.255.224":
        prefix="27"
    elif mask_value=="255.255.255.240":
        prefix="28"
    elif mask_value=="255.255.255.248":
        prefix="29"
    elif mask_value=="255.255.255.252":
        prefix="30"
    elif mask_value=="255.255.255.254":
        prefix="31"
    elif mask_value=="255.255.255.255":
        prefix="32"
    return prefix

#SMC_IP=input("This API Integration uses http protocol only, Please Enter SMC IP Address: ")
#SMC_Port=input("Please, Enter SMC API Port: ")
#Key=input("Please, Enter API Key: ")
#session.login(url="http://"+str(SMC_IP)+":"+ str(SMC_Port), api_key=str(Key))
#SMC IP=10.19.100.58
#SMC Port=8082
#key="tJ7UqyFMLHm9JFF67ZvXmsB2"
#file_path=input('Please, Enter FTD Configuration file path using following format '+repr('C:\\Users\\student\\Desktop\\WAN_FTD.log')+": ")
#file = open(str(file_path), 'r')

session.login(url='http://10.19.100.58:8082', api_key='tJ7UqyFMLHm9JFF67ZvXmsB2')
file = open('C:\\Users\\student\\Desktop\\WAN_FTD.log', 'r')
output_file=open('C:\\Users\\student\\Desktop\\output.txt','w')
Lines = file.readlines()
x=0
y=0
z=0
m=0
hosts_count=0 
range_count=0
network_count=0
count_failed_udp=0
count_failed_tcp=0
tcp_service_count=0
udp_service_count=0
network_group_count=0
count=0


###################################################  Migrating Network subnets ####################################################
    if obj_name_line[0]=="object" and obj_name_line[1]=="network" and x==0:
        obj_name=obj_name_line[2].strip("\n")
        x=1
        

    elif obj_name_line[0]=="" and obj_name_line[1]=="subnet" and x==1:
        network_ID_value=obj_name_line[2]
        mask_value=obj_name_line[3].strip("\n")
        prefix=get_prefix(mask_value)
        try:
            Network.create(name=obj_name, ipv4_network=network_ID_value+'/'+str(prefix))
            #print(obj_name+":"+network_ID_value+"/"+mask_value+" prefix is: "+str(prefix))
            network_count+=1
        except Exception:
            pass

        obj_name=""
        network_ID_value=""
        mask_value=""
        x=0

##############################################   Migrating Hosts ###########################################################################

    elif obj_name_line[0]=="" and obj_name_line[1]=="host" and x==1:
        host_value=obj_name_line[2].strip("\n")
        try:
            Host.create(name=obj_name, address=host_value)
            #print(obj_name+":"+host_value)
            hosts_count+=1
        except Exception:
            pass
        
        obj_name=""
        host_value=""
        x=0
         



output_file.close()
session.logout()    



'''
session.login(url='http://10.19.100.58:8082', api_key='tJ7UqyFMLHm9JFF67ZvXmsB2')
#Host.create(name='ourHost2', address='2.2.2.2')
Network.create(name='Ournetwork-mina', ipv4_network='4.3.3.0/24', comment='mynet')
#AddressRange.create(name='myaddrrange', ip_range='1.1.1.1-1.1.1.10')
#TCPService.create(name='aservice', min_dst_port=9090)
#UDPService.create(name='OurUdpservice', min_dst_port=9090)

