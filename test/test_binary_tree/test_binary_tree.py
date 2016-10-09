from binary_tree import BinaryTree


def test_binary_tree_pre_order():

	binary_tree = BinaryTree()
	binary_tree.insert(binary_tree.root, 1)
	binary_tree.insert(binary_tree.root, 2)
	binary_tree.insert(binary_tree.root, 3)
	binary_tree.insert(binary_tree.root, 4)
	binary_tree.insert(binary_tree.root, 4)
	binary_tree.insert(binary_tree.root, 3)
	binary_tree.insert(binary_tree.root, 4)
	binary_tree.insert(binary_tree.root, -12)
	binary_tree.insert(binary_tree.root, 2**256)

	array = binary_tree.pre_order(binary_tree.root)
	array.pop(0)
	assert sorted(array) == array, 'binary tree not pre-order:\n{0}'.format(array)
	