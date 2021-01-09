
class Host:
    # host - dict, one of multiple dicts in json response of get_hosts in hosts array
    def __init__(self, host):
        self.id = host["id"]                       # str
        self.mac = host["mac"]                     # str
        self.vlan = host["vlan"]                   # str
        self.innerVlan = host["innerVlan"]         # str
        self.outerTpid = host["outerTpid"]         # str
        self.configured = host["configured"]       # str
        self.suspended = host["suspended"]         # str
        self.ipAddresses = host["ipAddresses"]     # list of str
        self.locations = host["locations"]         # dict {elementId, port}

        self.connected_switch = str()               # str

    def show(self):
        print(f'id : {self.id}')
        print(f'mac : {self.mac}')
        print(f'vlan : {self.vlan}')
        print(f'innerVlan : {self.innerVlan}')
        print(f'outerTpid : {self.outerTpid}')
        print(f'configured : {self.configured}')
        print(f'suspended : {self.suspended}')
        print(f'ipAddresses : {self.ipAddresses}')
        print(f'locations : {self.locations}')

    def set_connected_switch(self, switch):
        self.connected_switch = switch
