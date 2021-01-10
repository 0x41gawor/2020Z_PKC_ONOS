class Graph:
    def __init__(self):
        self.V = []
        self.E = []

    def add_node(self, node):
        self.V.append(node)

    def add_link(self, src, dst):
        for edge in self.E:
            if edge[0] == src and edge[1] == dst:
                return
        self.E.append([src, dst])
        self.E.append([dst, src])

    def remove_link(self, src, dst):
        if [src, dst] in self.E:
            self.E.remove([src, dst])
            self.E.remove([dst, src])
            print("Deleted",[src,dst])
        else:
            print("DUPA")

    def show_nodes(self):
        for v in self.V:
            print(v)

    def show_links(self):
        for e in self.E:
            print(e[0], " <--> ", e[1])

    def shortest(self, src, dst):
        dist = {}
        prev = {}
        done = {}
        for node in self.V:
            dist[node] = len(self.V)
            prev[node] = None
            done[node] = False
        dist[src] = 0

        for cout in range(len(self.V)):
            current = None
            for node in self.V:
                if done[node] == False and (current == None or dist[node] < dist[current]):
                    current = node
            for edge in self.E:
                if edge[0] == current and dist[edge[1]] > dist[edge[0]] + 1:
                    dist[edge[1]] = dist[edge[0]] + 1
                    prev[edge[1]] = edge[0]
            done[current] = True

        res = []
        current = dst
        while current != src:
            res.append(current)
            current = prev[current]
        res.append(src)
        res.reverse()
        return res
