import time
import random
class Packet:
    """A class that naively models a network packet """
    
    def __init__(self, ctrl_info, payload=None):
       
        if isinstance(ctrl_info, (Control_Information)):
            self._ctrlinfo = ctrl_info
            self._packets = list(payload)
        else:
            self._packets = list()

    def append_to_packets(self,item):
        self._packets.append(item)

    def __delitem__(self,k):
        del self._packets[k]

    def __getitem__(self, location):
        return self._packets[location]
    
    def __setitem__(self, j, value):
        self._packets[j] = value
    
class Control_Information:
    """A class that simulates a packets control information
    Source and Destination IP address i.e., Alice and Bob's
    network addresses
    """
   
    def __init__(self, username, net_addrs):
        """Initialize the Control Information
        username    username of the sender or receiver of the nework packet
        net_addrs   ip address of the sender or receiver
        """
        self._username = username
        self._address = net_addrs

    def __str__(self):
        """String representation of the control information"""
        return self._username + ":" + self._address



class Payload:
    """A class that models the schema of a sent data"""
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return str(self._data)
    def __len__(self):
        return len(self._data)
class Internet_Application:
    print("***Internet application simulation***")
    time.sleep(2)
    print("loading...")
    if __name__ == '__main__':
        
        alice = Control_Information("Alice", "172.16.254.1")
        bob = Control_Information("Bob", "192.168.1.15")
      
        bob_packets = Packet(bob, "")
        outbound_packet_list= ["The Cybers will be thorough with surveillance today, be careful out there",
        None,
        "The secure login password is 'Wxx124DDDcxxx18934FFccc'",
        "Taking control of the security panel now",
        "Alright, security cameras have been frozen, you 5 minutes tops.",
        "We have been compromised, get out fast!!!",
        "Good job Agent Azure, you paycheck awaits you at the dragon's nest.",
        None]
        alice_packets = Packet(alice,outbound_packet_list)
        alice_message_intervals = random.randint(1,4)
       
        bobs_inbound_pack_list = list()
        for x in range(len(alice_packets._packets)):
            time.sleep(alice_message_intervals)
            if  alice_packets[x] == None:
                pass
            else:
                bob_packets.append_to_packets(alice_packets._packets[x])
                print(bob_packets[0])
                del bob_packets[0]
            
               
          
    
    


    
