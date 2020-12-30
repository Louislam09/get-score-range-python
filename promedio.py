from os import system
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt

TITLE = 'Student Score Average'

workblook = 'averages.xlsx'
STUDENTS_DATA = []
STUDENTS_AVERAGE = []

def ask_data(txt):
    global content
    content = input(txt)

    if len(content) == 0:
        ask_data(txt)
    else:
        return content


def get_average(data):
    STUDENTS_AVERAGE = []
    for student in data:
        student_info = f'{student[0]}({student[1]})' 
        average = (student[2] + student[3]+ student[4]+ student[5]) / 4
        STUDENTS_AVERAGE.append([student_info,average])

    dataFrame = pd.DataFrame(STUDENTS_AVERAGE,columns=['Info','Promedio'])
    dataFrame.to_excel(workblook)




def add_student():
    system('cls')
    print('Solicitud de datos del estudiante\n')
    name = ask_data('Escribe el nombre: ')
    enrollment = int(ask_data('Escribe la matricula: '))
    note1 = int(ask_data('Escribe la nota 1: '))
    note2 = int(ask_data('Escribe la nota 2: '))
    note3 = int(ask_data('Escribe la nota 3: '))
    note4 = int(ask_data('Escribe la nota 4: '))

    STUDENTS_DATA.append([name,enrollment,note1,note2,note3,note4])
    get_average(STUDENTS_DATA)

    print('\nDatos añadido con exito!\n')

    print('Presion cualquier tecla para volver al Menu...')
    input()
    Menu()

def show_graph():
    system('cls')
    print('Grafica de Estudiantes\n')
    
    dataFrame = pd.read_excel(workblook)

    values = dataFrame[['Info','Promedio']]

    print(values)
    ax = values.plot.bar(x='Info',y='Promedio',rot=0)
    plt.show()

    print('Presion cualquier tecla para volver al Menu...')
    input()
    Menu()

def Menu():
    system('cls')
    print(TITLE)

    print("""
    1-Añadir datos de estudiante
    2-Mostrar grafica
    3-Salir
    """)

    option = input('Escribe tu opcion: ')

    options = ['1','2','3']

    if option in options:
        if option == "1":
            add_student()
        elif option == '2':
            show_graph()
        else:
            return
    else:
        print('La opcion ingresada no es valida ingresa una opcion valida\n')
        sleep(2)
        Menu()

Menu()