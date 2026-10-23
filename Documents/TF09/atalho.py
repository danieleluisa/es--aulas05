class Medivel:
    # Interface / classe mixin para objetos que possuem tamanho
    def espaco_total(self):
        return self.tamanho()


class Item(Medivel):
    # Classe base para itens do sistema de arquivos
    __slots__ = ('__nome',)
    
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def tamanho(self):
        raise NotImplementedError

    def mostrar(self):
        raise NotImplementedError


class Atalho(Item):
    # Classe Atalho aplicando encapsulamento (__slots__ e __destino) e polimorfismo
    __slots__ = ('__destino',)

    def __init__(self, nome, destino):
        super().__init__(nome)
        self.__destino = destino

    @property
    def destino(self):
        # Propriedade apenas de leitura para o destino encapsulado
        return self.__destino

    def redirecionar(self, novo_destino):
        # Método para alterar o destino de forma segura e controlada
        self.__destino = novo_destino

    def tamanho(self):
        # Polimorfismo: calcula o tamanho baseando-se no destino
        return self.destino.tamanho()

    def mostrar(self):
        # Polimorfismo: exibe o atalho formatado
        print(f"Atalho -> {self.nome} aponta para {self.destino.nome}")


# --- Demonstração e as 3 tentativas que falham de propósito ---
if __name__ == "__main__":
    
    # Simulando um objeto destino fictício simples para testes
    class ArquivoFalso(Item):
        def __init__(self, nome, tam):
            super().__init__(nome)
            self.tam = tam
        def tamanho(self):
            return self.tam
        def mostrar(self):
            print(f"Arquivo: {self.nome}")

    doc = ArquivoFalso("documento.txt", 150)
    atalho = Atalho("atalho_doc", doc)

    # Tentativa 1: Falha ao tentar acessar atributo privado diretamente (__destino)
    try:
        print(atalho.__destino)
    except AttributeError:
        print("Tentativa 1 falhou de propósito: O atributo __destino é privado e protegido.")

    # Tentativa 2: Falha ao tentar alterar a propriedade 'destino' diretamente (só leitura)
    try:
        atalho.destino = "outro_lugar"
    except AttributeError:
        print("Tentativa 2 falhou de propósito: A propriedade 'destino' é somente de leitura.")

    # Tentativa 3: Falha ao chamar um método que não existe na classe
    try:
        atalho.metodo_inexistente()
    except AttributeError:
        print("Tentativa 3 falhou de propósito: Método inexistente gerou exceção.")