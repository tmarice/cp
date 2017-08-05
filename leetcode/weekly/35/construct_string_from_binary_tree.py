

class Solution(object):

   def tree2str(self, t):
        if t is None:
            return ""

        if t.left is None and t.right is None:
            return "{0}".format(t.val)
        elif t.left is None:
            return "{0}()({1})".format(t.val, self.tree2str(t.right))
        elif t.right is None:
            return "{0}({1})".format(t.val, self.tree2str(t.left))
        else:
            return "{0}({1})({2})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
