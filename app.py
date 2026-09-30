from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/save', methods=['POST'])
def save_data():
    """Принимает текст с фронтенда и сохраняет в data.txt."""
    data = request.get_json()
    text = data.get('text', '')
    
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    
    return jsonify({'status': 'success', 'message': 'Данные сохранены'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

