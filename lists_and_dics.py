def run():
    my_list = [1, "Hello", True, 4.5]
    my_dics = {"firsname":"Ignacio", "lastname":"García"}

    super_list = [
        {"firsname":"Ignacio", "lastname":"García"},
        {"firsname":"Jesús", "lastname":"Fernández"},
        {"firsname":"David", "lastname":"García"},
        {"firsname":"George", "lastname":"Lucas"},
        {"firsname":"Harrison", "lastname":"Ford"}
    ]

    super_dic = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items():
        print(key, "-",  value)

    for lista in super_list:
        print(lista.items())

    for lista2 in super_list:
        for key, value in lista2.items():
            print(key, "-",  value)

    for lista3 in super_list:
        print(lista3("firstname"), "-", lista3("lastname"))


if __name__ == "__main__":
    run()