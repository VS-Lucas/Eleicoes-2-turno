from time import sleep
from datetime import datetime
import pandas as pd
import json
import requests

bars = '-'*45

while True:
    candidato = []
    votos = []
    porcentagem = []
    numero = []

    dados = requests.get(
        "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"
    )

    dadosJson = json.loads(dados.content)

    att = datetime.now().strftime('%H:%M:%S')

    for infos in dadosJson['cand']:
        candidato.append(infos['nm'])
        numero.append(infos['n'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, numero, votos, porcentagem)),
        columns=['Candidato', 'Número', 'Nº votos', 'Porcentagem']
    )
    
    print(f'Atualizado às {att}\n{df_eleicao}\n{bars}')
    sleep(20)
