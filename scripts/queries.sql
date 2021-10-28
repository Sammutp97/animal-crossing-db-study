-- accessories
  -- generalities
  -- what are the attributes of all craftable accessories?
SELECT name, variation, sell, miles_price, seasonal_availability, villager_equippable, color_1, color_2
FROM accessories
WHERE diy=true;
  -- what is the average price of the accessories?
SELECT AVG(sell)
FROM accessories;
  -- what is the average loss of selling an accessory?
SELECT AVG(sell-CASE WHEN buy=-1 THEN 0 ELSE buy END)
FROM accessories;
  -- what buyable accessory can be sold for the highest profit?
  -- can be extended to all buyable items, i.e. almost all tables,
  -- except reactions, villagers, recipes, ...
SELECT name, variation, source, sell-buy AS profit
FROM accessories
WHERE buy<>-1
AND sell-buy=(
	SELECT MAX(sell-buy)
	FROM accessories
	WHERE buy<>-1
);
  -- what are the names and recipes of all craftable accessories?
  -- can be extended to all craftable item categories, i.e.
  -- accessories, bags, bottoms, dress_up, fencing, floors, headwear,
  -- housewares, miscellaneous, other, photos, rugs, shoes, socks,
  -- tools, tops, umbrellas, wall_mounted, wallpaper

SELECT name, nb_1, material_1, nb_2, material_2, nb_3, material_3, nb_4, material_4, nb_5, material_5, nb_6, material_6
FROM recipes
WHERE name IN (
	SELECT name
	FROM accessories
	WHERE diy=true
);

  -- What are all possible variations for the accessories, sorted in
  -- alphabetical order?
  -- can be extend to any column of any relation, to gain access to
  -- what is in the given column of the given relation.
SELECT DISTINCT variation FROM accessories GROUP BY variation ORDER BY variation;
SELECT variation FROM accessories GROUP BY variation ORDER BY variation;
SELECT DISTINCT variation FROM accessories ORDER BY variation;

-- art
  -- generalities
SELECT nb,
       name,
       award_criteria,
       num_of_tiers,
       CASE WHEN num_of_tiers=1 THEN tier_1
            WHEN num_of_tiers=2 THEN tier_2
            WHEN num_of_tiers=3 THEN tier_3
            WHEN num_of_tiers=4 THEN tier_4
            WHEN num_of_tiers=5 THEN tier_5
       ELSE NULL END AS condition,
       CASE WHEN num_of_tiers=1 THEN reward_tier_1
            WHEN num_of_tiers=2 THEN reward_tier_1+reward_tier_2
            WHEN num_of_tiers=3 THEN reward_tier_1+reward_tier_2+reward_tier_3
            WHEN num_of_tiers=4 THEN reward_tier_1+reward_tier_2+reward_tier_3+reward_tier_4
            WHEN num_of_tiers=5 THEN reward_tier_1+reward_tier_2+reward_tier_3+reward_tier_4+reward_tier_5
            WHEN num_of_tiers=6 THEN reward_tier_1+reward_tier_2+reward_tier_3+reward_tier_4+reward_tier_5+reward_tier_6
       ELSE NULL END AS cumulative_reward
FROM achievements;

-- art
  -- generalities
SELECT name, category, buy, sell, catalog, artist, museum_description
FROM art
WHERE size_of='1x1'
AND hha_concept_1='expensive'
AND hha_concept_2='folk art'
AND tag='Sculpture';
SELECT hha_concept_1 FROM art GROUP BY hha_concept_1;

  -- what are the recipes of all the craftable items in AC?
SELECT name, nb_1, material_1, nb_2, material_2, nb_3, material_3, nb_4, material_4, nb_5, material_5, nb_6, material_6
FROM recipes
WHERE name IN (
	SELECT name
	FROM (
		(SELECT name, diy FROM accessories   AS a) UNION ALL
		(SELECT name, diy FROM bags          AS b) UNION ALL
		(SELECT name, diy FROM bottoms       AS b) UNION ALL
		(SELECT name, diy FROM dress_up      AS d) UNION ALL
		(SELECT name, diy FROM fencing       AS f) UNION ALL
		(SELECT name, diy FROM floors        AS f) UNION ALL
		(SELECT name, diy FROM headwear      AS h) UNION ALL
		(SELECT name, diy FROM housewares    AS h) UNION ALL
		(SELECT name, diy FROM miscellaneous AS m) UNION ALL
		(SELECT name, diy FROM other         AS o) UNION ALL
		(SELECT name, diy FROM photos        AS p) UNION ALL
		(SELECT name, diy FROM rugs          AS r) UNION ALL
		(SELECT name, diy FROM shoes         AS s) UNION ALL
		(SELECT name, diy FROM socks         AS s) UNION ALL
		(SELECT name, diy FROM tools         AS t) UNION ALL
		(SELECT name, diy FROM tops          AS t) UNION ALL
		(SELECT name, diy FROM umbrellas     AS u) UNION ALL
		(SELECT name, diy FROM wall_mounted  AS w) UNION ALL
		(SELECT name, diy FROM wallpaper     AS w)
	) AS u
	WHERE diy=true)
