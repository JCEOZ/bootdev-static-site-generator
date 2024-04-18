import unittest

from src.block import markdown_to_blocks


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


if __name__ == '__main__':
    unittest.main()
