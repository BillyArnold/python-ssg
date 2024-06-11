import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_self_to_props(self):
        node = HTMLNode("tag", "value", "children", {"class": "this-class", "val": "3"})
        html = node.props_to_html()
        self.assertEqual(html, " class='this-class' val='3'")

if __name__ == "__main__":
    unittest.main()