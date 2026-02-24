import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode()
            node.to_html()

    def test_no_props_to_html(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_props_to_htm(self):
        test_prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=test_prop)
        self.assertEqual(node.props_to_html(),
        ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        test_prop = {
            "href": "https://www.home.com",
        }
        node = LeafNode("a", "home", test_prop )
        self.assertEqual(node.to_html(), '<a href="https://www.home.com">home</a>')

    def test_leaf_to_html_with_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("", None)
            node.to_html()

    def test_leaf_to_html_with_no_tag(self):
        node = LeafNode("", "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_repr(self):
        node = LeafNode(
            "a",
            "Hello hello",
            {"href": "https://www.google.com"}
            )

        self.assertEqual("LeafNode(a, Hello hello, {'href': 'https://www.google.com'})", node.__repr__())

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_child(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child_node]).to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode(
            "a", 
            "home",
            {"href": "https://www.google.com"}
            )
        parent_node = ParentNode(
            "div",
            [child_node],
            {"class": "page"}
            )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="page"><a href="https://www.google.com">home</a></div>'
        )
        
    def test_to_html_child_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("print('hello world')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello world')")

    def test_text_type_none(self):
        node = TextNode("This is invalid node", None)
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.hello.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href": "www.hello.com"})

    def test_image(self):
        node = TextNode("A cat", TextType.IMAGE, "www.cat.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"src": "www.cat.com",
        "alt": "A cat"})

if __name__ == "__main__":
    unittest.main()