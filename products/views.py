from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop-Каталог',
        'products': [
            {'title': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090,
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'image': '/static/vendor/img/products/Adidas-hoodie.png'},
            {'title': 'Синяя куртка The North Face', 'price': 23725,
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'title': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390,
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'title': 'Черный рюкзак Nike Heritage', 'price': 2340,
             'text': 'Плотная ткань. Легкий материал.',
             'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'text': 'Гладкий кожаный верх. Натуральный материал.',
             'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'title': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890,
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ]
    }
    return render(request, 'products/products.html', context)
