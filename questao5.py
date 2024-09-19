#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;
def inverteString(string):
    string_invertida = ""
    for char in string:
        string_invertida = char + string_invertida
    return string_invertida

# Example usage
input_string = "Hello, World!"
print("string original:", input_string)
print("string inversa:", inverteString(input_string))