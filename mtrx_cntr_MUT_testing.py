import sys
import numpy as np
import pytest
import matrix_counter as mc

def test_parse_matrix():
    s = '[[1, 2], [3, 4]]'
    result = mc.parse_matrix(s)
    expected = np.array([[1, 2], [3, 4]])
    assert np.array_equal(result, expected)

def test_parse_matrix_3x3():
    s = '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'
    result = mc.parse_matrix(s)
    expected = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    assert np.array_equal(result, expected)

def test_parse_matrix_invalid_json():
    with pytest.raises(Exception):
        mc.parse_matrix('not a matrix')

def test_matrix_addition():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = mc.matrix_addition(A, B)
    expected = np.array([[6, 8], [10, 12]])
    assert np.array_equal(result, expected)

def test_matrix_addition_with_negative_numbers():
    A = np.array([[-1, 2], [3, -4]])
    B = np.array([[5, -6], [-7, 8]])
    result = mc.matrix_addition(A, B)
    expected = np.array([[4, -4], [-4, 4]])
    assert np.array_equal(result, expected)

def test_matrix_subtraction():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = mc.matrix_subtraction(A, B)
    expected = np.array([[-4, -4], [-4, -4]])
    assert np.array_equal(result, expected)

def test_matrix_subtraction_with_negative_numbers():
    A = np.array([[-1, 2], [3, -4]])
    B = np.array([[5, -6], [-7, 8]])
    result = mc.matrix_subtraction(A, B)
    expected = np.array([[-6, 8], [10, -12]])
    assert np.array_equal(result, expected)

def test_matrix_multiplication():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = mc.matrix_multiplication(A, B)
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected)

def test_matrix_multiplication_rectangular():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    result = mc.matrix_multiplication(A, B)
    expected = np.array([[58, 64], [139, 154]])
    assert np.array_equal(result, expected)

def test_matrix_scaling():
    A = np.array([[1, 2], [3, 4]])
    num = 3
    result = mc.matrix_scaling(A, num)
    expected = np.array([[3, 6], [9, 12]])
    assert np.array_equal(result, expected)

def test_matrix_scaling_fraction():
    A = np.array([[2, 4],[6, 8]])
    num = 0.5
    result = mc.matrix_scaling(A, num)
    expected = np.array([[1, 2],[3, 4]])
    assert np.allclose(result, expected)

def test_matrix_scaling_zero():
    A = np.array([[1, -2],[3, -4]])
    result = mc.matrix_scaling(A, 0)
    expected = np.zeros((2, 2))
    assert np.array_equal(result, expected)

def test_matrix_determinant():
    A = np.array([[1, 2],[3, 4]])
    result = mc.matrix_determinant(A)
    expected = -2
    assert result == expected

def test_matrix_determinant_3x3():
    A = np.array([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ])
    result = mc.matrix_determinant(A)
    expected = -306
    assert result == expected

def test_matrix_determinant_identity():
    A = np.eye(3)
    result = mc.matrix_determinant(A)
    assert result == 1

class DummyTrace:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

class DummyScatter(DummyTrace):
    pass

class DummyScatter3d(DummyTrace):
    pass

class DummyFigure:
    def __init__(self):
        self.traces = []
        self.was_shown = False
    def add_trace(self, trace):
        self.traces.append(trace)
    def show(self):
        self.was_shown = True

def prepare_dummy_plot(monkeypatch):
    created_figures = []
    def figure_factory():
        figure = DummyFigure()
        created_figures.append(figure)
        return figure
    monkeypatch.setattr(mc, "Figure", figure_factory)
    monkeypatch.setattr(mc, "Scatter", DummyScatter)
    monkeypatch.setattr(mc, "Scatter3d", DummyScatter3d)
    return created_figures

def test_create_plot_2_columns(monkeypatch):
    figures = prepare_dummy_plot(monkeypatch)
    A = np.array([[1, 2],[3, 4]])
    mc.create_plot(A)
    assert len(figures) == 1
    assert len(figures[0].traces) == 1
    assert isinstance(figures[0].traces[0], DummyScatter)
    assert figures[0].was_shown is True

