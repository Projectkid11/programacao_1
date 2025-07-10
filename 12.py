def contar_vogais(palavra):
    vogais = "aeiou"
    palavra = palavra.lower()
    return sum(1 for letra in palavra if letra in vogais)
