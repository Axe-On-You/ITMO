package ru.itmo.prog.lab5.utility;

import java.util.Scanner;

/**
 * Управляет режимами ввода (интерактивный/файловый) и предоставляет доступ к сканеру.
 * @author pmih
 */
public class Interrogator {
    private static Scanner userScanner;
    private static boolean fileMode = false;

    /**
     * @return Текущий сканер для ввода данных.
     */
    public static Scanner getUserScanner() {
        return userScanner;
    }

    /**
     * Устанавливает сканер для ввода данных.
     * @param userScanner Сканер (может быть из файла или консоли).
     */
    public static void setUserScanner(Scanner userScanner) {
        Interrogator.userScanner = userScanner;
    }

    /**
     * @return true, если активен файловый режим ввода.
     */
    public static boolean isFileMode() {
        return fileMode;
    }

    /**
     * Переключает в режим интерактивного ввода с консоли.
     */
    public static void setUserMode() {
        Interrogator.fileMode = false;
    }

    /**
     * Переключает в режим чтения команд из файла.
     */
    public static void setFileMode() {
        Interrogator.fileMode = true;
    }
}