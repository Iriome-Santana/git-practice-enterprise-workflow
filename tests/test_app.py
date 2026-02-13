from src.app import main
import datetime

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
    expected_output = f"Hello Alice! Today is {datetime.date.today()}.\n"
    assert captured_output.getvalue() == expected_output


def test_placeholder():
    assert True
