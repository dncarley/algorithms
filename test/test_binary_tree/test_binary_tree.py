from binary_tree import BinaryTree


def test_binary_tree_pre_order():

	binary_tree = BinaryTree()
	binary_tree.insert(binary_tree.root, 1)
	binary_tree.insert(binary_tree.root, 2)
	binary_tree.insert(binary_tree.root, 4)
	binary_tree.insert(binary_tree.root, 3)
	binary_tree.insert(binary_tree.root, 2)
	binary_tree.insert(binary_tree.root, 3)

	array = binary_tree.pre_order(binary_tree.root)
	pre_order = [1, 2, 2, 4, 3, 3]
	assert array == pre_order, 'binary tree not pre-order:\n{0}'.format(array)
	
def test_binary_tree_in_order():

	binary_tree = BinaryTree()
	binary_tree.insert(binary_tree.root, 1)
	binary_tree.insert(binary_tree.root, 2)
	binary_tree.insert(binary_tree.root, 4)
	binary_tree.insert(binary_tree.root, 3)
	binary_tree.insert(binary_tree.root, 2)
	binary_tree.insert(binary_tree.root, 3)

	array = binary_tree.in_order(binary_tree.root)
	in_order = [1, 2, 2, 3, 3, 4]
	assert array == in_order, 'binary tree not in-order:\n{0}'.format(array)