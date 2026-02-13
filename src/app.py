def greet(name: str) -> None:
    print(f"Hello {name}!")


def main() -> None:
    name = input("What is your name? ")
    greet(name)


if __name__ == "__main__":
    main()
