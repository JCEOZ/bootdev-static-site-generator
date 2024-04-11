from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("At least one child node is required")
        children_html = self.__recursion__(self)
        return f"<{self.tag}>{children_html}</{self.tag}>"

    def __recursion__(self, node):
        html = ""
        if node.children is None or len(node.children) == 0:
            return node.to_html()

        for child in node.children:
            html += self.__recursion__(child)

        return html

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props=\"{self.props_to_html()}\")"
