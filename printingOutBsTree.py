import requests
from bs4 import BeautifulSoup, Tag
import csv
# TreeNode class remains mostly the same
class TreeNode:

    def __init__(self, content):

        self.content = content

        self.children = []

        self.parent = None



    def add_child(self, child_node):

        self.children.append(child_node)

        child_node.parent = self



    def is_root(self):

        return self.parent is None



    def __str__(self, level=0, last_child=True):
        """
        Create a string representation of the node and its children, visually similar to the `tree` command,
        with children contents indented and starting below the parent tag.
        """
        indent = "    " * level
        if level > 0:
            prefix = indent[:-4] + ("└── " if last_child else "├── ")
        else:
            prefix = ""

        parts = [prefix + self.content] if level > 0 else [self.content]

        for i, child in enumerate(self.children):
            parts.append(child.__str__(level + 1, i == len(self.children) - 1))

        return "\n".join(parts)
    


    @staticmethod
    def parse_csv(csv_content):
        """
        Parses CSV content and returns the root node of the tree.
        """
        root = TreeNode("CSV Root")
        reader = csv.reader(csv_content.splitlines())

        header = next(reader)
        for column in header:
            column_node = TreeNode(column)
            root.add_child(column_node)

        for row in reader:
            for i, cell in enumerate(row):
                cell_node = TreeNode(cell)
                root.children[i].add_child(cell_node)

        return root

    @staticmethod
    def parse_csv_new(csv_content):
        """
        Parses CSV content into a tree where each row becomes a token under the root.
        """
        root = TreeNode("CSV Root")
        header_node = TreeNode("Header")
        root.add_child(header_node)
        reader = csv.reader(csv_content.splitlines())

        next(reader)

        for row in reader:
            row_data = " | ".join(row)
            row_node = TreeNode(row_data)
            header_node.add_child(row_node)

        return root

    @staticmethod
    def from_html_tag(tag):
        """
        Recursively converts an HTML tag into a tree node structure.
        """
        if isinstance(tag, Tag):
            node = TreeNode(tag.name)
            for child in tag.children:
                child_node = TreeNode.from_html_tag(child)
                if child_node:
                    node.add_child(child_node)
        elif tag.string and tag.string.strip():
            node = TreeNode(tag.string.strip())
        else:
            return None
        return node

# Example usage
if __name__ == "__main__":
    # URL to parse - replace this with the actual URL
    url = 'https://www.w3schools.com/cssref/css_selectors.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the main BeautifulSoup object into a TreeNode
    root = TreeNode.from_html_tag(soup.html)

    # Print the tree representation
    print(root)