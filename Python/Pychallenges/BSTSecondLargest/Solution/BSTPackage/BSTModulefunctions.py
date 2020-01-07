from Solution.BSTPackage.BinaryTreeNode import BinaryTreeNode

def assignnewValue(node1, node2):
    if not node2 or not node1 :
        node1 = None
    else:
        node1 = BinaryTreeNode(node2.value)
    return node1


def secondLargestValue(nodetree):
    if not nodetree:
        return None
    else:
        return nodetree.value

def secondLargest(nodetree, maxnodetree, scdnodetree):
    if not nodetree:
        return scdnodetree
    elif maxnodetree == None:
        maxnodetree = assignnewValue(maxnodetree, nodetree)
    elif not maxnodetree == None:
        if nodetree.value > maxnodetree.value:
            scdnodetree = assignnewValue(scdnodetree, maxnodetree)
            maxnodetree = assignnewValue(maxnodetree, nodetree)
        else:
            scdnodetree = assignnewValue(scdnodetree, nodetree)
    if nodetree.right:
        return secondLargest(nodetree.right, maxnodetree, scdnodetree)
    else:
        return secondLargest(nodetree.left, maxnodetree, scdnodetree)

def isaleaf(nodetree):
    if nodetree == None:
        return False
    return not (nodetree.left or nodetree.right)
