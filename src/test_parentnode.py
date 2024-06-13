import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):

    def test_empty_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("a", "value", None, {"href": "/"})
            node.to_html() 

    def test_empty_val(self):
        with self.assertRaises(ValueError):
            node = ParentNode("a", None, None, {"href": "/"})
            node.to_html()

    def test_basic_example(self):
        node = ParentNode("a", None, [LeafNode("p", "Value", {"class": "bold"})], {"href": "/"})
        html = node.to_html()
        self.assertEqual(html, "<a href='/'><p class='bold'>Value</p></a>")

if __name__ == "__main__":
    unittest.main()