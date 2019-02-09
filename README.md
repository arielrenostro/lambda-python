Este é um projeto bem simples de Lambdas que são disparados por alguns endpoints do API Gateway.

Os Lambdas que começam com "notificar" tem o papel de receber alguns dados pelo corpo da requisição e inserir no ElasticSearch. Os demais Lambdas tem o papel de consultar algum dado no ElasticSearch e retornar.

Cada um dos arquivos abaixo corresponde a um Lambda diferente:
 - ultimaCompraCartaoCredito
 - ultimaConsultaCPF
 - movimentacoesFinanceiras
 - notificarCompraCartaoCredito
 - notificarConsultaBureau
 - notificarMovimentacaoFinanceira