import unittest

from textnode import TextNode


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


if __name__ == '__main__':
    unittest.main()
