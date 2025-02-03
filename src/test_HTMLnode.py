import unittest

from htmlnode import Htmlnode 


class TestTextNode(unittest.TestCase):
    # tag str, value str, children Htmlnode, props dict.
    def test_eq(self):
        node = Htmlnode()
        node2 = Htmlnode()
        self.assertEqual(node, node2)

        test_dict = {}

        node2 = Htmlnode( children = node, props = test_dict)
        node3 = Htmlnode( children = node, props = test_dict)
        self.assertEqual(node3, node2)

        props1 = {"test_element":"test_element_value"}
        props2 = {"test_element":"test_element_value"}

        node1 = Htmlnode(props = props1)
        node2extras = Htmlnode(props = props2)
        self.assertEqual(node1,node2extras  )

    def test_not_eq(self):

        node = Htmlnode(tag = "tagged")
        node_extra = Htmlnode()

        node1 = Htmlnode(children = node)
        node2 = Htmlnode(children = node_extra)

        self.assertNotEqual(node1.children, node2.children)
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()
