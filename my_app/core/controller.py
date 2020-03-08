from flask import request, Blueprint, render_template

core = Blueprint('core', __name__,url_prefix="/")

#Pagina web de consulta da API 
@core.route('', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
