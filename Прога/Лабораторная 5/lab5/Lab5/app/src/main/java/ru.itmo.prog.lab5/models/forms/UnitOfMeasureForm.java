package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.models.UnitOfMeasure;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.NoSuchElementException;

/**
 * Форма единицы измерения продукта.
 * @author pmih
 */
public class UnitOfMeasureForm extends Form<UnitOfMeasure> {
    private final Console console;

    public UnitOfMeasureForm(Console console) {
        this.console = console;
    }

    @Override
    public UnitOfMeasure build() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        UnitOfMeasure unitOfMeasure;
        while (true) {
            try {
                console.println("Доступные единицы измерения: " + UnitOfMeasure.names());
                console.println("Введите единицу измерения:");
                console.ps2();

                String input = Interrogator.getUserScanner().nextLine().trim().toUpperCase();
                if (fileMode) console.println(input);

                unitOfMeasure = UnitOfMeasure.valueOf(input);
                break;
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (IllegalArgumentException e) {
                console.printError("Такой единицы измерения нет в списке!");
                if (fileMode) throw new IncorrectInputInScriptException();
            }
        }
        return unitOfMeasure;
    }
}