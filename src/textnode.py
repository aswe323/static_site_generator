from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE: TextType, URL = None):
        self.text = TEXT
        self.text_type = TEXT_TYPE.value
        self.url = URL

    def getTextType(self):
        return self.text_type

    def __eq__(self , obj):
        if (obj.text == self.text and
            self.getTextType() == obj.getTextType() and
            self.url == obj.url):
            return True

        return False
    def __repr__(self):
        return f"TextNode({self.text} {self.getTextType()} {self.url})"

