package ru.itmo.prog.lab5.exceptions;

public class CollectionIsEmptyException extends RuntimeException {
    public CollectionIsEmptyException(String message) {
        super(message);
    }
}
