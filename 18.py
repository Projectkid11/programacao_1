def senha_segura(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    return len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero
