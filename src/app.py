def greet(name: str) -> str:
    print(f"Hello {name}!")


def main():
    name = input("What is your name? ")
    greet(name)


if __name__ == "__main__":
    main()
