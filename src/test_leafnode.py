import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_raise_error_when_empty_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None, None)

    def test_to_html_only_value(self):
        node = LeafNode(None, "Example text.", None)
        expected = "Example text."
        self.assertEqual(expected, node.to_html())

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.", None)
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(expected, node.to_html())

    def test_to_html_one_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(expected, node.to_html())

    def test_to_html_multiple_props(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        expected = "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>"
        self.assertEqual(expected, node.to_html())

    def test_leaf_nodes_equal(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_leaf_nodes_equal_different_tag(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("i", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)

    def test_leaf_nodes_equal_different_value(self):
        node1 = LeafNode("i", "Don't click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("i", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)

    def test_leaf_nodes_equal_different_props(self):
        node1 = LeafNode("i", "Click me!", {"href": "https://www.boot.dev"})
        node2 = LeafNode("i", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)


if __name__ == '__main__':
    unittest.main()
