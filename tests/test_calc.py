import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
import pytest

from commonutils import calc

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 3) == -3

def test_multiply():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(0, 5) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(3, 2) == 1.5

def test_divide_by_zero(capsys):
    result = calc.divide(5, 0)
    captured = capsys.readouterr()
    assert "Division by zero" in captured.out
    assert result is None
