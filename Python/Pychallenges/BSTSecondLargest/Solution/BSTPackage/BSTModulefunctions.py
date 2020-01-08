from Solution.BSTPackage.BinaryTreeNode import BinaryTreeNode

def assignnewValue(node1, node2):
    if not node2:
        node1 = None
    else:
        node1 = BinaryTreeNode(node2.value)
    return node1



def secondSmallestValue(nodetree, minimum_node, scd_minimum_node):
    if not nodetree:
        return scd_minimum_node

    elif not minimum_node:
        minimum_node = assignnewValue(minimum_node, nodetree)
    elif minimum_node:
        if nodetree.value < minimum_node.value:
            scd_minimum_node = assignnewValue(scd_minimum_node, minimum_node)
            minimum_node = assignnewValue(minimum_node, nodetree)
        #elif not scd_minimum_node:
            #scd_minimum_node = assignnewValue(scd_minimum_node, nodetree)
        else:
            #if nodetree.value >= minimum_node.value and nodetree.value < scd_minimum_node.value:
            scd_minimum_node = assignnewValue(scd_minimum_node, nodetree)

    if nodetree.left:
        return secondSmallestValue(nodetree.left, minimum_node, scd_minimum_node)
    else:
        return secondSmallestValue(nodetree.right, minimum_node, scd_minimum_node)





def secondLargestValue(nodetree):
    if not nodetree:
        return None
    else:
        return nodetree.value

def secondLargest(nodetree, maxnodetree, scdnodetree):
    if not nodetree:
        return scdnodetree
    elif not maxnodetree:
        maxnodetree = assignnewValue(maxnodetree, nodetree)
    elif maxnodetree:
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



def maximum_tree(nodetree, maximum_node):
    """ Return the maximum value in the tree or None if does not exist """
    if not nodetree:
        return maximum_node
    elif not maximum_node:
        maximum_node = nodetree
    elif maximum_node:
        if maximum_node.value < nodetree.value:
            maximum_node = assignnewValue(maximum_node, nodetree)
    if nodetree.right:
       return maximum_tree(nodetree.right, maximum_node)
    else:
        return maximum_tree(nodetree.left, maximum_node)


def minimum_tree(nodetree, minimum_node):
    """ Return the minimum value in the tree or None if does not exist """
    if not nodetree:
        return minimum_node
    elif not minimum_node:
        minimum_node = nodetree
    elif minimum_node:
        if minimum_node.value > nodetree.value:
            minimum_node = assignnewValue(minimum_node, nodetree)
    if nodetree.left:
       return minimum_tree(nodetree.left, minimum_node)
    else:
        return minimum_tree(nodetree.right, minimum_node)


