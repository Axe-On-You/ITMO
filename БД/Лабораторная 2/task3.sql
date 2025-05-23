﻿-- 3.
-- Составить запрос, который ответит на вопрос,
-- есть ли среди студентов группы 3102 те, кто младше 20 лет.

SELECT COUNT(*)
FROM "Н_УЧЕНИКИ"
JOIN "Н_ОБУЧЕНИЯ" ON "Н_УЧЕНИКИ"."ИД" = "Н_ОБУЧЕНИЯ"."ЧЛВК_ИД"
JOIN "Н_ЛЮДИ" ON "Н_ОБУЧЕНИЯ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
WHERE "Н_УЧЕНИКИ"."ГРУППА" = '3102'
AND DATE_PART('year', AGE("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")) < 20;

-- Для проверки использовалось следующее (какие вообще возраста есть в группе?):
/*
SELECT DATE_PART('year', AGE("Н_ЛЮДИ"."ДАТА_РОЖДЕНИЯ")) AS возраст, COUNT(*)
FROM "Н_УЧЕНИКИ"
JOIN "Н_ОБУЧЕНИЯ" ON "Н_УЧЕНИКИ"."ИД" = "Н_ОБУЧЕНИЯ"."ЧЛВК_ИД"
JOIN "Н_ЛЮДИ" ON "Н_ОБУЧЕНИЯ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
WHERE "Н_УЧЕНИКИ"."ГРУППА" = '3102'
GROUP BY возраст
ORDER BY возраст;

 возраст | count
---------+-------
      32 |     2
      33 |     1
      37 |     1
      40 |     1
(4 строки)
*/
-- Как видно, в группе нет студентов младше 20
