from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/greet', methods=['POST'])
def greet():
    name = request.json.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')