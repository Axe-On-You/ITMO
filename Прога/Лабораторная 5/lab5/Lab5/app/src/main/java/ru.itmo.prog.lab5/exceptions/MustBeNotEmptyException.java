package ru.itmo.prog.lab5.exceptions;

public class MustBeNotEmptyException extends RuntimeException {
    public MustBeNotEmptyException(String message) {
        super(message);
    }
}
