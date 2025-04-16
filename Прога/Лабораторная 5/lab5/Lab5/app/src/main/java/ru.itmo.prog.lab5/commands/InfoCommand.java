package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.utility.console.Console;
import java.time.LocalDateTime;

/**
 * Команда 'info'. Выводит информацию о коллекции.
 * @author pmih
 */
public class InfoCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public InfoCommand(Console console, CollectionManager collectionManager) {
        super("info", "вывести информацию о коллекции");
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

            LocalDateTime lastInitTime = collectionManager.getLastInitTime();
            String lastInitTimeString = (lastInitTime == null) ?
                    "в данной сессии инициализации еще не происходило" :
                    lastInitTime.toLocalDate() + " " + lastInitTime.toLocalTime();

            LocalDateTime lastSaveTime = collectionManager.getLastSaveTime();
            String lastSaveTimeString = (lastSaveTime == null) ?
                    "в данной сессии сохранения еще не происходило" :
                    lastSaveTime.toLocalDate() + " " + lastSaveTime.toLocalTime();

            console.println("Сведения о коллекции:");
            console.println(" Тип: " + collectionManager.collectionType());
            console.println(" Количество элементов: " + collectionManager.collectionSize());
            console.println(" Дата последнего сохранения: " + lastSaveTimeString);
            console.println(" Дата последней инициализации: " + lastInitTimeString);
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}