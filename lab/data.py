def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print('File not found')
        exit()
