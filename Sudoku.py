class Sudoku:
    def __init__(self, input_string):
        self.array = [[0 for _ in range(9)] for _ in range(9)]
        self.init_values(input_string)
        self.print()

    def init_values(self, values):
        if len(values) != 81:
            raise ValueError("Input string must be exactly 81 characters long.")
        for i in range(9):
            for j in range(9):
                char = values[i * 9 + j]
                if char.isdigit():
                    self.array[i][j] = int(char)
                elif char == ".":
                    self.array[i][j] = " "
                else:
                    raise ValueError(f"Invalid charakter: '{char}' (Expected 0,1,2,..,9 or '.')")

    def print(self):
        hl = "+---+---+---+---+---+---+---+---+---+"
        for i, row in enumerate(self.array):
            print(hl)
            row_display = "| " + " | ".join(f"{cell if cell != 0 else ' '}" for cell in row) + " |"
            print(row_display)
        print(hl)
        