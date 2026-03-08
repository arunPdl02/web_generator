from textnode import TextNode, TextType
from md_to_html import markdown_to_html_node

def main():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

### This is a heading with **bolded** for extra emphasis

```
This is text that _should_ remain
the **same** even with inline stuff
```

> This is a
> long quote

1. this is bullet1
2. this is bullet2
3. this is bullet3

"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)


if __name__ == "__main__":
    main()