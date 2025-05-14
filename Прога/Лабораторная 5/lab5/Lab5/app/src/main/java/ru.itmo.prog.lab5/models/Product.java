package ru.itmo.prog.lab5.models;

import ru.itmo.prog.lab5.managers.CollectionManager;
import ru.itmo.prog.lab5.utility.Element;

import java.time.LocalDateTime;
import java.util.Objects;

/**
 * Класс продукта
 * @author pmih
 */
public class Product extends Element {
    private static long nextId = 1;

    private final long id; //Значение поля должно быть больше 0, Значение этого поля должно быть уникальным, Значение этого поля должно генерироваться автоматически
    private String name; //Поле не может быть null, Строка не может быть пустой
    private Coordinates coordinates; //Поле не может быть null
    private LocalDateTime creationDate; //Поле не может быть null, Значение этого поля должно генерироваться автоматически
    private Integer price; //Поле может быть null, Значение поля должно быть больше 0
    private Integer manufactureCost; //Поле может быть null
    private UnitOfMeasure unitOfMeasure; //Поле не может быть null
    private Organization manufacturer; //Поле не может быть null

    public Product(String name, Coordinates coordinates, LocalDateTime creationDate,
                   Integer price, Integer manufactureCost, UnitOfMeasure unitOfMeasure, Organization manufacturer) {
        this.id = nextId;
        this.name = name;
        this.coordinates = coordinates;
        this.creationDate = creationDate;
        this.price = price;
        this.manufactureCost = manufactureCost;
        this.unitOfMeasure = unitOfMeasure;
        this.manufacturer = manufacturer;
    }

    /**
     * Обновляет указатель следующего ID
     * @param collectionManager манагер коллекций
     */
    public static void updateNextId(CollectionManager collectionManager) {
        var maxId = collectionManager
                .getCollection()
                .stream().filter(Objects::nonNull)
                .map(Product::getId)
                .mapToLong(Long::longValue).max().orElse(0);
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
        if (coordinates == null || !coordinates.validate()) return false;
        if (creationDate == null) return false;
        return price == null || price > 0;
    }

    public void update(Product product) {
        this.name = product.name;
        this.coordinates = product.coordinates;
        this.creationDate = product.creationDate;
        this.price = product.price;
        this.manufactureCost = product.manufactureCost;
        this.unitOfMeasure = product.unitOfMeasure;
        this.manufacturer = product.manufacturer;
    }

    public static void touchNextId() {
        nextId++;
    }

    @Override
    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Coordinates getCoordinates() {
        return coordinates;
    }

    public LocalDateTime getCreationDate() {
        return creationDate;
    }

    public Integer getPrice() {
        return price;
    }

    public Integer getManufactureCost() {
        return manufactureCost;
    }

    public UnitOfMeasure getUnitOfMeasure() {
        return unitOfMeasure;
    }

    public Organization getManufacturer() {
        return manufacturer;
    }

    @Override
    public int compareTo(Element element) {
        return Long.compare(this.id, element.getId());
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return id == product.id &&
                Objects.equals(name, product.name) &&
                Objects.equals(coordinates, product.coordinates) &&
                Objects.equals(creationDate, product.creationDate) &&
                Objects.equals(price, product.price) &&
                Objects.equals(manufactureCost, product.manufactureCost) &&
                unitOfMeasure == product.unitOfMeasure &&
                Objects.equals(manufacturer, product.manufacturer);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, coordinates, creationDate, price, manufactureCost, unitOfMeasure, manufacturer);
    }

    @Override
    public String toString() {
        return "Продукт №" + id +
                " (добавлен " + creationDate + ")" +
                "\n Название: " + name +
                "\n Местоположение: " + coordinates +
                "\n Цена: " + price +
                "\n Стоимость производства: " + (manufactureCost != null ? manufactureCost : "не указано") +
                "\n Единица измерения: " + unitOfMeasure +
                "\n Производитель:\n    " + manufacturer;
    }
}