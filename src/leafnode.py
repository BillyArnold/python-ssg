from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('all leaf nodes require a value')
        
        if self.tag == None:
            return self.value
        
        prop_html = self.props_to_html()
        
        return f"<{self.tag}{prop_html}>{self.value}</{self.tag}>"