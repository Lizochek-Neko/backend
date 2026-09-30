from flask import Flask, request, jsonify
import os

app = Flask(__name__)

DATA_FILE = 'data.txt'

@app.route('/api/save', methods=['POST'])
def save_data():
    """Принимает текст и сохраняет в data.txt."""
    data = request.get_json()
    text = data.get('text', '')
    
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    return jsonify({'status': 'success', 'message': 'Данные сохранены'})

@app.route('/api/read', methods=['GET'])
def read_data():
    """Читает содержимое data.txt и возвращает на фронтенд."""
    if not os.path.exists(DATA_FILE):
        return jsonify({'status': 'success', 'data': ''})
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return jsonify({'status': 'success', 'data': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



#Backend 1.0
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/api/save', methods=['POST'])
# def save_data():
#     """Принимает текст с фронтенда и сохраняет в data.txt."""
#     data = request.get_json()
#     text = data.get('text', '')
    
#     with open('data.txt', 'a', encoding='utf-8') as f:
#         f.write(text + '\n')
    
#     return jsonify({'status': 'success', 'message': 'Данные сохранены'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

