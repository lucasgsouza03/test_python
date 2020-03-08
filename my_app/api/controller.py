from json import loads, dumps
from flask import request, jsonify, Blueprint
from my_app import app, mongo
from datetime import datetime
from decimal import Decimal
 
api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/controle_troco', methods=['GET', 'POST'])
def controleTroco():
    controle = {'100': 0, '50': 0, '10': 0, '5': 0, '1': 0, '0.50': 0, '0.10': 0, '0.05': 0, '0.01': 0}
    if request.method == 'POST':
        valores = request.get_json() #pega valor json da request com o valor pago e total da compra
        valor_pago = valores['valor_pago']
        valor_total = valores['valor_total']
        troco = round(Decimal(valor_pago) - Decimal(valor_total), 2) #efetua a dedução dos valores para pegar o valor do troco
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #define a data atual para registro do banco de dados
        dados = {"valor_pago":valor_pago, "valor_total": valor_total, 'troco':float(troco), "date":date} # dicionário com dados
        #efetua a validação das melhores notas e moeda para serem utilizada no troco
        if troco > 0:
            for key, value in controle.items():
                n = Decimal(key)
                if troco >= n:
                    value = troco//n
                    troco = round((troco - n*value),2)
                controle[key] = int(value)
        elif troco == 0:
            controle = "Nao sera necessario troco!"
        else:
            controle = "Valor do pagamento insuficiente!"
        dados['controle_troco'] = controle #adiciona a validação do troco no dicionário de dados
        mongo.db.troco.update({"date":date}, dados, upsert=True) #efetua o registro dos dados na collection 'troco' 
        return jsonify(dados) #retorna os dados em formato Json
    else:
        return jsonify({"metodo":"GET"}) #caso o endpint for chamado com GET apensa retorn um Json informando o metodo usado