package ru.itmo.prog.lab5.exceptions;

public class ScriptRecursionException extends RuntimeException {
    public ScriptRecursionException(String message) {
        super(message);
    }
}
