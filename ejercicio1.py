import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]   
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Variable que selecciona aleatoriamente pregunta, respuesta y respuesta correcta, sin tener que acceder a las 3 listas usando indices
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)

#Inicializo la puntuacion
punctuation = 0

# El usuario deberá contestar 3 preguntas
for question, option, correct_answer in questions_to_ask:

    # Se selecciona una pregunta aleatoria
    #question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(option, start = 1):
        print(f"{i}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        #Evalua si lo ingresado es un numero, en caso de no serlo el programa termina
        if str.isnumeric(user_answer) == False:
            print ("Respuesta no valida")
            sys.exit(1)
        else:
            #Aca el input es un numero
            user_answer = (int(user_answer)) - 1
            #Evalua si lo ingresado pertenece a las opciones, sino se termina el programa
            if user_answer < 0 or user_answer > 3:
                print ("Respuesta no valida")
                sys.exit(1)
            else:
                #Verifica si la respuesta es correcta
                if user_answer == correct_answer:
                    print ("Respuesta correcta!")
                    punctuation += 1
                    break
                else:
                    if intento == 0:
                        print ("Incorrecto. Proba de nuevo")
                        punctuation -= 0.5
                    else:
                    # Si el usuario no responde correctamente después de 2 intentos,
                    # se muestra la respuesta correcta
                        print(f"Incorrecto. La respuesta correcta es la numero {correct_answer + 1}")

# Se imprime un blanco al final de la pregunta
print ("Su puntuacion es: ", punctuation)
print()