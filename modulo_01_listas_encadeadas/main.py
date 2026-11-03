from linked_list import LinkedList


def main() -> None:
    lista = LinkedList()
    lista.adicionar_fim("Estudar algoritmos de ordenação")
    lista.adicionar_fim("Fazer compras no supermercado")
    lista.adicionar_fim("Revisar código do módulo de lista encadeada")
    lista.adicionar_fim("Agendar consulta médica")
    lista.adicionar_fim("Configurar as chaves SSH do Git")

    print(f"Número de elementos na lista: {lista.tamanho()}")
    print("Tarefas na lista:")
    print(lista.listar_todas())

    lista.remover("Configurar as chaves SSH do Git")
    print(f"Número de elementos na lista: {lista.tamanho()}")
    print("Tarefas na lista:")
    print(lista.listar_todas())

    print(lista.remover("Dar banho no totó"))
    lista.remover("Revisar código do módulo de lista encadeada")

    print(f"Número de elementos na lista: {lista.tamanho()}")
    print("Tarefas na lista:")
    print(lista.listar_todas())



if __name__ == '__main__':
    main()
