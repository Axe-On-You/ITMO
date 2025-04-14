package ru.itmo.prog.lab5.managers;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Оперирует коллекцией.
 * @author pmih
 */
public class CollectionManager {
    private Set<Product> collection = new HashSet<>();
    private LocalDateTime lastInitTime;
    private LocalDateTime lastSaveTime;
    private final DumpManager dumpManager;

    public CollectionManager(DumpManager dumpManager) {
        this.dumpManager = dumpManager;
        loadCollection();
    }

    public void validateAll(Console console) {
        collection.forEach(product -> {
            if (!product.validate()) {
                console.printError("Продукт с id=" + product.getId() + " имеет невалидные поля.");
            }
        });
        console.println("! Загруженные продукты валидны.");
    }

    /**
     * @return коллекция.
     */
    public Set<Product> getCollection() {
        return collection;
    }

    /**
     * @return Последнее время инициализации.
     */
    public LocalDateTime getLastInitTime() {
        return lastInitTime;
    }

    /**
     * @return Последнее время сохранения.
     */
    public LocalDateTime getLastSaveTime() {
        return lastSaveTime;
    }

    /**
     * @return Имя типа коллекции.
     */
    public String collectionType() {
        return collection.getClass().getName();
    }

    /**
     * @return Размер коллекции.
     */
    public int collectionSize() {
        return collection.size();
    }

    /**
     * @param id ID элемента.
     * @return Элемент по его ID или null, если не найдено.
     */
    public Product getById(long id) {
        return collection.stream()
                .filter(product -> product.getId() == id)
                .findFirst()
                .orElse(null);
    }

    /**
     * @param id ID элемента.
     * @return Проверяет, существует ли элемент с таким ID.
     */
    public boolean checkExist(long id) {
        return collection.stream().anyMatch(product -> product.getId() == id);
    }

    /**
     * Добавляет элемент в коллекцию
     * @param element Элемент для добавления.
     */
    public void addToCollection(Product element) {
        collection.add(element);
        Product.touchNextId();
    }

    /**
     * Удаляет элемент из коллекции.
     * @param element Элемент для удаления.
     */
    public void removeFromCollection(Product element) {
        collection.remove(element);
    }

    /**
     * Очищает коллекцию.
     */
    public void clearCollection() {
        collection.clear();
    }

    /**
     * Сохраняет коллекцию в файл
     */
    public void saveCollection() {
        dumpManager.writeCollection(collection);
        lastSaveTime = LocalDateTime.now();
    }

    /**
     * Загружает коллекцию из файла.
     */
    private void loadCollection() {
        collection = dumpManager.readCollection();
        lastInitTime = LocalDateTime.now();
    }

    @Override
    public String toString() {
        if (collection.isEmpty()) return "Коллекция пуста!";
        return String.join("\n\n", collection.stream().map(Product::toString).toList());
    }
}