;

-- bags
  -- generalities
SELECT name, variation, sell, miles_price, seasonal_availability, villager_equippable, color_1, color_2 FROM bags WHERE diy=false;

-- bottoms
  -- generalities
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2 FROM bottoms WHERE diy=false AND source='Recycle bin' AND label_themes='goth';

-- construction
  -- generalities
SELECT name, source FROM construction WHERE category='Bridge' AND buy<100000;

-- dress-up
  -- generalities
SELECT name, variation, sell, seasonal_availability, villager_equippable, primary_shape, secondary_shape, color_1, color_2, label_themes FROM dress_up WHERE diy=false AND source='Recycle bin';

-- fencing: all diy and stack size of 50
  -- generalities
SELECT name, sell, source_notes FROM fencing;

-- fish
  -- generalities
SELECT name, sell, color_1, color_2, shadow, total_catches_to_unlock, spawn_rates, rain_snow_catch_up FROM fish WHERE where_how='Sea' AND lighting_type='Fluorescent' ORDER BY total_catches_to_unlock, name;

-- floors
  -- generalities
SELECT name, buy, sell, catalog, vfx, color_1, color_2, tag, source FROM floors WHERE hha_concept_1='expensive' AND hha_concept_2='facility';

-- fossils
  -- generalities
SELECT name, sell, color_1, color_2, size_of FROM fossils WHERE museum='Room 2';

-- headwear
  -- generalities
SELECT name, variation, buy, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes, style, type_of FROM headwear WHERE diy=false AND source='Gulliver';

-- housewares
  -- generalities
SELECT name, buy, sell, catalog, color_1, color_2, source, outdoor FROM housewares WHERE hha_concept_1='expensive' AND tag='Toy';


-- list all outfits with same colors
SELECT
	bo.name, bo.color_1, bo.color_2,
	t.name, t.color_1, t.color_2
FROM
 bottoms       AS bo,
 tops          AS t
WHERE (bo.color_1='Black' OR bo.color_2='Black')
AND (t.color_1='Black' OR t.color_2='Black');

-- SELECT
-- 	bo.name, bo.color_1, bo.color_2,
-- 	sh.name, sh.color_1, sh.color_2,
-- 	t.name, t.color_1, t.color_2
-- FROM
--  bottoms       AS bo,
--  shoes         AS sh,
--  tops          AS t
-- WHERE (bo.color_1='Black' OR bo.color_2='Black')
-- AND (sh.color_1='Black' OR sh.color_2='Black')
-- AND (t.color_1='Black' OR t.color_2='Black');


-- SELECT
-- 	a.name, a.color_1, a.color_2,
-- 	ba.name, ba.color_1, ba.color_2,
-- 	bo.name, bo.color_1, bo.color_2,
-- 	d.name, d.color_1, d.color_2,
-- 	h.name, h.color_1, h.color_2,
-- 	m.name, m.color_1, m.color_2,
-- 	o.name, o.color_1, o.color_2,
-- 	r.name, r.color_1, r.color_2,
-- 	sh.name, sh.color_1, sh.color_2,
-- 	so.name, so.color_1, so.color_2,
-- 	t.name, t.color_1, t.color_2,
-- 	u.name, u.color_1, u.color_2
-- FROM
--  accessories   AS a,
--  bags          AS ba,
--  bottoms       AS bo,
--  dress_up      AS d,
--  headwear      AS h,
--  miscellaneous AS m,
--  other         AS o,
--  rugs          AS r,
--  shoes         AS sh,
--  socks         AS so,
--  tops          AS t,
--  umbrellas     AS u
-- WHERE (a.color_1='Black' OR a.color_2='Black')
-- AND (ba.color_1='Black' OR ba.color_2='Black')
-- WHERE (bo.color_1='Black' OR bo.color_2='Black')
-- AND (d.color_1='Black' OR d.color_2='Black')
-- AND (h.color_1='Black' OR h.color_2='Black')
-- AND (m.color_1='Black' OR m.color_2='Black')
-- AND (o.color_1='Black' OR o.color_2='Black')
-- AND (r.color_1='Black' OR r.color_2='Black')
-- AND (sh.color_1='Black' OR sh.color_2='Black')
-- AND (so.color_1='Black' OR so.color_2='Black')
-- AND (t.color_1='Black' OR t.color_2='Black')
-- AND (u.color_1='Black' OR u.color_2='Black');

-- insects
  -- generalities
SELECT name, sell, color_1, color_2, total_catches_to_unlock, spawn_rates FROM insects WHERE where_how='On palm trees' AND weather='Any weather' ORDER BY total_catches_to_unlock, name;

-- miscellaneous
  -- generalities
SELECT name, buy, sell, catalog, color_1, color_2, source, outdoor, hha_concept_1, hha_concept_2, speaker_type, lighting_type, tag FROM miscellaneous;

-- music
  -- generalities
SELECT name, buy, sell, catalog, color_1, color_2, source, source_notes, size_of FROM music;

-- other
  -- generalities
SELECT name, sell, miles_price, source, source_notes, tag, color_1, color_2 FROM other WHERE stack_size<30;

