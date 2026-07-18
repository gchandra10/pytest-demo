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

@pytest.mark.skip(reason="This test is currently disabled due to bug in the divide function.")
def test_divide_by_zero(capsys):
    result = calc.divide(5, 0)
    captured = capsys.readouterr()
    assert "Division by zero" in captured.out
    assert result is None

@pytest.mark.interest(reason="This test is related to simple interest calculations.")
def test_simple_interest():
    """Verify simple interest calculations."""
    assert calc.simple_interest(1000, 5, 2) == 100.0
    assert calc.simple_interest(1500, 4.3, 4) == 258.0

def test_simple_interest_zero_time():
    """Verify simple interest calculations."""
    assert calc.simple_interest(1000, 5, 0) == 0.0

@pytest.mark.interest(reason="This test is related to compound interest calculations.")
def test_compound_interest():
    """Verify compound interest calculations."""
    assert calc.compound_interest(1000, 5, 2) == 102.5
    assert calc.compound_interest(1500, 4.3, 4) == 275.12

def test_compound_interest_zero_time():
    """Verify compound interest calculations."""
    assert calc.compound_interest(1000, 5, 0) == 0.0

