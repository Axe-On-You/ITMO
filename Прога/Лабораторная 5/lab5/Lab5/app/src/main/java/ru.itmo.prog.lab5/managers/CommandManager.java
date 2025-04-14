package ru.itmo.prog.lab5.managers;

import ru.itmo.prog.lab5.commands.Command;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
     * @return Словарь команд.
     */
    public Map<String, Command> getCommands() {
        return commands;
    }

    /**
     * @return История команд (последние 11 выполненных команд).
     */
    public List<String> getCommandHistory() {
        int fromIndex = Math.max(commandHistory.size() - 11, 0);
        return new ArrayList<>(commandHistory.subList(fromIndex, commandHistory.size()));
    }

    /**
     * Добавляет команду в историю (сохраняет только последние 11 команд).
     * @param command Команда.
     */
    public void addToHistory(String command) {
        commandHistory.add(command);
        if (commandHistory.size() > 11) {
            commandHistory.removeFirst();
        }
    }
}