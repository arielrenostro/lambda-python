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
    corpo = json.loads(event['body'])
    cpf = SistemaCUtils.get_campo(corpo, 'cpf')
    
    if SistemaCUtils.is_cpf_valido(cpf):
        return SistemaCUtils.get_retorno_cpf_invalido()

    headers = { 
        "Content-Type": "application/json" 
    }
    
    url = url_base + cpf
    r = requests.post(url, auth=awsauth, headers=headers, data=json.dumps(consulta_cartao))

    response = SistemaCUtils.get_retorno("200")
    response['body'] = json.dumps({
        "situacao": "OK"
    })
    return response
	
def get_consulta_cartao(corpo):
	valor = SistemaCUtils.get_campo(corpo, 'valor')
    data = SistemaCUtils.get_campo(corpo, 'data')
    instituicao = SistemaCUtils.get_campo(corpo, 'instituicao')
    autorizacao = SistemaCUtils.get_campo(corpo, 'autorizacao')
    banco = SistemaCUtils.get_campo(corpo, 'banco')
    
    return {
        'valor': valor,
        'data': data,
        'banco': banco,
        'instituicao': instituicao,
        'autorizacao': autorizacao
    }