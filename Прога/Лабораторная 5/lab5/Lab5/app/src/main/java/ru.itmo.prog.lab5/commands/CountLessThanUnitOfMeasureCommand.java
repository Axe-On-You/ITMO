package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.UnitOfMeasure;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'count_less_than_unit_of_measure'. Выводит количество элементов, у которых unitOfMeasure меньше заданного.
 * @author pmih
 */
public class CountLessThanUnitOfMeasureCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public CountLessThanUnitOfMeasureCommand(Console console, CollectionManager collectionManager) {
        super("count_less_than_unit_of_measure <unit>", "вывести количество элементов с unitOfMeasure меньше заданного");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length < 2 || arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            UnitOfMeasure targetUnit = UnitOfMeasure.valueOf(arguments[1].toUpperCase());
            long count = collectionManager.getCollection().stream()
                    .filter(product -> product.getUnitOfMeasure().ordinal() < targetUnit.ordinal())
                    .count();

            console.println("Количество элементов с unitOfMeasure меньше " + targetUnit + ": " + count);
            return true;

        } catch (WrongAmountOfElementsException e) {
            console.printError("Неправильное количество аргументов!");
            console.println("Использование: '" + getName() + "'");
        } catch (IllegalArgumentException e) {
            console.printError("Некорректный unitOfMeasure!");
            console.println("Допустимые значения: " + UnitOfMeasure.names());
        }
        return false;
    }
}