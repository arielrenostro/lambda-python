import os
import boto3
import json
import requests
from sistema_c_utils import SistemaCUtils
from requests_aws4auth import AWS4Auth

region = 'us-east-1'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = os.environ['ES_HOST']
index = os.environ['ES_INDEX']
url_base = 'https://' + host + '/' + index + '/_doc/'

def handler(event, context):
    cabecalho = event['headers']
    cpf = SistemaCUtils.get_campo(cabecalho, 'cpf')

    if SistemaCUtils.is_cpf_valido(cpf):
        return SistemaCUtils.get_retorno_cpf_invalido()
    
    headers = {
        "Content-Type": "application/json"
    }
    
    url = url_base + cpf
    r = requests.get(url, auth=awsauth, headers=headers)
    
    resposta_es = SistemaCUtils.get_resposta_es(r)
    if not resposta_es:
        response = get_retorno("400")
        response["body"] = json.dumps({
            'erro': 'DADO NAO ENCONTRADO'
        })
        return response
    
    response = SistemaCUtils.get_retorno("200")
    response["body"] = json.dumps(SistemaCUtils.get_campo(resposta_es, 'movimentacoes'))
    return response