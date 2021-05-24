

def count(*, message):
    return len(message)


if __name__ == "__main__":
    message = input("count this message: ")
    message = f"""{message}"""
    print(f"Character Count: {count(message=message)}")