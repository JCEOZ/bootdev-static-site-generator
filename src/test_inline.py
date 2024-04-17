import unittest

from src.inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, \
    split_nodes_link
from src.textnode import TextNode, text_type_text, text_type_code, text_type_italic, text_type_bold, text_type_image, \
    text_type_link


class TestInline(unittest.TestCase):
    def test_split_text_node_with_code_block(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        result = split_nodes_delimiter([node], "`", text_type_code)

        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_code_block_at_the_beginning(self):
        node = TextNode("`code block` text node", text_type_text)
        result = split_nodes_delimiter([node], "`", text_type_code)

        expected = [
            TextNode("code block", text_type_code),
            TextNode(" text node", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_code_block_at_the_end(self):
        node = TextNode("Text node with `code block`", text_type_text)
        result = split_nodes_delimiter([node], "`", text_type_code)

        expected = [
            TextNode("Text node with ", text_type_text),
            TextNode("code block", text_type_code),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_italic_block(self):
        node = TextNode("This is text with a *italic block* word", text_type_text)
        result = split_nodes_delimiter([node], "*", text_type_italic)

        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic block", text_type_italic),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_italic_block_at_the_beginning(self):
        node = TextNode("*italic block* text node", text_type_text)
        result = split_nodes_delimiter([node], "*", text_type_italic)

        expected = [
            TextNode("italic block", text_type_italic),
            TextNode(" text node", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_italic_block_at_the_end(self):
        node = TextNode("Text node with *italic block*", text_type_text)
        result = split_nodes_delimiter([node], "*", text_type_italic)

        expected = [
            TextNode("Text node with ", text_type_text),
            TextNode("italic block", text_type_italic),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_bold_block(self):
        node = TextNode("This is text with a **bold block** word", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)

        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold block", text_type_bold),
            TextNode(" word", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_bold_block_at_the_beginning(self):
        node = TextNode("**bold block** text node", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)

        expected = [
            TextNode("bold block", text_type_bold),
            TextNode(" text node", text_type_text),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_with_bold_block_at_the_end(self):
        node = TextNode("Text node with **bold block**", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)

        expected = [
            TextNode("Text node with ", text_type_text),
            TextNode("bold block", text_type_bold),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_multiple_markdown(self):
        node = TextNode("Text **node** with **bold block**", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)

        expected = [
            TextNode("Text ", text_type_text),
            TextNode("node", text_type_bold),
            TextNode(" with ", text_type_text),
            TextNode("bold block", text_type_bold),
        ]

        self.assertEqual(expected, result)

    def test_split_text_node_no_markdown(self):
        node = TextNode("Text without modifications", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)

        expected = [
            node
        ]

        self.assertEqual(expected, result)

    def test_split_non_text_nodes(self):
        node = TextNode("some code", text_type_code)
        result = split_nodes_delimiter([node], "`", text_type_code)

        expected = [
            node
        ]

        self.assertEqual(expected, result)

    def test_split_multiple_text_nodes(self):
        node = TextNode("Text without modifications", text_type_text)
        node2 = TextNode("some code", text_type_code)
        node3 = TextNode("Text **node** with **bold block**", text_type_text)
        node4 = TextNode("Text node with **bold block**", text_type_text)
        result = split_nodes_delimiter([node, node2, node3, node4], "**", text_type_bold)

        expected = [
            node,
            node2,
            TextNode("Text ", text_type_text),
            TextNode("node", text_type_bold),
            TextNode(" with ", text_type_text),
            TextNode("bold block", text_type_bold),
            TextNode("Text node with ", text_type_text),
            TextNode("bold block", text_type_bold),
        ]

        self.assertEqual(expected, result)

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

        self.assertEqual(expected, extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

        self.assertEqual(expected, extract_markdown_links(text))

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                    ),
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("link", text_type_link,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", text_type_link,
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                    ),
        ]
        self.assertEqual(expected, split_nodes_link([node]))


if __name__ == '__main__':
    unittest.main()
