class Solution(object):
    def isSubtree(self, s, t):
       
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and 
                   isSame(x.left, y.left) and 
                   isSame(x.right, y.right)

        def isSameTree(s, t):
            return s != None and 
                   (isSame(s, t) or 
                    isSameTree(s.left, t) or 
                    isSameTree(s.right, t))

        return isSameTree(s, t)
