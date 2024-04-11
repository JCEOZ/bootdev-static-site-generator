import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_for_one_prop(self):
        node = HTMLNode("p", "Example paragraph", None, {"href": "https://www.google.com"})
        expected = " href=\"https://www.google.com\""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_multiple_props(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("p", "Example paragraph", None, props)
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_none_props(self):
        node = HTMLNode("p", "Example paragraph", None, None)
        expected = ""
        self.assertEqual(expected, node.props_to_html())


if __name__ == '__main__':
    unittest.main()
