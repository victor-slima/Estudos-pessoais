# Primeiramente, uma lista estática encadeada utiliza uma estrutura de nós, encadeados, para armazenar os elementos.
# cada nó armazena o valor do elemento, e o ponteiro que aponta para o proximo nó.
# ou seja, o nó é o valor do elemento, e o ponteiro ao mesmo tempo.

# Vantagens da Lista estática encadeada:
    # Inserção e remoção sem realocar todos os elementos;
    # Mais flexível que a lista estática sequencial;
    # Facilita o rearranjo de elementos.  

# Desvantagens da lista estática encadeada:
    # Acesso a elementos em posições específicas é mais lento, visto que precisa-se percorrer os nós anteriores;
    # Gera overhead de memória, visto que armazena os ponteiros.

# Quando usar:
    # Quando se precisa de flexibilidade na inserção/remoção;
    # Quando a realocação de elementos de uma lista sequencial, seria custosa.

