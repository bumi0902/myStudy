stack = []


def inorder(arr, idx):
    if(idx >= len(arr)):
        return
    inorder(arr, idx*2)
    stack.append(arr[idx])
    inorder(arr, idx*2 + 1)

def preorder(arr, idx):
    if(idx >= len(arr)):
        return
    stack.append(arr[idx])
    preorder(arr, idx*2)
    preorder(arr, idx*2 + 1)

def postorder(arr, idx):
    if(idx >= len(arr)):
        return
    postorder(arr, idx*2)
    postorder(arr, idx*2 + 1)
    stack.append(arr[idx])

arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# preorder(arr1, 1)
# inorder(arr1, 1)
postorder(arr1, 1)
print(stack)