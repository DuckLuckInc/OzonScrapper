# Ozon scrapper
[![Docker build status](https://github.com/DuckLuckInc/OzonScrapper/actions/workflows/docker-build.yml/badge.svg)](https://github.com/DuckLuckInc/OzonScrapper/actions/workflows/docker-build.yml)

Скраппер для сбора информации о товарах на сайте [Ozon](https://www.ozon.ru) для одноименного учебного проекта в рамках курса [Технопарк](https://park.mail.ru/).

На данный момент не поддерживается получение товаров с возрастным ограничением

# Пример информации о товаре
```json
{"_id": ObjectId("60dca6b4231e25bbc5f2b400"),
  "brand": {"cellTrackingInfo": {"brandMap": {"brand": {"id": 32686750,
                                                        "type": "brand"}}},
            "coverImage": "https://nowatermark.ozone.ru/s3/multimedia-r/6059120559.jpg",
            "id": 32686750,
            "link": "/category/routery-15534000/xiaomi-32686750/",
            "name": "Все товары Xiaomi",
            "popover": {"contentRs": [{"items": [[{"content": "Официальные "
                                                              "поставщики. "
                                                              "Гарантия от "
                                                              "производителя",
                                                   "type": "text"}],
                                                 [{"content": "Товар "
                                                              "сертифицирован, "
                                                              "ввезен "
                                                              "официально на "
                                                              "территорию РФ. "
                                                              "Соответствует "
                                                              "всем стандартам",
                                                   "type": "text"}],
                                                 [{"content": "Обслуживание в "
                                                              "официальных "
                                                              "сервисных "
                                                              "центрах",
                                                   "type": "text"}]],
                                       "type": "list"}]},
            "titleRs": [{"content": "Только оригинальные товары бренда",
                         "type": "textBold"}]},
  "categories": {"brandId": 32686750,
                 "brandName": "Xiaomi",
                 "categoryId": 15534000,
                 "categoryName": "Сетевое оборудование",
                 "currentPageUrl": "https://www.ozon.ru/product/wi-fi-router-xiaomi-mi-router-4a-giga-version-210882663/",
                 "deviceType": "desktop",
                 "hierarchy": "Ozon Express/Электроника/Ноутбуки и аксессуары "
                              "для компьютеров/Сетевое оборудование/Xiaomi",
                 "layoutId": 11852,
                 "layoutVersion": 514,
                 "pageType": "pdp",
                 "platform": "site",
                 "ruleId": 2149,
                 "templateType": "desktop"},
  "characteristics": {"short": [{"key": "WifFiFrequency",
                                 "name": "Частоты Wi-Fi",
                                 "values": [{"key": "WifFiFrequency_0",
                                             "text": "2.4 ГГц"},
                                            {"key": "WifFiFrequency_1",
                                             "text": "5 ГГц"}]},
                                {"key": "LANPorts",
                                 "name": "Количество LAN портов",
                                 "values": [{"key": "LANPorts_0", "text": "2"}]},
                                {"key": "LanSpeedMax",
                                 "name": "Макс. скорость Ethernet",
                                 "values": [{"key": "LanSpeedMax_0",
                                             "text": "1000 Мбит/сек"}]},
                                {"key": "MaxWirelessSpeed",
                                 "name": "Макс. скорость беспроводного "
                                         "соединения, Мбит/с",
                                 "values": [{"key": "MaxWirelessSpeed_0",
                                             "text": "100"}]},
                                {"key": "WiFiRouterStandart",
                                 "name": "Стандарт Wi-Fi",
                                 "values": [{"key": "WiFiRouterStandart_0",
                                             "text": "Wi-Fi 5 (802.11ac)"}]}],
                      "title": ""},
  "collection": "Ozon Express",
  "description": {"@context": "http://schema.org",
                  "@type": "Product",
                  "aggregateRating": {"@type": "AggregateRating",
                                      "ratingValue": "4.8",
                                      "reviewCount": "481"},
                  "brand": "Xiaomi",
                  "description": "Маршрутизатор Xiaomi Mi WiFi Router 4A "
                                 "GIGABIT рассчитан на одновременную передачу "
                                 "данных по частотам 2.4 и 5 ГГц, что позволяет "
                                 "ему обеспечивать скорость Wi-Fi-соединения. "
                                 "Благодаря 4 наружным антеннам с коэффициентом "
                                 "усиления сигнала Wi-Fi на уровне 6 dbi точка "
                                 "доступа в белом корпусе характеризуется "
                                 "большой зоной покрытия и стабильностью "
                                 "подключения беспроводной техники. Для защиты "
                                 "соединения эта модель получила поддержку "
                                 "протоколов WEP, WPA и WPA2.Благодаря одному "
                                 "гигабитному WAN-порту и 2 гигабитным "
                                 "LAN-интерфейсам маршрутизатор Xiaomi Mi WiFi "
                                 "Router 4A GIGABIT может решать задачу "
                                 "проводного подключения пары ПК или других "
                                 "стационарных устройств. Настроить рабочую "
                                 "конфигурацию устройства вам позволит как "
                                 "Web-интерфейс, так и мобильное приложение MI "
                                 "WI-FI для платформ Android и iOS от Xiaomi. "
                                 "Кабель питания и документация представлены в "
                                 "комплекте с этим практичным сетевым решением "
                                 "для дома.",
                  "image": "https://cdn1.ozone.ru/multimedia/1037017096.jpg",
                  "name": "Wi-Fi роутер Xiaomi Mi Router 4A Giga Version",
                  "offers": {"@type": "Offer",
                             "availability": "http://schema.org/InStock",
                             "price": "2791",
                             "priceCurrency": "RUB",
                             "url": "https://www.ozon.ru/product/wi-fi-router-xiaomi-mi-router-4a-giga-version-210882663/"},
                  "sku": "210882663"},
  "images": {"coverImage": "https://cdn1.ozone.ru/multimedia/1037017096.jpg",
             "images": [{"alt": "Wi-Fi роутер Xiaomi Mi Router 4A Giga Version "
                                "#1",
                         "src": "https://cdn1.ozone.ru/multimedia/1037017096.jpg"},
                        {"alt": "Wi-Fi роутер Xiaomi Mi Router 4A Giga Version "
                                "#2",
                         "src": "https://cdn1.ozone.ru/s3/multimedia-m/6007594582.jpg"},
                        {"alt": "Wi-Fi роутер Xiaomi Mi Router 4A Giga Version "
                                "#3",
                         "src": "https://cdn1.ozone.ru/s3/multimedia-s/6007594588.jpg"},
                        {"alt": "Wi-Fi роутер Xiaomi Mi Router 4A Giga Version "
                                "#4",
                         "src": "https://cdn1.ozone.ru/multimedia/1037017097.jpg"}],
             "sku": 210882663},
  "price": {"hintLink": "https://www.ozon.ru/section/credit/",
            "hintText": "Приблизительный расчет. Платеж зависит от срока и типа "
                        "кредитного продукта",
            "isAvailable": True,
            "message": "Доставка за час!",
            "mode": "credit",
            "originalPrice": "2\xa0990\xa0₽",
            "payment": "279\xa0₽",
            "paymentTerm": "12 мес",
            "price": "2\xa0791\xa0₽",
            "showOriginalPrice": True}}

```

# Запуск скраппера
```bash
$ git clone https://github.com/DuckLuckInc/OzonScrapper.git
$ cd OzonScrapper
$ docker build -t ozon_scrapper .
$ docker-compose up -d
```

# Подключение к mongodb
```bash
$ docker exec -it ozonscrapper_mongodb_1 bash
root@c0de6a4af989:/# mongo
MongoDB shell version v4.4.6
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("bf539482-aef1-4fdd-962b-7b5ddaf079da") }
MongoDB server version: 4.4.6
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
	https://community.mongodb.com
---
The server generated these startup warnings when booting:
        2021-06-30T17:41:18.576+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
---
---
        Enable MongoDB\'s free cloud-based monitoring service, which will then receive and display
        metrics about your deployment (disk utilization, CPU, operation statistics, etc).

        The monitoring data will be available on a MongoDB website with a unique URL accessible to you
        and anyone you share the URL with. MongoDB may use this information to make product
        improvements and to suggest MongoDB products and deployment options to you.

        To enable free monitoring, run the following command: db.enableFreeMonitoring()
        To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---
> show collections
> ()
uncaught exception: SyntaxError: expected expression, got ')' :
@(shell):1:1
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
ozon    0.001GB
> use ozon
switched to db ozon
> show collections
Ozon Express
Дом и сад
Обувь
Одежда
Электроника
>
```


#  Изменение настроек

По умолчанию собирается информация не более чеи о 50 товаров из каждой основной категории.

Все изменения происходят в файле [settings.py](https://github.com/DuckLuckInc/OzonScrapper/blob/master/settings.py).

Для изменения максимального количества товаров из каждой категории необходимо изменить значение константы:
```python
# Max items from category
MAX_ITEMS = 50
```

Для изменения категорий необходимо изменить список категорий: 
```python
# Ozon categories
CATEGORIES = [
   {'deeplink': '',
     'id': 15500,
     'image': 'https://cdn1.ozone.ru/s3/cms/02/t58/1-3x.png',
     'sliceTrackingInfo': {'id': '15500',
                           'index': 1,
                           'title': 'Электроника',
                           'type': 'category'},
     'title': 'Электроника',
     'url': '/category/elektronika-15500/'},
    ...
]
```

Для изменения скорости скраппинга (НЕ рекомендуется это делать, т.к. можно получить бан от озона) необходимо изменить значение константы:
```python
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
```
