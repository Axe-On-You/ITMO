package ru.itmo.prog.lab5.managers;

import ru.itmo.prog.lab5.commands.Command;
import ru.itmo.prog.lab5.exceptions.CommandNotFoundException;

import java.util.*;

/**
 * Управляет командами.
 * @author pmih
 */
public class CommandManager {
    private final Map<String, Command> commands = new HashMap<>();
    private final List<String> commandHistory = new ArrayList<>();

    /**
     * Добавляет команду.
     * @param commandName Название команды.
     * @param command Команда.
     */
    public void register(String commandName, Command command) {
        commands.put(commandName, command);
    }

    /**
     * Выполняет команду по её имени и аргументам.
     * @param arguments Аргументы команды (первый элемент — имя команды).
     * @return Успешность выполнения команды.
     */
    public boolean executeCommand(String[] arguments) {
        if (arguments == null || arguments.length == 0 || arguments[0].isEmpty()) {
            return false;
        }

        String commandName = arguments[0];
        Command command = commands.get(commandName);
        if (command == null) {
            throw new CommandNotFoundException("Команда '" + commandName + "' не найдена!");
        }

        addToHistory(commandName);
        return command.apply(arguments);
    }

    /**
     * @return Словарь команд.
     */
    public Map<String, Command> getCommands() {
        return Collections.unmodifiableMap(commands);
    }

    /**
     * @return История команд (последние 11 выполненных команд).
     */
    public List<String> getCommandHistory() {
        int toIndex = Math.min(commandHistory.size(), 11);
        return new ArrayList<>(commandHistory.subList(0, toIndex));
    }

    /**
     * Добавляет команду в историю (сохраняет только последние 11 команд).
     * @param command Команда.
     */
    public void addToHistory(String command) {
        commandHistory.addFirst(command);
        if (commandHistory.size() > 11) {
            commandHistory.removeLast();
        }
    }
}