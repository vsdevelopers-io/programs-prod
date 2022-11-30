

class Node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 


def VSDpostorder(root):
    if root:
        VSDpostorder(root.left)
        VSDpostorder(root.right)
        print(root.data)


if __name__=="__main__":
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60)
    root.right.right=Node(70)

    VSDpostorder(root)