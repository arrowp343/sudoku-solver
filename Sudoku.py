import math

class Sudoku:
    def is_square_number(self, n: int):
        if n < 0:
            return False
        root = math.isqrt(n)
        return root**2 == n

    def __init__(self, N: int, input_string):
        if not self.is_square_number(N):
            raise ValueError(f"N must be square number (like 4, 9, 16, but was {N})")
        self.size = N
        self.block_size = math.isqrt(N)
        self.amount_cells = self.size**2
        self.array = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.init_values(input_string)
        self.print()

    def init_values(self, values: str):
        if len(values) != self.amount_cells:
            print(values)
            raise ValueError(f"For N = {self.size}, Input string must be exactly {self.amount_cells} characters long. (was {len(values)})")
        for i in range(self.size):
            for j in range(self.size):
                char = (values[i * self.size + j])
                if char.isdigit():
                    self.array[i][j] = int(char)
                elif char.isupper():
                    self.array[i][j] = ord(char) - ord('A') + 10
                elif char == ".":
                    self.array[i][j] = " "
                else:
                    raise ValueError(f"Invalid charakter: '{char}' (Expected 0,1,2,..,9,A,B,C,... or '.')")

    def print(self):
        hl = self.size * "+---" + "+"
        for i, row in enumerate(self.array):
            print(hl)
            row_values = []
            for cell in row:
                row_values.append(self.convert_cell_to_char(str(cell)))
            print("| " + " | ".join(row_values) + " |")
        print(hl)

    def convert_cell_to_char(self, cell):
        #print("nummer:" + str(cell))
        if cell.isdigit():
            if int(cell) < 10:
                return cell
            else:
                #print(chr(int(cell) - 10 + ord('A')))
                return chr(int(cell) - 10 + ord('A'))
        else:
            return cell
