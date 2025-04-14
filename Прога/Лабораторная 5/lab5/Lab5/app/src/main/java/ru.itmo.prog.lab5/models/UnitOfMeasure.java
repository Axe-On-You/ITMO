package ru.itmo.prog.lab5.models;

/**
 * Перечисление единиц измерения продукта.
 * @author pmih
 */
public enum UnitOfMeasure {
    KILOGRAMS,
    PCS,
    LITERS,
    GRAMS,
    MILLIGRAMS;

    /**
     * @return Строка со всеми константами перечисления через запятую.
     */
    public static String names() {
        StringBuilder nameList = new StringBuilder();
        for (UnitOfMeasure unit : values()) {
            nameList.append(unit.name()).append(", ");
        }
        return nameList.substring(0, nameList.length() - 2);
    }
}