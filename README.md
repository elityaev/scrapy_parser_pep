<h1 align="center">Парсинг списка документации Python 
и количества статусов PEP</h1>

<h3 align="center">Описание</h3>
Парсер выводит данные со списком всех РЕР (файл c префиксом `pep_` в папке `results/`) и 
таблицу с количеством РЕР в каждом статусе 
(файл c префиксом `status_summary_` в папке `results/`)


<h3 align="center">Используемые технологии:</h3>
* Python
* Scrapy

<h3 align="center">Запуск</h3>

Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:elityaev/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
```
.\venv\Scripts\activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

<h3 align="center">Использование</h3>

Что бы запустить парсер необходимо выполнить команду

```
scrapy crawl pep 
```
_Автор
Литяев Евгений_