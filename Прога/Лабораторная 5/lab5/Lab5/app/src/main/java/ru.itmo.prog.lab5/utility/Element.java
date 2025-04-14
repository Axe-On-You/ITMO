package ru.itmo.prog.lab5.utility;

/**
 * Абстрактный класс для элементов коллекции, поддерживающих уникальный идентификатор и сравнение.
 * @author pmih
 */
public abstract class Element implements Comparable<Element>, Validatable {
    /**
     * Возвращает уникальный идентификатор элемента.
     * @return Идентификатор в формате long.
     */
    abstract public long getId();
}