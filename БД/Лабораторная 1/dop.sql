SELECT moon.id AS moon_id, moon.planet_name FROM moon
LEFT JOIN road ON moon.id = road.moon_id
LEFT JOIN activity ON road.ship_id = activity.radar_id
LEFT JOIN signals ON activity.signals_id = signals.id
WHERE signals.reflection IS DISTINCT FROM TRUE;