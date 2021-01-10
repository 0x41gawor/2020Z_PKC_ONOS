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
            src_host = self.hosts[self.get_host_index_by_id(intent.inElements[0])]
            dst_host = self.hosts[self.get_host_index_by_id(intent.outElements[0])]
            print(src_host.ipAddresses[0], " ---> ", dst_host.ipAddresses[0])
            src_switch = src_host.connected_switch
            dst_switch = dst_host.connected_switch
            print(self.graph.shortest(src_switch, dst_switch))

    #  Funkcji podajemy ip_adresy miedzy hostami, ktorych intencje maja byc priorytetowe
    def shortest_paths_priority_first(self, src_ip_address, dst_ip_address):
        print("\n======== S H O R T E S T   P A T H S   W I T H   P R I O R I T Y ==========\n")
        # Hosty miedzy ktorymi jest priorytet
        src_host = self.hosts[self.get_host_index_by_ip_address(src_ip_address)]  # Host
        dst_host = self.hosts[self.get_host_index_by_ip_address(dst_ip_address)]  # Host

        # sciezka dla kazdej intencji
        intents_paths = list()  #  lista tupli typu ( Intent, Graph.shortest )

        # Kopia listy intentów, żeby można było usunąć
        intents = self.intents

        used_intents = list()

        #  Najpierw wyznaczymy tylko sciezki dla intencji, ktore sa miedzy hostami: src_host i dst_host
        for intent in intents:
            print("\n")
            intent_src_id = intent.key[0:len(intent.key)//2]
            intent_dst_id = intent.key[len(intent.key)//2 if len(intent.key)%2 == 0 else ((len(intent.key)//2)+1):]

            if (intent_src_id == src_host.id) and (intent_dst_id == dst_host.id) or (intent_src_id == dst_host.id) and (intent_dst_id == src_host.id):
                intents_paths.append((intent, self.shortest_path(intent)))
                print("src_host.id: ", src_host.ipAddresses[0])
                print("dst_host.id: ", dst_host.ipAddresses[0])
                print(intent_src_id)
                print(intent_dst_id)
                used_intents.append(intent)

        # usuniecie intencji, dla których juz sa sciezki
        for used_intent in used_intents:
            intents.remove(used_intent)

        #  Usuniecie wykorzystanych laczy
        for intent_path in intents_paths:
            list_of_nodes = intent_path[1]
            for i in range(len(list_of_nodes)-1):
                print("Chce usunac:", list_of_nodes[i], " ", list_of_nodes[i+1])
                self.graph.remove_link(list_of_nodes[i], list_of_nodes[i+1])
        #  Wyznaczenie pozostalych sciezek
        for intent in intents:
            intents_paths.append((intent, self.shortest_path(intent)))

        #  Wyswietlenie sciezek
        for intent_path in intents_paths:
            intent = intent_path[0]
            path = intent_path[1]
            print("\nIntent ", intent.inElements[0], " ---> ", intent.outElements[0])
            src_host = self.hosts[self.get_host_index_by_id(intent.inElements[0])]
            dst_host = self.hosts[self.get_host_index_by_id(intent.outElements[0])]
            print(src_host.ipAddresses[0], " ---> ", dst_host.ipAddresses[0])
            print("Path", path)

    def shortest_path(self, intent):
        src_host = self.hosts[self.get_host_index_by_id(intent.inElements[0])]
        dst_host = self.hosts[self.get_host_index_by_id(intent.outElements[0])]
        src_switch = src_host.connected_switch
        dst_switch = dst_host.connected_switch
        return self.graph.shortest(src_switch, dst_switch)

    #  Funkcji podajemy id hosta odczytane z intenta a funkcja zwraca indeks tego hosta z listy self.hosts
    def get_host_index_by_id(self, id):
        for index in range(len(self.hosts)):
            if self.hosts[index].id == id:
                return index
        return None

    #  Funkcji podajemy adres hosta  a funkcja zwraca indeks tego hosta z listy self.hosts
    def get_host_index_by_ip_address(self, ipAddress):
        for index in range(len(self.hosts)):
            if self.hosts[index].ipAddresses[0] == ipAddress:
                return index
        return None
