from textnode import *
from htmlnode import Htmlnode
from leafnode import leafnode

def trim_tag(texttype:TextType, text:str):
    if texttype == texttype.NORMAL:
        return text
    tag_letter= {texttype.BOLD:"b",
                 texttype.CODE:"code",
                 texttype.IMAGE:"img",
                 texttype.ITALIC:"i",
                 texttype.LINK:"a",
                 texttype.NORMAL:""
            }
    def extract_attributes():
        nonlocal text
        dic = {}
        attributes = text.split(">")[0].lstrip(f"<{tag_letter[texttype]}").split(" ")
        for attribute in attributes:
            dic[attribute.split("=")[0]] = attribute.split("=")[1]
        return dic
            

    trimmed_text= text.rstrip(f"</{tag_letter[texttype]}>")[text.index(">")+1:]
    return trimmed_text, extract_attributes

def text_node_to_html_node(text_node: TextNode):
    
    value, attributs_getter = trim_tag(text_node.getTextType(), text_node.text)
    match text_node.getTextType():
        case "normal":
            return  leafnode(None, value)
        case "bold":
            return  leafnode("b", value)
        case "italic":
            return  leafnode("i", value)
        case "code":
            return  leafnode("code", value, attributs_getter()  )
        case "link":
            return  leafnode("code", value)
            pass
        case "image":
            pass
        case _:
            pass



    pass

def main():
    pass
main()
