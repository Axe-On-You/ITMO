package ru.itmo.prog.lab5.exceptions;

/**
 * Выбрасывается при обнаружении рекурсивного вызова скриптов.
 * @author pmih
 */
public class ScriptRecursionException extends Exception {
    public ScriptRecursionException(String message) {
        super(message);
    }
}