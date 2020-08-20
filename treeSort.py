node = 31   #perfect binary tree의 가장 큰 node(혹은 tree내의 node의 총 개수)

A = node + 1    #level계산을 위한 변수
stairs = 0  #총 level의 수를 저장하는 변수
while A != 1:
    A //= 2
    stairs += 1

level = [[] for row in range(stairs)]   #각 level마다 해당하는 nodes를 저장할 2차원 list

PresentLevel = stairs   #현재 위치의 level
step = 2    #공차
MyNode = 1  #1부터 시작한다.

while len(level[0]) == 0:   #최상위 level에 원소가 채워질때까지
    while MyNode < node + 1:    #가장 큰 node보다 작으면
        level[PresentLevel - 1].append(MyNode)  #마지막 level부터 역순으로 node들을 저장한다.
        MyNode += step  #이 때, step이라는 공차만큼 커진다.
    step *= 2   #step은 level이 증가할 때마다 2배가 된다.
    PresentLevel -= 1   #level은 역순으로 간다.
    MyNode = 2**(stairs - PresentLevel) #각 level의 가장 왼쪽 node
print("level 순으로 정렬시:")
print(level)