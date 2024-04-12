import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_generate_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text LN1"),
                LeafNode(None, "Normal text LN2"),
                LeafNode("i", "italic text LN3"),
                LeafNode(None, "Normal text LN4"),
            ],
        )
        expected_html = ("<p>"
                         "<b>Bold text LN1</b>"
                         "Normal text LN2"
                         "<i>italic text LN3</i>"
                         "Normal text LN4"
                         "</p>")
        self.assertEqual(expected_html, node.to_html())

    def test_generate_html_with_props(self):
        props = {"href": "https://www.google.com"}
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text LN1", props),
                LeafNode(None, "Normal text LN2"),
                LeafNode("i", "italic text LN3"),
                LeafNode(None, "Normal text LN4"),
            ],
            props
        )
        expected_html = ("<p href=\"https://www.google.com\">"
                         "<b href=\"https://www.google.com\">Bold text LN1</b>"
                         "Normal text LN2"
                         "<i>italic text LN3</i>"
                         "Normal text LN4"
                         "</p>")
        self.assertEqual(expected_html, node.to_html())

    def test_generate_html_multiple_levels(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p1",
                    [
                        LeafNode("b", "PN PN1 LN1"),
                        LeafNode(None, "PN PN1 LN2"),
                        LeafNode("i", "PN PN1 LN3"),
                        LeafNode(None, "PN PN1 LN4"),
                    ]
                ),
                ParentNode(
                    "p2",
                    [
                        LeafNode("b", "PN PN2 LN1"),
                        LeafNode(None, "PN PN2 LN2"),
                        LeafNode("i", "PN PN2 LN3"),
                        LeafNode(None, "PN PN2 LN4"),
                    ]
                )
            ]
        )
        expected_html = ("<p>"
                         "<p1>"
                         "<b>PN PN1 LN1</b>"
                         "PN PN1 LN2"
                         "<i>PN PN1 LN3</i>"
                         "PN PN1 LN4"
                         "</p1>"
                         "<p2>"
                         "<b>PN PN2 LN1</b>"
                         "PN PN2 LN2"
                         "<i>PN PN2 LN3</i>"
                         "PN PN2 LN4"
                         "</p2>"
                         "</p>")
        self.assertEqual(expected_html, node.to_html())

    def test_generate_html_with_props_multiple_levels(self):
        props = {"href": "https://www.google.com"}
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p1",
                    [
                        LeafNode("b", "PN PN1 LN1", props),
                        LeafNode(None, "PN PN1 LN2"),
                        LeafNode("i", "PN PN1 LN3"),
                        LeafNode(None, "PN PN1 LN4"),
                    ],
                    props
                ),
                ParentNode(
                    "p2",
                    [
                        LeafNode("b", "PN PN2 LN1"),
                        LeafNode(None, "PN PN2 LN2"),
                        LeafNode("i", "PN PN2 LN3", props),
                        LeafNode(None, "PN PN2 LN4"),
                    ],
                    props
                )
            ],
            props
        )
        expected_html = ("<p href=\"https://www.google.com\">"
                         "<p1 href=\"https://www.google.com\">"
                         "<b href=\"https://www.google.com\">PN PN1 LN1</b>"
                         "PN PN1 LN2"
                         "<i>PN PN1 LN3</i>"
                         "PN PN1 LN4"
                         "</p1>"
                         "<p2 href=\"https://www.google.com\">"
                         "<b>PN PN2 LN1</b>"
                         "PN PN2 LN2"
                         "<i href=\"https://www.google.com\">PN PN2 LN3</i>"
                         "PN PN2 LN4"
                         "</p2>"
                         "</p>")
        self.assertEqual(expected_html, node.to_html())

    def test_raise_error_when_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text LN1"),
                LeafNode(None, "Normal text LN2"),
                LeafNode("i", "italic text LN3"),
                LeafNode(None, "Normal text LN4"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raise_error_when_no_children(self):
        node = ParentNode(
            "p",
            [],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raise_error_when_none_children(self):
        node = ParentNode(
            "p",
            None,
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raise_error_no_tag_on_child(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    None,
                    [
                        LeafNode("b", "PN PN1 LN1"),
                        LeafNode(None, "PN PN1 LN2"),
                        LeafNode("i", "PN PN1 LN3"),
                        LeafNode(None, "PN PN1 LN4"),
                    ]
                ),
                ParentNode(
                    "p2",
                    [
                        LeafNode("b", "PN PN2 LN1"),
                        LeafNode(None, "PN PN2 LN2"),
                        LeafNode("i", "PN PN2 LN3"),
                        LeafNode(None, "PN PN2 LN4"),
                    ]
                )
            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raise_error_no_children_on_child(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p1",
                    [

                    ]
                ),
                ParentNode(
                    "p2",
                    [
                        LeafNode("b", "PN PN2 LN1"),
                        LeafNode(None, "PN PN2 LN2"),
                        LeafNode("i", "PN PN2 LN3"),
                        LeafNode(None, "PN PN2 LN4"),
                    ]
                )
            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raise_error_none_children_on_child(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p1",
                    None
                ),
                ParentNode(
                    "p2",
                    [
                        LeafNode("b", "PN PN2 LN1"),
                        LeafNode(None, "PN PN2 LN2"),
                        LeafNode("i", "PN PN2 LN3"),
                        LeafNode(None, "PN PN2 LN4"),
                    ]
                )
            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == '__main__':
    unittest.main()
