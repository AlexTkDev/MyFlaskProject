# Документация к магазину на FastAPI

## Описание проекта

Этот проект представляет собой онлайн-магазин, разработанный с использованием FastAPI. Он позволяет пользователям просматривать товары, добавлять их в корзину и оформлять заказы. Проект использует шаблоны для отображения страниц и Bootstrap 5 для стилизации.

## Структура проекта

```
myshop/
├── instance/
│   ├── __init__.py
│   └── config.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── product.html
│   ├── cart.html
│   └── checkout.html
├── app.py
├── requirements.txt
└── README.md
```

### Описание директорий и файлов

- `instance/`: Директория, содержащая конфигурационные файлы.
  - `__init__.py`: Инициализационный файл для пакета.
  - `config.py`: Файл конфигурации приложения.
  
- `templates/`: Директория, содержащая HTML-шаблоны для отображения страниц.
  - `base.html`: Базовый шаблон, включающий общую структуру страницы.
  - `index.html`: Шаблон главной страницы.
  - `product.html`: Шаблон страницы товара.
  - `cart.html`: Шаблон страницы корзины.
  - `checkout.html`: Шаблон страницы оформления заказа.
  
- `app.py`: Основной файл приложения, содержащий код для запуска сервера и определения маршрутов.
  
- `requirements.txt`: Файл, содержащий список зависимостей проекта.

- `README.md`: Файл с описанием проекта и инструкциями по его запуску.

## Установка и запуск проекта

### Предварительные требования

Убедитесь, что у вас установлены следующие компоненты:

- Python 3.8+
- pip

### Клонирование репозитория

Клонируйте репозиторий с помощью следующей команды:

```bash
git clone <URL вашего репозитория>
cd myshop
```

### Установка зависимостей

Установите зависимости, указанные в файле `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Запуск приложения

Для запуска приложения выполните следующую команду:

```bash
hypercorn app:app --reload
```

Приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Использование Bootstrap 5

В проекте используется Bootstrap 5 для стилизации страниц. Все стили подключены через базовый шаблон `base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">MyShop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/cart">Cart</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/checkout">Checkout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

Все остальные шаблоны наследуют этот базовый шаблон и заполняют блок `content` соответствующим содержимым.

## Маршруты приложения

### Главная страница

Маршрут: `/`

Описание: Отображает главную страницу магазина с перечнем товаров.

### Страница товара

Маршрут: `/product/{product_id}`

Описание: Отображает информацию о выбранном товаре.

### Корзина

Маршрут: `/cart`

Описание: Отображает корзину пользователя с добавленными товарами.

### Оформление заказа

Маршрут: `/checkout`

Описание: Отображает страницу для оформления заказа.

## Заключение

Этот проект представляет собой простой онлайн-магазин, который можно расширять и модифицировать в соответствии с вашими потребностями. FastAPI обеспечивает высокую производительность и удобство разработки, а использование шаблонов и Bootstrap 5 позволяет легко создавать современные и отзывчивые интерфейсы.
