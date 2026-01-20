from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if not self.tag:
      raise ValueError("invalid HTML: no tag")
    if len(self.children) < 1:
      raise ValueError("invalid HTML: no children")
    children_html = ""
    for child in self.children:
      try:
        children_html += child.to_html()
      except Exception as e:
        print("ERRO no child index:", child)
        print("Tipo:", type(child))
        print("Dict:", getattr(child, "__dict__", None))
        raise

    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"