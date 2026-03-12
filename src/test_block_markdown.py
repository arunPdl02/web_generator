import unittest

from md_to_html import markdown_to_blocks
from blocknode import block_to_block_type, BlockType, markdown_to_blocks, extract_title

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiline(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        text = ""
        self.assertEqual(markdown_to_blocks(text),
        [])

    def text_markdown_to_blocks_single(self):
        text = "this is a single block\nThis is second line of the same block"
        self.assertEqual(markdown_to_blocks(text),["this is a single block\nThis is second line of the same block"])


class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_block_type_paragraph(self):
        md = "this is just a paragraph block"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        md1 = "# this is heading1"
        self.assertEqual(block_to_block_type(md1), BlockType.HEADING)

        md2 = "### this is heading3"
        self.assertEqual(block_to_block_type(md2), BlockType.HEADING)

    def test_block_to_block_type_invalid_heading(self):
        md1 = "#this is invalid heading"
        self.assertNotEqual(block_to_block_type(md1), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        md = "```\nprint('hello world')\n```"
        self.assertEqual(block_to_block_type(md),
        BlockType.CODE)

    def test_block_to_block_type_invalid_code(self):
        md = "```print('hello world')```"
        self.assertNotEqual(block_to_block_type(md),
        BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        md = "> this is a quote"
        self.assertEqual(block_to_block_type(md),
        BlockType.QUOTE)
    
    def test_block_to_block_type_invalid_quote(self):
        md = "test test > this is not a quote"
        self.assertNotEqual(block_to_block_type(md),
        BlockType.QUOTE)

        md = "\> this is esacaped so not a quote"
        self.assertNotEqual(block_to_block_type(md),
        BlockType.QUOTE)

    def test_block_to_block_type_ulist(self):
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

    def test_block_to_block_type_invalid_ulist(self):
        block = "- list\n-items"
        self.assertNotEqual(block_to_block_type(block), BlockType.ULIST)

    def test_block_to_block_type_olist(self):
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)

    def test_block_to_block_type_invalid_olist(self):
        block = "1. list\n2.items"
        self.assertNotEqual(block_to_block_type(block), BlockType.OLIST)

    def test_extract_title(self):
        h1 = "# Hello\n this is awesome"
        self.assertEqual(extract_title(h1),"Hello")

    def test_extract_title_invalid(self):
        h1 = "Hi, how you doing"
        with self.assertRaises(Exception):
            extract_title(h1)

if __name__ == "__main__":
    unittest.main()