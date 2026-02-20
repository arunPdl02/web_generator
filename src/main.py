from textnode import TextNode, TextType

def main():
    my_text = TextNode("hello world",TextType.ITALIC,"www.helloworld.com" )
    print(my_text)


if __name__ == "__main__":
    main()