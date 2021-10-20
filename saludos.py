def saludo(func):
    func()

def hola():
    print("La paz sea con vosotros")

def adios():
    print("Que Dios te bendiga")


def run():
    saludo(hola)
    saludo(adios)

if __name__ == "__main__":
    run()