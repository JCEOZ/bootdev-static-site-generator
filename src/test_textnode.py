import unittest

from src.leafnode import LeafNode
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, \
    text_type_image


class TestTextNode(unittest.TestCase):
    def test_eq_all_attributes(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_no_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq_no_text_type(self):
        node = TextNode("This is a text node", None, "https://www.boot.dev")
        node2 = TextNode("This is a text node", None, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_no_text(self):
        node = TextNode(None, "bold", "https://www.boot.dev")
        node2 = TextNode(None, "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_all_attributes(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is another text node", "italic", "https://www.jz.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is another text node", "bold", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_invalid_text_type(self):
        node = TextNode("This is a text node", "invalid", "https://www.boot.dev")
        with self.assertRaises(ValueError):
            node.to_html_node()

    def test_text_node_to_html_text(self):
        text = "Example text"
        node = TextNode(text, text_type_text, None)
        expected = LeafNode(None, text, None)
        self.assertEqual(expected, node.to_html_node())

    def test_text_node_to_html_bold(self):
        text = "Example text"
        node = TextNode(text, text_type_bold, None)
        expected = LeafNode("b", text, None)
        self.assertEqual(node.to_html_node(), expected)

    def test_text_node_to_html_italic(self):
        text = "Example text"
        node = TextNode(text, text_type_italic, None)
        expected = LeafNode("i", text, None)
        self.assertEqual(node.to_html_node(), expected)

    def test_text_node_to_html_code(self):
        text = "Example text"
        node = TextNode(text, text_type_code, None)
        expected = LeafNode("code", text, None)
        self.assertEqual(node.to_html_node(), expected)

    def test_text_node_to_html_link(self):
        text = "Example text"
        url = "https://www.boot.dev"
        node = TextNode(text, text_type_link, url)
        expected = LeafNode("a", text, {"href": url})
        self.assertEqual(node.to_html_node(), expected)

    def test_text_node_to_html_image(self):
        text = "Example text"
        url = "https://www.boot.dev/cat.png"
        node = TextNode(text, text_type_image, url)
        expected = LeafNode("img", "", {"src": url, "alt": text})
        self.assertEqual(node.to_html_node(), expected)


if __name__ == '__main__':
    unittest.main()
