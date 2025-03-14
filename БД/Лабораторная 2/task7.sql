﻿-- 7.
-- Вывести список студентов, имеющих одинаковые имена, но не совпадающие даты рождения.

SELECT DISTINCT "ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", "ДАТА_РОЖДЕНИЯ"
FROM "Н_ЛЮДИ"
WHERE "ИМЯ" IN (
    SELECT "ИМЯ"
    FROM "Н_ЛЮДИ"
    GROUP BY "ИМЯ"
    HAVING COUNT(DISTINCT "ДАТА_РОЖДЕНИЯ") > 1
)
ORDER BY "ИМЯ", "ДАТА_РОЖДЕНИЯ";