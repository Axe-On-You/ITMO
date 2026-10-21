# Playlist Manager

## Студент
- ФИО: Михайлов Петр Сергеевич
- Группа: P3211
- ИСУ: 466730
- Вариант: 4
- collection: linked list

## Описание
Консольное приложение-менеджер плейлиста:
- хранит композиции (автор, название, длительность),
- позволяет добавлять, удалять, смотреть список,
- искать по автору или названию.

Коллекция реализована как собственный односвязный список (linked list) на языке C.
---

## 1) Склонировать репозиторий
Если вы ещё не скачали проект:
```gitbash
git clone https://gitlab.se.ifmo.ru/Axe-On-Me/proglangtask1
cd <папка_проекта>
```
---

## 2) Запуск проекта (через терминал)

### Windows (через MSYS2 MinGW64)
1) Установите MSYS2: [msys2.org](https://www.msys2.org/)
2) Откройте “MSYS2 MinGW 64-bit”.
3) Установите инструменты:
```bash
pacman -S --needed mingw-w64-x86_64-gcc make
```
4) Перейдите в папку проекта (пример):
```bash
cd /c/Projects/playlist_manager
```
5) Соберите:
```bash
gcc -std=c11 -Wall -Wextra -O2 src/collections.c src/domain.c src/ui.c src/main.c -o playlist_manager
```
6) Запустите:
```bash
./playlist_manager.exe
```

Если русские буквы отображаются неправильно:
- Выполните в MSYS2: `chcp.com 65001` в отдельном окне cmd перед запуском exe,
- или запускайте в Windows Terminal.

### WSL (Ubuntu) или Linux
1) Установите инструменты (один раз):
```bash
sudo apt update && sudo apt install -y build-essential
```
2) Перейдите в папку проекта:
```bash
cd /путь/к/проекту
```
3) Сборка:
```bash
gcc -std=c11 -Wall -Wextra -O2 src/collections.c src/domain.c src/ui.c src/main.c -o playlist_manager
```
4) Запуск:
```bash
./playlist_manager
```

### macOS (через Homebrew)
1) Установите инструменты (если нужно):
```bash
xcode-select --install
brew install gcc
```
2) Сборка:
```bash
gcc -std=c11 -Wall -Wextra -O2 src/collections.c src/domain.c src/ui.c src/main.c -o playlist_manager
```
3) Запуск:
```bash
./playlist_manager
```