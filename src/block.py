import itertools

from src.inline import text_to_textnodes
from src.parentnode import ParentNode

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
    for i in range(0, len(lines)):
        prefix = f"{i + 1}. "
        if not lines[i].startswith(prefix):
            return False
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children_nodes.append(__heading_block_to_html_node__(block))
        if block_type == block_type_code:
            children_nodes.append(__code_block_to_html_node__(block))
        if block_type == block_type_quote:
            children_nodes.append(__quote_block_to_html_node__(block))
        if block_type == block_type_unordered_list:
            children_nodes.append(__unordered_list_block_to_html_node__(block))
        if block_type == block_type_ordered_list:
            children_nodes.append(__ordered_list_block_to_html_node__(block))
        if block_type == block_type_paragraph:
            children_nodes.append(__paragraph_block_to_html_node__(block))
    top_level_html_node = ParentNode(tag="div", children=children_nodes)
    return top_level_html_node


def __text_nodes_to_html_nodes__(text_nodes):
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node.to_html_node())
    return html_nodes


def __heading_block_to_html_node__(block):
    tag = ""
    text = ""
    if block.startswith("# "):
        tag = "h1"
        # stripping leading "# "
        text = block[len("# "):]
    if block.startswith("## "):
        tag = "h2"
        # stripping leading "## "
        text = block[len("## "):]
    if block.startswith("### "):
        tag = "h3"
        # stripping leading "### "
        text = block[len("### "):]
    if block.startswith("#### "):
        tag = "h4"
        # stripping leading "#### "
        text = block[len("#### "):]
    if block.startswith("##### "):
        tag = "h5"
        # stripping leading "##### "
        text = block[len("##### "):]
    if block.startswith("###### "):
        tag = "h6"
        # stripping leading "###### "
        text = block[len("###### "):]
    children_text_nodes = text_to_textnodes(text)
    children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
    return ParentNode(tag=tag, children=children_html_nodes)


def __code_block_to_html_node__(block):
    # Stripping leading and trailing "```"
    text = block[4:-3]
    children_text_nodes = text_to_textnodes(text)
    children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
    code_node = ParentNode(tag="code", children=children_html_nodes)
    pre_node = ParentNode(tag="pre", children=[code_node])
    return pre_node


def __quote_block_to_html_node__(block):
    lines = block.split('\n')
    strip_lines = []
    for line in lines:
        strip_lines.append(line.lstrip(">").strip())
    text = " ".join(strip_lines)
    children_text_nodes = text_to_textnodes(text)
    children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
    return ParentNode(tag="blockquote", children=children_html_nodes)


def __unordered_list_block_to_html_node__(block):
    li_nodes = []
    lines = block.split('\n')
    for line in lines:
        #stripping leading "* " or "- "
        text = line[2:]
        children_text_nodes = text_to_textnodes(text)
        children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
        li_nodes.append(ParentNode(tag="li", children=children_html_nodes))
    ul_node = ParentNode(tag="ul", children=li_nodes)
    return ul_node


def __ordered_list_block_to_html_node__(block):
    li_nodes = []
    lines = block.split('\n')
    for line in lines:
        text_start_index = line.index(". ") + 2
        # stripping "X. " where "X" is list order number
        text = line[text_start_index:]
        children_text_nodes = text_to_textnodes(text)
        children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
        li_nodes.append(ParentNode(tag="li", children=children_html_nodes))
    ol_node = ParentNode(tag="ol", children=li_nodes)
    return ol_node


def __paragraph_block_to_html_node__(block):
    lines = block.split('\n')
    text = " ".join(lines)
    children_text_nodes = text_to_textnodes(text)
    children_html_nodes = __text_nodes_to_html_nodes__(children_text_nodes)
    return ParentNode(tag="p", children=children_html_nodes)
