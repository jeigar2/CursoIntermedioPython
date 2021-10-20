def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="UTF-8") as f:
        for line in f:
            numbers.append(int(line))

        print(numbers)


def write():
    names = ["Jesús", "María", "José", "Isabel", "Zacarías"]
    with open("./archivos/names.txt", "w", encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()

if __name__ == "__main__":
    run()