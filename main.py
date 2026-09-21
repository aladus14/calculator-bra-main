# Importações
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    """Calcula o consumo estimado com base na área, número de luminárias e aparelhos.

    Args:
        size (int): Tamanho (área) da residência
        lights (int): Quantidade de luminárias
        device (int): Quantidade de aparelhos

    Returns:
        float: Consumo estimado
    """
    # Coeficientes usados no cálculo do consumo de energia
    
# ATIVIDADE 4 - ADICIONE UMA CONDIÇÃO PARA CASO O BOTÃO ESPECIAL SEJA CLICADO A FUNÇÃO RETORNE 150 (RESULTADO PERFEITO)
    
    if device == 11:
        return 150
    
    else: 
     home_coef = 100
     light_coef = 0.04
     devices_coef = 5
     return size * home_coef + lights * light_coef + device * devices_coef
    
###################################################
# A primeira página
@app.route('/')
def index():
    return render_template('index.html')

# A segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# A terceira página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
    
@app.route('/form')
def form():
    return render_template('form.html')

#ATIVIDADE 4 VAMOS ADICIONAR OS VALORES DO FORMULÁRIO PARA A FUNÇÃO DE RESULTADO
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variáveis para a coleta dos dados use o exemplo abaixo para criar as variáveis para os outros campos do formulário
    name = request.form['name']

    # Aqui você pode salvar os dados ou enviá-los por email
    return render_template('form_result.html', 
                           # Coloque as variáveis aqui, usando o mesmo padrão do exemplo abaixo
                           name=name,
                           )
    
app.run(debug=True)
