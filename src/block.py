
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
