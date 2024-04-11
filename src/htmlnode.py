class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html_attributes = []
        for prop in self.props:
            html_attributes.append(f" {prop}=\"{self.props[prop]}\"")
        return "".join(html_attributes)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props=\"{self.props_to_html()}\")"
