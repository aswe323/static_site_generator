import unittest

from leafnode import leafnode


class Testleafnode(unittest.TestCase):
    def test_eq(self):
        lnode0 = leafnode(None,"para\n graph", None)
        self.assertEqual("para\n graph", lnode0.to_html())

        lnode1 = leafnode("p","para\n graph", None)
        lnode1_html_rep = "<p>para\n graph</p>"
        self.assertEqual(lnode1.to_html(), lnode1_html_rep )

        lnode2 = leafnode("a", "this text", {"href":"www.google.com"})
        lnode3 = leafnode("a", "this text", {"href":"www.google.com"})
        self.assertEqual(lnode2, lnode3)



    def test_not_eq(self):
        lnode1 = leafnode("p","para\n graph", None)
        lnode2 = leafnode("p","look at this\n graph", None)
        self.assertNotEqual(lnode1, lnode2)





if __name__ == "__main__":
    unittest.main()
