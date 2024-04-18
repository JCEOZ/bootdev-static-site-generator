import unittest

from src.block import markdown_to_blocks, block_type_heading, block_to_block_type, block_type_code, \
    block_type_paragraph, block_type_quote, block_type_unordered_list, block_type_ordered_list


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

if __name__ == '__main__':
    unittest.main()
