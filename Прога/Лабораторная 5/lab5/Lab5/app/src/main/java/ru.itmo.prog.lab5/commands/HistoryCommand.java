package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CommandManager;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'history'. Выводит историю выполненных команд.
 * @author pmih
 */
public class HistoryCommand extends Command {
    private final Console console;
    private final CommandManager commandManager;

    public HistoryCommand(Console console, CommandManager commandManager) {
        super("history", "вывести историю выполненных команд");
        this.console = console;
        this.commandManager = commandManager;
    }

    @Override
    public boolean apply(String[] arguments) {
        try {
            if (arguments.length > 1 && !arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            var history = commandManager.getCommandHistory();
            if (history.isEmpty()) {
                console.println("История команд пуста.");
            } else {
                console.println("Последние " + history.size() + " команд:");
                history.forEach(console::println);
            }
            return true;

        } catch (WrongAmountOfElementsException e) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}