from src.app import main


def test_main(monkeypatch):
    # Simulate user input for the name
    monkeypatch.setattr("builtins.input", lambda _: "Alice")

    # Capture the output of the main function
    import io
    import sys

    captured_output = io.StringIO()
    sys.stdout = captured_output

    main()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check if the output is correct
    assert captured_output.getvalue() == "Hello Alice!\n"


def test_placeholder():
    assert True
