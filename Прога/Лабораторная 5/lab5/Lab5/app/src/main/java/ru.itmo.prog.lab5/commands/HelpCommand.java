package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CommandManager;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Команда 'help'. Выводит справку по доступным командам.
 * @author pmih
 */
public class HelpCommand extends Command {
    private final Console console;
    private final CommandManager commandManager;

    public HelpCommand(Console console, CommandManager commandManager) {
        super("help", "вывести справку по доступным командам");
        this.console = console;
        this.commandManager = commandManager;
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

            console.println("Доступные команды:");
            commandManager.getCommands().values().forEach(command ->
                    console.printTable(command.getName(), command.getDescription())
            );
            return true;

        } catch (WrongAmountOfElementsException exception) {
            console.printError("Аргументы отсутствуют!");
            console.println("Использование: '" + getName() + "'");
            return false;
        }
    }
}