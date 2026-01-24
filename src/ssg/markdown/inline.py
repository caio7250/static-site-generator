import re
from ..nodes.text import TextNode, TextType

def text_to_textnodes(text):
  node = [TextNode(text, TextType.TEXT)]
  nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_links(nodes)
  nodes = split_nodes_image(nodes)
  return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  final_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      final_list.append(node)
      continue

    splitted_list = node.text.split(delimiter)
    nodes_list = []
    if len(splitted_list) % 2 == 0:
      raise Exception("That's invalid Markdown syntax")
    for index,item in enumerate(splitted_list):
      if item == "":
        continue
      nodes_list.append(TextNode(item, TextType.TEXT if index % 2 == 0 else text_type))
    final_list.extend(nodes_list)
  return final_list

def split_nodes_image(old_nodes):
  nodes_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      nodes_list.append(node)
      continue
    images = extract_markdown_images(node.text)
    current_string = node.text
    if len(images) == 0:
      nodes_list.append(node)
      continue
    for item in images:
      word_list = current_string.split(f"![{item[0]}]({item[1]})", maxsplit=1)
      if len(word_list) != 2:
        raise ValueError("invalid markdown, image section not closed")
      current_string = word_list[1]
      if word_list[0] != "":
        nodes_list.append(TextNode(word_list[0], TextType.TEXT))
      nodes_list.append(TextNode(item[0], TextType.IMAGE, item[1]))
    if current_string != "":
      nodes_list.append(TextNode(current_string, TextType.TEXT))
  return nodes_list

def split_nodes_links(old_nodes):
  nodes_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      nodes_list.append(node)
      continue
    links = extract_markdown_links(node.text)
    current_string = node.text
    if len(links) == 0:
      nodes_list.append(node)
      continue
    for item in links:
      word_list = current_string.split(f"[{item[0]}]({item[1]})", maxsplit=1)
      if len(word_list) != 2:
        raise ValueError("invalid markdown, link section not closed")
      current_string = word_list[1]
      if word_list[0] != "":
        nodes_list.append(TextNode(word_list[0], TextType.TEXT))
      nodes_list.append(TextNode(item[0], TextType.LINK, item[1]))
    if current_string != "":
      nodes_list.append(TextNode(current_string, TextType.TEXT))
  return nodes_list

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
