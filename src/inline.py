import re

from src.textnode import TextNode, split_nodes_supported_delimiter_types, text_type_text, text_type_image, \
    text_type_link


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


def extract_markdown_images(text):
    regex = re.compile(r"!\[(.*?)]\((.*?)\)")
    matches = regex.findall(text)
    return matches


def extract_markdown_links(text):
    regex = re.compile(r"\[(.*?)]\((.*?)\)")
    matches = regex.findall(text)
    return matches


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
            continue

        original_text = old_node.text

        images = extract_markdown_images(original_text)
        if len(images) == 0:
            result.append(old_node)
            continue

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], text_type_text))
            result.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, text_type_text))
    return result


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            result.append(old_node)
            continue

        original_text = old_node.text

        links = extract_markdown_links(original_text)
        if len(links) == 0:
            result.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], text_type_text))
            result.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, text_type_text))
    return result


def text_to_textnodes(text):
    text_node = TextNode(text, text_type_text)
    result = [text_node]
    for supported_delimiter in split_nodes_supported_delimiter_types:
        result = split_nodes_delimiter(result,
                                       supported_delimiter,
                                       split_nodes_supported_delimiter_types[supported_delimiter])
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
