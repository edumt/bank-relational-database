import sqlite3

conn = sqlite3.connect("bank.db").cursor()

sql_create_tables_dictionary = {
    # todo: add foreign keys references
    # Servico
    "create_servico_table": (
        "CREATE TABLE IF NOT EXISTS servico ("
        + "id_servico integer PRIMARY KEY AUTOINCREMENT,"
        + "num_cartao integer,"
        + "id_aplicacao integer,"
        + "id_seguro integer,"
        + "id_conta integer,"
        + "nome text,"
        + "data_contratada text,"
        + "data_vencimento text,"
        + "FOREIGN KEY(num_cartao) REFERENCES cartao(num_cartao),"
        + "FOREIGN KEY(id_aplicacao) REFERENCES aplicacao(id_aplicacao),"
        + "FOREIGN KEY(id_seguro) REFERENCES seguro(id_seguro),"
        + "FOREIGN KEY(id_conta) REFERENCES conta(id_conta)"
        + ");"
    ),
    "create_cartao_table": (
        "CREATE TABLE IF NOT EXISTS cartao ("
        + "num_cartao integer PRIMARY KEY,"
        + "id_tipo integer,"
        + "limite integer,"
        + "fatura integer,"
        + "data_fatura text,"
        + "data_expiracao text,"
        + "cvv integer,"
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo)"
        + ");"
    ),
    "create_aplicacao_table": (
        "CREATE TABLE IF NOT EXISTS aplicacao ("
        + "id_aplicacao integer PRIMARY KEY AUTOINCREMENT,"
        + "id_tipo integer,"
        + "nome text,"
        + "valor_aplicado integer,"
        + "data_retirada text,"
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo)"
        + ");"
    ),
    "create_seguro_table": (
        "CREATE TABLE IF NOT EXISTS seguro ("
        + "id_seguro integer PRIMARY KEY AUTOINCREMENT,"
        + "id_tipo integer,"
        + "carencia text,"  # text ou integer
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo)"
        + ");"
    ),
    "create_tipo_servico_table": (
        "CREATE TABLE IF NOT EXISTS tipo_servico ("
        + "id_tipo integer PRIMARY KEY AUTOINCREMENT,"
        + "nome text"
        # talvez tenha que adicionar mais um atributo
        + ");"
    ),
    # Conta
    "create_conta_table": (
        "CREATE TABLE IF NOT EXISTS conta ("
        + "id_conta integer PRIMARY KEY AUTOINCREMENT,"
        + "CPF text,"
        + "CNPJ text,"
        + "num_agencia integer,"
        + "id_gerente integer,"
        + "tipo text,"  # text ou integer
        + "saldo integer,"
        + "status text,"  # text ou integer
        + "FOREIGN KEY(CPF, CNPJ) REFERENCES cliente(CPF, CNPJ),"
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia),"
        + "FOREIGN KEY(id_gerente) REFERENCES funcionario(id_funcionario)"
        + ");"
    ),
    "create_cliente_table": (
        "CREATE TABLE IF NOT EXISTS cliente ("
        + "CPF text,"
        + "CNPJ text,"
        + "nome text,"
        + "sobrenome text,"
        + "CEP integer,"
        + "rua text,"
        + "num_endereco integer,"
        + "cidade text,"
        + "estado text,"
        + "renda integer,"
        + "PRIMARY KEY(CPF, CNPJ)"
        + ");"
    ),
    "create_telefone_table": (
        "CREATE TABLE IF NOT EXISTS telefone ("
        + "CPF text,"
        + "CNPJ text,"
        + "num_agencia integer,"
        + "telefone text,"
        + "PRIMARY KEY(CPF, CNPJ, num_agencia, telefone),"
        + "FOREIGN KEY(CPF, CNPJ) REFERENCES cliente(CPF, CNPJ),"
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia)"
        + ");"
    ),
    "create_transfere_para_table": (
        "CREATE TABLE IF NOT EXISTS transfere_para ("
        + "id_transferencia integer PRIMARY KEY AUTOINCREMENT,"
        + "id_remetente integer,"
        + "id_destino integer,"
        + "valor integer,"
        + "data text,"
        + "horario text,"
        + "FOREIGN KEY(id_remetente) REFERENCES conta(id_conta),"
        + "FOREIGN KEY(id_destino) REFERENCES conta(id_conta)"
        + ");"
    ),
    # Agencia
    "create_agencia_table": (
        "CREATE TABLE IF NOT EXISTS agencia ("
        + "num_agencia integer PRIMARY KEY,"
        + "CEP integer,"
        + "rua text,"
        + "num_endereco integer"
        + ");"
    ),
    # Funcionario
    "create_funcionario_table": (
        "CREATE TABLE IF NOT EXISTS funcionario ("
        + "id_funcionario integer PRIMARY KEY AUTOINCREMENT,"
        + "data_de_nascimento text,"
        + "nome text,"
        + "bonificacao integer,"
        + "num_agencia int,"
        + "horas_trabalhadas int,"
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia),"
        + ");"
    ),
}


for sql_create_table in sql_create_tables_dictionary.values():
    conn.execute(sql_create_table)
"""
#testing
for i in range(5):
    conn.execute("INSERT INTO AGENCIA (num_agencia, CEP, rua, num_endereco) VALUES (1, 1, 'TESTE', 1)")
conn.execute("COMMIT")
print(conn.execute("SELECT * FROM AGENCIA").fetchall())

"""
