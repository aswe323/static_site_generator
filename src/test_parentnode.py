import unittest

from parentnode import Parentnode
from leafnode import leafnode


class Testleafnode(unittest.TestCase):
    def test_eq(self):

        pnode0 = Parentnode("p",
                        [leafnode("ul","item one"), 
                         leafnode("ul","item two"),
                         leafnode("ul","item 3")
                         ]
                            )
        pnode0_text_rep = "<p><ul>item one</ul><ul>item two</ul><ul>item 3</ul></p>"
        pnode1 = Parentnode("ol",[pnode0])
        self.assertEqual(pnode0.to_html(), pnode0_text_rep)
        pnode1_text_rep = f"<ol>{pnode0_text_rep}</ol>"
        self.assertEqual(pnode1.to_html(), pnode1_text_rep)



if __name__ == "__main__":
    unittest.main()
