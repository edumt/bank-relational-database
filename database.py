import sqlite3

conn = sqlite3.connect("bank.db").cursor()

sql_create_tables_dictionary = {
    # Servico
    "create_servico_table": (
        "CREATE TABLE IF NOT EXISTS servico ("
        + "id_servico integer PRIMARY KEY AUTOINCREMENT,"
        + "num_cartao integer,"
        + "id_aplicacao integer,"
        + "id_seguro integer,"
        + "id_conta integer NOT NULL,"
        + "nome text NOT NULL,"
        + "data_contratada text NOT NULL,"
        + "data_vencimento text,"
        + "FOREIGN KEY(num_cartao) REFERENCES cartao(num_cartao) ON DELETE CASCADE,"
        + "FOREIGN KEY(id_aplicacao) REFERENCES aplicacao(id_aplicacao) ON DELETE CASCADE,"
        + "FOREIGN KEY(id_seguro) REFERENCES seguro(id_seguro) ON DELETE CASCADE,"
        + "FOREIGN KEY(id_conta) REFERENCES conta(id_conta) ON DELETE CASCADE"
        + ");"
    ),
    "create_cartao_table": (
        "CREATE TABLE IF NOT EXISTS cartao ("
        + "num_cartao integer PRIMARY KEY,"
        + "id_tipo integer NOT NULL,"
        + "limite integer,"
        + "fatura integer,"
        + "data_fatura text,"
        + "data_expiracao text,"
        + "cvv integer NOT NULL,"
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo) ON DELETE RESTRICT"
        + ");"
    ),
    "create_aplicacao_table": (
        "CREATE TABLE IF NOT EXISTS aplicacao ("
        + "id_aplicacao integer PRIMARY KEY AUTOINCREMENT,"
        + "id_tipo integer NOT NULL,"
        + "nome text NOT NULL,"
        + "valor_aplicado integer NOT NULL,"
        + "data_retirada text,"
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo) ON DELETE RESTRICT"
        + ");"
    ),
    "create_seguro_table": (
        "CREATE TABLE IF NOT EXISTS seguro ("
        + "id_seguro integer PRIMARY KEY AUTOINCREMENT,"
        + "id_tipo integer NOT NULL,"
        + "carencia integer,"  # integer ou text
        + "FOREIGN KEY(id_tipo) REFERENCES tipo_servico(id_tipo) ON DELETE RESTRICT"
        + ");"
    ),
    "create_tipo_servico_table": (
        "CREATE TABLE IF NOT EXISTS tipo_servico ("
        + "id_tipo integer PRIMARY KEY AUTOINCREMENT,"
        + "nome text NOT NULL"
        # talvez tenha que adicionar mais um atributo
        + ");"
    ),
    # Conta
    "create_conta_table": (
        "CREATE TABLE IF NOT EXISTS conta ("
        + "id_conta integer PRIMARY KEY AUTOINCREMENT,"
        + "CPF text,"
        + "CNPJ text,"
        + "num_agencia integer NOT NULL,"
        + "id_gerente integer NOT NULL,"
        + "tipo text NOT NULL,"  # text ou integer
        + "saldo integer NOT NULL,"
        + "status text NOT NULL,"  # text ou integer
        + "FOREIGN KEY(CPF, CNPJ) REFERENCES cliente(CPF, CNPJ) ON DELETE CASCADE,"  # CASCADE?
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia) ON DELETE RESTRICT,"
        + "FOREIGN KEY(id_gerente) REFERENCES funcionario(id_funcionario) ON DELETE RESTRICT"
        + ");"
    ),
    "create_cliente_table": (
        "CREATE TABLE IF NOT EXISTS cliente ("
        + "CPF text,"
        + "CNPJ text,"
        + "nome text NOT NULL,"
        + "sobrenome text NOT NULL,"
        + "CEP integer NOT NULL,"
        + "rua text,"
        + "num_endereco integer,"
        + "cidade text NOT NULL,"
        + "estado text NOT NULL,"
        + "renda integer NOT NULL,"
        + "PRIMARY KEY(CPF, CNPJ)"
        + ");"
    ),
    "create_telefone_table": (
        "CREATE TABLE IF NOT EXISTS telefone ("
        + "CPF text,"
        + "CNPJ text,"
        + "num_agencia integer,"
        + "telefone text NOT NULL CHECK (length(telefone) >= 11),"
        + "PRIMARY KEY(CPF, CNPJ, num_agencia, telefone),"
        + "FOREIGN KEY(CPF, CNPJ) REFERENCES cliente(CPF, CNPJ) ON DELETE CASCADE,"
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia) ON DELETE CASCADE"
        + ");"
    ),
    "create_transfere_para_table": (
        "CREATE TABLE IF NOT EXISTS transfere_para ("
        + "id_transferencia integer PRIMARY KEY AUTOINCREMENT,"
        + "id_remetente integer NOT NULL,"
        + "id_destino integer NOT NULL,"
        + "valor integer NOT NULL,"
        + "data text NOT NULL,"
        + "horario text,"
        + "FOREIGN KEY(id_remetente) REFERENCES conta(id_conta) ON DELETE RESTRICT,"
        + "FOREIGN KEY(id_destino) REFERENCES conta(id_conta) ON DELETE RESTRICT"
        + ");"
    ),
    # Agencia
    "create_agencia_table": (
        "CREATE TABLE IF NOT EXISTS agencia ("
        + "num_agencia integer PRIMARY KEY,"
        + "CEP integer NOT NULL,"
        + "rua text,"
        + "num_endereco integer"
        + ");"
    ),
    # Funcionario
    "create_funcionario_table": (
        "CREATE TABLE IF NOT EXISTS funcionario ("
        + "id_funcionario integer PRIMARY KEY AUTOINCREMENT,"
        + "data_de_nascimento text NOT NULL,"
        + "nome text NOT NULL,"
        + "bonificacao integer,"
        + "num_agencia integer NOT NULL,"
        + "horas_trabalhadas integer NOT NULL,"
        + "FOREIGN KEY(num_agencia) REFERENCES agencia(num_agencia) ON DELETE RESTRICT"
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
