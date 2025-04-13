package ru.itmo.prog.lab5.exceptions;

public class HistoryIsEmptyException extends RuntimeException {
    public HistoryIsEmptyException(String message) {
        super(message);
    }
}
