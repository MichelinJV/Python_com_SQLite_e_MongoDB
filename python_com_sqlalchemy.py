from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Criar uma instância do motor de banco de dados
engine = create_engine('sqlite:///banco_de_dados.db', echo=True)

# Declarar uma base
Base = declarative_base()

# Definir a classe Cliente
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)

    # Relacionamento com a tabela Conta
    contas = relationship("Conta", back_populates="cliente")

# Definir a classe Conta
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(String)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float)

    # Relacionamento com a tabela Cliente
    cliente = relationship("Cliente", back_populates="contas")

# Criar todas as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de uso
# Criar um cliente
cliente1 = Cliente(nome='Fulano', cpf='123.456.789-00', endereco='Rua ABC, 123')
session.add(cliente1)
session.commit()

# Criar uma conta associada a esse cliente
conta1 = Conta(tipo='corrente', agencia='001', numero='12345-6', cliente=cliente1, saldo=1000.0)
session.add(conta1)
session.commit()

# Consultar contas de um cliente específico
cliente = session.query(Cliente).filter_by(nome='Fulano').first()
print("Contas de", cliente.nome)
for conta in cliente.contas:
    print("Tipo:", conta.tipo, "Agência:", conta.agencia, "Número:", conta.numero, "Saldo:", conta.saldo)

# Fechar a sessão
session.close()
