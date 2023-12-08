class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def serialize_helper(node):
            if not node:
                return "None,"
            return str(node.val) + "," + serialize_helper(node.left) + serialize_helper(node.right)
        
        return serialize_helper(root)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def deserialize_helper(data_list):
            if data_list[0] == "None":
                data_list.pop(0)
                return None
            root = TreeNode(int(data_list[0]))
            data_list.pop(0)
            root.left = deserialize_helper(data_list)
            root.right = deserialize_helper(data_list)
            return root

        data_list = data.split(',')
        return deserialize_helper(data_list)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
