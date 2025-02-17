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