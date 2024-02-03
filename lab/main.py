from data import load_data
from strip_array import strip_array, split_list

def main():
    data = load_data("test.txt")
    data = split_list(data)
    data = strip_array(data)
    print(data)

if __name__ == "__main__":
    main()