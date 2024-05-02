import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

endereco = "C:\\Users\\decar\\OneDrive\\Documentos\\Estudos\\Pós-Graduação\\Banco de dados relacional\\material-professor\\pucrs-banco_de_dados_relacional\\Dados\\Exercício\\"

dp = pd.read_csv(endereco + "DP.csv",sep=",")
responsavelDP = pd.read_excel(endereco + "ResponsavelDP.xlsx")
municipio = dp.read_csv(endereco + "Municipio.csv",sep=",")
ocorrencias = pd.read_excel(endereco + "ocorrencias.xlsx")

tbDP = pd.DataFrame(dp)
tbResponsavelDP = pd.DataFrame(responsavelDP)
tbMunicipio = pd.DataFrame(municipio)
tbOcorrencia = pd.DataFrame(ocorrencias)

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")

conn = engine.connect()
metadata = sa.schema.MetaData(bind=engine)
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

#DP
DadosDP = tbDP.to_dict(orient="records")
tabela_DP = sa.Table(oc.tbDP.__tablename__, metadata, autoload=True)
try:
    conn.execute(tabela_DP.insert,DadosDP)
    sessao.commit

except ValueError:
    ValueError()
print("Dados inseridos na tbDP")


#ResponsavelDP
RespDP = tbResponsavelDP.to_dict(orient="records")
tabela_respDP = sa.Table(oc.tbResponsavelSP.__tablename__, metadata, autoload=True)
try:
    conn.execute(tabela_respDP.insert,RespDP)
    sessao.commit

except ValueError:
    ValueError()

print("Dados inseridos na tbResponsavelDP")


#Municipio
DadosMunicipio = tbMunicipio.to_dict(orient="records")
tabela_municipio = sa.Table(oc.tbMunicipio.__tablename__, metadata, autoload=True)
try:
    conn.execute(tabela_municipio.insert,DadosMunicipio)
    sessao.commit

except ValueError:
    ValueError()

print("Dados inseridos na tbMunicipio")


#Ocorrencia
DadosOcorrencia = tbOcorrencia.to_dict(orient="records")
tabela_ocorrencia = sa.Table(oc.tbOcorrencias.__tablename__, metadata, autoload=True)
try:
    conn.execute(tabela_ocorrencia.insert,DadosOcorrencia)
    sessao.commit

except ValueError:
    ValueError()

print("Dados inseridos na tbOcorrencia")
sessao.close_all()
print("Carga de dados finalizada.")