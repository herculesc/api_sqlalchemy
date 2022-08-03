from models import Pessoas


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='kira', idade=18)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoas = Pessoas.query.filter_by(nome="kira").first()
    print(pessoas.idade)


# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="kira").first()
    pessoa.nome = 'Héscules'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclue_pessoas():
    pessoa = Pessoas.query.filter_by(nome="kira").first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclue_pessoas()
    consulta_pessoas()
