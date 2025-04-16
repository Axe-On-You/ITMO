package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.models.forms.ProductForm;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.Objects;

/**
 * Команда 'add_if_min'. Добавляет новый элемент в коллекцию, если его цена меньше минимальной.
 * @author pmih
 */
public class AddIfMinCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public AddIfMinCommand(Console console, CollectionManager collectionManager) {
        super("add_if_min {element}", "добавить новый элемент в коллекцию, если его цена меньше минимальной цены этой коллекции");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    /**
     * Выполняет команду
     * @return Успешность выполнения команды.
     */
    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length > 1 && !arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            console.println("* Создание нового продукта (add_if_min):");
            Product product = new ProductForm(console).build(); // Исправлен вызов конструктора
            Integer minPrice = getMinPrice();

            if (minPrice == null || product.getPrice() == null || product.getPrice() < minPrice) {
                collectionManager.addToCollection(product);
                console.println("Продукт успешно добавлен!");
            } else {
                console.println("Продукт не добавлен, цена не минимальная (" + product.getPrice() + " >= " + minPrice + ")");
            }
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Неправильное количество аргументов!");
            console.println("Использование: '" + getName() + "'");
        } catch (InvalidFormException exception) {
            console.printError("Поля продукта не валидны! Продукт не создан!");
        } catch (IncorrectInputInScriptException ignored) {}
        return false;
    }

    /**
     * Возвращает минимальную цену в коллекции.
     * @return Минимальная цена или null, если коллекция пуста.
     */
    private Integer getMinPrice() {
        return collectionManager.getCollection().stream()
                .map(Product::getPrice)
                .filter(Objects::nonNull)
                .min(Integer::compare)
                .orElse(null);
    }
}