# FirstDjango_28102024

## Инструкция по развертыванию проекта
1. `python3 -m venv django_venv`
2. `source django_venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py loaddata ./fixtures/items.json`
6. `python manage.py runserver`

## Выгрузка и загрузка данных из БД
### Выгрузить данные из БД для приложения MainApp(все классы)
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
### Выгрузить данные из БД для приложения MainApp, только Item модель(один класс)
python manage.py dumpdata MainApp.item --indent 4 > ./fixtures/only_items.json

### Загрузить данные из БД
python manage.py loaddata ./fixtures/items.json

## Дополнительно
1. Полезное дополнение для шаблонов `Django`
ext install batisteo.vscode-django

Добавить в settings.json
    "emmet.includeLanguages": {
        "django-html": "html",
    },
    "files.associations": {
        "*.html": "django-html"
    }

##  Antares
https://antares-sql.app/
Запускать из командной строки: Antares-xxx --no-sandbox
cd ~/Downloads
./Antares-0.7.29-linux_x86_64.AppImage --no-sandbox

## Запуск `ipython` в контексте приложений `django`
python manage.py shell_plus --ipython

## bpython
python manage.py shell_plus --bpython


## ----------------------------------------
## я сама дописала:
http://127.0.0.1:8000/

https://github.com/olg2olg/FirstDjango_2024_10_28

https://github.com/olg2olg/FirstDjango__20241028

## Миграция:
1. изменить класс Таблицы БД
2. python manage.py makemigrations
3. python manage.py migrate
 
## Выгрузить и загрузить данные из БД:
1. python manage.py dumpdata --help
2. python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
3. cat items.json
4. vi items.json
5. python manage.py loaddata items.json

