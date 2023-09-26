ROWS = 10

grid = []


class Spot:
    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.neighbors = []

    def __str__(self) -> str:
        if self.color == "BLACK":
            return "b"
        elif self.color == "WHITE":
            return "w"


for i in range(ROWS):
    grid.append([])
    for j in range(ROWS):
        grid[i].append(Spot(i, j, "BLACK"))

for i in range(ROWS):
    for j in range(ROWS):
        print(str(grid[i][j]) + " ", end="")
    print("\n")
