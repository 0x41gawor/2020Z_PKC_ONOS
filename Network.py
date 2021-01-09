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
        #print("======== I N T E N T S ========")
        #for intent in self.intents:
         #   print(intent.inElements[0], " --> ", intent.outElements[0])
