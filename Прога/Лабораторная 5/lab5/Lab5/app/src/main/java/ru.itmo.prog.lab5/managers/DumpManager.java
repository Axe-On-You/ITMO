package ru.itmo.prog.lab5.managers;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.google.gson.JsonParseException;

import java.io.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

import ru.itmo.prog.lab5.models.Product;
import ru.itmo.prog.lab5.utility.LocalDateAdapter;
import ru.itmo.prog.lab5.utility.adapters.LocalDateTimeAdapter;
import ru.itmo.prog.lab5.utility.console.Console;

/**
 * Использует файл для сохранения и загрузки коллекции.
 * @author pmih
 */
public class DumpManager {
    private final Gson gson = new GsonBuilder()
            .setPrettyPrinting()
            .serializeNulls()
            .registerTypeAdapter(LocalDate.class, new LocalDateAdapter())
            .registerTypeAdapter(LocalDateTime.class, new LocalDateTimeAdapter())
            .create();

    private final String fileName;
    private final Console console;

    public DumpManager(String fileName, Console console) {
        this.fileName = fileName;
        this.console = console;
    }

    /**
     * Записывает коллекцию в файл.
     * @param collection коллекция
     */
    public void writeCollection(Set<Product> collection) {
        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write(gson.toJson(collection));
        } catch (IOException exception) {
            console.printError("Ошибка записи в файл!");
        }
    }

    /**
     * Считывает коллекцию из файла.
     * @return Считанная коллекция
     */
    public Set<Product> readCollection() {
        try (Scanner scanner = new Scanner(new File(fileName))) {
            StringBuilder jsonString = new StringBuilder();
            while (scanner.hasNextLine()) jsonString.append(scanner.nextLine().trim());

            return gson.fromJson(
                    jsonString.toString(),
                    new TypeToken<HashSet<Product>>(){}.getType()
            );
        } catch (FileNotFoundException e) {
            console.printError("Загрузочный файл не найден!");
        } catch (JsonParseException e) {
            console.printError("Некорректный формат данных в файле!");
        }
        return new HashSet<>();
    }
}