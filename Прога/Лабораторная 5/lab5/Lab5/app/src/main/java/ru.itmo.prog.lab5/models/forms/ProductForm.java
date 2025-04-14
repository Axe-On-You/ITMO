package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.MustBeNotEmptyException;
import ru.itmo.prog.lab5.exceptions.NotInDeclaredLimitsException;
import ru.itmo.prog.lab5.models.Coordinates;
import ru.itmo.prog.lab5.models.Organization;
import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.models.UnitOfMeasure;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.console.Console;
import java.time.LocalDateTime;
import java.util.NoSuchElementException;

/**
 * Форма продукта.
 * @author pmih
 */
public class ProductForm extends Form<Product> {
    private final Console console;

    public ProductForm(Console console) {
        this.console = console;
    }

    @Override
    public Product build() throws IncorrectInputInScriptException, InvalidFormException {
        var product = new Product(
                askName(),
                askCoordinates(),
                LocalDateTime.now(),
                askPrice(),
                askManufactureCost(),
                askUnitOfMeasure(),
                askManufacturer()
        );
        if (!product.validate()) throw new InvalidFormException();
        return product;
    }

    /**
     * Запрашивает название продукта.
     * @return Непустая строка.
     */
    private String askName() throws IncorrectInputInScriptException {
        String name;
        boolean fileMode = Interrogator.isFileMode();
        while (true) {
            try {
                console.println("Введите название продукта:");
                console.ps2();
                name = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(name);
                if (name.isEmpty()) throw new MustBeNotEmptyException();
                break;
            } catch (MustBeNotEmptyException e) {
                console.printError("Название не может быть пустым!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return name;
    }

    /**
     * Запрашивает координаты.
     * @return Объект Coordinates.
     */
    private Coordinates askCoordinates() throws IncorrectInputInScriptException, InvalidFormException {
        return new CoordinatesForm(console).build();
    }

    /**
     * Запрашивает цену (может быть null).
     * @return Цена > 0 или null.
     */
    private Integer askPrice() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        int price;
        while (true) {
            try {
                console.println("Введите цену продукта (число > 0 или пустая строка для null):");
                console.ps2();
                String input = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(input);

                if (input.isEmpty()) return null;

                price = Integer.parseInt(input);
                if (price <= 0) throw new NotInDeclaredLimitsException();
                break;
            } catch (NumberFormatException e) {
                console.printError("Цена должна быть целым числом!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NotInDeclaredLimitsException e) {
                console.printError("Цена должна быть больше нуля!");
                if (fileMode) throw new IncorrectInputInScriptException();
            }
        }
        return price;
    }

    /**
     * Запрашивает стоимость производства (может быть null).
     * @return Целое число или null.
     */
    private Integer askManufactureCost() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        int cost;
        while (true) {
            try {
                console.println("Введите стоимость производства (целое число или пустая строка для null):");
                console.ps2();
                String input = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(input);

                if (input.isEmpty()) return null;

                cost = Integer.parseInt(input);
                break;
            } catch (NumberFormatException e) {
                console.printError("Введите целое число!");
                if (fileMode) throw new IncorrectInputInScriptException();
            }
        }
        return cost;
    }

    /**
     * Запрашивает единицу измерения (не может быть null).
     * @return Объект UnitOfMeasure.
     */
    private UnitOfMeasure askUnitOfMeasure() throws IncorrectInputInScriptException {
        return new UnitOfMeasureForm(console).build();
    }

    /**
     * Запрашивает производителя (может быть null).
     * @return Объект Organization или null.
     */
    private Organization askManufacturer() throws IncorrectInputInScriptException, InvalidFormException {
        return new OrganizationForm(console).build();
    }
}