import unittest
from src.generatepage import __extract_title__


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
        # Page title
        
        Some other content
        """
        expected = "Page title"

        self.assertEqual(expected, __extract_title__(markdown))

    def test_extract_title_no_title(self):
        markdown = """
                Some content

                Some other content
                """
        with self.assertRaises(Exception):
            __extract_title__(markdown)


if __name__ == '__main__':
    unittest.main()