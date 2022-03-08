import subprocess 
import optparse 
import re 
import random
 
#region Help strings
help_interface = "Interface name"
 
help_mac = """New mac adress, It must start with 00 
              and contains 'only' 6 digits-letters"""
#endregion
 
 
def rand_mac():
    return "00:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )
random_mac = rand_mac()
 
 
def get_user_input():
    usage_String = "Type only interface name if you want to generate a random mac address"
    parse_object = optparse.OptionParser(usage=usage_String)
    parse_object.add_option("-i", "--interface", dest="interface", help=help_interface)
    parse_object.add_option("-m", "--mac", dest="mac_address", help=help_mac)
 
    return  parse_object.parse_args()
 
def change_mac_adress(user_interface,user_mac_address):
 
    subprocess.call(["ifconfig", user_interface, "down"])  
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
 
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) 
    if new_mac:
        return new_mac.group(0) 
    else:
        return None
 
def mac_changer(mac_address):
    change_mac_adress(user_input.interface, mac_address)
    finalized_mac = control_new_mac(str(user_input.interface))
 
    if str(finalized_mac).upper() == str(mac_address).upper():
        print("Success!")
    else:
        print("Error!")
 
 
print("Welcome the MacChanger")
 
(user_input,arguments) = get_user_input()
if(user_input.mac_address is None):
    mac_changer(random_mac)
else:
    mac_changer(user_input.mac_address)