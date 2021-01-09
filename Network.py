from Graph import Graph


def assign_switch_to_host(ipAddress):
    return {
        '10.0.0.1': "of:0000000000000001",
        '10.0.0.2': "of:0000000000000002",
        '10.0.0.3': "of:0000000000000003",
        '10.0.0.4': "of:0000000000000004"
    }[ipAddress]


class Network:

    def __init__(self, switches, links, hosts, intents):
        self.switches = switches
        self.links = links
        self.hosts = hosts
        self.intents = intents
        self.graph = Graph()
        for switch in switches:
            self.graph.add_node(switch.id)
        for link in links:
            self.graph.add_link(link.src["device"], link.dst["device"])

        # Zmapowanie hostów na switche do których są podłączone
        for host in self.hosts:
            host.set_connected_switch(assign_switch_to_host(host.ipAddresses[0]))

    def show(self):
        print("====== S W I T C H E S =======")
        self.graph.show_nodes()
        print("========== L I N K S ==========")
        self.graph.show_links()
        print("========== H O S T S ==========")
        for host in self.hosts:
            print("[", host.id, " ", host.ipAddresses[0],  "] -->", host.connected_switch)
        print("======== I N T E N T S ========")
        i = 1  # Zmienna pomocnicza, bo czesto te intecje sie nie usuwaja
        for intent in self.intents:
            print(i, ":  ", end='')
            i = i + 1
            print(intent.inElements[0], " --> ", intent.outElements[0])

    def shortest_paths(self):
        print("\n======== S H O R T E S T   P A T H S ==========\n")
        for intent in self.intents:
            print("\nIntent ", intent.inElements[0], " ---> ", intent.outElements[0])
            src_host = self.hosts[self.get_index_by_id(intent.inElements[0])]
            dst_host = self.hosts[self.get_index_by_id(intent.outElements[0])]
            print(src_host.ipAddresses[0], " ---> ", dst_host.ipAddresses[0])
            src_switch = src_host.connected_switch
            dst_switch = dst_host.connected_switch
            print(self.graph.shortest(src_switch, dst_switch))

    # Funkcji podajemy id hosta odczytane z intenta a funkcja zwraca indeks tego hosta z listy self.hosts
    def get_index_by_id(self, id):
        for index in range(len(self.hosts)):
            if self.hosts[index].id == id:
                return index
        return None
