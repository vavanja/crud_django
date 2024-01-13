## Інструкція по встановленню

- git clone https://github.com/vavanja/crud_django.git
- python -m venv venv
- Активація venv: venv/Scripts/activate
- pip install -m requirements.txt
- cd django_project
- python manage.py runserver

### Реалізовано
- Ендпоінт /api/. Точка з якої переходимо по гіперпосиланню на команди(teams) або гравці(players)
- Тестові дані вже є в бд.
- Для команд: список гравців в команді + сторінка кожного гравця.
- Для гравців: реалізований вибір команди, зміна даних гравця.