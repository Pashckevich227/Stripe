# Интернет магазин с подключением к Stripe.API
____
В данном проекте реализован простой функционал интернет магазина.
Пользователь может:
* Просматривать существующие товары
* Покупать поштучно с использованием стороннего API (оплата товаров)
* Добавлять товары в корзину
* Удалять товары из корзины
* Оформлять заказ из корзины
____
Протестировать -> http://pashckevich227.pythonanywhere.com/
____
Скачать через Docker:

`docker pull pash4ckevich/django_stripe:main`

`docker run —name django_stripe -d -p 8000:8000 pash4ckevich/django_stripe:main`

После чего в браузере перейдите на `http://localhost:8000/`
____
Склонировать проект к себе:
Специально добавил в общий доступ файл .env с ключами, чтобы все корректно работало, если захотите склонировать. Обычно так не делается и он добавляется в .gitignore

Установка:
`pip install -r requirements.txt`

Запуск:

На Windows:
`python manage.py runserver`

На Linus:
`python3 manage.py runserver`
____
## Главная страница:
![Скриншот 14-02-2023 151619](https://user-images.githubusercontent.com/65419742/218735980-45c5beee-fb88-44cb-b9af-d24c27a6c9f8.jpg)

## Просмотр деталей товара:
![Скриншот 14-02-2023 152230](https://user-images.githubusercontent.com/65419742/218737635-2199a663-dcc4-4175-9dbd-5ac26c81f9c0.jpg)
При нажатии на кнопку Buy пользователя переадрессовывает на страницу оплаты товара (смотри ниже)
____
## Оплата товара
![Скриншот 14-02-2023 152339](https://user-images.githubusercontent.com/65419742/218737823-18e6cb1b-d3f9-483d-884f-5b9d60c53e4d.jpg)

Данный функционал реализован при помощи функции create_checkout_session:
```
def create_checkout_session(request, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': 'Telephone',
                },
                'unit_amount': Item.objects.get(pk=pk),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/item/1',
        cancel_url='http://localhost:8000/item/1',
    )
    return HttpResponse(session.id)
```
В ней необходимо указать информацию о товаре (что-то фиксированное, что-то беру из базы данных), методы оплаты (Stripe предоставляет возможность оформления подписок и товаров)

И js-скрипта в Django templates
```
<script type="text/javascript">
      var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
      var buyButton = document.getElementById('buy-button');
      buyButton.addEventListener('click', function() {
        fetch('/order/checkout', {method: 'GET'})
        .then(response => response.text())
        .then(session => stripe.redirectToCheckout({ sessionId: session }))
      });
    </script>
```
Функция create_checkout_session возвращает id сессии и передается на кнопку, которая перенаправляет пользователя на оплату. 

При GET запросе на http://localhost:8000/buy/1 
![image](https://user-images.githubusercontent.com/65419742/218741644-66ae7c39-9914-43a4-8343-0c0a37af4e1a.png)

При GET запросе на http://localhost:8000/item/1 возвращается HTML страница с описанием товара
![image](https://user-images.githubusercontent.com/65419742/218742243-b5d90cba-835e-4167-840c-d58a2a657401.png)

____
Также реализована корзина, она отображает товары, добавленние в нее, и кнопку Buy all, которая переадрессовывает пользователя на страницу оплаты:
![image](https://user-images.githubusercontent.com/65419742/218743201-404aa976-a1a0-4ff2-b377-16ddfadcd597.png)
![image](https://user-images.githubusercontent.com/65419742/218743329-1da9bd9b-6cbf-4aef-b497-d6ad345db5a3.png)

Для того чтобы совершить оплату введите
* Почта: любая
* Код карты: 4242 4242 4242 4242
* Дата: любой будующий месяц и год
* CVV: любые 3 цифры 
* Фамилия и имя: в верхнем регистре любые два слова (например, PAVEL KHRAMKO)

После успешной оплаты Вас отправят на главную страницу магазина
