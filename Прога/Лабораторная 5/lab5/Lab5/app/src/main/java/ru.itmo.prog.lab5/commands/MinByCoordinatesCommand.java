package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.CollectionIsEmptyException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Coordinates;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'min_by_coordinates'. Выводит любой продукт с минимальными координатами.
 * @author pmih
 */
public class MinByCoordinatesCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public MinByCoordinatesCommand(Console console, CollectionManager collectionManager) {
        super("min_by_coordinates", "вывести продукт с минимальными координатами");
        this.console = console;
        this.collectionManager = collectionManager;
    }

    @Override
    public boolean apply(String[] arguments) {
        try {
            if (collectionManager.collectionSize() == 0)
                throw new CollectionIsEmptyException();

            Product minProduct = collectionManager.getCollection().stream()
                    .min((p1, p2) -> compareCoordinates(p1.getCoordinates(), p2.getCoordinates()))
                    .orElse(null);

            console.println("Продукт с минимальными координатами:\n" + minProduct);
            return true;

        } catch (CollectionIsEmptyException e) {
            console.printError("Коллекция пуста!");
            return false;
        }
    }

    private int compareCoordinates(Coordinates c1, Coordinates c2) {
        // Сравнение по x, затем по y
        int xCompare = Float.compare(c1.x(), c2.x());
        return (xCompare != 0) ? xCompare : Double.compare(c1.y(), c2.y());
    }
}