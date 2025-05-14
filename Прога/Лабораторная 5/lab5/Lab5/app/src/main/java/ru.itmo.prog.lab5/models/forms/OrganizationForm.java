package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.MustBeNotEmptyException;
import ru.itmo.prog.lab5.exceptions.NotInDeclaredLimitsException;
import ru.itmo.prog.lab5.models.Address;
import ru.itmo.prog.lab5.models.Organization;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.NoSuchElementException;

/**
 * Форма организации.
 * @author pmih
 */
public class OrganizationForm extends Form<Organization> {
    private final Console console;

    public OrganizationForm(Console console) {
        this.console = console;
    }

    @Override
    public Organization build() throws IncorrectInputInScriptException, InvalidFormException {
        console.println("Введите слово 'null' в консоль, чтобы оставить организацию пустой. Любой другой ввод, в т. ч. пустая строка, создаст новую организацию:");
        console.ps2();

        boolean fileMode = Interrogator.isFileMode();
        String input = Interrogator.getUserScanner().nextLine().trim();
        if (fileMode) console.println(input);
        if (input.equalsIgnoreCase("null")) return null;

        console.println("! Создание новой организации:");
        var organization = new Organization(
                askName(),
                askFullName(),
                askAnnualTurnover(),
                askPostalAddress()
        );
        if (!organization.validate()) throw new InvalidFormException();
        return organization;
    }

    /**
     * Запрашивает название организации.
     * @return Непустая строка.
     */
    private String askName() throws IncorrectInputInScriptException {
        String name;
        boolean fileMode = Interrogator.isFileMode();
        while (true) {
            try {
                console.println("Введите название организации:");
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
     * Запрашивает полное название организации.
     * @return Строка длиной до 1564 символов.
     */
    private String askFullName() throws IncorrectInputInScriptException {
        String fullName;
        boolean fileMode = Interrogator.isFileMode();
        while (true) {
            try {
                console.println("Введите полное название организации (до 1564 символов):");
                console.ps2();
                fullName = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(fullName);
                if (fullName.isEmpty()) throw new MustBeNotEmptyException();
                if (fullName.length() > 1564) throw new NotInDeclaredLimitsException();
                break;
            } catch (MustBeNotEmptyException e) {
                console.printError("Полное название не может быть пустым!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NotInDeclaredLimitsException e) {
                console.printError("Длина не должна превышать 1564 символов!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return fullName;
    }

    /**
     * Запрашивает годовой оборот.
     * @return Число > 0.
     */
    private float askAnnualTurnover() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        float annualTurnover;
        while (true) {
            try {
                console.println("Введите годовой оборот (число > 0):");
                console.ps2();
                String input = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(input);

                annualTurnover = Float.parseFloat(input);
                if (annualTurnover <= 0) throw new NotInDeclaredLimitsException();
                break;
            } catch (NumberFormatException e) {
                console.printError("Введите число!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NotInDeclaredLimitsException e) {
                console.printError("Значение должно быть больше нуля!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return annualTurnover;
    }

    /**
     * Запрашивает почтовый адрес (может быть null).
     * @return Объект Address или null.
     */
    private Address askPostalAddress() throws IncorrectInputInScriptException, InvalidFormException {
        console.println("Введите слово 'null' в консоль, чтобы оставить адрес пустым. Любой другой ввод, в т. ч. пустая строка, создаст новый адрес:");
        console.ps2();
        String input = Interrogator.getUserScanner().nextLine().trim();
        if (input.equalsIgnoreCase("null")) return null;
        return new AddressForm(console).build();
    }
}