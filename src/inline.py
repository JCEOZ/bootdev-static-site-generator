from src.textnode import TextNode, split_nodes_supported_delimiter_types, text_type_text


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in split_nodes_supported_delimiter_types.values():
        raise ValueError(f"Unsupported text type: {text_type}")
    if delimiter not in split_nodes_supported_delimiter_types:
        return ValueError(f"Unsupported delimiter: {delimiter}")
    result = []
    for old_node in old_nodes:
        # TODO: fix this code - all old_nodes suppose to be TextNode, but TextNode has different text_types and this should be checked if equals text_type_text
        if not isinstance(old_node, TextNode):
            result.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        # TODO: seems like TextNode value can have multiple occurrences of word wrapped with delimiter, not just one
        if len(split_text) != 3:
            raise ValueError(f"Not found opening or closing {delimiter} after splitting {old_node.text}")
        if split_text[0] != "":
            result.append(TextNode(split_text[0], text_type_text))
        result.append(TextNode(split_text[1], text_type))
        if split_text[2] != "":
            result.append(TextNode(split_text[2], text_type_text))

    return result
