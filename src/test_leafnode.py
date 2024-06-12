import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_full_props(self):
        node = LeafNode("a", "This is a link", {"href": "/main"})
        self.assertEqual(node.to_html(), "<a href='/main'>This is a link</a>")
    
    def test_missing_tag(self):
        node = LeafNode(None, "This is a link", {"href": "/"})
        self.assertEqual(node.to_html(), "This is a link")

    def test_missing_val(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None, {"href": "/main"}) 
            node.to_html()

if __name__ == "__main__":
    unittest.main()