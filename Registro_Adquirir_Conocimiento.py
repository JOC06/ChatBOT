# -*- coding: utf-8 -*-
"""Practica2.ipynb

"""

def guardar_retroalimentacion(retroalimentacion, archivo):
   
    with open(archivo, 'a') as f:
        f.write(retroalimentacion + '\n')

# Respuestas precargadas y retroalimentación
respuestas = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo te llamas?": "Me llamo ChatBot.",
    "¿Que puesto podrias desempeñar?": "Lo siento, no puedo decirte la hora en este momento."
}

# Función para manejar la conversación
def chat():
    archivo_retroalimentacion = "retroalimentacion_chatbot.txt"
    print("Bienvenido al ChatBot. Escribe 'Salir' para terminar la conversación.")

    while True:
        # Recibe la entrada del usuario
        user_input = input("Tú: ")

        # Verifica si el usuario quiere salir

        if user_input.lower() == 'salir':
            print("ChatBot: ¡Hasta luego!")
            break
        
        # Verifica si la entrada del usuario tiene una respuesta predefinida
        if user_input in respuestas:
            respuesta = respuestas[user_input]
            print("ChatBot:", respuesta)
        else:
            # Si no hay una respuesta predefinida, solicita al usuario que proporcione una respuesta
            nueva_respuesta = input("ChatBot: No sé qué decir. ¿Qué debo responder a eso? ")
            respuestas[user_input] = nueva_respuesta
            guardar_retroalimentacion(f"Pregunta: {user_input} - Respuesta: {nueva_respuesta}", archivo_retroalimentacion)
            print("ChatBot: Gracias por la retroalimentación.")
            

 

                       


# Inicio del chat
if __name__ == "__main__":
    chat()
