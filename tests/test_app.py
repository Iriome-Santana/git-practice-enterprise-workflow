
from src.app import main

def test_default_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello World" in captured.out

def test_placeholder():
    assert True