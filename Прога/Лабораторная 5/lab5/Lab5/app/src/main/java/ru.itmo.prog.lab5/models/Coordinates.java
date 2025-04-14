package ru.itmo.prog.lab5.models;

import ru.itmo.prog.lab5.utility.Validatable;
import java.util.Objects;

/**
 * Класс координат.
 *
 * @param x Максимальное значение поля: 12
 * @param y Максимальное значение поля: 6, Поле не может быть null
 * @author pmih
 */
public record Coordinates(float x, Double y) implements Validatable {

    /**
     * Валидирует правильность полей.
     *
     * @return true, если все верно, иначе false
     */
    @Override
    public boolean validate() {
        return x <= 12 && y != null && y <= 6;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coordinates that = (Coordinates) o;
        return Float.compare(x, that.x) == 0 && Objects.equals(y, that.y);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}