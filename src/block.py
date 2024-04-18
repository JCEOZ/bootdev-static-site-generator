import itertools

from src.htmlnode import HTMLNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered-list"
block_type_ordered_list = "ordered-list"


def markdown_to_blocks(markdown):
    blocks = []
    tmp = []
    lines = markdown.split('\n')
    for line in lines:
        if line.strip() == "" and len(tmp) > 0:
            blocks.append("\n".join(tmp))
            tmp = []
            continue
        if line.strip() != "":
            tmp.append(line.strip())
    if len(tmp) > 0:
        blocks.append("\n".join(tmp))
    return blocks


def block_to_block_type(block):
    if __is_block_type_heading__(block): return block_type_heading
    if __is_block_type_code__(block): return block_type_code
    if __is_block_type_quote__(block): return block_type_quote
    if __is_block_type_unordered_list__(block): return block_type_unordered_list
    if __is_block_type_ordered_list__(block): return block_type_ordered_list
    return block_type_paragraph

def __is_block_type_heading__(block_type):
    lines = block_type.split('\n')
    if len(lines) != 1: return False
    line = lines[0]
    for i in range(1, 7):
        prefix = "".join(itertools.repeat("#", i))
        if line.startswith(f"{prefix} "):
            return True
    return False


def __is_block_type_code__(block_type):
    return block_type.startswith("```") and block_type.endswith("```")


def __is_block_type_quote__(block_type):
    lines = block_type.split('\n')
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def __is_block_type_unordered_list__(block_type):
    lines = block_type.split('\n')
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True


def __is_block_type_ordered_list__(block_type):
    lines = block_type.split('\n')
    for i in range(1, len(lines)):
        prefix = f"{i}. "
        if not lines[i - 1].startswith(prefix):
            return False
    return True

# TODO: refactor to use ParentNodes and TextNodes instead of HTMLNode
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            html_nodes.append(__heading_block_to_html_node__(block))
        if block_type == block_type_code:
            html_nodes.append(__code_block_to_html_node__(block))
        if block_type == block_type_quote:
            html_nodes.append(__quote_block_to_html_node__(block))
        if block_type == block_type_unordered_list:
            html_nodes.append(__unordered_list_block_to_html_node__(block))
        if block_type == block_type_ordered_list:
            html_nodes.append(__ordered_list_block_to_html_node__(block))
        if block_type == block_type_paragraph:
            html_nodes.append(__paragraph_block_to_html_node__(block))
    top_level_html_node = HTMLNode(tag="<div>", children=html_nodes)
    return top_level_html_node


def __heading_block_to_html_node__(block):
    tag = ""
    if block.startswith("# "): tag = "<h1>"
    if block.startswith("## "): tag = "<h2>"
    if block.startswith("### "): tag = "<h3>"
    if block.startswith("#### "): tag = "<h4>"
    if block.startswith("##### "): tag = "<h5>"
    if block.startswith("###### "): tag = "<h6>"
    return HTMLNode(tag=tag, value=block)


def __code_block_to_html_node__(block):
    child_node = HTMLNode(tag="<code>", value=block)
    parent_node = HTMLNode(tag="<pre>", children=[child_node])
    return parent_node


def __quote_block_to_html_node__(block):
    return HTMLNode(tag="<blockquote", value=block)


def __unordered_list_block_to_html_node__(block):
    children_nodes = []
    lines = block.split('\n')
    for line in lines:
        children_nodes.append(HTMLNode(tag="<li>", value=line))
    parent_node = HTMLNode(tag="<ul>", children=children_nodes)
    return parent_node


def __ordered_list_block_to_html_node__(block):
    children_nodes = []
    lines = block.split('\n')
    for line in lines:
        children_nodes.append(HTMLNode(tag="<li>", value=line))
    parent_node = HTMLNode(tag="<ol>", children=children_nodes)
    return parent_node


def __paragraph_block_to_html_node__(block):
    return HTMLNode(tag="<p>", value=block)
