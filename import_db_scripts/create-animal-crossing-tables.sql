DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
  name VARCHAR(50),
  nb_1 INTEGER,
  material_1 VARCHAR(50),
  nb_2 INTEGER,
  material_2 VARCHAR(50),
  nb_3 INTEGER,
  material_3 VARCHAR(50),
  nb_4 INTEGER,
  material_4 VARCHAR(50),
  nb_5 INTEGER,
  material_5 VARCHAR(50),
  nb_6 INTEGER,
  material_6 VARCHAR(50),
  buy VARCHAR(50),
  sell INTEGER,
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  recipes_to_unlock INTEGER,
  version VARCHAR(20),
  category VARCHAR(30),
  serial_id INTEGER,
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY recipes(name, nb_1, material_1, nb_2, material_2, nb_3, material_3, nb_4, material_4, nb_5, material_5, nb_6, material_6, buy, sell, miles_price, source, source_notes, recipes_to_unlock, version, category, serial_id, internal_id, entry_id)
FROM :recipes_path
DELIMITER ','
CSV HEADER;
