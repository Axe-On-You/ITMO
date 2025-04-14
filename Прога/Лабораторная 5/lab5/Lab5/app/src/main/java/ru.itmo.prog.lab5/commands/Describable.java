package ru.itmo.prog.lab5.commands;

/**
 * Интерфейс для объектов, которые могут быть описаны (например, команды).
 * @author pmih
 */
public interface Describable {
    /**
     * Возвращает название команды.
     * @return Название команды (например, "add", "update").
     */
    String getName();

    /**
     * Возвращает описание команды.
     * @return Описание формата и функциональности команды.
     */
    String getDescription();
}