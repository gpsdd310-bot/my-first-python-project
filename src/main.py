def greet(name: str) -> str:
    return f"Hello, {name}!"


def main():
    user_name = "Rami"
    message = greet(user_name)
    print(message)


if __name__ == "__main__":
    main()
