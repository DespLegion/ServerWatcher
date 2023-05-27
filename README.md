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

Вместе с проектом идет шаблон .bat файла `\autorun\watcher.bat`.
1) Создайте ярлык .bat файла
2) Поместите ярлык в папку автозагрузки Windows `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`
Или добавьте .bat файл в планировщик задач Windows

#### Если вы хотите вручную создать и заполнить .bat файл:
1) Создать .bat файл
2) Прописать в файле путь до `python.exe` (для запуска в фоне `pythonw.exe`) из виртуального окружения. Пример: `D:\"project name"\"env name"\Scripts\python.exe` Далее через пробел прописать путь до `core.py`
3) Пример: 
```
@echo off
C:\ServerWatcher\venv\Scripts\pythonw.exe C:\ServerWatcher\core.py
```
4) Добавить .bat файл в автозагрузку или в планировщик задач Windows

### Linux

#### На основе шаблона:
Вместе с проектом идет шаблон service файла `\autorun\watcher.service`. 
1) Создайте символическу ссылку на service файл идущий вместе с проектом командой: `ln -s /home/watcher/ServerWatcher/autorun/watcher.service /usr/lib/systemd/system/watcher.service`
2) После создания/изменения systemd файла необходимо перезапустить демона: `sudo systemctl daemon-reload`
3) Активируйте сервис командой `sudo systemctl enable "project name.service"`
4) Запустите сервис командой `sudo systemctl start "project name".service`

#### Если вы хотите вручную создать и заполнить service файл:
1) Создайте systemd файл проета по пути `/lib/systemd/system/"project name".service`
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
3) После создания/изменения systemd файла необходимо перезапустить демона: `sudo systemctl daemon-reload`
4) Активируйте сервис командой `sudo systemctl enable "project name.service"`
5) Запустите сервис командой `sudo systemctl start "project name".service`

## Список версий и изменений
#### 1.0.0

#### 1.1.0
1) Добавлен отлов ошибок при обновлении статуса бота
2) Добавлены шаблоны .service и .bat файлов
3) Расширена инструкция по установке и использованию приложения