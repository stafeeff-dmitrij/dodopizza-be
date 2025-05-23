# ДОДОПИЦЦА v0.2.0 (DRF API)

Цель данного пет-проекта - реализовать приближенный к [оригиналу](https://dodopizza.ru) сайт с возможностью просмотра
и поиска товаров, регистрацией (смс, email), авторизацией, добавлением товаров в корзину, оформлением заказов,
просмотром истории заказов и оплатой заказов через сервис ЮКассы.

**Фронт** - https://github.com/stafeeff-dmitrij/dodopizza-fe

## Инструменты
* **Python (3.13)**;
* **Django + DRF** (web framework);
* **PostgreSQL** (database);
* **Redis** (caching);
* **Nginx** (web server).
* **Docker Compose** (build, deploy).

Сборка и запуск приложения (с импортом фикстур):
```
docker compose up -d
```

## Демо

При первом посещении сайта нужно запросить доступ:
![](/screens/1.png)
![](/screens/2.png)

При запросе доступа и его подтверждении через админку на почту приходят соответствующие уведомления:
![](/screens/3.png)
![](/screens/4.png)

Главная страница с основными категориями товаров:
![](/screens/5.png)
![](/screens/6.png)
![](/screens/7.png)

Страница конкретной категории товаров с возможностью фильтрации, пагинации и сортировки.
Параметры фильтрации сохраняются и считываются из URL:
![](/screens/8.png)
![](/screens/9.png)

Детальная страница товара с рекомендациями из той же категории:
![](/screens/10.png)

## Развитие

* **~~Каталог (v0.1.0)~~** - главная страница, страница категории с фильтрацией, пагинацией и сортировкой.
Поиск товаров по названию. Детальная информация о товаре;
* **~~Ограничение доступа (v0.2.0)~~** - ограничение доступа к сайту по ip, с возможностью запроса и предоставления доступа
с уведомлением по email;
* **Регистрация, авторизация (v0.3.0)** - регистрация, авторизация по email и смс, а также через сторонние сайты;
* **Профиль (v0.4.0)** - просмотр и редактирование профиля пользователя. Сброс пароля;
* **Корзина (v0.5.0)** - добавление, просмотр и удаление товаров из корзины;
* **Оформление заказа (v0.6.0)** - оформление и оплата заказа с оплатой через сервис ЮКассы. Просмотр истории заказов;
* **Мониторинг логов (v0.7.0)** - подключение стека ElasticSearch, Logstash, Kibana (ELK) для мониторинга логов;
* **Мониторинг метрик (v0.8.0)** - подключение Prometheus и Grafana для мониторинга метрик;
* **CI/CD (v0.9.0)** - добавление gitlab-ci.yml, деплой на сервер через CI/CD;
* **Релиз (v1.0.0)**.

## Dev

В проекте используются git-хуки для автоматической проверки и форматирования кода перед созданием коммита.

Установка **pre-commit**:
   ```
   pip install pre-commit
   ```

Активация хуков:
   ```
   pre-commit install
   ```

Предварительная проверка и форматирование кода:
   ```
   pre-commit run --all-files
   ```

Создание коммита через commitizen:
   ```
   cz commit
   ```
