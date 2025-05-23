-- Создание таблицы для журнала обнаружений
CREATE TABLE reflection_log (
    id SERIAL PRIMARY KEY,
    radar_id INT NOT NULL,
    ship_id INT NOT NULL,
    moon_id INT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signal_power TEXT,
    signal_frequency TEXT,
    description TEXT
);

-- Создание функции триггера
CREATE OR REPLACE FUNCTION log_reflection_detection()
RETURNS TRIGGER AS $$
DECLARE
    v_ship_id INT;
    v_radar_type TEXT;
    v_moon_id INT;
    v_power TEXT;
    v_frequency TEXT;
    v_description TEXT;
BEGIN
    IF NEW.reflection = TRUE THEN
        SELECT r.ship_id, r.radar_type::TEXT INTO v_ship_id, v_radar_type
        FROM radar r
        WHERE r.id = NEW.radar_id;
        
        SELECT a.moon_id, a.power, a.frequency INTO v_moon_id, v_power, v_frequency
        FROM activity a
        WHERE a.signals_id = NEW.id
        LIMIT 1;
        
        v_description := 'Радар типа "' || v_radar_type || 
                        '" обнаружил отраженный сигнал';
        
        IF v_moon_id IS NOT NULL THEN
            v_description := v_description || ' от луны с ID ' || v_moon_id;
        END IF;
        
        INSERT INTO reflection_log (radar_id, ship_id, moon_id, signal_power, 
                                    signal_frequency, description)
        VALUES (NEW.radar_id, v_ship_id, v_moon_id, v_power, v_frequency, v_description);
        
        RAISE NOTICE 'Обнаружен отраженный сигнал от радара %', NEW.radar_id;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создание триггера
CREATE TRIGGER reflection_detection_trigger
AFTER INSERT OR UPDATE ON signals
FOR EACH ROW
EXECUTE FUNCTION log_reflection_detection();