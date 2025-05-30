﻿-- 2.
-- Сделать запрос для получения атрибутов из указанных таблиц, применив фильтры по указанным условиям:
-- Таблицы: Н_ЛЮДИ, Н_ВЕДОМОСТИ, Н_СЕССИЯ.
-- Вывести атрибуты: Н_ЛЮДИ.ОТЧЕСТВО, Н_ВЕДОМОСТИ.ДАТА, Н_СЕССИЯ.ИД.
-- Фильтры (AND):
-- a) Н_ЛЮДИ.ИМЯ > Ярослав.
-- b) Н_ВЕДОМОСТИ.ИД < 1250972.
-- Вид соединения: INNER JOIN.

SELECT "Н_ЛЮДИ"."ОТЧЕСТВО", "Н_ВЕДОМОСТИ"."ДАТА", "Н_СЕССИЯ"."ИД"
FROM "Н_ЛЮДИ"
INNER JOIN "Н_СЕССИЯ" ON "Н_ЛЮДИ"."ИД" = "Н_СЕССИЯ"."ЧЛВК_ИД"
INNER JOIN "Н_ВЕДОМОСТИ" ON "Н_СЕССИЯ"."СЭС_ИД" = "Н_ВЕДОМОСТИ"."ИД"
WHERE "Н_ЛЮДИ"."ИМЯ" > 'Ярослав'
AND "Н_ВЕДОМОСТИ"."ИД" < 1250972;

-- Для проверки использовалось следующее:
/*
SELECT DISTINCT "ИМЯ" FROM "Н_ЛЮДИ" ORDER BY "ИМЯ" DESC LIMIT 10;
      ИМЯ
----------------
 Яхья Али Галеб
 Ярослав
 Янис
 Яна
 Ян
 Яков
 Юсаф
 Юрий
 Юлия
 Юлий
(10 строк)
*/
-- Есть всего одно ИМЯ >, чем Ярослав