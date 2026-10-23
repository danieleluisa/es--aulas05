class Commit:
    # Representa um único commit no histórico de objetos
    def __init__(self, id_unico, mensagem, autor, pai):
        self.id = id_unico
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai  # Referência para o commit anterior (ou None se for o primeiro)

    def historico(self):
        # Retorna a lista de commits subindo de pai em pai
        # Usamos uma abordagem iterativa sem usar 'else'
        lista_commits = []
        atual = self
        
        while atual is not None:
            lista_commits.append(atual)
            atual = atual.pai
            
        return lista_commits


class Repositorio:
    # Gerencia o repositório e a criação de novos commits
    def __init__(self, nome):
        self.nome = nome
        self.contador_id = 0
        self.ultimo_commit = None
        self.quantidade_commits = 0

    def commitar(self, mensagem, autor):
        # Incrementa o contador para gerar um id único
        self.contador_id = self.contador_id + 1
        novo_id = self.contador_id
        
        # Cria o novo commit apontando para o commit anterior (pai)
        novo_commit = Commit(novo_id, mensagem, autor, self.ultimo_commit)
        
        # Atualiza o último commit do repositório
        self.ultimo_commit = novo_commit
        self.quantidade_commits = self.quantidade_commits + 1
        
        return novo_commit

    def log(self):
        # Exibe o histórico completo de commits do repositório
        if self.ultimo_commit is None:
            print("Repositório vazio.")
            
        # Se houver commits, percorre a cadeia do último até o primeiro
        historico_atual = self.ultimo_commit.historico()
        
        for c in historico_atual:
            print(f"Commit ID: {c.id}")
            print(f"Mensagem: {c.mensagem}")
            print(f"Autor: {c.autor}")
            print("-" * 30)

    def total_de_commits(self):
        # Retorna o total de commits realizados
        return self.quantidade_commits


# --- Testando e criando os 3 commits obrigatórios ---
# Substitui com o teu nome e RA
meu_autor = "Dani - RA: 6326262"

# Inicializa o repositório tf-08
repo = Repositorio("tf-08")

# Realiza 3 commits com mensagens próprias
repo.commitar("Estrutura inicial do projeto commit.py", meu_autor)
repo.commitar("Adicionada classe Commit e metodo historico", meu_autor)
repo.commitar("Implementada classe Repositorio com log e contador", meu_autor)

# Exibe o log na consola para conferir
repo.log()
print(f"Total de commits: {repo.total_de_commits()}")