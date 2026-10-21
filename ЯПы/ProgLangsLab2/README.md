# Кулинарная книга (Консольное приложение)

Простое консольное приложение на C# (.NET) для управления рецептами с использованием PostgreSQL в качестве базы данных. Проект является выполнением лабораторной работы №2 по курсу "Языки Программирования".

## Необходимое ПО

Перед запуском убедитесь, что у вас установлены:

*   [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) или новее.
*   [PostgreSQL](https://www.postgresql.org/download/) (версия 14 или новее).
*   [Git](https://git-scm.com/downloads).

## Установка и запуск

**1. Клонирование репозитория**

Откройте терминал (командную строку) и выполните команду:

```bash
git clone https://gitlab.se.ifmo.ru/Axe-On-Me/proglangstask2.git
cd proglangstask2
```

**2. Настройка базы данных PostgreSQL**

1.  Убедитесь, что ваш сервер PostgreSQL запущен.
2.  Создайте новую базу данных с именем `CookbookDb`. Это можно сделать с помощью утилиты pgAdmin или выполнить команду `createdb CookbookDb` в терминале.

**3. Настройка строки подключения**

1.  Откройте проект в вашем любимом редакторе кода (например, Visual Studio или VS Code).
2.  Найдите и откройте файл `Program.cs`.
3.  Найдите строку, которая начинается с `private const string ConnectionString = ...;`:

    ```csharp
    private const string ConnectionString = "Server=localhost;Port=5432;Database=CookbookDb;User Id=postgres;Password=your_password;";
    ```

4.  **Важно:** Замените `your_password` на реальный пароль, который вы установили для пользователя `postgres` при установке PostgreSQL.

**4. Запуск приложения**

1.  Откройте терминал в корневой папке проекта (где находится файл `.csproj`).
2.  Выполните команду для запуска:

    ```bash
    dotnet run
    ```

3.  При первом запуске Entity Framework Core автоматически создаст таблицу `Recipes` в вашей базе данных. После этого в консоли появится главное меню программы.