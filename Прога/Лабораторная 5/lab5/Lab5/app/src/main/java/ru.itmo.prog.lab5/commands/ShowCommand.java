package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'show'. Выводит все элементы коллекции.
 * @author pmih
 */
public class ShowCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public ShowCommand(Console console, CollectionManager collectionManager) {
        super("show", "вывести все элементы коллекции");
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

            console.println("Элементы коллекции:");
            console.println(collectionManager.toString());
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}