app.py

import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# Абсолютный путь к базе данных
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'database')

# Если папки для базы данных нет, создаем ее
if not os.path.exists(database_path):
    os.makedirs(database_path)

# Настройка URI для базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(database_path, "database.db")}'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

# Модель данных для игры
class Clock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Clock {self.title}>'

# Инициализация админ-панели
admin = Admin(app, name='ClockStore Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Clock, db.session))

# Главная страница с динамическим контентом
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # Получаем номер страницы
    search_query = request.args.get('search', '')  # Получаем поисковый запрос
    min_price = request.args.get('min_price', 0, type=float)  # Минимальная цена
    max_price = request.args.get('max_price', 1000, type=float)  # Максимальная цена
    sort_by = request.args.get('sort_by', 'title')  # Сортировка по названию или цене
    sort_order = request.args.get('sort_order', 'asc')  # Порядок сортировки: по возрастанию или убыванию

    # Фильтрация игр по поисковому запросу и цене
    query = Clock.query.filter(Clock.price >= min_price, Clock.price <= max_price)
    if search_query:
        query = query.filter(Clock.title.ilike(f'%{search_query}%'))

    # Сортировка
    if sort_by == 'price':
        if sort_order == 'asc':
            query = query.order_by(Clock.price.asc())
        else:
            query = query.order_by(Clock.price.desc())
    else:
        if sort_order == 'asc':
            query = query.order_by(Clock.title.asc())
        else:
            query = query.order_by(Clock.title.desc())

    # Пагинация
    games = query.paginate(page=page, per_page=6, error_out=False)

    return render_template('index.html', games=games, search_query=search_query,
                           min_price=min_price, max_price=max_price, sort_by=sort_by, sort_order=sort_order)

with app.app_context():
    db.create_all()

app.run(debug=True)


index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clock Store</title>
    <!-- Подключаем Bootstrap и внешний файл стилей -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body class="fade-in">

    <!-- Навигационная панель -->
    <nav class="navbar navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#">Clock Store</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>
            </ul>
        </div>
    </nav>

    <div class="container">
        <h1 class="mt-4">Clock Store</h1>

        <!-- Форма фильтрации и поиска -->
        <form method="get" action="/" class="mb-4">
            <div class="row">
                <div class="col-md-3">
                    <input type="text" class="form-control" name="search" value="{{ search_query }}" placeholder="Search by title">
                </div>
                <div class="col-md-2">
                    <input type="number" class="form-control" name="min_price" value="{{ min_price }}" placeholder="Min price">
                </div>
                <div class="col-md-2">
                    <input type="number" class="form-control" name="max_price" value="{{ max_price }}" placeholder="Max price">
                </div>
                <div class="col-md-2">
                    <select class="form-control" name="sort_by">
                        <option value="title" {% if sort_by == 'title' %}selected{% endif %}>Sort by title</option>
                        <option value="price" {% if sort_by == 'price' %}selected{% endif %}>Sort by price</option>
                    </select>
                </div>
                <div class="col-md-2">
                    <button type="submit" class="btn btn-primary btn-block">Filter</button>
                </div>
            </div>
        </form>

        <!-- Список игр -->
        <div class="row">
            {% for game in games.items %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{{ game.image_url }}" class="card-img-top" alt="{{ game.title }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ game.title }}</h5>
                            <p class="card-text">{{ game.description[:150] }}...</p>
                        </div>
                        <div class="card-footer">
                            <p><strong>${{ game.price }}</strong></p>
                            <a href="#" class="btn btn-primary">Buy Now</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>

        <!-- Пагинация -->
        <div class="pagination">
            {% if games.has_prev %}
                <a href="{{ url_for('index', page=games.prev_num) }}" class="btn btn-outline-primary">Previous</a>
            {% endif %}
            <span>Page {{ games.page }} of {{ games.pages }}</span>
            {% if games.has_next %}
                <a href="{{ url_for('index', page=games.next_num) }}" class="btn btn-outline-primary">Next</a>
            {% endif %}
        </div>
    </div>

    <!-- Подвал -->
    <footer class="footer">
        <p>&copy; 2025 Clock Store. All rights reserved. <a href="#">Privacy Policy</a></p>
    </footer>
    
<section class="footer" id="contact">
    <div class="box-container">
        </div class="box">
            <a href="https://www.instagram.com/ashmmsm">instagram</a>
            <a href="https://t.me/nevcomer">telegram</a>
    </div>
<div class="box">
    <h3>Contact info</h3>
    <a href="#">+996707227482</a>
    <a href="#">ashirmamatovasumaya@gmail.com</a>
    <a href="#">Kyrgyzstan - Bishkek</a>
</div>
    <!-- Скрипты для работы Bootstrap -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

style.css

/* Общие стили */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f6f9;
    color: #75a13a;
}

a {
    text-decoration: none;
    color: inherit;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
}

/* Навигационная панель */
.navbar {
    background-color: #c78915;
    padding: 20px;
}

.navbar-brand {
    color: #ecf0f1;
    font-size: 2rem;
    font-weight: bold;
}

.navbar-light .navbar-nav .nav-link {
    color: #ecf0f1;
    font-size: 1.1rem;
    transition: color 0.3s;
}

.navbar-light .navbar-nav .nav-link:hover {
    color: #ffdb58;
}

.navbar-toggler-icon {
    background-color: #ecf0f1;
}

/* Карточки с играми */
.card {
    border: none;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.651);
    transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card-img-top {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    height: 250px;
    object-fit: cover;
    transition: transform 0.3s;
}

.card-img-top:hover {
    transform: scale(1.05);
}

.card-body {
    background-color: #ffffff;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    padding: 20px;
}

.card-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin-bottom: 15px;
}

.card-text {
    font-size: 1rem;
    margin-bottom: 15px;
}

.card-footer {
    background-color: #f1f1f1;
    padding: 10px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    text-align: center;
}

.card-footer .btn {
    width: 100%;
    background-color: #3498db;
    color: #fff;
    border: none;
    padding: 10px;
    font-size: 1.1rem;
    transition: background-color 0.3s;
}

.card-footer .btn:hover {
    background-color: #2980b9;
}

/* Пагинация */
.pagination {
    justify-content: center;
    margin-top: 20px;
}

.pagination a {
    border-radius: 50%;
    margin: 0 5px;
    padding: 10px 15px;
    background-color: #3498db;
    color: white;
    font-weight: bold;
    transition: background-color 0.3s;
}

.pagination a:hover {
    background-color: #2980b9;
}

.pagination .disabled {
    background-color: #bdc3c7;
    cursor: not-allowed;
}

/* Подвал */
.footer {
    background-color: #5f311c;
    color: #ecf0f1;
    padding: 30px;
    text-align: center;
    font-size: 1rem;
}

.footer a {
    color: #ffdb58;
    transition: color 0.3s;
}

.footer a:hover {
    color: #fff;
}

/* Анимации */
.fade-in {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Адаптивность */
@media (max-width: 767px) {
    .navbar-brand {
        font-size: 1.6rem;
    }

    .card-img-top {
        height: 200px;
    }

    .card-body {
        padding: 15px;
    }

    .pagination a {
        padding: 8px 10px;
    }
}



