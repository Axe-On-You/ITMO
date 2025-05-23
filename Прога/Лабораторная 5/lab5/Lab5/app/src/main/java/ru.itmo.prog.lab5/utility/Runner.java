package ru.itmo.prog.lab5.utility;

import ru.itmo.prog.lab5.exceptions.ScriptRecursionException;
import ru.itmo.prog.lab5.managers.CommandManager;
import ru.itmo.prog.lab5.utility.console.Console;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * Управляет выполнением команд в интерактивном режиме и режиме скрипта.
 * @author pmih
 */
public class Runner {
    public enum ExitCode {
        OK,
        ERROR,
        EXIT,
    }

    private final Console console;
    private final CommandManager commandManager;
    private final Deque<String> scriptStack = new LinkedList<>();

    public Runner(Console console, CommandManager commandManager) {
        this.console = console;
        this.commandManager = commandManager;
    }

    /**
     * Запускает интерактивный режим ввода команд.
     */
    public void interactiveMode() {
        var userScanner = Interrogator.getUserScanner();
        boolean continueExecution = true;

        while (continueExecution) {
            try {
                ExitCode commandStatus;
                String[] userCommand;

                do {
                    console.ps1();
                    userCommand = (userScanner.nextLine().trim() + " ").split(" ", 2);
                    userCommand[1] = userCommand[1].trim();

                    commandManager.addToHistory(userCommand[0]);
                    commandStatus = launchCommand(userCommand);
                } while (commandStatus != ExitCode.EXIT);

                continueExecution = false;

            } catch (NoSuchElementException exception) {
                console.printError("Пользовательский ввод не обнаружен!");
                Interrogator.setUserScanner(new Scanner(System.in));
                userScanner = Interrogator.getUserScanner();
            } catch (IllegalStateException exception) {
                console.printError("Непредвиденная ошибка!");
                continueExecution = false;
            }
        }
    }

    /**
     * Запускает выполнение скрипта из файла.
     * @param argument Путь к файлу со скриптом.
     * @return Код завершения выполнения скрипта.
     */
    public ExitCode scriptMode(String argument) {
        String[] userCommand;
        ExitCode commandStatus;
        scriptStack.add(argument);

        if (!new File(argument).exists()) {
            argument = "../" + argument;
        }

        try (Scanner scriptScanner = new Scanner(new File(argument))) {
            if (!scriptScanner.hasNext()) throw new NoSuchElementException();
            Scanner tmpScanner = Interrogator.getUserScanner();
            Interrogator.setUserScanner(scriptScanner);
            Interrogator.setFileMode();

            do {

                do {
                    userCommand = (scriptScanner.nextLine().trim() + " ").split(" ", 2);
                    userCommand[1] = userCommand[1].trim();
                } while (scriptScanner.hasNextLine() && userCommand[0].isEmpty());

                console.println(console.getPS1() + String.join(" ", userCommand));

                // Проверка рекурсии
                if (userCommand[0].equals("execute_script")) {
                    for (String script : scriptStack) {
                        if (userCommand[1].equals(script)) throw new ScriptRecursionException("Рекурсивный вызов скриптов запрещен!");
                    }
                }

                commandStatus = launchCommand(userCommand);
            } while (commandStatus == ExitCode.OK && scriptScanner.hasNextLine());

            Interrogator.setUserScanner(tmpScanner);
            Interrogator.setUserMode();

            if (commandStatus == ExitCode.ERROR && !(userCommand[0].equals("execute_script") && !userCommand[1].isEmpty())) {
                console.println("Проверьте скрипт на корректность введенных данных!");
            }

            return commandStatus;

        } catch (FileNotFoundException exception) {
            console.printError("Файл со скриптом не найден!");
        } catch (NoSuchElementException exception) {
            console.printError("Файл со скриптом пуст!");
        } catch (ScriptRecursionException exception) {
            console.printError("Рекурсивный вызов скриптов запрещен!");
        } catch (IllegalStateException exception) {
            console.printError("Непредвиденная ошибка!");
            System.exit(0);
        } finally {
            scriptStack.removeLast();
        }
        return ExitCode.ERROR;
    }

    /**
     * Выполняет команду.
     * @param userCommand Массив с именем команды и аргументом.
     * @return Код завершения выполнения команды.
     */
    private ExitCode launchCommand(String[] userCommand) {
        if (userCommand[0].isEmpty()) return ExitCode.OK;
        var command = commandManager.getCommands().get(userCommand[0]);

        if (command == null) {
            console.printError("Команда '" + userCommand[0] + "' не найдена. Наберите 'help' для справки");
            return ExitCode.ERROR;
        }

        if (userCommand[0].equals("exit")) {
            if (!commandManager.getCommands().get("exit").apply(userCommand)) return ExitCode.ERROR;
            else return ExitCode.EXIT;
        } else {
            if (!command.apply(userCommand)) return ExitCode.ERROR;
        }

        return ExitCode.OK;
    }
}