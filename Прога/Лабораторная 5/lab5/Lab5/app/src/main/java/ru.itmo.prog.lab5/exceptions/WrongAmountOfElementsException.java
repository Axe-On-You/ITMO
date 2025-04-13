package ru.itmo.prog.lab5.exceptions;

public class WrongAmountOfElementsException extends RuntimeException {
    public WrongAmountOfElementsException(String message) {
        super(message);
    }
}
