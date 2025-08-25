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

# CRIANDO A ESTRUTURA DO NÓ:
    # Primeiro, criamos uma classe simples, que chamaremos de "No", que contém 2 atributos:
    # info => armazenará o valor;
    # prox => cuidará do endereço do proximo elemento na lista.

class No:

    # Inciando o método construtor, e inserindo os parametros que os atributos irão receber:
    def __init__(self, valor, proximo):
        # primeiro atributo, que será o valor do elemento:
        self.info = valor
        # segundo atributo, que será o ponteiro:
        self.prox = proximo

# Agora precisaremos criar uma nova classe para a lista, que chamaremos de Lee:
# CRIANDOA ESTRUTURA DA CLASSE Lee:

class Lee:
    
    # Iniciando o método construtor, e inserindo seus parâmetros e atributos.
    def __init__(self, tamanho): # tamanho = tamanho da lista
        
        # atributo que será o tamanho máximo da lista:
        self.tam_maximo = tamanho

        # atributo que receberá uma lista com o valor None vezes o tamanho:
        self.vetor = [None] * self.tam_maximo

        # atributo que receberá a quantidade de elementos dentro da lista:
        self.quant = 0  # iniciando com zero elementos, lista vazia.

        # Agora temos mais atributos:
        
        # atributo que guarda o índice da próxima posição livre no vetor,
        # inicialmente, aponta para o primeiro elemento livre, (0),
        # e serve para você saber onde inserir o próximo nó sem precisar procurar pelo vetor inteiro:
        self.prox_pos_vazia = self.inicializar_estrutura()  # "onde posso colocar o proximo elemento"

        # atributo que guarda o índice do primeiro elemento válido da lista:
        # incialmente, a lista está vazia, então prim inicia valendo -1
        # quando voce insere o primeiro elemento, prim passa apontar para o índice desse nó:
        self.prim = -1

        # atributo que guarda o último elemento válido da lista.
        # Inicialmente também é -1 (lista vazia).
        # Quando inserimos, ult ajuda a manter referencia ao final da lista.
        self.ult = -1   
