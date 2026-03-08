import unittest

from md_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = """
> This is a
> long quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a long quote</blockquote></div>",
        )

    def test_headings(self):
        md = "## heading 2"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>heading 2</h2></div>",
        )

        md = "### heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>heading 3</h3></div>",
        )

        md = "#### heading 4"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>heading 4</h4></div>",
        )

        md = "##### heading 5"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>heading 5</h5></div>",
        )
    
    def test_ulist(self):
        md = """
- this is bullet1
- this is bullet2
- this is bullet3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is bullet1</li><li>this is bullet2</li><li>this is bullet3</li></ul></div>"
        )

    def test_olist(self):
        md = """
1. this is bullet1
2. this is bullet2
3. this is bullet3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>this is bullet1</li><li>this is bullet2</li><li>this is bullet3</li></ol></div>"
        )

    def test_mix(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

### This is a heading with **bolded** for extra emphasis

```
This is text that _should_ remain
the **same** even with inline stuff
```

> This is a
> long quote

1. this is bullet1
2. this is bullet2
3. this is bullet3

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><h3>This is a heading with <b>bolded</b> for extra emphasis</h3><pre><code>This is text that _should_ remain
the **same** even with inline stuff
</code></pre><blockquote>This is a long quote</blockquote><ol><li>this is bullet1</li><li>this is bullet2</li><li>this is bullet3</li></ol></div>"""
        )