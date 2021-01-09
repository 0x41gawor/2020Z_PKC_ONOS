
class Intent:
    # intent - dict, one of multiple dicts in json response of get_link in links array
    def __init__(self, intent):
        self.key = intent["key"]                  # str
        self.inElements = intent["inElements"]    # list of str
        self.outElements = intent["outElements"]  # list of str

    def show(self):
        print(f"key: {self.key}")
        print(f"inElements: {self.inElements}")
        print(f"outElements: {self.outElements}")
