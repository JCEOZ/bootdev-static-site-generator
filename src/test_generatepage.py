import unittest
from src.generatepage import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
        # Page title
        
        Some other content
        """
        expected = "Page title"

        self.assertEqual(expected, extract_title(markdown))

    def test_extract_title_no_title(self):
        markdown = """
                Some content

                Some other content
                """
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == '__main__':
    unittest.main()