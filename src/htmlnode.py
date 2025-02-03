
class Htmlnode():
    def __init__(self, 
                 tag = None, 
                 value = None, 
                 children = None, 
                 props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Should be overrided")

    def props_to_html(self):
        output = ""
        for key in self.props:
            output += f" \"{key}\"=\"{self.props[key]}\n"
        actual_output = output.replace("\n", "")
        return actual_output

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"

    def __eq__(self, obj):
        if (self.tag == obj.tag and
            self.value == obj.value and
            self.children == obj.children and
            self.__repr__() == obj.__repr__()
                ):
            return True
        return False
