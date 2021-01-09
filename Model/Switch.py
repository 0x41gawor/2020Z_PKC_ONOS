
class Switch:
    # device - dict, one of multiple dicts in json response of get_hosts in hosts array
    def __init__(self, device):
        self.id = device["id"]
        self.type = device["type"]
        self.available = device["available"]
        self.role = device["role"]
        self.mfr = device["mfr"]
        self.hw = device["hw"]
        self.sw = device["sw"]
        self.serial = device["serial"]
        self.driver = device["driver"]
        self.chassisId = device["chassisId"]
        self.lastUpdate = device["lastUpdate"]
        self.humanReadableLastUpdate = device["humanReadableLastUpdate"]
        self.annotations = device["annotations"]

    def show(self):
        print(f'id : {self.id}')
        print(f'type : {self.type}')
        print(f'available : {self.available}')
        print(f'role : {self.role}')
        print(f'mfr : {self.mfr}')
        print(f'hw : {self.hw}')
        print(f'sw : {self.sw}')
        print(f'serial : {self.serial}')
        print(f'driver : {self.driver}')
        print(f'chassisId : {self.chassisId}')
        print(f'lastUpdate : {self.lastUpdate}')
        print(f'humanReadableLastUpdate : {self.humanReadableLastUpdate}')
        print(f'annotations : {self.annotations}')
