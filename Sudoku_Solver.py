from pysat.solvers import Solver
from Sudoku import *
import time

class Sudoku_Solver:
    def __init__(self):
        pass

    def solve(self, sudoku: Sudoku):
        start_time = time.time()
        solver = Solver(name="g4")

        clauses = []

        # 3-dimensionale Matrix der Aussagenlogischen Variablen X_(z,s,w)
        x_zsw = []
        len_x_zsw = 0

        for z in range(sudoku.size):        # für jede zeile
            row_variables = []
            for s in range(sudoku.size):    # für jede zelle ( spalte in einer zeile )
                cell_variables = []
                for w in range(sudoku.size):          # für jeden wert, den eine Zelle annehmen kann
                    cell_variables.append((z * sudoku.size + s) * sudoku.size + w + 1)
                    len_x_zsw += 1
                row_variables.append(cell_variables)
            x_zsw.append(row_variables)

        #print(x_zsw)
        for row in x_zsw:
            for cell in row:
                solver.add_clause(cell)

        # jeder wert darf in jeder zeile nur einmal vorkommen:
        print("jeder wert darf in jeder zeile nur einmal vorkommen:")
        for w in range(sudoku.size):
            for row in range(sudoku.size):
                for i in range(sudoku.size):
                    #print(i+1)
                    for j in range(i+1, sudoku.size):
                        #print(f"compare: {i+1}-{j+1}")
                        solver.add_clause([-x_zsw[row][i][w], -x_zsw[row][j][w]])
                        clauses.append([-x_zsw[row][i][w], -x_zsw[row][j][w]])

        # jeder wert darf in jeder spalte nur einmal vorkommen
        print("jeder wert darf in jeder spalte nur einmal vorkommen")
        for w in range(sudoku.size):
            for column in range(sudoku.size):
                for i in range(sudoku.size):
                    #print(i+1)
                    for j in range(i+1, sudoku.size):
                        #print(f"compare {i+1}-{j+1}")
                        solver.add_clause([-x_zsw[i][column][w], -x_zsw[j][column][w]])
                        clauses.append([-x_zsw[i][column][w], -x_zsw[j][column][w]])

        # jeder wert darf in jedem block nur einmal vorkommen
        print("jeder wert darf in jedem block nur einmal vorkommen")
        for w in range(sudoku.size):
            for b_row in range(3):          # 3 block-reihen
                for b_block in range(3):   # 3 block-spalten
                    #print(f"block: {b_row}_{b_block}")
                    list_of_elemements_in_block = []
                    #list_of_elemements_in_block_as_int_tupel = [] 
                    for row in range(sudoku.block_size):
                        for column in range(sudoku.block_size):
                            #list_of_elemements_in_block_as_int_tupel.append((b_row * sudoku.block_size + row + 1, b_block * sudoku.block_size + column + 1))
                            list_of_elemements_in_block.append(x_zsw[b_row * sudoku.block_size + row][b_block * sudoku.block_size + column][w])
                    #print(list_of_elemements_in_block_as_int_tupel)
                    for i in range(sudoku.size):
                        #print(f"element{i}")
                        for j in range(i+1, sudoku.size):
                            #print(f"compare {list_of_elemements_in_block_as_int_tupel[i]}-{list_of_elemements_in_block_as_int_tupel[j]}")
                            solver.add_clause([-list_of_elemements_in_block[i], -list_of_elemements_in_block[j]])
                            clauses.append([-list_of_elemements_in_block[i], -list_of_elemements_in_block[j]])

        # zuweisen der vorgegebenen werte
        for i, row in enumerate(sudoku.array):
            for j, cell in enumerate(row):
                if cell != " ":
                    solver.add_clause([x_zsw[i][j][cell-1]])
                    clauses.append([x_zsw[i][j][cell-1]])
        
        solution = solver.solve()
        model = solver.get_model()
        if solution:
            print("SAT")
            finished_sudoku_string = ""
            for a in range(sudoku.size):
                for b in range(sudoku.size):
                    for c in range(sudoku.size):
                        if model[x_zsw[a][b][c] - 1] > 0:
                            value = c + 1
                            if value > 9:
                                value = chr(value - 10 + ord('A'))
                            finished_sudoku_string += str(value)
            finished_sudoku = Sudoku(sudoku.size, finished_sudoku_string)
            self.write_dimacs_to_file(clauses, len_x_zsw)
        else:
            print("UNSAT")

        finished_time = time.time()
        diff_time = finished_time - start_time
        print(f"Processing Time: {diff_time} Seconds")
    
    def write_dimacs_to_file(self, clauses, num_vars):
        filename = f"dimacs_{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())}.dimacs.txt"
        with open(filename, 'w') as file:
            file.write(f"p cnf {num_vars} {len(clauses)}\n")
            for clause in clauses:
                file.write(" ".join(map(str, clause)) + " 0\n")

