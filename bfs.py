def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


def build_graph():
    print("---- Build your Graph ----")
    student_graph = {}

    num_edges = int(input("Enter the number of edges in the graph: "))

    print("Enter each edge separately by a space (e.g. A B):")
    for i in range(num_edges):
        u, v = input(f"Edge {i + 1}: ").split()
        if u not in student_graph:
            student_graph[u] = []
        if v not in student_graph:
            student_graph[v] = []
        student_graph[u].append(v)
        student_graph[v].append(u)

    return student_graph


def main():
    student_graph = build_graph()
    start = input("Enter the starting node for BFS: ")

    print(f"Your graph dictionary: {student_graph}")
    print(f"Starting BFS from node: {start}")

    visited = bfs(student_graph, start)
    print(f"BFS order: {visited}")


if __name__ == "__main__":
    main()


 