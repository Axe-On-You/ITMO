package ru.itmo.prog.lab5.commands;

/**
 * Интерфейс для выполнения команд с аргументами.
 * @author pmih
 */
public interface Executable {
    /**
     * Выполняет команду.
     * @param arguments Аргументы команды (включая название).
     * @return true, если выполнение прошло успешно, иначе false.
     */
    boolean apply(String[] arguments);
}