from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('tag required for parent node')
        
        if self.children == None:
            raise ValueError('children required for parent node')
        
        children_string = ""

        for child_node in self.children:
            children_string += child_node.to_html()

        prop_html = self.props_to_html()

        return f"<{self.tag}{prop_html}>{children_string}</{self.tag}>"