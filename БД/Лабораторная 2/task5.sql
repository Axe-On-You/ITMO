﻿-- 5.
-- Выведите таблицу со средним возрастом студентов во всех группах
-- (Группа, Средний возраст), где средний возраст равен среднему
-- возрасту в группе 1100.

SELECT "Н_УЧЕНИКИ"."ГРУППА", avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")))
FROM "Н_ЛЮДИ"
JOIN "Н_УЧЕНИКИ" ON "Н_УЧЕНИКИ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
GROUP BY "Н_УЧЕНИКИ"."ГРУППА"
HAVING avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ"))) = (
	SELECT avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")))
	FROM "Н_ЛЮДИ"
	JOIN "Н_УЧЕНИКИ" ON "Н_УЧЕНИКИ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
	WHERE "Н_УЧЕНИКИ"."ГРУППА" = '1100'
);

-- Так как считается с высокой точностью, то выводится лишь одна группа из всех (сама 1100)
-- Можно сделать так:
/*
SELECT "Н_УЧЕНИКИ"."ГРУППА", avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")))
FROM "Н_ЛЮДИ"
JOIN "Н_УЧЕНИКИ" ON "Н_УЧЕНИКИ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
GROUP BY "Н_УЧЕНИКИ"."ГРУППА"
HAVING floor(avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")))) = (
	SELECT floor(avg(date_part('year', age("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ"))))
	FROM "Н_ЛЮДИ"
	JOIN "Н_УЧЕНИКИ" ON "Н_УЧЕНИКИ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
	WHERE "Н_УЧЕНИКИ"."ГРУППА" = '1100'
);
*/
-- Вывод всех групп, где целая часть == группе 1100