
def adicionar_item(lista_de_compras):
    item = input('Digite um item: ').lower()
    quantidade = int(input('Digite a quantidade: '))
    if item in lista_de_compras:
        lista_de_compras[item] += quantidade
    else:
        lista_de_compras[item] = quantidade

def remover_item(lista_de_compras):
    item = input('Remover item: ').lower()
    if item in lista_de_compras:
        quantidade = int(input('Digite a quantidade: '))
        if quantidade >= lista_de_compras[item]:
            del lista_de_compras[item]
        else:
            lista_de_compras[item] -= quantidade
    else:
        print("Item não está na lista de compras")

def mostrar_lista(lista_de_compras):
    for item, quantidade in lista_de_compras.items():
        print(f'{item}: {quantidade}')


def main():

    lista_de_compras = {}

    while True:
        print()

        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Ver lista')
        print('4 Sair')

        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            adicionar_item(lista_de_compras)
        elif escolha == '2':
            remover_item(lista_de_compras)
        elif escolha == '3':
            mostrar_lista(lista_de_compras)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()



