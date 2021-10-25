catalog:               if we can buy items.
diy:                   if items can be crafted.
source:                where to buy an item.
seasonal_availability: when to buy an item.
variation:             when items are duplicate.


fishs and insects:
  NH / SH:                when to catch
  wheather / where / how: conditions to catch

+-----------------------------------------------------------+
|                                                accessories|
|int: buy, sell, miles_price                                |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of,                 |
|     source, source_notes, seasonal_availability,          |
|     version, style, label_themes, type_of,                |
|     catalog, filename                                     |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                achievement|
|int: nb, award_criteria, num_of_tiers, tier_1-5,           |
|     reward_tier_1-6                                       |
|bool: sequential                                           |
|str: internal_name, internal_category, version             |
+-----------------------------------------------------------+
tiers -> rewards; no link.

+-----------------------------------------------------------+
|                                                        art|
|int: buy in, sell                                          |
|bool: genuine, interact                                    |
|str: category, color_1, color_2, size_of,                  |
|     real_artwork_title, artist, museum_description,       |
|     source, source_notes, version, hha_concept_1,         |
|     hha_concept_2, hha_series, hha_set, tag,              |
|     speaker_type, lighting_type, catalog, filename        |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                       bags|
|int: buy in, sell, miles_price                             |
|bool: diy, villager_equippable                             |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version,         |
|     style, label_themes, catalog, filename                |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    bottoms|
|int: buy, sell                                             |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version,         |
|     style, label_themes, catalog, filename                |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                               construction|
|int: buy                                                   |
|str: category, source, filename, version                   |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                   dress_up|
|int: buy, sell                                             |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version,         |
|     style, label_themes, catalog, primary_shape,          |
|     secondary_shape, filename                             |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    fencing|
|int: stack_size, buy, sell                                 |
|bool: diy                                                  |
|str: source, source_notes, version, filename               |
+-----------------------------------------------------------+
can only be crafted.

+-----------------------------------------------------------+
|                                                       fish|
|int: nb, sell, total_catches_to_unlock                     |
|bool: rain_snow_catch_up                                   |
|str: where_how, shadow, spawn_rates, nhs, shs,             |
|     color_1, color_2, size_of, lighting_type,             |
|     icon_filename, critterpedia_filename,                 |
|     furniture_filename                                    |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                     floors|
|int: buy, sell, miles_price                                |
|bool: vfx, diy                                             |
|str: color_1, color_2, source, source_notes, version,      |
|     hha_concept_1, hha_concept_2, hha_series, tag,        |
|     catalog, filename                                     |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    fossils|
|int: buy, sell                                             |
|bool: interact                                             |
|str: color_1, color_2, size_of, source, museum,            |
|     version, catalog, filename                            |
+-----------------------------------------------------------+
none for sale.
all must be assessed.
some can interact.

+-----------------------------------------------------------+
|                                                   headwear|
|int: buy, sell, miles_price                                |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version,         |
|     style, label_themes, type_of, catalog, filename       |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                 housewares|
|int: buy, sell, miles_price, kit_cost                      |
|bool: diy, body_customize, pattern_customize, outdoor      |
|str: variation, body_title, pattern, pattern_title,        |
|     color_1, color_2, size_of, source, source_notes,      |
|     version, hha_concept_1, hha_concept_2, hha_series,    |
|     hha_set, interact, tag, speaker_type, lighting_type,  |
|     catalog, filename, variant_id                         |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    insects|
|int: nb, sell, total_catches_to_unlock                     |
|str: where_how, weather, spawn_rates, nhs, shs, color_1,   |
|     color_2, icon_filename, critterpedia_filename,        |
|     furniture_filename                                    |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                              miscellaneous|
|int: kit_cost, buy, sell                                   |
|bool: diy, outdoor                                         |
|str: variation, body_title, pattern, pattern_title,        |
|     body_customize, pattern_customize, color_1, color_2,  |
|     size_of, source, source_notes, version, hha_concept_1,|
|     hha_concept_2, hha_series, hha_set, interact, tag,    |
|     speaker_type, lighting_type, catalog, filename,       |
|     variant_id                                            |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                      music|
|int: buy, sell                                             |
|str: color_1, color_2, size_of, source, source_notes,      |
|     version, catalog, filename                            |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                      other|
|int: stack_size, buy, sell, miles_price                    |
|bool: diy                                                  |
|str: source, source_notes, tag, color_1, color_2,          |
|     version, filename                                     |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                     photos|
|int: kit_cost, buy, sell                                   |
|bool: diy                                                  |
|str: variation, body_title, pattern, pattern_title,        |
|     customize, color_1, color_2, size_of, source,         |
|     version, catalog, filename, variant_id                |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    posters|
|int: buy, sell                                             |
|str: color_1, color_2, size_of, source, source_notes,      |
|     version, catalog, filename                            |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                  reactions|
|str: source, source_notes                                  |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                    recipes|
|int: nb_1-6, buy, sell, miles_price, recipes_to_unlock,    |
|     serial_id                                             |
|str: material_1-6, source, source_notes, version, category |
+-----------------------------------------------------------+
no information about where the material is...

+-----------------------------------------------------------+
|                                                       rugs|
|int: buy, sell, miles_price                                |
|bool: diy                                                  |
|str: color_1, color_2, size_of, source, source_notes,      |
|     version, hha_concept_1, hha_concept_2, hha_series,    |
|     tag, catalog, filename                                |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                      shoes|
|int: buy, sell, miles_price                                |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version, style,  |
|     label_themes, catalog, filename                       |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                      socks|
|int: buy, sell, miles_price                                |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version, style,  |
|     label_themes, catalog, filename                       |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                      tools|
|int: kit_cost, stack_size, buy, sell, miles_price          |
|bool: diy                                                  |
|str: variation, body_title, customize, uses, color_1,      |
|     color_2, size_of, set_of, source, source_notes,       |
|     version, filename, variant_id                         |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                       tops|
|int: buy, sell, miles_price                                |
|bool: diy, mannequin_piece, villager_equippable            |
|str: variation, color_1, color_2, size_of, source,         |
|     source_notes, seasonal_availability, version,         |
|     style, label_themes, catalog, filename                |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                  umbrellas|
|int: buy, sell, miles_price                                |
|bool: diy, villager_equippable                             |
|str: color_1, color_2, size_of, source, source_notes,      |
|     version, catalog, filename                            |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                  villagers|
|str: species, gender, personality, hobby, birthday,        |
|     catchphrase, favorite_song, style_1, style_2,         |
|     color_1, color_2, wallpaper, flooring,                |
|     furniture_list, filename                              |
+-----------------------------------------------------------+
furniture_list: list of internal ids?

+-----------------------------------------------------------+
|                                                all_mounted|
|int: kit_cost, buy, sell                                   |
|bool: diy, interact, outdoor                               |
|str: variation, body_title, pattern, pattern_title,        |
|     body_customize, pattern_customize, color_1, color_2,  |
|     size_of, source, source_notes, version,               |
|     hha_concept_1, hha_concept_2, hha_series, hha_set,    |
|     tag, lighting_type, door_deco, catalog, filename,     |
|     variant_id                                            |
+-----------------------------------------------------------+

+-----------------------------------------------------------+
|                                                  wallpaper|
|int: buy, sell, miles_price                                |
|bool: vfx, diy                                             |
|str: vfx_type, color_1, color_2, source, source_notes,     |
|     catalog, window_type, window_color, pane_type,        |
|     curtain_type, curtain_color, ceiling_type,            |
|     hha_concept_1, hha_concept_2, hha_series, tag,        |
|     version, filename                                     |
+-----------------------------------------------------------+
