from flask import Flask, render_template, request, jsonify
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clima', methods=['POST'])
def get_clima():
    data = request.get_json()
    cidade = data.get('cidade')
    
    if not cidade:
        return jsonify({"erro": "Cidade não informada"}), 400
    
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt&format=json"
    try:
        geo_res = requests.get(geo_url).json()
        
        if not geo_res.get('results'):
            return jsonify({"erro": "Cidade não encontrada"}), 404
        
        local = geo_res['results'][0]
        lat, lon = local['latitude'], local['longitude']

        # Busca Clima
        clima_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        clima_res = requests.get(clima_url).json()
        
        if 'current_weather' in clima_res:
            current = clima_res['current_weather']
            return jsonify({
                "temp": current['temperature'],
                "cidade": local['name'],
                "estado": local.get('admin1', ''),
                "wind": current['windspeed'],
                "code": current['weathercode']
            })
            
    except Exception as e:
        return jsonify({"erro": f"Falha na conexão: {str(e)}"}), 500
    
    return jsonify({"erro": "Erro ao buscar clima"}), 500

if __name__ == '__main__':
    app.run(debug=True)