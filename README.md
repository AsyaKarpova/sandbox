# Бухгалтерская отчетность организаций

Пакет `boo` позволяет скачать и использовать годовую бухгалтерскую отчетность российских компаний, которую 
[Росстат публикует][gks] начиная с 2012 года.

[gks]: http://www.gks.ru/opendata/dataset?q=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C+%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B9+&sort=score+desc%2C+metadata_modified+desc


## Начало работы

```
git clone https://github.com/ru-corporate/sandbox
cd sandbox
pip install -r requirements.txt 
python -i start.py
```

`start.py` включает следующий пример:

```
from boo import Corporate

# Please be prepared download and build operations take a long time!

d = Corporate(2012)

# download row file from Rosstat
d.download()

# create truncated version with fewer columns and rename columns 
d.build()

# read trimmed version as pandas dataframe
df = d.dataframe()
```

После выполнения всей последовательности команд в переменной `df` будет 
датафрейм с данными отчтености компаний за 2012 год. 

См. также [справочник по обозначениям переменных][rename]

[rename]: boo/rename.py

## Учебные задания 

### Текущие задания

1. Изучить используемые [названия переменных][rename]. 
   Из каких частей баланса они берутся? Как они взимосвязаны?
2. Получить данные за 2012 год ([start.py](start.py))
3. Выбрать крупную компанию, найти на ее сайте отчетность по РСБУ за 2012 год,
   сравнить данные с сайта и из базы отчтености Росстата.  
4. Проверить правильность составления отчетности через равенства и неравенства
   (например `ta` = `tp`, `debt_long` < `tp_long`).
3. Вывести список крупнейших российских компаний по объему активов и по 
   объему продаж. Что не так с этим списком? Как его модифцировать?
   (задание - сначала сделать самостоятельно, затем посмотерть `play.py`).

### Будущие задания

- Чего в принципе нет в данных отчетности. Какие подходы есть это оценить?
      
## Задачи по развитию

*(\*)* - приоритеты:

- [ ] крупнейшие компании
- [ ] окаймляющие занчения
- [ ] визуализация в виде карты экономики

### 1. Документация 

- названия переменных и счетов бухучета в виде справочной функции
- размер файлов по годам и (вставить в README.md)

### 2. Финансовый анализ

- типовые финансовые коэффициенты, формулы, их значения для групп компаний
- типы компаний (производственная, холдинговая, финансвая компания)
  и ситуации (рост, инвестиции, банкротство)

### 3. Качество информации 

- составить список крупнейших российискх компаний, соответствующий рейтингам 
  Эксперт, Коммерсант, РБК (\*)
- анализ полноты базы компаний по данным отраслевой статистики (\*)

### 4. Анализ

- модель кредитного скоринга компаний (Altman-Z)
- налоговая нагрузка
- региональная экономика (ЖКХ, транспорт)

### 5. Добавления

- котировальный список ММВБ
- справочник ОКВЭД
- аналогичные системы раскрытия информации за рубежом (EDGAR)

### 6. Парсинг 

- предложения по повышению эффективности алгоритма в `boo.reader`
- склеить данные по компаниям за несколько лет
- более интеллектуальный поиск ошибок в данных

### 7. Визуализация

- Карта российской экономики (\*)

### 8. Пакет

- частичное скачивание 
- тесты
- `pip install boo`
- управление местом расположения данных
- управление проектом через `invoke`

### 9. Выдача - форматы публикация

*Простейшие варианты*

- [ ] markdown  
- [ ] html руками
- [ ] jupiter notebook

*Чуть более сложные варианты*
- [ ] pdf/latex
- [ ] pdf/reportlab
- [ ] react.js презенатция
- [ ] небольшой статичный сайт (jekyll)
- [ ] дополнить?

## Дополнительные ссылки

### Официальные источники

- [Сервис Росстата по получению отчетности](http://www.gks.ru/accounting_report)
- [Выписки из ЕГРЮЛ](https://egrul.nalog.ru/index.html)

### Он-лайн доступ к тем же данным 

- [sbis](https://sbis.ru/contragents/7825706086)
- [list-org](https://www.list-org.com/company/19562)

### Крупные провайдеры (тех же и других данных)

- [Спарк (Интерфакс)](http://www.spark-interfax.ru/ru/about)
- [БИР-Аналитик](https://bir.1prime.ru/)
- [Скрин](https://kontragent.skrin.ru/)
- [Фира-Про]https://pro.fira.ru
