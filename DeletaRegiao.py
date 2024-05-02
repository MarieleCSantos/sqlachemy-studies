import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

metadado = sa.MetaData(bind=engine)
sa.MetaData.reflect(metadado)

tbMunicipio = metadado.tables[oc.tbMunicipio.__tablename__]

deleta_regiao = sa.delete(tbMunicipio).where(
                                            tbMunicipio.c.regiao == "Capital"
                                        )
try:
    engine.execute(deleta_regiao)
    print("Dados deletados")
except ValueError:
    ValueError()