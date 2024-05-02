import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

base = orm.declarative_base()

# Tabela tbDP
class tbDP(base):
    __tablename__ = "tbDP"

    codDP = sa.Column(sa.INTEGER, primary_key = True, index = True)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    endereco = sa.Column(sa.VARCHAR(255), nullable = False)

# Tabela tbResponsavelSP
class tbResponsavelSP(base):
    __tablename__ = "tbResponsavelSP"

    codDP = sa.Column(sa.INTEGER, sa.ForeignKey("tbDP.codDP",ondelete="NO ACTION",onupdate="CASCADE"), primary_key = True, index = True)
    delegado = sa.Column(sa.VARCHAR(100), nullable = False)

# Tabela tbMunicipio
class tbMunicipio(base):
    __tablename__ = "tbMunicipio"

    codIBGE = sa.Column(sa.INTEGER, primary_key = True, index = True)
    municipio = sa.Column(sa.VARCHAR(100),  nullable = False)
    regiao = sa.Column(sa.VARCHAR(25), nullable = False)

# Tabela tbOcorrencias
class tbOcorrencias(base):
    __tablename__ = "tbOcorrencias"

    idRegistro = sa.Column(sa.INTEGER, primary_key = True, index = True)
    codDP = sa.Column(sa.INTEGER, sa.ForeignKey("tbDP.codDP",ondelete="NO ACTION",onupdate="CASCADE"), index = True)
    codIBGE = sa.Column(sa.INTEGER, sa.ForeignKey("tbMunicipio.codIBGE",ondelete="NO ACTION",onupdate="CASCADE"), index = True)
    ano = sa.Column(sa.CHAR(4), nullable = False)
    mes = sa.Column(sa.VARCHAR(2), nullable = False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable = False)
    qtde = sa.Column(sa.INTEGER, nullable = False)

try: 
    base.metadata.create_all(engine) #cria as tabelas
    print("Tabelas criadas")   
except ValueError:
    ValueError()