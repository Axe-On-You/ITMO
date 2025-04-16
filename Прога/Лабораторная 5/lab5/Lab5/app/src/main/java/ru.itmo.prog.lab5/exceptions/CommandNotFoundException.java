package ru.itmo.prog.lab5.exceptions;

/**
 * Выбрасывается, если команда не найдена.
 * @author pmih
 */
public class CommandNotFoundException extends RuntimeException {
    public CommandNotFoundException(String message) {
        super(message);
    }
}