from blocknode import BlockType, block_to_block_type,  markdown_to_blocks

from textnode import text_node_to_html_node, TextType, TextNode

from inline_markdown import text_to_textnodes

from htmlnode import ParentNode

import re


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(paragraph_to_html_nodes(block))

            case BlockType.HEADING:
                children.append(heading_to_html_nodes(block))

            case BlockType.CODE:
                children.append(code_to_html_nodes(block))
            
            case BlockType.QUOTE:
                children.append(quote_to_html_nodes(block))
            
            case BlockType.ULIST:
                children.append(ulist_to_html_nodes(block))
            
            case BlockType.OLIST:
                children.append(olist_to_html_nodes(block))                

    return ParentNode("div", children)


def text_to_text_html(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def paragraph_to_html_nodes(block):
    html_nodes = text_to_text_html(block.replace("\n", " "))
    return ParentNode("p", html_nodes)


def heading_to_html_nodes(block):
    html_nodes = text_to_text_html(block.replace("#", "").lstrip())
    i = 0
    while(block[i] == "#"):
        i += 1
    return ParentNode(f'h{i}', html_nodes)


def code_to_html_nodes(block):
    code_content = block[4:-3]
    code_text_node = TextNode(code_content, TextType.CODE)
    code_html = text_node_to_html_node(code_text_node)
    return ParentNode("pre",[code_html])


def quote_to_html_nodes(block):
    quote_content = block.lstrip("> ").replace("\n> ", " ").replace("\n", " ")
    html_nodes = text_to_text_html(quote_content)
    return ParentNode("blockquote", html_nodes)


def ulist_to_html_nodes(block):
    ulist_bullets = block.lstrip("- ").split("\n- ")
    bullet_htmls = list_html(ulist_bullets)
    return ParentNode("ul", bullet_htmls)


def olist_to_html_nodes(block):
    olist_bullets = block.lstrip("1. ")
    olist_bullets = re.split(r'\n\d. ', olist_bullets)
    bullet_htmls = list_html(olist_bullets)
    return ParentNode("ol", bullet_htmls)

def list_html(bullet_list):
    result = []
    for bullet in bullet_list:
        result.append(
            ParentNode("li", text_to_text_html(bullet))
        )
    return result