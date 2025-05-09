package ru.itmo.prog.lab5.models;

import ru.itmo.prog.lab5.utility.Validatable;
import java.util.Objects;

/**
 * Класс адреса.
 * @author pmih
 */
public class Address implements Validatable {
    private final String street; //Строка не может быть пустой, Поле не может быть null
    private final String zipCode; //Поле не может быть null

    public Address(String street, String zipCode) {
        this.street = street;
        this.zipCode = zipCode;
    }

    /**
     * Валидирует правильность полей.
     * @return true, если все верно, иначе false
     */
    @Override
    public boolean validate() {
        return street != null && !street.isEmpty()
                && zipCode != null;
    }

    public String getStreet() {
        return street;
    }

    public String getZipCode() {
        return zipCode;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Address address = (Address) o;
        return Objects.equals(street, address.street) && Objects.equals(zipCode, address.zipCode);
    }

    @Override
    public int hashCode() {
        return Objects.hash(street, zipCode);
    }

    @Override
    public String toString() {
        return "ул. " + street + ", " + zipCode;
    }
}