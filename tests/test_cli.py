from calculator import cli

def test_quit(monkeypatch, capsys):
    # Simulate entering 'quit' immediately
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    cli.calculator()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out
