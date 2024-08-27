from collections import defaultdict
def findDuplicateSubtrees(root):
    subtrees = defaultdict(list)
    res = []

    def dfs(node):
        if not node:
            return "null"
        
        s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
        if len(subtrees[s]) == 1:
            res.append(node)
        subtrees[s].append(node)

        return s;
    
    dfs(root)
    return res;
    



findDuplicateSubtrees([1,2,3,4,None,2,4,None,None,4])
findDuplicateSubtrees([2,2,2,3,None,3,None])
