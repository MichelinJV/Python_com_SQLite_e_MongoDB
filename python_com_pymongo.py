from pymongo import MongoClient

# Conectar ao servidor MongoDB
client = MongoClient('localhost', 27017)

# Criar ou acessar o banco de dados
db = client['banco_de_dados']

# Criar coleções para clientes e contas
clientes_collection = db['clientes']
contas_collection = db['contas']

# Função para inserir cliente
def inserir_cliente(nome, cpf, endereco):
    cliente_data = {
        'nome': nome,
        'cpf': cpf,
        'endereco': endereco
    }
    result = clientes_collection.insert_one(cliente_data)
    return result.inserted_id

# Função para inserir conta
def inserir_conta(tipo, agencia, numero, id_cliente, saldo):
    conta_data = {
        'tipo': tipo,
        'agencia': agencia,
        'numero': numero,
        'id_cliente': id_cliente,
        'saldo': saldo
    }
    result = contas_collection.insert_one(conta_data)
    return result.inserted_id

# Função para buscar contas de um cliente
def buscar_contas_do_cliente(id_cliente):
    contas = contas_collection.find({'id_cliente': id_cliente})
    return list(contas)

# Inserir um cliente
id_cliente = inserir_cliente('Fulano', '123.456.789-00', 'Rua ABC, 123')

# Inserir uma conta associada ao cliente
id_conta = inserir_conta('corrente', '001', '12345-6', id_cliente, 1000.0)

# Buscar contas de um cliente específico
contas_do_cliente = buscar_contas_do_cliente(id_cliente)
print("Contas do cliente:")
for conta in contas_do_cliente:
    print("Tipo:", conta['tipo'], "Agência:", conta['agencia'], "Número:", conta['numero'], "Saldo:", conta['saldo'])

# Fechar a conexão com o MongoDB
client.close()
