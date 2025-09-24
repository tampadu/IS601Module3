# tests/test_cli.py
import pytest
import runpy
from calculator import cli

# --- 1. Quit immediately ---
def test_cli_quit(monkeypatch, capsys):
    inputs = iter(['quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

# --- 2. Add operation ---
def test_cli_add(monkeypatch, capsys):
    inputs = iter(['add', '2', '3', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

# --- 3. Subtract operation ---
def test_cli_subtract(monkeypatch, capsys):
    inputs = iter(['subtract', '10', '4', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

# --- 4. Multiply operation ---
def test_cli_multiply(monkeypatch, capsys):
    inputs = iter(['multiply', '3', '5', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Result: 15.0" in captured.out

# --- 5. Divide operation ---
def test_cli_divide(monkeypatch, capsys):
    inputs = iter(['divide', '10', '2', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

# --- 6. Division by zero ---
def test_cli_divide_by_zero(monkeypatch, capsys):
    inputs = iter(['divide', '5', '0', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Divide by Zero error" in captured.out

# --- 7. Invalid operation ---
def test_cli_invalid_operation(monkeypatch, capsys):
    inputs = iter(['invalid_op', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

# --- 8. Invalid number input ---
def test_cli_invalid_number(monkeypatch, capsys):
    inputs = iter(['add', 'abc', '2', '3', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter a number." in captured.out
    assert "Result: 5.0" in captured.out

# --- 9. Test main function ---
def test_cli_main(monkeypatch, capsys):
    """
    This test runs calculator/cli.py as __main__ to cover the
    final line: if __name__ == "__main__": calculator()
    """
    # Simulate user input: immediately quit
    inputs = iter(['quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the cli.py module as __main__
    runpy.run_module("calculator.cli", run_name="__main__")
    
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out
