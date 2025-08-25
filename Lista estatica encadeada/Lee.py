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
        # esse metodo e esse atributo são responsáveis por construir a estrutura da nossa lista, e permitir
        # que ela seja trabalhada de forma encadeada.

        # atributo que guarda o índice do primeiro elemento válido da lista:
        # incialmente, a lista está vazia, então prim inicia valendo -1
        # quando voce insere o primeiro elemento, prim passa apontar para o índice desse nó:
        self.prim = -1

        # atributo que guarda o último elemento válido da lista.
        # Inicialmente também é -1 (lista vazia).
        # Quando inserimos, ult ajuda a manter referencia ao final da lista.
        self.ult = -1   

        # CRIANDO O MÉTODO INICIALIZAR ESTRUTURA:
        def incializar_estrutura(self):
            # o loop percorre até o penultimo índice da lista.
            for i in range(self.tam_maximo -1):
                # A primeira posição da lista receberá o nó, com a estrutura None para self.info, e i + 1 para self.prox .
                # ou seja, o valor será sempre None na inicialização, mas o i sera incrementado, apontando para o próximo
                # nó.  
                self.vetor[i] = No(None, i + 1)
            # agora, tratando o último índice da lista, que receberá None para info, e -1 para prox .
            # o -1 indica que é o último nó.
            self.vetor[self.tam_maximo - 1] = No(None, -1)
            # agora o metodo deve retornar o endereço da primeira posição do vetor, que no caso é zero.
            return 0 # esse valor ficara armazenado no atributo prox_pos_vazia .
        
        # CRIANDO O MÉTODO INSERIR_INICIO:
        def inserir_inicio(self, valor):
            # se a lista estiver vazia:
            if self.quant == 0:
                # o prim e o ult recebem o valor, e -1, pois o primeiro valor é o primeiro e o ultimo ao mesmo tempo.
                # no caso os dois atributos receberão o mesmo valor, se o valor inserido for o primeiro.
                self.prim = self.ult = self.ocupa_no(valor, -1)
                # incrementando a quantidade de elementos
                self.quant += 1
            # sea lista nao estiver vazia:
            else:
                # 
                self.prim = self.ocupa_no(valor, self.prim)
                self.quant += 1