package Exceptions;

public class AgeException extends Exception {
    private final String customMessage;

    public AgeException(String message) {
        super(message);
        this.customMessage = message;
    }

    @Override
    public String getMessage() {
        return "Ошибка возраста: " + customMessage;
    }
}