package ru.itmo.prog.lab5.exceptions;

public class NotInDeclaredLimitsException extends RuntimeException {
    public NotInDeclaredLimitsException(String message) {
        super(message);
    }
}
