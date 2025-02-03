from htmlnode import Htmlnode

class leafnode(Htmlnode):
    def __init__(self, tag, value: str, props = None):
        super().__init__(tag,value,None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leafnodes need a value")
        if self.tag == None:
            return self.value

        attributes = ""
        if self.props is not None:
            for prop in self.props:
                attributes += f" {prop}=\"{self.props[prop]}\""

        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"




