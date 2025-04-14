package ru.itmo.prog.lab5.models.forms;

import ru.itmo.prog.lab5.exceptions.IncorrectInputInScriptException;
import ru.itmo.prog.lab5.exceptions.InvalidFormException;

/**
 * Абстрактная форма для создания объектов через пользовательский ввод.
 * @param <T> Тип создаваемого объекта.
 * @author pmih
 */
public abstract class Form<T> {
    /**
     * Создает объект типа T на основе введенных данных.
     * @return Созданный объект.
     * @throws IncorrectInputInScriptException Если ошибка ввода в режиме скрипта.
     * @throws InvalidFormException Если данные формы невалидны.
     */
    public abstract T build() throws IncorrectInputInScriptException, InvalidFormException;
}