import hashlib


def create_hash(text):

    # Cria um objeto hash usando o algoritmo SHA-256
    hash_obj = hashlib.sha256()

    # Atualiza o objeto hash com a codificação da frase
    hash_obj.update(text.encode("utf-8"))

    # Retorna o valor de hash em hexadecimal
    return hash_obj.hexdigest()
