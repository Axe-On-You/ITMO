-- Создание типов
CREATE TYPE RADAR_TYPE AS ENUM ('Корабельный', 'рабочий');
CREATE TYPE ROAD_LOCATION AS ENUM ('идет к луне', 'обходит луну');

-- Создание таблиц
CREATE TABLE ship (
    id SERIAL PRIMARY KEY,
    ship_name TEXT,
    ship_speed INT
);

CREATE TABLE radar (
    id SERIAL PRIMARY KEY,
    ship_id INT NOT NULL REFERENCES ship(id),
    radar_type RADAR_TYPE
);

CREATE TABLE moon (
    id SERIAL PRIMARY KEY,
    planet_name TEXT,
    diameter INT,
    moon_type TEXT
);

CREATE TABLE signals (
    id SERIAL PRIMARY KEY,
    radar_id INT NOT NULL REFERENCES radar(id),
    reflection BOOLEAN
);

CREATE TABLE road (
    id SERIAL PRIMARY KEY,
    ship_id INT NOT NULL REFERENCES ship(id),
    moon_id INT NOT NULL REFERENCES moon(id),
    road_type ROAD_LOCATION
);

CREATE TABLE activity (
    id SERIAL PRIMARY KEY,
    radar_id INT NOT NULL REFERENCES radar(id),
    signals_id INT NOT NULL REFERENCES signals(id),
    moon_id INT NOT NULL REFERENCES moon(id),
    power TEXT,
    frequency TEXT
);

-- Вставка данных
INSERT INTO ship(ship_name, ship_speed)
    VALUES ('Дискавери', 150000);

INSERT INTO radar(radar_type, ship_id)
    VALUES
        ('Корабельный', 1),
        ('рабочий', 1);

INSERT INTO moon(planet_name, diameter, moon_type)
    VALUES ('Юпитер', 10000, 'летающие горы');

INSERT INTO road(road_type, ship_id, moon_id)
    VALUES
        ('идет к луне', 1, 1),
        ('обходит луну', 1, 1);

INSERT INTO signals(reflection, radar_id)
    VALUES (FALSE, 1);

INSERT INTO activity(power, frequency, radar_id, signals_id, moon_id)
    VALUES ('подобные беззвучным грозовым разрядам', 'раз в несколько минут', 1, 1, 1);

--И здесь, в тридцати миллионах километров,
--мчались луны Юпитера - другие, намного меньшие.
--Это были просто летающие горы поперечником в десятки километров,
--но трасса корабля не подходила близко ни к одной из них.
--Корабельный радар с промежутками в несколько минут
--посылал в пространство импульсы энергии,
--подобные беззвучным грозовым разрядам,
--и не получал ни одного отраженного сигнала из ближайших зон -
--вокруг было пусто.