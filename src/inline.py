from src.textnode import TextNode, split_nodes_supported_delimiter_types, text_type_text


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in split_nodes_supported_delimiter_types.values():
        raise ValueError(f"Unsupported text type: {text_type}")
    if delimiter not in split_nodes_supported_delimiter_types:
        return ValueError(f"Unsupported delimiter: {delimiter}")
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
            continue

        number_of_delimiters = old_node.text.count(delimiter)
        if number_of_delimiters == 0:
            result.append(old_node)
            continue
        if number_of_delimiters % 2 != 0:
            raise ValueError(f"Invalid number of delimiters: \"{delimiter}\" in \"{old_node.text}\"")

        sections = old_node.text.split(delimiter)
        split_nodes = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        result.extend(split_nodes)
    return result
