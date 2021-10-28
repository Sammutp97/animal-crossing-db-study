-- accessories
SELECT name, variation, sell, miles_price, seasonal_availability, villager_equippable, color_1, color_2 FROM accessories WHERE diy=true;

-- art
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
SELECT name, category, buy, sell, catalog, artist, museum_description FROM art WHERE size_of='1x1' AND hha_concept_1='expensive' AND hha_concept_2='folk art' AND tag='Sculpture';
SELECT hha_concept_1 FROM art GROUP BY hha_concept_1;

-- bags
SELECT name, variation, sell, miles_price, seasonal_availability, villager_equippable, color_1, color_2 FROM bags WHERE diy=false;

-- bottoms
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2 FROM bottoms WHERE diy=false AND source='Recycle bin' AND label_themes='goth';

-- construction
SELECT name, source FROM construction WHERE category='Bridge' AND buy<100000;

-- dress-up
SELECT name, variation, sell, seasonal_availability, villager_equippable, primary_shape, secondary_shape, color_1, color_2, label_themes FROM dress_up WHERE diy=false AND source='Recycle bin';

-- fencing: all diy and stack size of 50
SELECT name, sell, source_notes FROM fencing;

-- fish
SELECT name, sell, color_1, color_2, shadow, total_catches_to_unlock, spawn_rates, rain_snow_catch_up FROM fish WHERE where_how='Sea' AND lighting_type='Fluorescent' ORDER BY total_catches_to_unlock, name;

-- floors
SELECT name, buy, sell, catalog, vfx, color_1, color_2, tag, source FROM floors WHERE hha_concept_1='expensive' AND hha_concept_2='facility';

-- fossils
SELECT name, sell, color_1, color_2, size_of FROM fossils WHERE museum='Room 2';

-- headwear
SELECT name, variation, buy, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes, style, type_of FROM headwear WHERE diy=false AND source='Gulliver';

-- housewares
SELECT name, buy, sell, catalog, color_1, color_2, source, outdoor FROM housewares WHERE hha_concept_1='expensive' AND tag='Toy';


-- list all outfits with same colors
-- crafts

-- insects
SELECT name, sell, color_1, color_2, total_catches_to_unlock, spawn_rates FROM insects WHERE where_how='On palm trees' AND weather='Any weather' ORDER BY total_catches_to_unlock, name;

-- miscellaneous
SELECT name, buy, sell, catalog, color_1, color_2, source, outdoor, hha_concept_1, hha_concept_2, speaker_type, lighting_type, tag FROM miscellaneous;

-- music
SELECT name, buy, sell, catalog, color_1, color_2, source, source_notes, size_of FROM music;

-- other
SELECT name, sell, miles_price, source, source_notes, tag, color_1, color_2 FROM other WHERE stack_size<30;

-- photos
SELECT name, buy, sell, catalog, color_1, color_2, body_title FROM photos WHERE size_of='1x1' AND source<>'High Friendship';

-- posters
SELECT name, buy, sell, catalog, source, source_notes FROM posters WHERE size_of='1x1' AND color_1='Blue' AND color_2='Gray';

-- reactions
SELECT name, source_notes FROM reactions WHERE source='Big Sister';

-- recipes
SELECT name, category, sell, source, recipes_to_unlock FROM recipes;

-- rugs
SELECT name, diy, buy, sell, catalog, source, source_notes, color_1, color_2 FROM rugs WHERE size_of='3x3' AND hha_concept_1='living room' AND tag='Pattern Rugs';

-- shoes
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM shoes WHERE diy=false AND source='Kicks';

-- socks
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM socks WHERE diy=false AND source='Kicks';

-- tools
SELECT name, variation, buy, sell, color_1, color_2, source, set_of, stack_size FROM tools WHERE diy=true AND uses='Unlimited';

-- tops
SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes FROM tops WHERE diy=false AND source='Recycle bin';

-- umbrellas
SELECT name, buy, sell, color_1, color_2 FROM umbrellas WHERE diy=false AND source='Bug-Off' AND size_of='1x1';

-- villagers
SELECT name, personality, hobby, birthday, catchphrase, favorite_song, style_1, style_2, color_1, color_2, wallpaper, furniture_list FROM villagers WHERE species='Bird' AND gender='Male' AND flooring='tatami';

-- wall-mounted
SELECT name, buy, sell, catalog, pattern, diy, source, source_notes, outdoor FROM wall_mounted WHERE size_of='1x1' AND color_1='Beige' AND color_2='Yellow';

-- wallpaper
SELECT name, buy, sell, vfx, color_1, color_2, catalog, source, window_type, window_color, pane_type, curtain_type, curtain_color, ceiling_type FROM wallpaper WHERE hha_concept_1='zen-style' AND tag='Nature Walls' AND diy=false;
