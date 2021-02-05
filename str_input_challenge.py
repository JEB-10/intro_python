name = input('¿What is your name?: ')

greeting_user = f'Hi {name}, pleased to meet you. The total characters of this sentence is'

greeting_len = len(greeting_user) # En total 91 caracteres sin contar el número en sí mismo (91)

str_greeting_len = str(greeting_len) + ' ' # Se pasa el 91 a str para sumarlo y se le suma un espacio que no es reconocido en la suma de las longitudes.
###-->ESTO SE HACE PORQUE LOS OBJETOS DE TIPO INT NO TIENEN LONGITUD.

greeting_num_count = len(str_greeting_len) # --> Se cuenta la longitud del str 91 y del espacio vacío que no era reconocido en el conteo inicial (--> 91 = 2 caracteres + ' ' 1 caracter, para un total de 3 caracteres)

sume_len = greeting_len + greeting_num_count # --> Aquí se suman los caracteres de la cadena inicaial y la nueva cadena, para agregar el resultado al final del output.

concatenate_all = (f'{greeting_user} {sume_len}') # Aquí se concatena el texto_1 con el texto_2

print(concatenate_all)
