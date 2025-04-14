package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.models.forms.ProductForm;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'add'. Добавляет новый элемент в коллекцию.
 * @author pmih
 */
public class AddCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public AddCommand(Console console, CollectionManager collectionManager) {
        super("add {element}", "добавить новый элемент в коллекцию");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    /**
     * Выполняет команду.
     * @param arguments Аргументы команды (ожидается отсутствие аргументов).
     * @return Успешность выполнения команды.
     */
    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length > 1 && !arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            console.println("* Создание нового продукта:");
            Product product = new ProductForm(console).build();
            collectionManager.addToCollection(product);
            console.println("Продукт успешно добавлен!");
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
        } catch (InvalidFormException exception) {
            console.printError("Невалидные поля продукта! Создание отменено.");
        } catch (IncorrectInputInScriptException ignored) {
            // Игнорируется, чтобы не прерывать выполнение скрипта
        }
        return false;
    }
}