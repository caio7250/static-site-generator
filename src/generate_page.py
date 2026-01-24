import os
from block_markdown import markdown_to_html_node
from extract_title import extract_title


def _root_path(dest_path, dest_root):
  dest_dir = os.path.dirname(dest_path)
  rel_path = os.path.relpath(dest_root, dest_dir)
  if rel_path == ".":
    return "./"
  return rel_path.replace(os.sep, "/").rstrip("/") + "/"


def generate_page(from_path, template_path, dest_path, dest_root, base_path):
  print(f"Generating page from from_path to dest_path using template_path")

  with open(from_path, "r") as archieve:
    markdown_content = archieve.read()

  with open(template_path, "r") as archieve:
    template_content = archieve.read()

  html = markdown_to_html_node(markdown_content).to_html()
  title = extract_title(markdown_content)

  if base_path and base_path != "/":
    root_path = base_path if base_path.endswith("/") else f"{base_path}/"
  else:
    root_path = _root_path(dest_path, dest_root)

  template_content = template_content.replace("{{ Title }}", title)
  template_content = template_content.replace("{{ Content }}", html)
  template_content = template_content.replace("{{ RootPath }}", root_path)
  template_content = template_content.replace('href="/', f'href="{root_path}')
  template_content = template_content.replace('src="/', f'src="{root_path}')

  os.makedirs(os.path.dirname(dest_path), exist_ok=True)
  with open(dest_path, "w") as f:
    f.write(template_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path, dest_root=None):
  if dest_root is None:
    dest_root = dest_dir_path
  files_in_dir = os.listdir(dir_path_content)
  for file in files_in_dir:
    file_dest_path = os.path.join(dest_dir_path, file)
    file_dir_path = os.path.join(dir_path_content, file)

    if os.path.isfile(file_dir_path):
      file_dest_path = file_dest_path.replace(".md", ".html")
      generate_page(file_dir_path, template_path, file_dest_path, dest_root, base_path)
      continue

    generate_pages_recursive(file_dir_path, template_path, file_dest_path, base_path, dest_root)
