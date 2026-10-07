import argparse
import numpy as np
import argparse
from plotly.graph_objects import Scatter, Scatter3d, Figure
import json

main_options = """
help - prints entier comma list
ol - list of happened commands
cm - count matrixes
"""

cm_options = """
Choose operation: 
ma - ma = A(ij) + B(ij)
ms - ma = A(ij) - B(ij)
mm - ma = A(ij) * B(jk)
sm - ma = scalar * A(ij)
dm - find matrix determinant
"""

def parse_matrix(s):
    return np.array(json.loads(s))
    
def create_plot(A):
    A = np.atleast_2d(A)
    cols = A.shape[1]
    if cols not in (2, 3):
        print(f"(plot skipped: need 2 or 3 columns, got {cols})")
        return
    A = np.vstack([np.zeros(cols), A])
    fig = Figure()
    if cols == 2:
        fig.add_trace(Scatter(x=A[:,0], y=A[:,1], mode='lines+markers'))
    else:
        fig.add_trace(Scatter3d(x=A[:,0], y=A[:,1], z=A[:,2], mode='lines+markers'))
    fig.show()

def matrix_addition(A, B):
    return np.add(np.array(A), np.array(B))

def matrix_subtraction(A, B):
    return np.subtract(np.array(A), np.array(B))

def matrix_multiplication(A, B):
    return np.matmul(np.array(A), np.array(B))

def matrix_scaling(A, num):
    return np.array(A) * num

def matrix_determinant(A):
    return round(np.linalg.det(A))

def main():
    parser = argparse.ArgumentParser(description='Matrix operations')
    
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('cm', help='Count matrixes')
    add_parser.add_argument('operation', choices=['ma', 'ms', 'mm', 'sm', 'dm'], help=cm_options)
    add_parser.add_argument('A', type=parse_matrix, help='First Matrix')
    add_parser.add_argument('B', type=parse_matrix, nargs='?', default=None, help='Second Matrix (for operations ma, ms and mm)')
    add_parser.add_argument('scalar', type=float, nargs='?', default=1, help='Scalar value (for operation sm)')
    
    args = parser.parse_args()
    
    if args.operation == 'ma':
        ma_res = matrix_addition(args.A, args.B)
        create_plot(ma_res)
        print(ma_res)
    elif args.operation == 'ms':
        ms_res = matrix_subtraction(args.A, args.B)
        create_plot(ms_res)
        print(ms_res)
    elif args.operation == 'mm':
        mm_res = matrix_multiplication(args.A, args.B)
        create_plot(mm_res)
        print(mm_res)
    elif args.operation == 'sm':
        sm_res = matrix_scaling(args.A, args.scalar)
        create_plot(sm_res)
        print(sm_res)
    elif args.operation == 'dm':
        print(matrix_determinant(args.A))
    
    


if __name__ == '__main__':
    main()
