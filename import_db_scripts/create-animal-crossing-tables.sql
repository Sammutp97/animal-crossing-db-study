DROP TABLE IF EXISTS accessories;
CREATE TABLE accessories (
  name VARCHAR(100),
  variation VARCHAR(30),
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  seasonal_availability VARCHAR(30),
  mannequin_piece BOOLEAN,
  version VARCHAR(20),
  style VARCHAR(20),
  label_themes VARCHAR(100),
  type_of VARCHAR(30),
  villager_equippable BOOLEAN,
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY accessories(name, variation, diy, buy, sell, color_1, color_2, size_of, miles_price, source, source_notes, seasonal_availability, mannequin_piece, version, style, label_themes, type_of, villager_equippable, catalog, filename, internal_id, entry_id)
FROM :path_to_accessories
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS achievements;
CREATE TABLE achievements (
  name VARCHAR(100),
  award_criteria VARCHAR(200),
  nb INTEGER,
  internal_id INTEGER,
  internal_name VARCHAR(50),
  internal_category VARCHAR(30),
  num_of_tiers INTEGER,
  tier_1 INTEGER,
  tier_2 INTEGER,
  tier_3 INTEGER,
  tier_4 INTEGER,
  tier_5 INTEGER,
  reward_tier_1 INTEGER,
  reward_tier_2 INTEGER,
  reward_tier_3 INTEGER,
  reward_tier_4 INTEGER,
  reward_tier_5 INTEGER,
  reward_tier_6 INTEGER,
  sequential BOOLEAN,
  version VARCHAR(20),
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY achievements(name,award_criteria,nb,internal_id,internal_name,internal_category,num_of_tiers,tier_1,tier_2,tier_3,tier_4,tier_5,reward_tier_1,reward_tier_2,reward_tier_3,reward_tier_4,reward_tier_5,reward_tier_6,sequential,version,entry_id)
FROM :path_to_achievements
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS art;
CREATE TABLE art (
  name VARCHAR(100),
  genuine BOOLEAN,
  category VARCHAR(30),
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  real_artwork_title VARCHAR(100),
  artist VARCHAR(100),
  museum_description VARCHAR(1000),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  version VARCHAR(20),
  hha_concept_1 VARCHAR(20),
  hha_concept_2 VARCHAR(20),
  hha_series VARCHAR(20),
  hha_set VARCHAR(20),
  interact BOOLEAN,
  tag VARCHAR(20),
  speaker_type VARCHAR(30),
  lighting_type VARCHAR(20),
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY art(name,genuine,category,buy,sell,color_1,color_2, size_of,real_artwork_title,artist,museum_description,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,hha_set,interact,tag,speaker_type,lighting_type,catalog,filename,internal_id,entry_id)
FROM :path_to_art
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS bags;
CREATE TABLE bags (
  name VARCHAR(100),
  variation VARCHAR(30),
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  seasonal_availability VARCHAR(30),
  version VARCHAR(20),
  style VARCHAR(20),
  label_themes VARCHAR(100),
  villager_equippable BOOLEAN,
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY bags(name,variation,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,seasonal_availability,version,style,label_themes,villager_equippable,catalog,filename,internal_id,entry_id)
FROM :path_to_bags
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS bottoms;
CREATE TABLE bottoms (
  name VARCHAR(100),
  variation VARCHAR(30),
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  seasonal_availability VARCHAR(30),
  mannequin_piece BOOLEAN,
  version VARCHAR(20),
  style VARCHAR(20),
  label_themes VARCHAR(100),
  villager_equippable BOOLEAN,
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY bottoms(name,variation,diy,buy,sell,color_1,color_2, size_of,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,villager_equippable,catalog,filename,internal_id,entry_id)
FROM :path_to_bottoms
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS construction;
CREATE TABLE construction (
  name VARCHAR(100),
  buy VARCHAR(50),
  category VARCHAR(30),
  source VARCHAR(100),
  filename VARCHAR(50),
  version VARCHAR(20),
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY construction(name,buy,category,source,filename,version,entry_id)
FROM :path_to_construction
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS dress_up;
CREATE TABLE dress_up (
  name VARCHAR(100),
  variation VARCHAR(30),
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  seasonal_availability VARCHAR(30),
  mannequin_piece BOOLEAN,
  version VARCHAR(20),
  style VARCHAR(20),
  label_themes VARCHAR(100),
  villager_equippable BOOLEAN,
  catalog VARCHAR(30),
  primary_shape VARCHAR(20),
  secondary_shape VARCHAR(10),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY dress_up(name,variation,diy,buy,sell,color_1,color_2, size_of,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,villager_equippable,catalog,primary_shape,secondary_shape,filename,internal_id,entry_id)
FROM :path_to_dress_up
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS fencing;
CREATE TABLE fencing (
  name VARCHAR(100),
  diy BOOLEAN,
  stack_size INTEGER,
  buy VARCHAR(50),
  sell INTEGER,
  source VARCHAR(100),
  source_notes VARCHAR(100),
  version VARCHAR(20),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY fencing(name,diy,stack_size,buy,sell,source,source_notes,version,filename,internal_id,entry_id)
FROM :path_to_fencing
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS floors;
CREATE TABLE floors (
  name VARCHAR(100),
  vfx BOOLEAN,
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  version VARCHAR(20),
  hha_concept_1 VARCHAR(20),
  hha_concept_2 VARCHAR(20),
  hha_series VARCHAR(50),
  tag VARCHAR(50),
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY floors(name,vfx,diy,buy,sell,color_1,color_2,miles_price,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,tag,catalog,filename,internal_id,entry_id)
FROM :path_to_floors
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS fossils;
CREATE TABLE fossils (
  name VARCHAR(100),
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  source VARCHAR(100),
  museum VARCHAR(20),
  version VARCHAR(20),
  interact BOOLEAN,
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY fossils(name,buy,sell,color_1,color_2, size_of,source,museum,version,interact,catalog,filename,internal_id,entry_id)
FROM :path_to_fossils
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS headwear;
CREATE TABLE headwear (
  name VARCHAR(100),
  variation VARCHAR(30),
  diy BOOLEAN,
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  seasonal_availability VARCHAR(30),
  mannequin_piece BOOLEAN,
  version VARCHAR(20),
  style VARCHAR(20),
  label_themes VARCHAR(100),
  type_of VARCHAR(30),
  villager_equippable BOOLEAN,
  catalog VARCHAR(30),
  filename VARCHAR(50),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY headwear(name,variation,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,type_of,villager_equippable,catalog,filename,internal_id,entry_id)
FROM :path_to_headwear
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS housewares;
CREATE TABLE housewares (
  name VARCHAR(100),
  variation VARCHAR(30),
  body_title VARCHAR(20),
  pattern VARCHAR(20),
  pattern_title VARCHAR(20),
  diy BOOLEAN,
  body_customize BOOLEAN,
  pattern_customize BOOLEAN,
  kit_cost VARCHAR(10),
  buy VARCHAR(50),
  sell INTEGER,
  color_1 VARCHAR(30),
  color_2 VARCHAR(30),
  size_of VARCHAR(10),
  miles_price VARCHAR(30),
  source VARCHAR(100),
  source_notes VARCHAR(100),
  version VARCHAR(20),
  hha_concept_1 VARCHAR(20),
  hha_concept_2 VARCHAR(20),
  hha_series VARCHAR(50),
  hha_set VARCHAR(20),
  interact VARCHAR(20),
  tag VARCHAR(30),
  outdoor BOOLEAN,
  speaker_type VARCHAR(40),
  lighting_type VARCHAR(20),
  catalog VARCHAR(30),
  filename VARCHAR(50),
  variant_id VARCHAR(20),
  internal_id INTEGER,
  entry_id VARCHAR(100),
  PRIMARY KEY (entry_id)
);

COPY housewares(name,variation,body_title,pattern,pattern_title,diy,body_customize,pattern_customize,kit_cost,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,hha_set,interact,tag,outdoor,speaker_type,lighting_type,catalog,filename,variant_id,internal_id,entry_id)
FROM :path_to_housewares
DELIMITER ','
CSV HEADER;

--DROP TABLE IF EXISTS insects;
--CREATE TABLE insects (
--  nb,
--  name VARCHAR(100),
--  sell INTEGER,
--  where_how VARCHAR(50),
--  weather VARCHAR(50),
--  total_catches_to_unlock INTEGER,
--  spawn_rates INTEGER,
--  nh_jan VARCHAR(50),
--  nh_feb VARCHAR(50),
--  nh_mar VARCHAR(50),
--  nh_apr VARCHAR(50),
--  nh_may VARCHAR(50),
--  nh_jun VARCHAR(50),
--  nh_jul VARCHAR(50),
--  nh_aug VARCHAR(50),
--  nh_sep VARCHAR(50),
--  nh_oct VARCHAR(50),
--  nh_nov VARCHAR(50),
--  nh_dec VARCHAR(50),
--  sh_jan VARCHAR(50),
--  sh_feb VARCHAR(50),
--  sh_mar VARCHAR(50),
--  sh_apr VARCHAR(50),
--  sh_may VARCHAR(50),
--  sh_jun VARCHAR(50),
--  sh_jul VARCHAR(50),
--  sh_aug VARCHAR(50),
--  sh_sep VARCHAR(50),
--  sh_oct VARCHAR(50),
--  sh_nov VARCHAR(50),
--  sh_dec VARCHAR(50),
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  icon_filename VARCHAR(50),
--  critterpedia_filename VARCHAR(50),
--  furniture_filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY insects(nb,name,sell,where_how,weather,total_catches_to_unlock,spawn_rates,nh_jan,nh_feb,nh_mar,nh_apr,nh_may,nh_jun,nh_jul,nh_aug,nh_sep,nh_oct,nh_nov,nh_dec,sh_jan,sh_feb,sh_mar,sh_apr,sh_may,sh_jun,sh_jul,sh_aug,sh_sep,sh_oct,sh_nov,sh_dec,color_1,color_2,icon_filename,critterpedia_filename,furniture_filename,internal_id,entry_id)
--FROM :path_to_insects
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS miscellaneous;
--CREATE TABLE miscellaneous (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  body_title VARCHAR(50),
--  pattern VARCHAR(50),
--  pattern_title VARCHAR(50),
--  diy BOOLEAN,
--  body_customize VARCHAR(50),
--  pattern_customize VARCHAR(50),
--  kit_cost VARCHAR(50),
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  hha_concept_1 VARCHAR(50),
--  hha_concept_2 VARCHAR(50),
--  hha_series VARCHAR(50),
--  hha_set VARCHAR(50),
--  interact BOOLEAN,
--  tag VARCHAR(50),
--  outdoor BOOLEAN,
--  speaker_type VARCHAR(50),
--  lighting_type VARCHAR(50),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  variant_id VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY miscellaneous(name,variation,body_title,pattern,pattern_title,diy,body_customize,pattern_customize,kit_cost,buy,sell,color_1,color_2, size_of,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,hha_set,interact,tag,outdoor,speaker_type,lighting_type,catalog,filename,variant_id,internal_id,entry_id)
--FROM :path_to_miscellaneous
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS music;
--CREATE TABLE music (
--  name VARCHAR(100),
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY music(name,buy,sell,color_1,color_2, size_of,source,source_notes,version,catalog,filename,internal_id,entry_id)
--FROM :path_to_csv
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS other;
--CREATE TABLE other (
--  name VARCHAR(100),
--  diy BOOLEAN,
--  stack_size INTEGER,
--  buy VARCHAR(50),
--  sell INTEGER,
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  tag VARCHAR(50),
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  version VARCHAR(20),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY other(name,diy,stack_size,buy,sell,miles_price,source,source_notes,tag,color_1,color_2,version,filename,internal_id,entry_id)
--FROM :path_to_csv
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS photos;
--CREATE TABLE photos (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  body_title VARCHAR(50),
--  pattern VARCHAR(50),
--  pattern_title VARCHAR(50),
--  diy BOOLEAN,
--  customize VARCHAR(50),
--  kit_cost INTEGER,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  source VARCHAR(100),
--  version VARCHAR(20),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  variant_id VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY photos(name,variation,body_title,pattern,pattern_title,diy,customize,kit_cost,buy,sell,color_1,color_2, size_of,source,version,catalog,filename,variant_id,internal_id,entry_id)
--FROM :path_to_photos
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS posters;
--CREATE TABLE posters (
--  name VARCHAR(100),
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY posters(name,buy,sell,color_1,color_2, size_of,source,source_notes,version,catalog,filename,internal_id,entry_id)
--FROM :path_to_posters
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS reactions;
--CREATE TABLE reactions (
--  name VARCHAR(100),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY reactions(name,source,source_notes,internal_id,entry_id)
--FROM :path_to_reactions
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS recipes;
--CREATE TABLE recipes (
--  name VARCHAR(50),
--  nb_1 INTEGER,
--  material_1 VARCHAR(50),
--  nb_2 INTEGER,
--  material_2 VARCHAR(50),
--  nb_3 INTEGER,
--  material_3 VARCHAR(50),
--  nb_4 INTEGER,
--  material_4 VARCHAR(50),
--  nb_5 INTEGER,
--  material_5 VARCHAR(50),
--  nb_6 INTEGER,
--  material_6 VARCHAR(50),
--  buy VARCHAR(50),
--  sell INTEGER,
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  recipes_to_unlock INTEGER,
--  version VARCHAR(20),
--  category VARCHAR(30),
--  serial_id INTEGER,
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--
--COPY recipes(name,nb_1,material_1,nb_2,material_2,nb_3,material_3,nb_4,material_4,nb_5,material_5,nb_6,material_6,buy,sell,miles_price,source,source_notes,recipes_to_unlock,version,category,serial_id,internal_id,entry_id)
--FROM :path_to_recipes
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS rugs;
--CREATE TABLE rugs (
--  name VARCHAR(100),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  hha_concept_1 VARCHAR(50),
--  hha_concept_2 VARCHAR(50),
--  hha_series VARCHAR(50),
--  tag VARCHAR(50),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY rugs(name,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,tag,catalog,filename,internal_id,entry_id)
--FROM :path_to_rugs
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS shoes;
--CREATE TABLE shoes (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  seasonal_availability VARCHAR(30),
--  mannequin_piece BOOLEAN,
--  version VARCHAR(20),
--  style VARCHAR(20),
--  label_themes VARCHAR(100),
--  villager_equippable BOOLEAN,
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY shoes(name,variation,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,villager_equippable,catalog,filename,internal_id,entry_id)
--FROM :path_to_shoes
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS socks;
--CREATE TABLE socks (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  seasonal_availability VARCHAR(30),
--  mannequin_piece BOOLEAN,
--  version VARCHAR(20),
--  style VARCHAR(20),
--  label_themes VARCHAR(100),
--  villager_equippable BOOLEAN,
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY socks(name,variation,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,villager_equippable,catalog,filename,internal_id,entry_id)
--FROM :path_to_socks
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS tools;
--CREATE TABLE tools (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  body_title VARCHAR(50),
--  diy BOOLEAN,
--  customize VARCHAR(50),
--  kit_cost INTEGER,
--  uses, VARCHAR(50)
--  stack_size INTEGER,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  set_of VARCHAR(50),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  filename VARCHAR(50),
--  variant_id VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY tools(name,variation,body_title,diy,customize,kit_cost,uses,stack_size,buy,sell,color_1,color_2, size_of,set_of,miles_price,source,source_notes,version,filename,variant_id,internal_id,entry_id)
--FROM :path_to_tools
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS tops;
--CREATE TABLE tops (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  seasonal_availability VARCHAR(30),
--  mannequin_piece BOOLEAN,
--  version VARCHAR(20),
--  style VARCHAR(20),
--  label_themes VARCHAR(100),
--  villager_equippable BOOLEAN,
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY tops(name,variation,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,seasonal_availability,mannequin_piece,version,style,label_themes,villager_equippable,catalog,filename,internal_id,entry_id)
--FROM :path_to_tops
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS umbrellas;
--CREATE TABLE umbrellas (
--  name VARCHAR(100),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  villager_equippable BOOLEAN,
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY umbrellas(name,diy,buy,sell,color_1,color_2, size_of,miles_price,source,source_notes,version,villager_equippable,catalog,filename,internal_id,entry_id)
--FROM :path_to_umbrellas
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS villagers;
--CREATE TABLE villagers (
--  name VARCHAR(100),
--  species VARCHAR(50),
--  gender VARCHAR(50),
--  personality VARCHAR(50),
--  hobby VARCHAR(50),
--  birthday VARCHAR(50),
--  catchphrase VARCHAR(50),
--  favorite_song VARCHAR(50),
--  style_1 VARCHAR(50),
--  style_2 VARCHAR(50),
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  wallpaper VARCHAR(50),
--  flooring VARCHAR(50),
--  furniture_list VARCHAR(50),
--  filename VARCHAR(50),
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY villagers(name,species,gender,personality,hobby,birthday,catchphrase,favorite_song,style_1,style_2,color_1,color_2,wallpaper,flooring,furniture_list,filename,entry_id)
--FROM :path_to_villagers
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS wall_mounted;
--CREATE TABLE wall_mounted (
--  name VARCHAR(100),
--  variation VARCHAR(30),
--  body_title VARCHAR(50),
--  pattern VARCHAR(50),
--  pattern_title VARCHAR(50),
--  diy BOOLEAN,
--  body_customize VARCHAR(50),
--  pattern_customize VARCHAR(50),
--  kit_cost INTEGER,
--  buy VARCHAR(50),
--  sell INTEGER,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  size_of VARCHAR(10),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  version VARCHAR(20),
--  hha_concept_1 VARCHAR(50),
--  hha_concept_2 VARCHAR(50),
--  hha_series VARCHAR(50),
--  hha_set VARCHAR(50),
--  interact BOOLEAN,
--  tag VARCHAR(50),
--  outdoor BOOLEAN,
--  lighting_type VARCHAR(50),
--  door_deco VARCHAR(50),
--  catalog VARCHAR(30),
--  filename VARCHAR(50),
--  variant_id VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY wall_mounted(name,variation,body_title,pattern,pattern_title,diy,body_customize,pattern_customize,kit_cost,buy,sell,color_1,color_2, size_of,source,source_notes,version,hha_concept_1,hha_concept_2,hha_series,hha_set,interact,tag,outdoor,lighting_type,door_deco,catalog,filename,variant_id,internal_id,entry_id)
--FROM :path_to_wall_mounted
--DELIMITER ','
--CSV HEADER;
--
--DROP TABLE IF EXISTS wallpaper;
--CREATE TABLE wallpaper (
--  name VARCHAR(100),
--  vfx BOOLEAN,
--  vfx_type VARCHAR(20),
--  diy BOOLEAN,
--  buy VARCHAR(50),
--  sell REAL,
--  color_1 VARCHAR(30),
--  color_2 VARCHAR(30),
--  miles_price VARCHAR(30),
--  source VARCHAR(100),
--  source_notes VARCHAR(100),
--  catalog VARCHAR(30),
--  window_type VARCHAR(50),
--  window_color VARCHAR(50),
--  pane_type VARCHAR(50),
--  curtain_type VARCHAR(50),
--  curtain_color VARCHAR(50),
--  ceiling_type VARCHAR(50),
--  hha_concept_1 VARCHAR(50),
--  hha_concept_2 VARCHAR(50),
--  hha_series VARCHAR(50),
--  tag VARCHAR(50),
--  version VARCHAR(20),
--  filename VARCHAR(50),
--  internal_id INTEGER,
--  entry_id VARCHAR(100),
--  PRIMARY KEY (entry_id)
--);
--
--COPY wallpaper(name,vfx,vfx_type,diy,buy,sell,color_1,color_2,miles_price,source,source_notes,catalog,window_type,window_color,pane_type,curtain_type,curtain_color,ceiling_type,hha_concept_1,hha_concept_2,hha_series,tag,version,filename,internal_id,entry_id)
--FROM :path_to_wallpaper
--DELIMITER ','
--CSV HEADER;
