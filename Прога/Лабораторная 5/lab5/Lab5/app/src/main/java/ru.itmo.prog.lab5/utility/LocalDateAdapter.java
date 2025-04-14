package ru.itmo.prog.lab5.utility;

import com.google.gson.*;
import java.lang.reflect.Type;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

/**
 * Адаптер для корректной сериализации и десериализации LocalDate в JSON.
 * @author pmih
 */
public class LocalDateAdapter implements JsonSerializer<LocalDate>, JsonDeserializer<LocalDate> {
    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ISO_LOCAL_DATE;

    /**
     * Сериализует LocalDate в строку формата "yyyy-MM-dd".
     */
    @Override
    public JsonElement serialize(LocalDate date, Type typeOfSrc, JsonSerializationContext context) {
        return new JsonPrimitive(date.format(FORMATTER));
    }

    /**
     * Десериализует строку формата "yyyy-MM-dd" в LocalDate.
     * @throws JsonParseException если строка имеет неверный формат.
     */
    @Override
    public LocalDate deserialize(JsonElement json, Type type, JsonDeserializationContext context)
            throws JsonParseException {
        return LocalDate.parse(json.getAsString(), FORMATTER);
    }
}