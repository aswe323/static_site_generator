from htmlnode import Htmlnode

class Parentnode(Htmlnode):
    def __init__(self, tag:str, children: list[Htmlnode], props: dict = {}):
        super().__init__(tag, None, children, props )

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if (self.children is None or len(self.children) == 0):
            raise ValueError("ParentNode must have children")
        
        value = ""
        for child in self.children:
            value += child.to_html()
        
        attributes = ""
        if self.props is not None and len(self.props) > 0:
            for prop in self.props:
                attributes += f" {prop}=\"{self.props[prop]}\""

        return f"<{self.tag}{attributes}>{value}</{self.tag}>"


