using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

/// <summary>
/// Контекст базы данных для работы с кулинарной книгой через Entity Framework Core.
/// </summary>
public class CookbookContext : DbContext
{
    // DbSet представляет таблицу "Recipes" в базе данных.
    public DbSet<Recipe> Recipes { get; set; }

    public CookbookContext(DbContextOptions<CookbookContext> options) : base(options)
    {
    }
}