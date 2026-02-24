class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        builder = [""]
        for key in self.props:
            builder.append( f'{key}="{self.props[key]}"')
        return ' '.join(builder)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value,props=None):
        super().__init__(tag,value,None,props)


    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError
        builder = []
        for child in self.children:
            builder.append(child.to_html())
        return f'<{self.tag}{self.props_to_html()}>{"".join(builder)}</{self.tag}>'