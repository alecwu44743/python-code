class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

sx, sy = map(int , input().split())

pos = Position(sx, sy)

stack = []
stack.append(pos)
print(pos.x)
print(pos.y)
print(len(stack))