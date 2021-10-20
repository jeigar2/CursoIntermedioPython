DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_dev = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_python_dev2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_dev2 = list(map(lambda worker: worker["name"], all_python_dev2))
    
    all_Platzy_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    all_Platzy_worker2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzy_worker2 = list(map(lambda worker: worker["name"], all_Platzy_worker2))


    adults = list(filter(lambda worker: worker["age"]>=20, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    adults2 = [worker["name"] for worker in DATA if worker["age"]>=20]

#    old_people = list(map(lambda worker:worker|{worker["age"]>70},DATA)) # version 3.9 python
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"]>70}},DATA)) # version 3.8 python
    old_people2 = [{**{"old": worker["age"]>70}} for worker in DATA]
    
    print ("python", all_python_dev)
    print ("python", all_python_dev2)

    print ("all_Platzy_worker",all_Platzy_worker)
    print ("all_Platzy_worker",all_Platzy_worker2)
    print ("adults",adults)
    print ("adults",adults2)

    print ("old_people",old_people)
    print ("old_people",old_people2)


if __name__ == "__main__":
    run()