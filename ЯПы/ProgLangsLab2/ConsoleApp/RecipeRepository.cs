using Microsoft.EntityFrameworkCore;
using System.Xml.Linq;

/// <summary>
/// Инкапсулирует логику работы с данными (CRUD), используя EF Core и коллекцию в памяти.
/// Использует SortedSet, который является реализацией бинарного дерева поиска.
/// </summary>
public class RecipeRepository
{
    private readonly DbContextOptions<CookbookContext> _dbContextOptions;
    // Используем SortedSet - коллекцию на основе бинарного дерева поиска (красно-черное дерево)
    private readonly SortedSet<Recipe> _recipesCache;

    public RecipeRepository(string connectionString)
    {
        _dbContextOptions = new DbContextOptionsBuilder<CookbookContext>()
            .UseNpgsql(connectionString)
            .Options;

        _recipesCache = new SortedSet<Recipe>();

        // Убедимся, что БД создана
        using (var context = new CookbookContext(_dbContextOptions))
        {
            context.Database.EnsureCreated();
        }

        LoadRecipes();
    }

    /// <summary>
    /// Загружает все рецепты из базы данных в кэш (SortedSet).
    /// </summary>
    private void LoadRecipes()
    {
        using (var context = new CookbookContext(_dbContextOptions))
        {
            _recipesCache.Clear();
            var recipesFromDb = context.Recipes.ToList();
            foreach (var recipe in recipesFromDb)
            {
                _recipesCache.Add(recipe);
            }
        }
    }

    /// <summary>
    /// Добавляет новый рецепт в БД и в кэш.
    /// </summary>
    public void AddRecipe(Recipe recipe)
    {
        using (var context = new CookbookContext(_dbContextOptions))
        {
            context.Recipes.Add(recipe);
            context.SaveChanges();
        }
        _recipesCache.Add(recipe);
    }

    /// <summary>
    /// Удаляет рецепт по названию.
    /// </summary>
    /// <returns>True, если рецепт был найден и удален, иначе false.</returns>
    public bool DeleteRecipeByTitle(string title)
    {
        // Ищем рецепт в кэше
        Recipe? recipeToDelete = _recipesCache.FirstOrDefault(r => r.Title.Equals(title, StringComparison.OrdinalIgnoreCase));

        if (recipeToDelete == null)
        {
            return false;
        }

        // Удаляем из БД
        using (var context = new CookbookContext(_dbContextOptions))
        {
            context.Recipes.Remove(recipeToDelete);
            context.SaveChanges();
        }

        // Удаляем из кэша
        _recipesCache.Remove(recipeToDelete);
        return true;
    }

    /// <summary>
    /// Ищет рецепты, используя LINQ.
    /// Поиск выполняется по словам в названии, описании или шагах.
    /// </summary>
    /// <param name="query">Строка поискового запроса.</param>
    /// <returns>Коллекция найденных рецептов.</returns>
    public IEnumerable<Recipe> SearchRecipes(string query)
    {
        // Разбиваем запрос на отдельные слова и приводим к нижнему регистру
        var keywords = query.ToLower().Split(' ', StringSplitOptions.RemoveEmptyEntries);

        // Используем LINQ для композиции условий поиска по кэшу
        // IQueryable не используется, т.к. мы работаем с коллекцией в памяти,
        // но принцип композиции условий сохранен.
        var results = _recipesCache.Where(recipe =>
        {
            var recipeText = (recipe.Title + " " + recipe.Description + " " + recipe.Steps).ToLower();
            // Проверяем, что ВЕСЬ текст рецепта содержит КАЖДОЕ ключевое слово
            // Это можно изменить на .Any(), если нужно, чтобы хотя бы одно слово совпадало
            return keywords.All(keyword => recipeText.Contains(keyword));
        });

        return results;
    }

    /// <summary>
    /// Возвращает все рецепты из кэша.
    /// </summary>
    public IEnumerable<Recipe> GetAllRecipes()
    {
        return _recipesCache;
    }
}