# Server Watcher

### Простой Discord бот, отображающий состояние сервера (или ПК) в статусе и позволяющий получить краткую информацию о системе и ресурсах системы

## Установка, настройка и запуск приложения:
1) Создать приложение (бота) на [discord.com/developers](https://discord.com/developers/applications/)
2) Создать директорию проекта
3) Склонировать этот репозиторий в созданную директрию
4) Создать виртуальное окружение (`python3 -m venv <myenvname>`)
5) Активировать виртуальное окружение (Win: `.\venv\Scripts\activate`, Lin: `source venv/bin/activate`)
6) Установить зависимости (`pip install -r requirements.txt`)
7) Заполнить `config.py`
8) Запустить `core.py` (В фоне: Win - `pythonw core.py`)

## Автозапуск
### Windows
1) Создать .bat файл
2) Прописать в файле путь до `python.exe` (для запуска в фоне `pythonw.exe`) из виртуального окружения. Пример: `D:\"project name"\"env name"\Scripts\python.exe` Далее через пробел прописать путь до `core.py`
3) Пример: 
```
@echo off
D:\ServerWatcher\venv\Scripts\pythonw.exe D:\ServerWatcher\core.py
```
4) Добавить .bat файл в автозагрузку или в планировщик задач Windows

### Linux
1) Создайте systemd файл проета по пути `/lib/systemd/system/"project name".service`
2) Пример заполнения 
``` 
[Unit]
Description="description"

[Service]
Type=simple
ExecStart="python venv path" "core.py path"

[Install]
WantedBy=multi-user.target
```
3) После создания/изменения systemd файла необходимо перезапустить демона: `sudo systemctl daemon-reload`
4) Запустите сервис командой `sudo systemctl start "project name".service`