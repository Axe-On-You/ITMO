package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.CollectionIsEmptyException;
import ru.itmo.prog.lab5.exceptions.NotFoundException;
import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'remove_by_id'. Удаляет элемент из коллекции по ID.
 * @author pmih
 */
public class RemoveByIdCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public RemoveByIdCommand(Console console, CollectionManager collectionManager) {
        super("remove_by_id <ID>", "удалить элемент из коллекции по ID");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    /**
     * Выполняет команду.
     * @param arguments Аргументы команды (ожидается 1 аргумент — ID элемента).
     * @return Успешность выполнения команды.
     */
    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length != 2 || arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            if (collectionManager.collectionSize() == 0)
                throw new CollectionIsEmptyException();

            int id = Integer.parseInt(arguments[1]);
            Product productToRemove = collectionManager.getById(id);
            if (productToRemove == null)
                throw new NotFoundException();

            collectionManager.removeFromCollection(productToRemove);
            console.println("Продукт с ID=" + id + " успешно удален.");
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
        }
        return false;
    }
}