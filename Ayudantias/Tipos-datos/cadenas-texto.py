texto = "Hola, mundo!"

#  Operaciones y metodos comunes
# -----------------------------

len(texto)  # Longitud de la cadena
texto.upper()  # "HOLA, MUNDO!" convierte a mayusculas
texto.lower()  # "hola, mundo!" convierte a minusculas
texto.replace("mundo", "Python")  # "Hola, Python!" reemplaza texto
texto.split(", ")  # ['Hola', 'mundo!'] separa en lista por comas
"Python" in texto  # True verifica si esta
"Java" not in texto  # True verifica si no esta
texto.strip()  # Elimina espacios al inicio y final
" ".join(["Hola", "mundo"])  # "Hola mundo" une una lista de palabras

#  Indexacion y slicing
# ----------------------

texto[0]  # 'H' primer caracter
texto[-1]  # '!' ultimo caracter
texto[0:4]  # 'Hola' subcadena desde indice 0 hasta 3
texto[6:]  # 'mundo!' subcadena desde indice 6 hasta el final
texto[:5]  # 'Hola,' subcadena desde el inicio hasta indice 4
texto[::2]  # 'Hl,mno' subcadena con paso 2, cada dos caracteres
