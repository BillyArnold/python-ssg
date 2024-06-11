import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_different_text_types(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_different_urls(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_different_text_and_url(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is another text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_empty_text(self):
        node = TextNode("", "bold")
        node2 = TextNode("", "bold")
        self.assertEqual(node, node2)

    def test_empty_text_and_url(self):
        node = TextNode("", "bold", "https://www.boot.dev")
        node2 = TextNode("", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
