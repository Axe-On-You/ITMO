package ru.itmo.prog.lab5.utility;

/**
 * Интерфейс для объектов, которые могут быть проверены на валидность.
 * @author pmih
 */
public interface Validatable {
    /**
     * Проверяет корректность состояния объекта.
     * @return true, если объект валиден, false — в противном случае.
     */
    boolean validate();
}