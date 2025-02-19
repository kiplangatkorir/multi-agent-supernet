import networkx as nx

class KnowledgeGraph:
    """
    A lightweight knowledge graph to help agents store and retrieve structured information.
    """

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_fact(self, subject, relation, obj):
        """
        Adds a fact to the knowledge graph.

        Args:
            subject (str): The entity (e.g., "AI Agents").
            relation (str): The relationship (e.g., "use").
            obj (str): The target entity (e.g., "Neural Networks").
        """
        self.graph.add_edge(subject, obj, relation=relation)

    def get_relations(self, subject):
        """
        Retrieves all relationships of a given entity.

        Args:
            subject (str): The entity to query.

        Returns:
            list: A list of tuples (relation, target).
        """
        return [(self.graph.edges[edge]["relation"], edge[1]) for edge in self.graph.out_edges(subject)]

    def find_path(self, start, end):
        """
        Finds a reasoning path between two entities if one exists.

        Args:
            start (str): The starting entity.
            end (str): The target entity.

        Returns:
            list: The path of relationships if found, else an empty list.
        """
        try:
            path = nx.shortest_path(self.graph, source=start, target=end)
            return path
        except nx.NetworkXNoPath:
            return []
