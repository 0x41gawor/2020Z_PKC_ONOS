
class Link:
    # link - dict, one of multiple dicts in json response of get_link in links array
    def __init__(self, link):
        self.src = link["src"]      # dict {port, device}
        self.dst = link["dst"]      # dict {port, device}
        self.type = link["type"]    # str
        self.state = link["state"]  # str

    def show(self):
        print(f'src : port: {self.src["port"]}, device: {self.src["device"]}')
        print(f'dst : port: {self.dst["port"]}, device: {self.dst["device"]}')
        print(f'type : {self.type}')
        print(f'state : {self.state}')
