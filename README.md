# Hack-back-chugun

EduConnect — это веб-платформа для студентов, преподавателей и работодателей, созданная с целью улучшения образовательного процесса и трудоустройства. Данный репозиторий содержит исходный код backend-приложения.

## 🚀 Стек технологий

- **Python**: ЯП для разбработки программного продукта.
- **MongoDB**: документоориентированная БД.
- **Fast API**: фреймворк для создания HTTP API-серверов.
- **Alembic**: Миграция сущностей БД.
- **Pydantic**: Валидация, сериализация, десериализация.
- **SqlAlchemy**: ORM для работы с postgreSQL.
- **Redis**: БД для кэширования.
- **Docker**: Для запуска контейнерных приложений.
- **Tensorflow**: Для разработки нейронной сети.

---

## 📁 Структура проекта

Hack-back-chugun/
      ├── ai/                                                  # работа с нейронной сетью
          ├── model/ 
                ├── data/                                      # датасет и готовые веса
                ├── src/
                      ├── predict.py                           # использование нейронной сети
                      ├── train.py                             # обучение нейронной сети
      ├── backend/                                             # работа с бэкендом
          ├── src/ 
                ├── core/                                      # основной функционал api
                ├── database/                                  # 3 базы данных
                ├── other/                                     # дополнительные модули 
      ├── tests/                                               # тестирование 
      └── Dockerfile                                           # контейнер



