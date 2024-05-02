import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

RankDP = pd.DataFrame(sessao.query(
            oc.tbDP.nome.label("DP"),
            sa.func.sum(oc.tbOcorrencias.qtde).label("Total")
        ).join(
            oc.tbOcorrencias,
            oc.tbOcorrencias.codDP == oc.tbDP.codDP
        ).join(
            oc.tbMunicipio,
            oc.tbOcorrencias.codIBGE == oc.tbMunicipio.codIBGE
        ).where(
            oc.tbMunicipio.regiao == "Interior",
            sa.or_(oc.tbOcorrencias.ocorrencia == "roubo_veiculo", oc.tbOcorrencias.ocorrencia == "furto_veiculos")
        ).group_by(
            oc.tbDP.nome
        ).order_by(
            sa.func.sum(oc.tbOcorrencias.qtde).label("Total").desc()
        ).all()
)
print(RankDP)
