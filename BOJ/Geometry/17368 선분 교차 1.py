x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

def ccw(P, Q, R):
    direction = (Q[0]-P[0])*(R[1]-P[1]) - (Q[1]-P[1])*(R[0]-P[0])
    if direction > 0:
        return 1
    if direction < 0:
        return -1
    if direction == 0:
        return 0

if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
    print(1)
else:
    print(0)

