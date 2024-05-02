import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

RankMunic = pd.DataFrame(sessao.query(
                oc.tbMunicipio.municipio.label("Município"),
                sa.func.sum(oc.tbOcorrencias.qtde).label("Total")
            ).join(
                oc.tbOcorrencias,
                oc.tbOcorrencias.codIBGE == oc.tbMunicipio.codIBGE
            ).where(
                oc.tbOcorrencias.ocorrencia == "roubo_veiculo"
            ).group_by(
                oc.tbMunicipio.municipio
            ).order_by(
                sa.func.sum(oc.tbOcorrencias.qtde).desc()
            ).all()
        )

print(RankMunic)