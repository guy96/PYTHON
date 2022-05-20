from funcoes_quinto_andar import *





def main():
    # Adicionar nomes com espaco normal
    #num_banheiros = 2
    #num_quartos = 2
    #valor_maximo = 5500
    #bairro = "Leme"
    #zona_do_bairro = "Zona Sul"

    lista_banheiros = [2, 3]
    lista_quartos = [2, 3]
    valor_maximo = 5500

    locais = [
        ["Leme", "Zona Sul"],
        ["Copacabana", "Zona Sul"],
        ["Ipanema", "Zona Sul"],
        ["Vila Isabel", "Zona Norte"],
        ["Tijuca", "Zona Norte"],
    ]

    for num_banheiros in lista_banheiros:
        for num_quartos in lista_quartos:
            for bairro, zona_do_bairro in locais[0], locais[1]:

                a = abrirSite(num_banheiros, num_quartos, valor_maximo, bairro, zona_do_bairro)

                c = verTodosApartamentos(a)


if __name__ == "__main__":
    main()