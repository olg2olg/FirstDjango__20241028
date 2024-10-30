# FirstDjango_28102024

## Инструкция по развертыванию проекта
1. `python3 -m venv django_venv`
2. `source django_venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py loaddata items.json`
6. `python manage.py runserver`

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

Миграция:
1)изменить класс Таблицы БД
2)python manage.py makemigrations
3)python manage.py migrate
 
Выгрузить и загрузить данные из БД:
python manage.py dumpdata --help
python manage.py dumpdata MainApp --indent 4 > items.json
cat items.json
vi items.json
python manage.py loaddata items.json

