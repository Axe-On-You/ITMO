package ru.itmo.prog.lab5.models;

import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.utility.Element;

import java.util.Objects;

/**
 * Класс организации
 * @author pmih
 */
public class Organization extends Element {
    private static int nextId = 1;

    private final int id; //Значение поля должно быть больше 0, Значение этого поля должно быть уникальным, Значение этого поля должно генерироваться автоматически
    private final String name; //Поле не может быть null, Строка не может быть пустой
    private final String fullName; //Длина строки не должна быть больше 1564, Строка не может быть пустой, Поле не может быть null
    private final float annualTurnover; //Значение поля должно быть больше 0
    private final Address postalAddress; //Поле может быть null

    public Organization(String name, String fullName, float annualTurnover, Address postalAddress) {
        this.id = nextId;
        nextId++;
        this.name = name;
        this.fullName = fullName;
        this.annualTurnover = annualTurnover;
        this.postalAddress = postalAddress;
    }

    /**
     * Обновляет указатель следующего ID
     * @param collectionManager манагер коллекций
     */
    public static void updateNextId(CollectionManager collectionManager) {
        int maxId = collectionManager
                .getCollection()
                .stream()
                .filter(Objects::nonNull)
                .map(Product::getManufacturer)
                .filter(Objects::nonNull)
                .mapToInt(org -> (int) org.getId())
                .max()
                .orElse(0);

        nextId = maxId + 1;
    }

    /**
     * Валидирует правильность полей.
     * @return true, если все верно, иначе false
     */
    @Override
    public boolean validate() {
        if (id <= 0) return false;
        if (name == null || name.isEmpty()) return false;
        if (fullName == null || fullName.isEmpty() || fullName.length() > 1564) return false;
        return annualTurnover > 0;
    }

    @Override
    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getFullName() {
        return fullName;
    }

    public float getAnnualTurnover() {
        return annualTurnover;
    }

    public Address getPostalAddress() {
        return postalAddress;
    }

    @Override
    public int compareTo(Element element) {
        return Long.compare(this.id, element.getId());
        }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Organization that = (Organization) o;
        return id == that.id &&
                Float.compare(annualTurnover, that.annualTurnover) == 0 &&
                Objects.equals(name, that.name) &&
                Objects.equals(fullName, that.fullName) &&
                Objects.equals(postalAddress, that.postalAddress);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, fullName, annualTurnover, postalAddress);
    }

    @Override
    public String toString() {
        return "Организация \"" + name + "\" №" + id +
                "\nПолное название: " + fullName +
                "\nГодовой оборот: " + annualTurnover +
                "\nАдрес: " + (postalAddress != null ? postalAddress : "не указан");
    }
}