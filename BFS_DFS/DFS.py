The LockedIn executives want us to add a depth-first search feature to geographic search.

Complete the depth_first_search and depth_first_search_r methods. The depth_first_search_r method is a recursive helper method for depth_first_search.

    Complete the depth_first_search function. It takes a start vertex as input, traverses the graph in a depth-first manner, records the vertices it visits in a list, and returns it. It should:
        Create an empty list to store visited vertices.
        Call depth_first_search_r with the empty list and the start vertex
        Return the list of visited vertices after depth_first_search_r has filled it in
    Complete the depth_first_search_r function. It takes a list of vertices that have been visited so far and a current vertex as input. It should:
        Visit the current vertex by adding it to the list
        Get a sorted list of the neighbors of the current vertex
        For each of those neighbors:
            If the neighboring vertex hasn't been visited yet, visit it by recursively calling depth_first_search_r with the neighboring vertex

class Graph:
    def depth_first_search(self, start_vertex: str) -> list[str]:
        visited_list = []
        self.depth_first_search_r(visited_list, start_vertex)
        return visited_list
    
    def depth_first_search_r(self, visited: list[str], current_vertex: str) -> None:
        visited.append(current_vertex)
        visited_sort = sorted(self.graph[current_vertex])
        for neigh in visited_sort:
            if neigh not in visited:
                self.depth_first_search_r(visited, neigh)

        # don't touch below this line

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: str, v: str) -> None:
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self) -> str:
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
