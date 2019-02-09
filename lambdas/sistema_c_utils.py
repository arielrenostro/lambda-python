import json

class SistemaCUtils:
    
    @staticmethod
    def is_cpf_valido(cpf):
        return not cpf or len(cpf) != 11
        
    @staticmethod
    def get_retorno_cpf_invalido():
        response = SistemaCUtils.get_retorno("400")
        response["body"] = json.dumps({
            'erro': 'CPF INVALIDO'
        })
        return response
    
    @staticmethod
    def get_retorno(codigo):
        return {
            "statusCode": codigo,
            "isBase64Encoded" : False,
            "headers": {
                "Content-Type": "application/json"
            }
        }
    
    @staticmethod    
    def get_campo(event, campo):
        try:
            return event[campo]
        except:
            return ''

    @staticmethod
    def get_resposta_es(r):
        json_resposta = json.loads(r.text)
        return SistemaCUtils.get_campo(json_resposta, "_source")

