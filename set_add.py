def contar_paises_distintos(lista_de_paises):
    """Devuelve cuántos países distintos hay en la lista."""
    return len(set(lista_de_paises))


if __name__ == "__main__":
    totalStamps = int(input("Cuántos sellos tienes?: "))
    paises = [input("País: ").strip() for _ in range(totalStamps)]
    print("Países distintos:", contar_paises_distintos(paises))

