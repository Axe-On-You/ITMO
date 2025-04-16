package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Команда 'filter_less_than_price'. Выводит элементы, значение поля price которых меньше заданного.
 * @author pmih
 */
public class FilterLessThanPriceCommand extends Command {
    private final Console console;
    private final CollectionManager collectionManager;

    public FilterLessThanPriceCommand(Console console, CollectionManager collectionManager) {
        super("filter_less_than_price <PRICE>", "вывести элементы, значение поля price которых меньше заданного");
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
            if (arguments.length < 2 || arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            int targetPrice = Integer.parseInt(arguments[1]);
            List<Product> filteredProducts = filterByPrice(targetPrice);

            if (filteredProducts.isEmpty()) {
                console.println("Продуктов с ценой меньше " + targetPrice + " не обнаружено.");
            } else {
                console.println("Найдено продуктов (цена < " + targetPrice + "): " + filteredProducts.size() + " шт.\n");
                filteredProducts.forEach(console::println);
            }
            return true;

        } catch (NumberFormatException e) {
            console.printError("Цена должна быть целым числом!");
        } catch (WrongAmountOfElementsException e) {
            console.printError("Неправильное количество аргументов!");
            console.println("Использование: '" + getName() + "'");
        }
        return false;
    }

    /**
     * Фильтрует продукты по цене (меньше заданного значения).
     * @param targetPrice Цена для сравнения.
     * @return Список продуктов, удовлетворяющих условию.
     */
    private List<Product> filterByPrice(int targetPrice) {
        return collectionManager.getCollection().stream()
                .filter(product -> product.getPrice() != null && product.getPrice() < targetPrice)
                .collect(Collectors.toList());
    }
}