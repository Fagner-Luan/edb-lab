class Node:
    """Representa um nó individual em uma lista encadeada.

    Attributes:
        tarefa (str): A descrição da tarefa armazenada no nó.
        next: (Node | None): Referência para o próximo nó da lista ou None.
    """

    def __init__(self, tarefa: str) -> None:
        """Inicializa um novo nó com a tarefa especificada.
        Args:
            tarefa: A string contendo o texto da tarefa.
        """

        self.tarefa: str = tarefa
        self.next: Node | None = None


class LinkedList:
    """Gerencia uma estrutura de dados do tipo Lista Encadeada Simples."""

    def __init__(self) -> None:
        """Inicializa a lista sem nenhum elemento."""
        self.head: Node | None = None

    def remover(self, tarefa: str) -> bool:
        """Busca e remove a primeira ocorrência da tarefa especificada.

        Ajusta os ponteiros dos nós vizinhos para manter a integridade da lista.

        Args:
            tarefa: A string exata da tarefa a ser removida.

        Returns:
            True se a tarefa foi encontrada e removida com sucesso;
            False caso a tarefa não esteja presente na lista.

        Raises:
            ValueError: Se o parâmetro tarefa for uma string vazia.
        """

        if not tarefa:
            raise ValueError("Não é possivel remover uma tarefa vazia.")


        sentinel = Node("")
        sentinel.next = self.head
        previous = sentinel
        current = self.head

        while current is not None:
            if current.tarefa == tarefa:
                previous.next = current.next
                self.head = sentinel.next
                return True

            previous = current
            current = current.next
        return False

    def esta_vazia(self) -> bool:
        """Verifica se a lista está vazia.

        Returns:
            True se a lista estiver vazia;
            False caso contrário.
        """

        return self.head is None

    def adicionar_fim(self, tarefa: str) -> None:
        """Adiciona uma nova tarefa ao final da lista.

        Raises:
            ValueError: Se o parâmetro tarefa for uma string vazia.
        """

        if not tarefa:
            raise ValueError("Não é possível salvar uma tarefa vazia.")

        new_node = Node(tarefa)
        # caso a lista esteja vazia
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def listar_todas(self) -> list[str]:
        """Joga todos os dados em uma lista python para exibição.

        Returns:
            Uma lista python com todas as tarefas caso a lista não estaja vazia;
            Uma lista vazia se não houver terefas.
        """

        tarefas = []
        current = self.head

        while current is not None:
            tarefas.append(current.tarefa)
            current = current.next

        return tarefas

    def tamanho(self) -> int:
        """Conta a quantidade de elementos da lista.

        Returns:
            A quantidade de elementos presentes na lista.
        """

        size = 0
        current = self.head

        while current is not None:
            size += 1
            current = current.next

        return size
