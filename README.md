# Matrix Counter

Matrix Counter is a command-line tool that performs various matrix operations. It uses numpy and argparse for parsing arguments and performing the operations. The 3D plotting feature uses Plotly's graph_objects module to create interactive 3D plots after each operation.

## Installation

To install this program, you need to have Python installed on your computer. You can download it from [here](https://www.python.org/downloads/). After installing Python, open a terminal or command prompt and run the following commands:

```bash
git clone https://github.com/yourusername/matrix_counter.git
cd matrix_counter
pip install numpy plotly argparse json
```

## Usage

To use this program, navigate to the directory where you cloned it and run `python matrix_counter.py` followed by your operation and matrices. For example:

```bash
python matrix_counter.py cm ma '[[1,2],[3,4]]' '[[5,6],[7,8]]'
```

This will perform a matrix addition on the two provided matrices and display a 3D plot of the result.

## Available Operations

Matrix Counter supports the following operations:

1. **ma** - Matrix Addition: This operation adds two matrices together. For example, if you have A = [[1,2],[3,4]] and B = [[5,6],[7,8]], the result will be res = [[6,8],[10,12]].

2. **ms** - Matrix Subtraction: This operation subtracts one matrix from another. For example, if you have A = [[1,2],[3,4]] and B = [[5,6],[7,8]], the result will be res = [[-4,-4],[-4,-4]].

3. **mm** - Matrix Multiplication: This operation multiplies two matrices together. For example, if you have A = [[1,2],[3,4]] and B = [[5,6],[7,8]], the result will be res = [[19,22],[43,50]].

4. **sm** - Scalar Multiplication: This operation multiplies each element of a matrix by a scalar value. For example, if you have A = [[1,2],[3,4]] and scalar = 2, the result will be res = [[2,4],[6,8]].

5. **dm** - Matrix Determinant: This operation calculates the determinant of a given square matrix. For example, if you have A = [[1,2],[3,4]], the result will be det(A).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
