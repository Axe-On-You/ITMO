package ru.itmo.prog.lab5.exceptions;

public class InvalidFormException extends RuntimeException {
    public InvalidFormException(String message) {
        super(message);
    }
}
