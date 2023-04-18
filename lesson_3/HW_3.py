from pympler import asizeof


def find_in_file(file_name: str):
    with open(file_name, "r") as file:
        pattern = input("Enter a word: ")
        while True:
            line: str = file.readline()
            if not line:
                break
            if pattern in line:
                yield line


def main():
    with open("./lesson_3/results.txt", "w") as file:
        lines = 0
        for i in find_in_file(file_name="./lesson_3/rockyou.txt"):
            file.write(i)
            lines += 1
        print(f"Found {lines} lines")
        file_size = asizeof.asizeof("results.txt")
        file_size2 = asizeof.asizeof(file)
        print(f"File size: {file_size} bytes")
        print(f"File size: {file_size2} bytes")


if __name__ == "__main__":
    main()
