import json
DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
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
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
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
        'position': 'internship',
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

    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
    op1 = [print(i) for i in DATA if i['language']== 'python']
    print('*'*100)

    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    op2 = [i for i in DATA if i['language']== 'python' and i['age']>20]
    print(op2,'\n','*'*100)

    # 3. obtener todos los trabajadores de ciancoders 
    op3 = [i for i in DATA if i['organization']== 'Ciancoders']
    print(op3,'\n','*'*100)

    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    #op4 = [i for i in DATA if i['organization']== 'Ciancoders' and i['age']>30]
    op4 = list(filter(lambda i: i['organization']== 'Ciancoders' and i['age']>30,DATA))
    print(op4,'\n','*'*100)

    # 5. obtener todos los trabajadores de mayores de 18 años
    #op5 = [(i) for i in DATA if i['age']>18]
    op5 = list(filter(lambda i: i['age']>18,DATA))
    print(op5,'\n','*'*100)

    # 6. obtener todos los trabajadores de mayores a 70 años
    op6 = [i for i in DATA if i['age']>70]
    print(op6,'\n','*'*100)

    pass

if __name__ == '__main__':
    run()