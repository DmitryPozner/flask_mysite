<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>


Реализация CI простейшего Flask приложения с использованием GitHub Actions, Docker.
Запуск Actions срабатывает после push в ветку master.
Этапы: build
    </br>
    - клонирование репозитория на vps сервер
    - авторизация и сборка образа на Dockerhub
    - pull с Docker registry и запуск докер контейнера с flask приложением, предварительно удалив неиспользуемые контейнеры.

url страницы http://80.76.42.94/
### :man_technologist: !!!!! :