def test_create_plot_3_columns(monkeypatch):
    figures = prepare_dummy_plot(monkeypatch)
    A = np.array([[1, 2, 3],[4, 5, 6]])
    mc.create_plot(A)
    assert len(figures) == 1
    assert len(figures[0].traces) == 1
    assert isinstance(figures[0].traces[0], DummyScatter3d)
    assert figures[0].was_shown is True

def test_create_plot_invalid_number_of_columns(monkeypatch, capsys):
    figures = prepare_dummy_plot(monkeypatch)
    A = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
    mc.create_plot(A)
    captured = capsys.readouterr()
    assert len(figures) == 0
    assert "plot skipped" in captured.out
    assert "4" in captured.out

def test_create_plot_2d_uses_scatter_not_scatter3d(monkeypatch):
    figures = prepare_dummy_plot(monkeypatch)
    A = np.array([[10, 20],[30, 40]])
    mc.create_plot(A)
    trace = figures[0].traces[0]
    assert isinstance(trace, DummyScatter)
    assert not isinstance(trace, DummyScatter3d)

def test_create_plot_3d_uses_scatter3d(monkeypatch):
    figures = prepare_dummy_plot(monkeypatch)
    A = np.array([[1, 2, 3],[4, 5, 6]])
    mc.create_plot(A)
    trace = figures[0].traces[0]
    assert isinstance(trace, DummyScatter3d)
    assert not isinstance(trace, DummyScatter)

def test_main_addition(monkeypatch, capsys):
    calls = []
    def fake_addition(A, B):
        calls.append("ma")
        return np.array([[10]])
    monkeypatch.setattr(mc, "matrix_addition", fake_addition)
    monkeypatch.setattr(mc, "create_plot", lambda A: None)
    monkeypatch.setattr(sys, "argv", ["matrix_counter.py", "cm", "ma", "[[1]]", "[[2]]"])
    mc.main()
    assert calls == ["ma"]
    captured = capsys.readouterr()
    assert "[[10]]" in captured.out

def test_main_subtraction(monkeypatch, capsys):
    calls = []
    def fake_subtraction(A, B):
        calls.append("ms")
        return np.array([[20]])
    monkeypatch.setattr(mc, "matrix_subtraction", fake_subtraction)
    monkeypatch.setattr(mc, "create_plot", lambda A: None)
    monkeypatch.setattr(sys, "argv", ["matrix_counter.py", "cm", "ms", "[[5]]", "[[2]]"])
    mc.main()
    assert calls == ["ms"]
    captured = capsys.readouterr()
    assert "[[20]]" in captured.out

def test_main_multiplication(monkeypatch, capsys):
    calls = []
    def fake_multiplication(A, B):
        calls.append("mm")
        return np.array([[30]])
    monkeypatch.setattr(mc, "matrix_multiplication", fake_multiplication)
    monkeypatch.setattr(mc, "create_plot", lambda A: None)
    monkeypatch.setattr(sys, "argv", ["matrix_counter.py", "cm", "mm", "[[5]]", "[[6]]"])
    mc.main()
    assert calls == ["mm"]
    captured = capsys.readouterr()
    assert "[[30]]" in captured.out

def test_main_scaling(monkeypatch, capsys):
    calls = []
    def fake_scaling(A, scalar):
        calls.append(("sm", scalar))
        return np.array([[40]])
    monkeypatch.setattr(mc, "matrix_scaling", fake_scaling)
    monkeypatch.setattr(mc, "create_plot", lambda A: None)
    monkeypatch.setattr(sys, "argv", ["matrix_counter.py", "cm", "sm", "[[5]]"])
    mc.main()
    assert calls == [("sm", 1)]
    captured = capsys.readouterr()
    assert "[[40]]" in captured.out

def test_main_determinant(monkeypatch, capsys):
    calls = []
    def fake_determinant(A):
        calls.append("dm")
        return 50
    monkeypatch.setattr(mc, "matrix_determinant", fake_determinant)
    monkeypatch.setattr(sys, "argv", ["matrix_counter.py", "cm", "dm", "[[5]]"])
    mc.main()
    assert calls == ["dm"]
    captured = capsys.readouterr()
    assert "50" in captured.out

def test_matrix_scaling_detects_wrong_operator():
    A = np.array([[2, 4], [6, 8]])

    result = mc.matrix_scaling(A, 3)

    expected = np.array([[6, 12], [18, 24]])

    assert np.array_equal(result, expected)