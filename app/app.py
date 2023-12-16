from flask import Flask, render_template, request


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/hello', methods=['POST'])
# def hello():
#     name = request.form.get('name')
#     return render_template('hello.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True)

# Создаем экземпляр приложения
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def hello():
    return "Домашнее задание 18.Test Мазуров Александр !"

# Запускаем сервер
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)