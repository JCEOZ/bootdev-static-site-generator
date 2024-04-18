import itertools


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
