package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;
import ru.itmo.prog.lab5.exceptions.MustBeNotEmptyException;
import ru.itmo.prog.lab5.exceptions.NotInDeclaredLimitsException;
import ru.itmo.prog.lab5.models.Coordinates;
import ru.itmo.prog.lab5.utility.Interrogator;
import ru.itmo.prog.lab5.utility.console.Console;
import java.util.NoSuchElementException;

/**
 * Форма для создания координат.
 * @author pmih
 */
public class CoordinatesForm extends Form<Coordinates> {
    private final Console console;

    public CoordinatesForm(Console console) {
        this.console = console;
    }

    @Override
    public Coordinates build() throws IncorrectInputInScriptException, InvalidFormException {
        var coordinates = new Coordinates(askX(), askY());
        if (!coordinates.validate()) throw new InvalidFormException();
        return coordinates;
    }

    /**
     * Запрашивает координату X.
     * @return X (float, <= 12).
     */
    private float askX() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        float x;
        while (true) {
            try {
                console.println("Введите координату X (число с плавающей точкой, <= 12):");
                console.ps2();
                String input = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(input);

                x = Float.parseFloat(input);
                if (x > 12) throw new NotInDeclaredLimitsException();
                break;
            } catch (NumberFormatException e) {
                console.printError("X должен быть числом!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NotInDeclaredLimitsException e) {
                console.printError("X не может превышать 12!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return x;
    }

    /**
     * Запрашивает координату Y.
     * @return Y (Double, не null, <= 6).
     */
    private Double askY() throws IncorrectInputInScriptException {
        boolean fileMode = Interrogator.isFileMode();
        double y;
        while (true) {
            try {
                console.println("Введите координату Y (число с плавающей точкой, <= 6):");
                console.ps2();
                String input = Interrogator.getUserScanner().nextLine().trim();
                if (fileMode) console.println(input);

                if (input.isEmpty()) throw new MustBeNotEmptyException(); // Y не может быть null
                y = Double.parseDouble(input);
                if (y > 6) throw new NotInDeclaredLimitsException();
                break;
            } catch (NumberFormatException e) {
                console.printError("Y должен быть числом!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NotInDeclaredLimitsException e) {
                console.printError("Y не может превышать 6!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (MustBeNotEmptyException e) {
                console.printError("Y не может быть null!");
                if (fileMode) throw new IncorrectInputInScriptException();
            } catch (NoSuchElementException e) {
                console.printError("Ошибка чтения!");
                System.exit(0);
            }
        }
        return y;
    }
}