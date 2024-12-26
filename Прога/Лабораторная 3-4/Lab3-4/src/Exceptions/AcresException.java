package Exceptions;

public class AcresException extends RuntimeException {
    private final int cause;
    private final String info;
    public AcresException(int cause, String info){
        this.cause = cause;
        this.info = info;
    }

    @Override
    public String getMessage() {
        return "Ошибка в размере акра: был взят " + cause + "-ой " + info;
    }
}