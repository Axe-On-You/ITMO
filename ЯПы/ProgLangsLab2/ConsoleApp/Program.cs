using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    // Строка подключения к вашей базе данных PostgreSQL.
    // Замените на ваши реальные данные!
    // Server=localhost;Port=5432;Database=CookbookDb;User Id=postgres;Password=your_password;
    private const string ConnectionString = "Server=localhost;Port=5432;Database=CookbookDb;User Id=postgres;Password=*********;";

    private static RecipeRepository? _repository;

    static void Main(string[] args)
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.InputEncoding = System.Text.Encoding.UTF8;

        try
        {
            _repository = new RecipeRepository(ConnectionString);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка подключения к базе данных. Убедитесь, что PostgreSQL запущен и строка подключения верна.");
            Console.WriteLine($"Подробности: {ex.Message}");
            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
            return;
        }

        bool running = true;
        while (running)
        {
            Console.WriteLine("\n--- Кулинарная книга ---");
            Console.WriteLine("1. Добавить новый рецепт");
            Console.WriteLine("2. Удалить рецепт по названию");
            Console.WriteLine("3. Найти рецепт");
            Console.WriteLine("4. Показать все рецепты");
            Console.WriteLine("5. Выход");
            Console.Write("Выберите действие: ");

            switch (Console.ReadLine())
            {
                case "1":
                    AddRecipeFlow();
                    break;
                case "2":
                    DeleteRecipeFlow();
                    break;
                case "3":
                    SearchRecipeFlow();
                    break;
                case "4":
                    ShowAllRecipesFlow();
                    break;
                case "5":
                    running = false;
                    break;
                default:
                    Console.WriteLine("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.");
                    break;
            }
        }

        Console.WriteLine("Программа завершена.");
    }

    private static void AddRecipeFlow()
    {
        Console.WriteLine("\n--- Добавление нового рецепта ---");

        Console.Write("Название: ");
        string title = Console.ReadLine() ?? "";

        Console.Write("Краткое описание: ");
        string description = Console.ReadLine() ?? "";

        Console.WriteLine("Введите шаги приготовления (для завершения введите пустую строку):");
        List<string> steps = new List<string>();
        string step;
        int stepNumber = 1;
        while (!string.IsNullOrWhiteSpace(step = Console.ReadLine() ?? ""))
        {
            steps.Add($"{stepNumber}. {step}");
            stepNumber++;
        }

        var newRecipe = new Recipe
        {
            Title = title,
            Description = description,
            // Объединяем шаги в одну строку с разделителем \n
            Steps = string.Join("\n", steps)
        };

        _repository!.AddRecipe(newRecipe);
        Console.WriteLine("Рецепт успешно добавлен!");
    }

    private static void DeleteRecipeFlow()
    {
        Console.WriteLine("\n--- Удаление рецепта ---");
        Console.Write("Введите точное название рецепта для удаления: ");
        string title = Console.ReadLine() ?? "";

        if (_repository!.DeleteRecipeByTitle(title))
        {
            Console.WriteLine("Рецепт успешно удален.");
        }
        else
        {
            Console.WriteLine("Рецепт с таким названием не найден.");
        }
    }

    private static void SearchRecipeFlow()
    {
        Console.WriteLine("\n--- Поиск рецепта ---");
        Console.Write("Введите слово или слова для поиска: ");
        string query = Console.ReadLine() ?? "";

        var results = _repository!.SearchRecipes(query).ToList();

        if (!results.Any())
        {
            Console.WriteLine("По вашему запросу ничего не найдено.");
        }
        else
        {
            Console.WriteLine($"Найдено рецептов: {results.Count}");
            foreach (var recipe in results)
            {
                Console.WriteLine("--------------------");
                Console.WriteLine(recipe.ToString());
            }
        }
    }

    private static void ShowAllRecipesFlow()
    {
        Console.WriteLine("\n--- Все рецепты ---");
        var allRecipes = _repository!.GetAllRecipes().ToList();

        if (!allRecipes.Any())
        {
            Console.WriteLine("В кулинарной книге пока нет ни одного рецепта.");
        }
        else
        {
            foreach (var recipe in allRecipes)
            {
                Console.WriteLine("--------------------");
                Console.WriteLine(recipe.ToString());
            }
        }
    }
}
