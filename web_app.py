from flask import Flask, request, jsonify, render_template, make_response

app = Flask(__name__)

# 1. Первый роут: GET-запросы
@app.route('/get', methods=['GET'])
def get_route():
    if request.method != 'GET':
        return make_response("Метод не поддерживается", 405)
    params = request.args.to_dict()
    return jsonify(params)

# 2. Второй роут: POST-запросы
@app.route('/post', methods=['POST'])
def post_route():
    if request.method != 'POST':
        return make_response("Метод не поддерживается", 405)
    params = request.form.to_dict()
    return jsonify(params)

# 3. Третий роут: HEAD-запросы
@app.route('/head', methods=['HEAD'])
def head_route():
    if request.method != 'HEAD':
        return make_response("Метод не поддерживается", 405)
    else:
        return make_response("OK", 200)

# 4. Четвертый роут: OPTIONS-запросы
@app.route('/options', methods=['OPTIONS'])
def options_route():
    if request.method != 'OPTIONS':
        return make_response("Метод не поддерживается", 405)
    else:
        return make_response("OK", 200)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

