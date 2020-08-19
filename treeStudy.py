A = 10
stack = []
status = 1

def findingPre():
    global status
    global A
    global stack
    if len(stack) == A:
        return
    elif status not in stack:
        stack.append(status)
        findingPre()
    else:
        if status*2 not in stack and status*2 <= A:
            status *= 2
            stack.append(status)
            findingPre()
        elif (status*2)+1 not in stack and (status*2)+1 <= A:
            status = (status*2)+1
            stack.append(status)
            findingPre()
        else:
            status //= 2
            findingPre()

def findingIn():
    global status
    global A
    global stack
    print(status)
    if len(stack) == A:
        return
    elif status*2 not in stack and status*2 <= A:   #leaf node가 아니면 계속 2로 나눠줌
        status *= 2
        findingIn()
    elif status*2 not in stack and status*2 > A:    #leaf node라면 탐색 후, root로 돌아감
        stack.append(status)
        status //= 2
        findingIn()
    elif status*2 in stack and status not in stack: #root를 탐색해줌
        stack.append(status)
        findingIn()
    elif status in stack and status*2 + 1 <= A and status*2 + 1 not in stack:   #left와 root를 탐색했다면 right를 방문함.
        status = status*2 +1
        findingIn()
    else:   #이외의 경우는 계속 부모 node로 상승
        status //= 2
        findingIn()

def findingPost():
    global status
    global A
    global stack
    # print(status)
    if len(stack) == A:
        return
    elif status*2 not in stack and status*2 <= A:   #leaf node가 아니면 계속 2로 나눠줌
        status *= 2
        findingPost()
    elif status*2 not in stack and status*2 > A:    #leaf node라면 탐색 후, root로 돌아감
        stack.append(status)
        status //= 2
        findingPost()
    elif status*2+1 not in stack and status*2+1 <= A:   #left를 탐색한 root상태에서 right가 있으면 방문
        status = status*2+1
        findingPost()
    else:   #나머지 경우에는 계속 부모 node로 올라감
        stack.append(status)
        status //= 2
        findingPost()


# findingPre()
# findingIn()
findingPost()
print('new')
print(stack)