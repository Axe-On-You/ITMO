package ru.itmo.prog.lab5.utility.console;

/**
 * Реализация консоли для взаимодействия с пользователем через стандартный ввод/вывод.
 * @author pmih
 */
public class StandardConsole implements Console {
    private static final String PS1 = "$ ";
    private static final String PS2 = "> ";

    @Override
    public void print(Object obj) {
        System.out.print(obj);
    }

    @Override
    public void println(Object obj) {
        System.out.println(obj);
    }

    @Override
    public void printError(Object obj) {
        System.out.println("Ошибка: " + obj);
    }

    @Override
    public void printTable(Object elementLeft, Object elementRight) {
        System.out.printf(" %-35s | %-35s%n", elementLeft, elementRight);
    }

    @Override
    public void ps1() {
        print(PS1);
    }

    @Override
    public void ps2() {
        print(PS2); // Исправлено: было PS1 → стало PS2
    }

    @Override
    public String getPS1() {
        return PS1;
    }

    @Override
    public String getPS2() {
        return PS2; // Исправлено: было PS1 → стало PS2
    }
}