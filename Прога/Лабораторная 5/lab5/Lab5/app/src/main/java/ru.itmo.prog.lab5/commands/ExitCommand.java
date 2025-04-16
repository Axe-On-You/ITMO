package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'exit'. Завершает выполнение.
 * @author pmih
 */
public class ExitCommand extends Command {
    private final Console console;

    public ExitCommand(Console console) {
        super("exit", "завершить программу (без сохранения в файл)");
        this.console = console;
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

            console.println("Завершение выполнения...");
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}