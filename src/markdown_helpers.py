from parentnode import ParentNode
from block_helpers import block_to_html_node, heading_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:

        if block.startswith("# "):
            heading_node = heading_to_html_node(block)
            return heading_node.to_html()
        
        raise Exception('Title not found in document')