-- photos
  -- generalities
SELECT name, buy, sell, catalog, color_1, color_2, body_title FROM photos WHERE size_of='1x1' AND source<>'High Friendship';

-- posters
  -- generalities
SELECT name, buy, sell, catalog, source, source_notes FROM posters WHERE size_of='1x1' AND color_1='Blue' AND color_2='Gray';

-- reactions
  -- generalities
SELECT name, source_notes FROM reactions WHERE source='Big Sister';

-- recipes
  -- generalities
SELECT name, category, sell, source, recipes_to_unlock FROM recipes;

-- rugs
  -- generalities
SELECT name, diy, buy, sell, catalog, source, source_notes, color_1, color_2 FROM rugs WHERE size_of='3x3' AND hha_concept_1='living room' AND tag='Pattern Rugs';

-- shoes
  -- generalities
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM shoes WHERE diy=false AND source='Kicks';

-- socks
  -- generalities
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM socks WHERE diy=false AND source='Kicks';

-- tools
  -- generalities
SELECT name, variation, buy, sell, color_1, color_2, source, set_of, stack_size FROM tools WHERE diy=true AND uses='Unlimited';

-- tops
  -- generalities
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM tops WHERE diy=false AND source='Recycle bin';

-- umbrellas
  -- generalities
SELECT name, buy, sell, color_1, color_2 FROM umbrellas WHERE diy=false AND source='Bug-Off' AND size_of='1x1';

-- villagers
  -- generalities
SELECT name, personality, hobby, birthday, catchphrase, favorite_song, style_1, style_2, color_1, color_2, wallpaper, furniture_list FROM villagers WHERE species='Bird' AND gender='Male' AND flooring='tatami';
  -- what are the sources and prices of all the favorite songs of the villagers, sorted by song name and then villager name?
SELECT v.name, v.favorite_song, m.source, m.buy FROM villagers AS v, music AS m WHERE v.favorite_song=m.name ORDER BY (m.name, v.name);
  -- tell the wallpapers and floors for all villagers, their names and prices and whether they are crafted or not and the total price.
SELECT DISTINCT v.name,
	v.flooring, CASE WHEN f.buy<>-1 THEN f.buy ELSE 0 END AS f_buy, f.diy,
	v.wallpaper, CASE WHEN w.buy<>-1 THEN w.buy ELSE 0 END AS w_buy, w.diy,
	CASE WHEN f.buy<>-1 AND w.buy<>-1 THEN f.buy+w.buy WHEN f.buy<>-1 THEN f.buy WHEN w.buy<>-1 THEN w.buy ELSE 0 END AS total
FROM villagers AS v, floors AS f, wallpaper AS w
WHERE v.flooring=f.name AND v.wallpaper=w.name
--FROM (villagers v JOIN floors f ON v.flooring=f.name) JOIN wallpaper w ON v.wallpaper=w.name
ORDER BY f.diy, w.diy;


-- wall-mounted
  -- generalities
SELECT name, buy, sell, catalog, pattern, diy, source, source_notes, outdoor FROM wall_mounted WHERE size_of='1x1' AND color_1='Beige' AND color_2='Yellow';

-- wallpaper
  -- generalities
SELECT name, buy, sell, vfx, color_1, color_2, catalog, source, window_type, window_color, pane_type, curtain_type, curtain_color, ceiling_type FROM wallpaper WHERE hha_concept_1='zen-style' AND tag='Nature Walls' AND diy=false;




-- drop lines (https://sql.sh/cours/delete)
--DELETE FROM `table`
--WHERE condition;
--
-- insert lines (https://sql.sh/cours/insert-into)
--INSERT INTO table VALUES ('valeur 1', 'valeur 2', ...);
--INSERT INTO table (nom_colonne_1, nom_colonne_2, ...
--	 VALUES ('valeur 1', 'valeur 2', ...);
--INSERT INTO client (prenom, nom, ville, age)
--	 VALUES
--	 ('Rébecca', 'Armand', 'Saint-Didier-des-Bois', 24),
--	 ('Aimée', 'Hebert', 'Marigny-le-Châtel', 36),
--	 ('Marielle', 'Ribeiro', 'Maillères', 27),
--	 ('Hilaire', 'Savary', 'Conie-Molitard', 58);
--
-- update table (https://sql.sh/cours/update)
--UPDATE table
--SET colonne_1 = 'valeur 1', colonne_2 = 'valeur 2', colonne_3 = 'valeur 3'
--WHERE condition
--
-- add column (https://sql.sh/cours/alter-table)
--ALTER TABLE nom_table
--ADD nom_colonne type_donnees
--
-- delete column (https://sql.sh/cours/alter-table)
--ALTER TABLE nom_table
--DROP COLUMN nom_colonne
--
-- modify column (https://sql.sh/cours/alter-table)
--ALTER TABLE nom_table
--ALTER COLUMN nom_colonne TYPE type_donnees
--
-- rename column (https://sql.sh/cours/alter-table)
--ALTER TABLE nom_table
--RENAME COLUMN colonne_ancien_nom TO colonne_nouveau_nom
