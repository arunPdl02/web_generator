import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_URL_passed(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.hello.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.hello.com")
        self.assertEqual(node, node2)

    def test_eq_text_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a lovely node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_textType_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_textURL_different(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.text.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.hello.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
        