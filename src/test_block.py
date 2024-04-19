import unittest

from src.block import markdown_to_blocks, block_type_heading, block_to_block_type, block_type_code, \
    block_type_paragraph, block_type_quote, block_type_unordered_list, block_type_ordered_list, markdown_to_html_node


class TestBlock(unittest.TestCase):
    def test_split_text_node_with_code_block(self):
        markdown = """
            This is **bolded** paragraph
            
            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line
            
            * This is a list
            * with items
            """

        expected = [
            'This is **bolded** paragraph',
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
            '* This is a list\n* with items'
        ]

        self.assertEqual(expected, markdown_to_blocks(markdown))

    def test_block_to_block_type_heading1(self):
        block = "# heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_heading2(self):
        block = "## heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_heading3(self):
        block = "### heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_heading4(self):
        block = "#### heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_heading5(self):
        block = "##### heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_heading6(self):
        block = "###### heading"
        expected = block_type_heading

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code(self):
        block = "```\nsome code example\nwith multiple lines\n ```"
        expected = block_type_code

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code_missing_prefix(self):
        block = "some code example\nwith multiple lines\n ```"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code_missing_suffix(self):
        block = "```\nsome code example\nwith multiple lines"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code_quote(self):
        block = "> this is some quote\n> which can be life changing\n> if applied"
        expected = block_type_quote

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code_quote_invalid_prefix(self):
        block = "< this is some quote\n< which can be life changing\n< if applied"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_code_quote_missing_prefix(self):
        block = "> this is some quote\n which can be life changing\n> if applied"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_unordered_list(self):
        block = "* list item\n- list item\n* list item"
        expected = block_type_unordered_list

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_unordered_list_missing_prefix(self):
        block = "* list item\n list item\n* list item"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_ordered_list(self):
        block = "1. list item\n2. list item\n3. list item"
        expected = block_type_ordered_list

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_ordered_list_missing_prefix(self):
        block = "1. list item\n list item\n3. list item"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_block_to_block_type_ordered_list_invalid_order(self):
        block = "1. list item\n5. list item\n3. list item"
        expected = block_type_paragraph

        self.assertEqual(expected, block_to_block_type(block))

    def test_paragraph(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here
            
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
            html,
        )

    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here
            
            This is another paragraph with *italic* text and `code` here
            
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
            - This is a list
            - with items
            - and *more* items
            
            1. This is an `ordered` list
            2. with items
            3. and more items
            
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
            # this is an h1
            
            this is paragraph text
            
            ## this is an h2
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
            > This is a
            > blockquote block
            
            this is paragraph text
            
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == '__main__':
    unittest.main()
