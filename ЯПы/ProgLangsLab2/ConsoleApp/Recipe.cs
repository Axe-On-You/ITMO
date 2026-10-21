using System.ComponentModel.DataAnnotations;

/// <summary>
/// Представляет один рецепт в кулинарной книге.
/// Реализует IComparable для возможности сортировки в коллекциях по названию.
/// </summary>
public class Recipe : IComparable<Recipe>
{
    // Уникальный идентификатор для базы данных
    public int Id { get; set; }

    [Required] // Атрибут указывает, что поле обязательно для EF Core
    [MaxLength(100)] // Ограничение длины
    public string Title { get; set; } = string.Empty;

    [MaxLength(500)]
    public string Description { get; set; } = string.Empty;

    // Шаги будут храниться как один текстовый блок, разделенный новой строкой
    public string Steps { get; set; } = string.Empty;

    public int CompareTo(Recipe? other)
    {
        if (other == null) return 1;
        // Рецепты сравниваются по названию для сортировки
        return string.Compare(Title, other.Title, StringComparison.OrdinalIgnoreCase);
    }

    public override string ToString()
    {
        var stepsFormatted = Steps.Replace("\n", "\n  ");
        return $"Название: {Title}\nОписание: {Description}\nШаги:\n  {stepsFormatted}";
    }
}