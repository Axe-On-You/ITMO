package ru.itmo.prog.lab5.commands;

import ru.itmo.prog.lab5.exceptions.ScriptRecursionException;
import ru.itmo.prog.lab5.exceptions.WrongAmountOfElementsException;
import ru.itmo.prog.lab5.managers.CommandManager;
import ru.itmo.prog.lab5.utility.console.Console;
import ru.itmo.prog.lab5.utility.Interrogator;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * Команда 'execute_script'. Выполнить скрипт из файла.
 * @author pmih
 */
public class ExecuteScriptCommand extends Command {
    private final Console console;
    private final CommandManager commandManager;
    private static final Set<String> scriptStack = new HashSet<>();

    public ExecuteScriptCommand(Console console, CommandManager commandManager) {
        super("execute_script <file_name>", "исполнить скрипт из указанного файла");
        this.console = console;
        this.commandManager = commandManager;
    }

    @Override
    public boolean apply(String[] arguments) {
        String scriptPath = null;
        try {
            if (arguments.length != 2 || arguments[1].isEmpty())
                throw new WrongAmountOfElementsException();

            String fileName = arguments[1];
            File scriptFile = new File(fileName);
            scriptPath = scriptFile.getAbsolutePath();

            // Проверка на рекурсию
            if (scriptStack.contains(scriptPath)) {
                throw new ScriptRecursionException("Рекурсивный вызов скрипта запрещен!");
            }
            console.println("[DEBUG] scriptStack до добавления: " + scriptStack);
            scriptStack.add(scriptPath);
            console.println("[DEBUG] scriptStack после добавления: " + scriptStack);

            // Чтение файла
            if (!scriptFile.exists()) throw new FileNotFoundException(fileName);
            if (!scriptFile.canRead()) throw new SecurityException("Нет прав на чтение файла: " + fileName);

            Scanner fileScanner = new Scanner(scriptFile);
            Interrogator.setUserScanner(fileScanner);
            Interrogator.setFileMode();

            console.println("[DEBUG] Начало выполнения скрипта: " + fileName);
            while (fileScanner.hasNextLine()) {
                String commandLine = fileScanner.nextLine().trim();
                if (commandLine.isEmpty()) continue;
                console.println("[DEBUG] Выполнение команды: " + commandLine);
                commandManager.executeCommand(commandLine.split(" "));
            }
            console.println("[DEBUG] Завершение скрипта: " + fileName);

            return true;

        } catch (WrongAmountOfElementsException e) {
            console.printError("Неправильное количество аргументов!");
            console.println("Использование: '" + getName() + "'");
        } catch (FileNotFoundException e) {
            console.printError("Файл не найден: " + e.getMessage());
        } catch (SecurityException e) {
            console.printError("Ошибка доступа: " + e.getMessage());
        } catch (ScriptRecursionException e) {
            console.printError(e.getMessage());
        } finally {
            // Восстановление интерактивного режима
            Interrogator.setUserScanner(new Scanner(System.in));
            Interrogator.setUserMode();
            // Удаляем только текущий скрипт из стека
            if (scriptPath != null) {
                scriptStack.remove(scriptPath);
                console.println("[DEBUG] Скрипт удален из стека: " + scriptPath);
                console.println("[DEBUG] scriptStack после удаления: " + scriptStack);
            }
        }
        return false;
    }
}