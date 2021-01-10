from Connection import Connection
from Network import Network

if __name__ == '__main__':
    api = Connection()

    list_of_hosts = api.get_hosts()
    list_of_links = api.get_links()
    list_of_switches = api.get_switches()
    id, name, list_of_intents = api.get_monitored_intents()

    network = Network(list_of_switches, list_of_links, list_of_hosts, list_of_intents)
    #network.show()
    network.shortest_paths_priority_first('10.0.0.1','10.0.0.4')
