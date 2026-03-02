from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        new_nodes = node.text.split(delimiter)
        if len(new_nodes) % 2 != 1:
            raise Exception(f"invalid Markdown syntax, close the delimiter {delimiter}")
        for i in range(len(new_nodes)):
            if i % 2 == 0 and new_nodes[i] != "":
                result.append(TextNode(new_nodes[i], TextType.TEXT))
            if i % 2 == 1:
                if new_nodes[i] == "":
                    raise ValueError("Empty markdown texts")
                result.append(TextNode(new_nodes[i], text_type))
    return result


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        i = 0
        while len(text) != 0 and i < len(images):
            alt_text = images[i][0]
            image_url = images[i][1]
            sections = text.split(f'![{alt_text}]({image_url})', 1) #split once
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            text = sections[1]
            i += 1
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        i = 0
        new_nodes = []
        while 0 != len(text) and i < len(links):
            alt_text = links[i][0]
            link_url = links[i][1]
            sections = text.split(f'[{alt_text}]({link_url})', 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.LINK, link_url))
            text = sections[1]
            i += 1
    return new_nodes


def extract_markdown_images(text):
    result = []
    alt_text = re.findall(r'!\[(.*?)\]', text)
    img_links = re.findall(r'\((.*?)\)', text)
    if len(alt_text) != len(img_links):
        raise ValueError("incorrect image markdown text")
    for i in range(len(alt_text)):
        result.append((alt_text[i],img_links[i]))
    return result


def extract_markdown_links(text):
    result = []
    alt_text = re.findall(r'(?<!!)\[(.*?)\]', text)
    links = re.findall(r'\((.*?)\)', text)
    if (len(alt_text)!= len(links)):
        raise ValueError("incorrect link markdown text")
    for i in range(len(alt_text)):
        result.append((alt_text[i],links[i]))
    return result
