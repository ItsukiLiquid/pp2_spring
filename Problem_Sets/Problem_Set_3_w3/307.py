# unsolved
class Point():
    def __init__(self, x1, y1, new_x1, new_y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.new_x1 = new_x1
        self.new_y1 = new_y1
        self.x2 = x2
        self.y2 = y2
    def show(self, x1, y1):
        print(f"({x1}, {y1})")
    def move(self, new_x1, new_y1):
        x1 = new_x1
        y1 = new_y1
    def dist(self, x2, y2):
        pass