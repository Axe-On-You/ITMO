package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.CollectionIsEmptyException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.NotFoundException;
import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.models.forms.ProductForm;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'update'. Обновляет элемент коллекции по ID.
 * @author pmih
 */
public class UpdateCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public UpdateCommand(Console console, CollectionManager collectionManager) {
        super("update <ID> {element}", "обновить значение элемента коллекции по ID");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    /**
     * Выполняет команду.
     * @param arguments Аргументы команды (ожидается ID элемента).
     * @return Успешность выполнения команды.
     */
    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length < 2 || arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            if (collectionManager.collectionSize() == 0)
                throw new CollectionIsEmptyException();

            int id = Integer.parseInt(arguments[1]);
            Product product = collectionManager.getById(id);
            if (product == null)
                throw new NotFoundException();

            console.println("* Введите данные обновленного продукта:");
            Product newProduct = new ProductForm(console).build();

            product.update(newProduct);
            console.println("Продукт с ID=" + id + " успешно обновлен.");
            return true;

        } catch (WrongAmountOfElementsException e) {
            console.printError("Неправильное количество аргументов!");
            console.println("Использование: '" + getName() + "'");
        } catch (CollectionIsEmptyException e) {
            console.printError("Коллекция пуста!");
        } catch (NumberFormatException e) {
            console.printError("ID должен быть целым числом!");
        } catch (NotFoundException e) {
            console.printError("Продукт с указанным ID не найден!");
        } catch (InvalidFormException e) {
            console.printError("Поля продукта не валидны! Обновление отменено.");
        } catch (IncorrectInputInScriptException ignored) {}
        return false;
    }
}