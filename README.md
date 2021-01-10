# N-Queens-Puzzle

The N-Queen-Puzzle is a problem of placing N chess queens on an NxN chessboard so that no queen can attack another queen.
For recall, a queen can move in a straight line, vertically or horizontally or diagonally and on as many squares as she wants.

This project contains two algorithms to solve the N-Queen-Puzzle : 
- The first one is "solve_n_queen_small" and uses a backtracking algorithm. This algorithm is only optimized for N < 25 queens.
- The second one is "solve_n_queen_big" and uses a min-conflicts algorithm, much more efficient than the backtracking. It can go up to N > 100 queens and even further. If the algorithm does not find a solution for N > 3, try to increase the max_step.

There is a function named "solve_n_queen_all_soluce" that computes all the solutions for a given N using the backtracking algorithm. It can be used for N <= 14.

There are also 3 utility functions : 
- "print_board" that display the chessboard
- "can_t_attack" a function indicating if no queen can attack each other
- "is_soluce" a function indicating whether the solution has been found and the number of queen.

## Requirement
- Python 3.9.0
- pytest 6.1.2

## Projet AAV - DUT Informatique - IUT de Paris
### Team :
- LIN Xiumin (github : Xiumin-Lin)
- VAN Steven (github : steven-van)