from pysat.solvers import Solver
from Sudoku import *

class Sudoku_Solver:
    def __init__(self):
        pass

    def solve(self, sudoku: Sudoku):
        solver = Solver()


        # 3-dimensionale Matrix der Aussagenlogischen Variablen X_(z,s,w)
        x_zsw = []

        for z in range(sudoku.size):        # für jede zeile
            row_variables = []
            for s in range(sudoku.size):    # für jede zelle ( spalte in einer zeile )
                cell_variables = []
                for w in range(9):          # für jeden wert, den eine Zelle annehmen kann
                    cell_variables.append((z * sudoku.size + s) * 9 + w + 1)
                row_variables.append(cell_variables)
            x_zsw.append(row_variables)

        #print(x_zsw)
        for row in x_zsw:
            for cell in row:
                solver.add_clause(cell)


        # jeder wert darf in jeder zeile nur einmal vorkommen:

        for w in range(9):
            for row in x_zsw:    
                for i, cell_i in enumerate(row):
                    #print(i)
                    for j, cell_j in enumerate(row[i+1:]):
                        #print(f"compare cell{i+1} with cell {j+i+2}")
                        solver.add_clause([-cell_i[w], -cell_j[w]])

        #tbd: jeder wert darf in jeder spalte nur einmal vorkommen



        #tbd: jeder wert darf in jedem block nur einmal vorkommen



        #tbd: zuweisen der vorgegebenen werte



        # example:
        # solver.add_clause([-1, 2])  # (-1 OR 2)
        # solver.add_clause([-2, 3])  # (-2 OR 3)
        # solver.add_clause([-3, 1])  # (-3 OR 1)

        solution = solver.solve()
        model = solver.get_model()

        if solution:
            print("SAT")
            output = [[0 for _ in range(sudoku.size)] for _ in range(sudoku.size)]
            for a in range(sudoku.size):
                for b in range(sudoku.size):
                    for c in range(sudoku.size):
                        if model[x_zsw[a][b][c] - 1] > 0:
                            output[a][b] = str(c + 1)

            #tbd: output in sudoku-objekt überführen und printen
            print("Aktualisiertes Array:", output)

        else:
            print("UNSAT")
