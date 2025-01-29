import unittest

from htmlnode import HTMLnode


class TestTextNode(unittest.TestCase):
    # tag str, value str, children HTMLnode, props dict.
    def test_eq(self):
        node = HTMLnode()
        node2 = HTMLnode()
        self.assertEqual(node, node2)

        test_dict = {}

        node2 = HTMLnode( children = node, props = test_dict)
        node3 = HTMLnode( children = node, props = test_dict)
        self.assertEqual(node3, node2)

        props1 = {"test_element":"test_element_value"}
        props2 = {"test_element":"test_element_value"}

        node1 = HTMLnode(props = props1)
        node2extras = HTMLnode(props = props2)
        self.assertEqual(node1,node2extras  )

    def test_not_eq(self):

        node = HTMLnode(tag = "tagged")
        node_extra = HTMLnode()

        node1 = HTMLnode(children = node)
        node2 = HTMLnode(children = node_extra)

        self.assertNotEqual(node1.children, node2.children)
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()
