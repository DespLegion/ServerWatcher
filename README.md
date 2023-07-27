# Server Watcher

### Простой Discord бот, отображающий состояние сервера (или ПК) в статусе и позволяющий получить краткую информацию о системе и ресурсах системы. Совместим как с Windows, так и с Linux

![](https://i.ibb.co/yN0WFYG/watchers.jpg)

## Доступные команды бота
1) `status` - Отображает актуальный статус системных ресурсов

![](https://i.ibb.co/tm3bzm2/sys-status.jpg)

2) `system` - Отображает общие ресурсы системы

![](https://i.ibb.co/vv4Ht6X/Sys-info.jpg)

3) `net` - Отображает актуальную статистику использования сети

![](https://i.ibb.co/vVdqhxw/net-status.jpg)

4) `shutdown` - Завершение работы приложения (бота)

## Требования
1) Python 3.10 или старше
2) Git

## Установка, настройка и запуск приложения:
1) Создать приложение (бота) на [discord.com/developers](https://discord.com/developers/applications/)
2) Создать директорию проекта `/home/watcher`
3) Склонировать этот репозиторий в созданную директрию (`git clone https://github.com/DespLegion/ServerWatcher.git`)
4) Создать виртуальное окружение (`python3 -m venv venv`)
5) Активировать виртуальное окружение (Win: `.\venv\Scripts\activate`, Linux: `source venv/bin/activate`)
6) Установить зависимости (`pip install -r requirements.txt`)
7) Заполнить `config.py`
8) Запустить `core.py` (В фоне: Win - `pythonw core.py`)

## Автозапуск
### Windows

#### На основе шаблона:

Вместе с проектом идет шаблон `.bat` файла `\autorun\watcher.bat`.
1) Создайте ярлык .bat файла
2) Поместите ярлык в папку автозагрузки Windows `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
Или добавьте `.bat` файл в планировщик задач Windows

#### Если вы хотите вручную создать и заполнить .bat файл:
1) Создать `.bat` файл
2) Через оператор `call` прописать путь до файла активации виртуального окружения `activate.bat`
3) Указать директорию проекта, в которой находится исполняемый файл `core.py`
4) Прописать запуск исполняемого файла `core.py` через `python.exe` (для запуска в фоне `pythonw.exe`)
5) Пример: 
```
@echo off
call C:\Watcher\ServerWatcher\venv\Scripts\activate.bat && cd C:\Watcher\ServerWatcher && pythonw core.py
```
4) Добавить .bat файл в автозагрузку или в планировщик задач Windows

### Linux

#### На основе шаблона:
Вместе с проектом идет шаблон `service` файла `\autorun\watcher.service`. 
1) Создайте символическу ссылку на `service` файл идущий вместе с проектом командой: `ln -s /home/watcher/ServerWatcher/autorun/watcher.service /usr/lib/systemd/system/watcher.service`
2) После создания/изменения `systemd` файла необходимо перезапустить демона: `sudo systemctl daemon-reload`
3) Активируйте сервис командой `sudo systemctl enable "project name.service"`
4) Запустите сервис командой `sudo systemctl start "project name".service`

#### Если вы хотите вручную создать и заполнить `service` файл:
1) Создайте `systemd` файл проета по пути `/lib/systemd/system/"project name".service`
2) Пример заполнения 
``` 
[Unit]
Description="description"

[Service]
WorkingDirectory="project work directory"
Type=simple
ExecStart="python venv path" "core.py path"
Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
```
3) После создания/изменения `systemd` файла необходимо перезапустить демона: `sudo systemctl daemon-reload`
4) Активируйте сервис командой `sudo systemctl enable "project name.service"`
5) Запустите сервис командой `sudo systemctl start "project name".service`

## Список версий и изменений
#### 1.0.0

#### 1.1.0
1) Добавлен отлов ошибок при обновлении статуса бота
2) Добавлены шаблоны .service и .bat файлов
3) Расширена инструкция по установке и использованию приложения

#### 1.2.0
1) Немного изменена структура проекта
2) Добавлены Таймауты для обновления статуса бота
3) Добавлено логирование ошибок при обновлении статуса бота
4) Обновлен config файл (ВАЖНО!)

#### 1.2.1
1) Обновлен шаблон .bat файла для Windows

#### 1.2.2
1) Переработана система ведения логов
2) Добавлен автоматический перезапуск для обновления статуса бота

#### 1.2.3
1) Откорректирован старт обновления статуса бота