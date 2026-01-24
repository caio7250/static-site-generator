def extract_title(markdown):
  lines = markdown.split("\n")
  for line in lines:
    if line[0:2] == "# ":
      return line[1:].strip()
  raise Exception("There's no title in this markdown")