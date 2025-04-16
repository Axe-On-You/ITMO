package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'head'. Выводит первый элемент коллекции.
 * @author pmih
 */
public class HeadCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public HeadCommand(Console console, CollectionManager collectionManager) {
        super("head", "вывести первый элемент коллекции");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length > 1 && !arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            Product firstProduct = collectionManager.getFirst();
            if (firstProduct == null) {
                console.println("Коллекция пуста!");
            } else {
                console.println("Первый элемент коллекции:\n" + firstProduct);
            }
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}