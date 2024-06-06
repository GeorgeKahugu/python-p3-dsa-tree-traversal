
class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Helper function to perform DFS
        def dfs(node):
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result
            return None
        
        if self.root is None:
            return None
        return dfs(self.root)

# Example Usage:
# Creating a tree with some nodes as dictionaries
node4 = {"id": "4", "children": []}
node5 = {"id": "5", "children": []}
node2 = {"id": "2", "children": [node4, node5]}
node3 = {"id": "3", "children": []}
node1 = {"id": "1", "children": [node2, node3]}

# Creating the tree
tree = Tree(node1)

# Searching for nodes
print(tree.get_element_by_id("4"))  # Output: {'id': '4', 'children': []}
print(tree.get_element_by_id("1"))  # Output: {'id': '1', 'children': [{'id': '2', 'children': [{'id': '4', 'children': []}, {'id': '5', 'children': []}]}, {'id': '3', 'children': []}]}
print(tree.get_element_by_id("6"))  # Output: None
