import csv

def main():
    fix("ouput.csv")
    fix("empty.csv")

def fix(path):
    list = read_file(path)

    for row in list:
        print(row)

    write(list, path)

def read_file(path):
    with open(path) as file:
        sheet = csv.reader(file, delimiter=",")
        array = []

        for row in sheet:
            if len(row) > 0:
                array.append(row)

    return array

def write(list, path):
    with open(path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list)


if __name__ == "__main__":
    main()
