package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.MustBeNotEmptyException;
import ru.itmo.prog.lab5.exceptions.NotInDeclaredLimitsException;
import ru.itmo.prog.lab5.models.Address;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.NoSuchElementException;

/**
 * Форма для создания адреса.
 * @author pmih
 */
public class AddressForm extends Form<Address> {
    private final Console console;

    public AddressForm(Console console) {
        this.console = console;
    }

    @Override
    public Address build() throws IncorrectInputInScriptException, InvalidFormException {
        var address = new Address(askStreet(), askZipCode());
        if (!address.validate()) throw new InvalidFormException();
        return address;
    }

    /**
     * Запрашивает улицу.
     * @return Непустая строка с названием улицы.
     */
    private String askStreet() throws IncorrectInputInScriptException {
        String street;
        boolean fileMode = Interrogator.isFileMode(); // Используем геттер
        while (true) {
            try {
                console.println("Введите название улицы:");
                console.ps2();
                street = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(street);
                if (street.isEmpty()) throw new MustBeNotEmptyException();
                break;
            } catch (MustBeNotEmptyException e) {
                console.printError("Улица не может быть пустой!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return street;
    }

    /**
     * Запрашивает почтовый индекс.
     * @return Строка с индексом (null, если введена пустая строка, иначе длина >=6).
     */
    private String askZipCode() throws IncorrectInputInScriptException {
        String zipCode;
        boolean fileMode = Interrogator.isFileMode(); // Используем геттер
        while (true) {
            try {
                console.println("Введите почтовый индекс:");
                console.ps2();
                zipCode = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(zipCode);

                if (zipCode.isEmpty()) return null;
                if (zipCode.length() < 6) throw new NotInDeclaredLimitsException();
                break;
            } catch (NotInDeclaredLimitsException e) {
                console.printError("Длина почтового индекса должна быть не менее 6 символов!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return zipCode;
    }
}