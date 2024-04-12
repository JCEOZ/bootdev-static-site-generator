from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Value is required")
        HTMLNode.__init__(self, tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props=\"{self.props_to_html()}\")"

    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return self.tag == other.tag and self.value == other.value and self.props == other.props
        return False
