# EXIOBASE 3 — full sector lists (products & industries)

Every sector EXIOBASE references, in both symmetric forms. EXIOBASE ships two builds (see [ADR 0005](../decisions/0005-exiobase-pxp-2022.md)):

- **pxp** — 200 **products** (product-by-product)
- **ixi** — 163 **industries** (industry-by-industry)

They run largely in parallel (e.g. the product *Paddy rice* ↔ the industry *Cultivation of paddy rice*); pxp splits some industries' output into several products, hence 200 vs 163. Each row carries an EXIOBASE code and a high-level consumption category; industries also map to an **ISIC** class.

**Source:** EXIOBASE 3 classification metadata, read via `pymrio.get_classification('exio3_pxp')` and `('exio3_ixi')` (pymrio 0.6.3). EXIOBASE concept DOI [10.5281/zenodo.3583070](https://doi.org/10.5281/zenodo.3583070); pymrio docs <https://pymrio.readthedocs.io/>. This page is generated from that classification.


## Products — pxp (200)

| # | Product | Exio code | Consumption category |
| ---: | --- | --- | --- |
| 1 | Paddy rice | p01.a | Food |
| 2 | Wheat | p01.b | Food |
| 3 | Cereal grains nec | p01.c | Food |
| 4 | Vegetables, fruit, nuts | p01.d | Food |
| 5 | Oil seeds | p01.e | Food |
| 6 | Sugar cane, sugar beet | p01.f | Food |
| 7 | Plant-based fibers | p01.g | Food |
| 8 | Crops nec | p01.h | Food |
| 9 | Cattle | p01.i | Food |
| 10 | Pigs | p01.j | Food |
| 11 | Poultry | p01.k | Food |
| 12 | Meat animals nec | p01.l | Food |
| 13 | Animal products nec | p01.m | Food |
| 14 | Raw milk | p01.n | Food |
| 15 | Wool, silk-worm cocoons | p01.o | Clothing |
| 16 | Manure (conventional treatment) | p01.w.1 | Food |
| 17 | Manure (biogas treatment) | p01.w.2 | Food |
| 18 | Products of forestry, logging and related services (02) | p02 | Shelter |
| 19 | Fish and other fishing products; services incidental of fishing (05) | p05 | Food |
| 20 | Anthracite | p10.a | Shelter |
| 21 | Coking Coal | p10.b | Shelter |
| 22 | Other Bituminous Coal | p10.c | Shelter |
| 23 | Sub-Bituminous Coal | p10.d | Shelter |
| 24 | Patent Fuel | p10.e | Shelter |
| 25 | Lignite/Brown Coal | p10.f | Shelter |
| 26 | BKB/Peat Briquettes | p10.g | Shelter |
| 27 | Peat | p10.h | Shelter |
| 28 | Crude petroleum and services related to crude oil extraction, excluding surveying | p11.a | Shelter |
| 29 | Natural gas and services related to natural gas extraction, excluding surveying | p11.b | Shelter |
| 30 | Natural Gas Liquids | p11.b.1 | Shelter |
| 31 | Other Hydrocarbons | p11.c | Shelter |
| 32 | Uranium and thorium ores (12) | p12 | Shelter |
| 33 | Iron ores | p13.1 | Construction |
| 34 | Copper ores and concentrates | p13.20.11 | Construction |
| 35 | Nickel ores and concentrates | p13.20.12 | Construction |
| 36 | Aluminium ores and concentrates | p13.20.13 | Construction |
| 37 | Precious metal ores and concentrates | p13.20.14 | Construction |
| 38 | Lead, zinc and tin ores and concentrates | p13.20.15 | Construction |
| 39 | Other non-ferrous metal ores and concentrates | p13.20.16 | Construction |
| 40 | Stone | p14.1 | Construction |
| 41 | Sand and clay | p14.2 | Construction |
| 42 | Chemical and fertilizer minerals, salt and other mining and quarrying products n.e.c. | p14.3 | Food |
| 43 | Products of meat cattle | p15.a | Food |
| 44 | Products of meat pigs | p15.b | Food |
| 45 | Products of meat poultry | p15.c | Food |
| 46 | Meat products nec | p15.d | Food |
| 47 | products of Vegetable oils and fats | p15.e | Food |
| 48 | Dairy products | p15.f | Food |
| 49 | Processed rice | p15.g | Food |
| 50 | Sugar | p15.h | Food |
| 51 | Food products nec | p15.i | Food |
| 52 | Beverages | p15.j | Food |
| 53 | Fish products | p15.k | Food |
| 54 | Tobacco products (16) | p16 | Food |
| 55 | Textiles (17) | p17 | Clothing |
| 56 | Wearing apparel; furs (18) | p18 | Clothing |
| 57 | Leather and leather products (19) | p19 | Clothing |
| 58 | Wood and products of wood and cork (except furniture); articles of straw and plaiting materials (20) | p20 | Shelter |
| 59 | Wood material for treatment, Re-processing of secondary wood material into new wood material | p20.w | Shelter |
| 60 | Pulp | p21.1 | Manufactured_products |
| 61 | Secondary paper for treatment, Re-processing of secondary paper into new pulp | p21.w.1 | Manufactured_products |
| 62 | Paper and paper products | p21.2 | Manufactured_products |
| 63 | Printed matter and recorded media (22) | p22 | Manufactured_products |
| 64 | Coke Oven Coke | p23.1.a | Shelter |
| 65 | Gas Coke | p23.1.b | Shelter |
| 66 | Coal Tar | p23.1.c | Shelter |
| 67 | Motor Gasoline | p23.20.a | Mobility |
| 68 | Aviation Gasoline | p23.20.b | Mobility |
| 69 | Gasoline Type Jet Fuel | p23.20.c | Mobility |
| 70 | Kerosene Type Jet Fuel | p23.20.d | Mobility |
| 71 | Kerosene | p23.20.e | Mobility |
| 72 | Gas/Diesel Oil | p23.20.f | Mobility |
| 73 | Heavy Fuel Oil | p23.20.g | Mobility |
| 74 | Refinery Gas | p23.20.h | Shelter |
| 75 | Liquefied Petroleum Gases (LPG) | p23.20.i | Shelter |
| 76 | Refinery Feedstocks | p23.20.j | Shelter |
| 77 | Ethane | p23.20.k | Shelter |
| 78 | Naphtha | p23.20.l | Shelter |
| 79 | White Spirit & SBP | p23.20.m | Shelter |
| 80 | Lubricants | p23.20.n | Shelter |
| 81 | Bitumen | p23.20.o | Shelter |
| 82 | Paraffin Waxes | p23.20.p | Shelter |
| 83 | Petroleum Coke | p23.20.q | Shelter |
| 84 | Non-specified Petroleum Products | p23.20.r | Shelter |
| 85 | Nuclear fuel | p23.3 | Shelter |
| 86 | Plastics, basic | p24.a | Manufactured_products |
| 87 | Secondary plastic for treatment, Re-processing of secondary plastic into new plastic | p24.a.w | Manufactured_products |
| 88 | N-fertiliser | p24.b | Food |
| 89 | P- and other fertiliser | p24.c | Food |
| 90 | Chemicals nec | p24.d | Manufactured_products |
| 91 | Charcoal | p24.e | Shelter |
| 92 | Additives/Blending Components | p24.f | Mobility |
| 93 | Biogasoline | p24.g | Mobility |
| 94 | Biodiesels | p24.h | Mobility |
| 95 | Other Liquid Biofuels | p24.i | Mobility |
| 96 | Rubber and plastic products (25) | p25 | Manufactured_products |
| 97 | Glass and glass products | p26.a | Construction |
| 98 | Secondary glass for treatment, Re-processing of secondary glass into new glass | p26.a.w | Construction |
| 99 | Ceramic goods | p26.b | Construction |
| 100 | Bricks, tiles and construction products, in baked clay | p26.c | Construction |
| 101 | Cement, lime and plaster | p26.d | Construction |
| 102 | Ash for treatment, Re-processing of ash into clinker | p26.d.w | Construction |
| 103 | Other non-metallic mineral products | p26.e | Construction |
| 104 | Basic iron and steel and of ferro-alloys and first products thereof | p27.a | Manufactured_products |
| 105 | Secondary steel for treatment, Re-processing of secondary steel into new steel | p27.a.w | Manufactured_products |
| 106 | Precious metals | p27.41 | Manufactured_products |
| 107 | Secondary preciuos metals for treatment, Re-processing of secondary preciuos metals into new preciuos metals | p27.41.w | Manufactured_products |
| 108 | Aluminium and aluminium products | p27.42 | Manufactured_products |
| 109 | Secondary aluminium for treatment, Re-processing of secondary aluminium into new aluminium | p27.42.w | Manufactured_products |
| 110 | Lead, zinc and tin and products thereof | p27.43 | Manufactured_products |
| 111 | Secondary lead for treatment, Re-processing of secondary lead into new lead | p27.43.w | Manufactured_products |
| 112 | Copper products | p27.44 | Manufactured_products |
| 113 | Secondary copper for treatment, Re-processing of secondary copper into new copper | p27.44.w | Manufactured_products |
| 114 | Other non-ferrous metal products | p27.45 | Manufactured_products |
| 115 | Secondary other non-ferrous metals for treatment, Re-processing of secondary other non-ferrous metals into new other non-ferrous metals | p27.45.w | Manufactured_products |
| 116 | Foundry work services | p27.5 | Manufactured_products |
| 117 | Fabricated metal products, except machinery and equipment (28) | p28 | Manufactured_products |
| 118 | Machinery and equipment n.e.c. (29) | p29 | Manufactured_products |
| 119 | Office machinery and computers (30) | p30 | Manufactured_products |
| 120 | Electrical machinery and apparatus n.e.c. (31) | p31 | Manufactured_products |
| 121 | Radio, television and communication equipment and apparatus (32) | p32 | Manufactured_products |
| 122 | Medical, precision and optical instruments, watches and clocks (33) | p33 | Manufactured_products |
| 123 | Motor vehicles, trailers and semi-trailers (34) | p34 | Manufactured_products |
| 124 | Other transport equipment (35) | p35 | Manufactured_products |
| 125 | Furniture; other manufactured goods n.e.c. (36) | p36 | Manufactured_products |
| 126 | Secondary raw materials | p37 | Manufactured_products |
| 127 | Bottles for treatment, Recycling of bottles by direct reuse | p37.w.1 | Manufactured_products |
| 128 | Electricity by coal | p40.11.a | Shelter |
| 129 | Electricity by gas | p40.11.b | Shelter |
| 130 | Electricity by nuclear | p40.11.c | Shelter |
| 131 | Electricity by hydro | p40.11.d | Shelter |
| 132 | Electricity by wind | p40.11.e | Shelter |
| 133 | Electricity by petroleum and other oil derivatives | p40.11.f | Shelter |
| 134 | Electricity by biomass and waste | p40.11.g | Shelter |
| 135 | Electricity by solar photovoltaic | p40.11.h | Shelter |
| 136 | Electricity by solar thermal | p40.11.i | Shelter |
| 137 | Electricity by tide, wave, ocean | p40.11.j | Shelter |
| 138 | Electricity by Geothermal | p40.11.k | Shelter |
| 139 | Electricity nec | p40.11.l | Shelter |
| 140 | Transmission services of electricity | p40.12 | Shelter |
| 141 | Distribution and trade services of electricity | p40.13 | Shelter |
| 142 | Coke oven gas | p40.2.a | Shelter |
| 143 | Blast Furnace Gas | p40.2.b | Shelter |
| 144 | Oxygen Steel Furnace Gas | p40.2.c | Shelter |
| 145 | Gas Works Gas | p40.2.d | Shelter |
| 146 | Biogas | p40.2.e | Shelter |
| 147 | Distribution services of gaseous fuels through mains | p40.2.1 | Shelter |
| 148 | Steam and hot water supply services | p40.3 | Shelter |
| 149 | Collected and purified water, distribution services of water (41) | p41 | Shelter |
| 150 | Construction work (45) | p45 | Construction |
| 151 | Secondary construction material for treatment, Re-processing of secondary construction material into aggregates | p45.w | Construction |
| 152 | Sale, maintenance, repair of motor vehicles, motor vehicles parts, motorcycles, motor cycles parts and accessoiries | p50.a | Trade |
| 153 | Retail trade services of motor fuel | p50.b | Trade |
| 154 | Wholesale trade and commission trade services, except of motor vehicles and motorcycles (51) | p51 | Trade |
| 155 | Retail  trade services, except of motor vehicles and motorcycles; repair services of personal and household goods (52) | p52 | Trade |
| 156 | Hotel and restaurant services (55) | p55 | Services |
| 157 | Railway transportation services | p60.1 | Mobility |
| 158 | Other land transportation services | p60.2 | Mobility |
| 159 | Transportation services via pipelines | p60.3 | Mobility |
| 160 | Sea and coastal water transportation services | p61.1 | Mobility |
| 161 | Inland water transportation services | p61.2 | Mobility |
| 162 | Air transport services (62) | p62 | Mobility |
| 163 | Supporting and auxiliary transport services; travel agency services (63) | p63 | Services |
| 164 | Post and telecommunication services (64) | p64 | Services |
| 165 | Financial intermediation services, except insurance and pension funding services (65) | p65 | Services |
| 166 | Insurance and pension funding services, except compulsory social security services (66) | p66 | Services |
| 167 | Services auxiliary to financial intermediation (67) | p67 | Services |
| 168 | Real estate services (70) | p70 | Services |
| 169 | Renting services of machinery and equipment without operator and of personal and household goods (71) | p71 | Services |
| 170 | Computer and related services (72) | p72 | Services |
| 171 | Research and development services (73) | p73 | Services |
| 172 | Other business services (74) | p74 | Services |
| 173 | Public administration and defence services; compulsory social security services (75) | p75 | Services |
| 174 | Education services (80) | p80 | Services |
| 175 | Health and social work services (85) | p85 | Services |
| 176 | Food waste for treatment: incineration | p90.1.a | Shelter |
| 177 | Paper waste for treatment: incineration | p90.1.b | Shelter |
| 178 | Plastic waste for treatment: incineration | p90.1.c | Shelter |
| 179 | Intert/metal waste for treatment: incineration | p90.1.d | Shelter |
| 180 | Textiles waste for treatment: incineration | p90.1.e | Shelter |
| 181 | Wood waste for treatment: incineration | p90.1.f | Shelter |
| 182 | Oil/hazardous waste for treatment: incineration | p90.1.g | Shelter |
| 183 | Food waste for treatment: biogasification and land application | p90.2.a | Shelter |
| 184 | Paper waste for treatment: biogasification and land application | p90.2.b | Shelter |
| 185 | Sewage sludge for treatment: biogasification and land application | p90.2.c | Shelter |
| 186 | Food waste for treatment: composting and land application | p90.3.a | Shelter |
| 187 | Paper and wood waste for treatment: composting and land application | p90.3.b | Shelter |
| 188 | Food waste for treatment: waste water treatment | p90.4.a | Shelter |
| 189 | Other waste for treatment: waste water treatment | p90.4.b | Shelter |
| 190 | Food waste for treatment: landfill | p90.5.a | Shelter |
| 191 | Paper for treatment: landfill | p90.5.b | Shelter |
| 192 | Plastic waste for treatment: landfill | p90.5.c | Shelter |
| 193 | Inert/metal/hazardous waste for treatment: landfill | p90.5.d | Shelter |
| 194 | Textiles waste for treatment: landfill | p90.5.e | Shelter |
| 195 | Wood waste for treatment: landfill | p90.5.f | Shelter |
| 196 | Membership organisation services n.e.c. (91) | p91 | Services |
| 197 | Recreational, cultural and sporting services (92) | p92 | Services |
| 198 | Other services (93) | p93 | Services |
| 199 | Private households with employed persons (95) | p95 | Shelter |
| 200 | Extra-territorial organizations and bodies | p99 | Services |

## Industries — ixi (163)

| # | Industry | Exio code | ISIC class | Consumption category |
| ---: | --- | --- | --- | --- |
| 1 | Cultivation of paddy rice | i01.a | Agriculture, hunting and related service activities (01) | Food |
| 2 | Cultivation of wheat | i01.b | Agriculture, hunting and related service activities (01) | Food |
| 3 | Cultivation of cereal grains nec | i01.c | Agriculture, hunting and related service activities (01) | Food |
| 4 | Cultivation of vegetables, fruit, nuts | i01.d | Agriculture, hunting and related service activities (01) | Food |
| 5 | Cultivation of oil seeds | i01.e | Agriculture, hunting and related service activities (01) | Food |
| 6 | Cultivation of sugar cane, sugar beet | i01.f | Agriculture, hunting and related service activities (01) | Food |
| 7 | Cultivation of plant-based fibers | i01.g | Agriculture, hunting and related service activities (01) | Food |
| 8 | Cultivation of crops nec | i01.h | Agriculture, hunting and related service activities (01) | Food |
| 9 | Cattle farming | i01.i | Agriculture, hunting and related service activities (01) | Food |
| 10 | Pigs farming | i01.j | Agriculture, hunting and related service activities (01) | Food |
| 11 | Poultry farming | i01.k | Agriculture, hunting and related service activities (01) | Food |
| 12 | Meat animals nec | i01.l | Agriculture, hunting and related service activities (01) | Food |
| 13 | Animal products nec | i01.m | Agriculture, hunting and related service activities (01) | Food |
| 14 | Raw milk | i01.n | Agriculture, hunting and related service activities (01) | Food |
| 15 | Wool, silk-worm cocoons | i01.o | Agriculture, hunting and related service activities (01) | Clothing |
| 16 | Manure treatment (conventional), storage and land application | i01.w.1 | Agriculture, hunting and related service activities (01) | Food |
| 17 | Manure treatment (biogas), storage and land application | i01.w.2 | Agriculture, hunting and related service activities (01) | Food |
| 18 | Forestry, logging and related service activities (02) | i02 | Forestry, logging and related service activities (02) | Shelter |
| 19 | Fishing, operating of fish hatcheries and fish farms; service activities incidental to fishing (05) | i05 | Fishing (B) | Food |
| 20 | Mining of coal and lignite; extraction of peat (10) | i10 | Mining and quarrying (C) | Shelter |
| 21 | Extraction of crude petroleum and services related to crude oil extraction, excluding surveying | i11.a | Mining and quarrying (C) | Shelter |
| 22 | Extraction of natural gas and services related to natural gas extraction, excluding surveying | i11.b | Mining and quarrying (C) | Shelter |
| 23 | Extraction, liquefaction, and regasification of other petroleum and gaseous materials | i11.c | Mining and quarrying (C) | Shelter |
| 24 | Mining of uranium and thorium ores (12) | i12 | Mining and quarrying (C) | Shelter |
| 25 | Mining of iron ores | i13.1 | Mining and quarrying (C) | Shelter |
| 26 | Mining of copper ores and concentrates | i13.20.11 | Mining and quarrying (C) | Construction |
| 27 | Mining of nickel ores and concentrates | i13.20.12 | Mining and quarrying (C) | Construction |
| 28 | Mining of aluminium ores and concentrates | i13.20.13 | Mining and quarrying (C) | Construction |
| 29 | Mining of precious metal ores and concentrates | i13.20.14 | Mining and quarrying (C) | Construction |
| 30 | Mining of lead, zinc and tin ores and concentrates | i13.20.15 | Mining and quarrying (C) | Construction |
| 31 | Mining of other non-ferrous metal ores and concentrates | i13.20.16 | Mining and quarrying (C) | Construction |
| 32 | Quarrying of stone | i14.1 | Mining and quarrying (C) | Construction |
| 33 | Quarrying of sand and clay | i14.2 | Mining and quarrying (C) | Construction |
| 34 | Mining of chemical and fertilizer minerals, production of salt, other mining and quarrying n.e.c. | i14.3 | Mining and quarrying (C) | Food |
| 35 | Processing of meat cattle | i15.a | Manufacturing (D) | Food |
| 36 | Processing of meat pigs | i15.b | Manufacturing (D) | Food |
| 37 | Processing of meat poultry | i15.c | Manufacturing (D) | Food |
| 38 | Production of meat products nec | i15.d | Manufacturing (D) | Food |
| 39 | Processing vegetable oils and fats | i15.e | Manufacturing (D) | Food |
| 40 | Processing of dairy products | i15.f | Manufacturing (D) | Food |
| 41 | Processed rice | i15.g | Manufacturing (D) | Food |
| 42 | Sugar refining | i15.h | Manufacturing (D) | Food |
| 43 | Processing of Food products nec | i15.i | Manufacturing (D) | Food |
| 44 | Manufacture of beverages | i15.j | Manufacturing (D) | Food |
| 45 | Manufacture of fish products | i15.k | Manufacturing (D) | Food |
| 46 | Manufacture of tobacco products (16) | i16 | Manufacturing (D) | Food |
| 47 | Manufacture of textiles (17) | i17 | Manufacturing (D) | Clothing |
| 48 | Manufacture of wearing apparel; dressing and dyeing of fur (18) | i18 | Manufacturing (D) | Clothing |
| 49 | Tanning and dressing of leather; manufacture of luggage, handbags, saddlery, harness and footwear (19) | i19 | Manufacturing (D) | Clothing |
| 50 | Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials (20) | i20 | Manufacturing (D) | Shelter |
| 51 | Re-processing of secondary wood material into new wood material | i20.w | Manufacturing (D) | Shelter |
| 52 | Pulp | i21.1 | Manufacturing (D) | Manufactured_products |
| 53 | Re-processing of secondary paper into new pulp | i21.w.1 | Manufacturing (D) | Manufactured_products |
| 54 | Paper | i21.2 | Manufacturing (D) | Manufactured_products |
| 55 | Publishing, printing and reproduction of recorded media (22) | i22 | Manufacturing (D) | Services |
| 56 | Manufacture of coke oven products | i23.1 | Manufacturing (D) | Shelter |
| 57 | Petroleum Refinery | i23.2 | Manufacturing (D) | Mobility |
| 58 | Processing of nuclear fuel | i23.3 | Manufacturing (D) | Shelter |
| 59 | Plastics, basic | i24.a | Manufacturing (D) | Manufactured_products |
| 60 | Re-processing of secondary plastic into new plastic | i24.a.w | Manufacturing (D) | Manufactured_products |
| 61 | N-fertiliser | i24.b | Manufacturing (D) | Food |
| 62 | P- and other fertiliser | i24.c | Manufacturing (D) | Food |
| 63 | Chemicals nec | i24.d | Manufacturing (D) | Manufactured_products |
| 64 | Manufacture of rubber and plastic products (25) | i25 | Manufacturing (D) | Manufactured_products |
| 65 | Manufacture of glass and glass products | i26.a | Manufacturing (D) | Construction |
| 66 | Re-processing of secondary glass into new glass | i26.a.w | Manufacturing (D) | Construction |
| 67 | Manufacture of ceramic goods | i26.b | Manufacturing (D) | Construction |
| 68 | Manufacture of bricks, tiles and construction products, in baked clay | i26.c | Manufacturing (D) | Construction |
| 69 | Manufacture of cement, lime and plaster | i26.d | Manufacturing (D) | Construction |
| 70 | Re-processing of ash into clinker | i26.d.w | Manufacturing (D) | Construction |
| 71 | Manufacture of other non-metallic mineral products n.e.c. | i26.e | Manufacturing (D) | Construction |
| 72 | Manufacture of basic iron and steel and of ferro-alloys and first products thereof | i27.a | Manufacturing (D) | Manufactured_products |
| 73 | Re-processing of secondary steel into new steel | i27.a.w | Manufacturing (D) | Manufactured_products |
| 74 | Precious metals production | i27.41 | Manufacturing (D) | Manufactured_products |
| 75 | Re-processing of secondary preciuos metals into new preciuos metals | i27.41.w | Manufacturing (D) | Manufactured_products |
| 76 | Aluminium production | i27.42 | Manufacturing (D) | Manufactured_products |
| 77 | Re-processing of secondary aluminium into new aluminium | i27.42.w | Manufacturing (D) | Manufactured_products |
| 78 | Lead, zinc and tin production | i27.43 | Manufacturing (D) | Manufactured_products |
| 79 | Re-processing of secondary lead into new lead, zinc and tin | i27.43.w | Manufacturing (D) | Manufactured_products |
| 80 | Copper production | i27.44 | Manufacturing (D) | Manufactured_products |
| 81 | Re-processing of secondary copper into new copper | i27.44.w | Manufacturing (D) | Manufactured_products |
| 82 | Other non-ferrous metal production | i27.45 | Manufacturing (D) | Manufactured_products |
| 83 | Re-processing of secondary other non-ferrous metals into new other non-ferrous metals | i27.45.w | Manufacturing (D) | Manufactured_products |
| 84 | Casting of metals | i27.5 | Manufacturing (D) | Manufactured_products |
| 85 | Manufacture of fabricated metal products, except machinery and equipment (28) | i28 | Manufacturing (D) | Manufactured_products |
| 86 | Manufacture of machinery and equipment n.e.c. (29) | i29 | Manufacturing (D) | Manufactured_products |
| 87 | Manufacture of office machinery and computers (30) | i30 | Manufacturing (D) | Manufactured_products |
| 88 | Manufacture of electrical machinery and apparatus n.e.c. (31) | i31 | Manufacturing (D) | Manufactured_products |
| 89 | Manufacture of radio, television and communication equipment and apparatus (32) | i32 | Manufacturing (D) | Manufactured_products |
| 90 | Manufacture of medical, precision and optical instruments, watches and clocks (33) | i33 | Manufacturing (D) | Manufactured_products |
| 91 | Manufacture of motor vehicles, trailers and semi-trailers (34) | i34 | Manufacturing (D) | Manufactured_products |
| 92 | Manufacture of other transport equipment (35) | i35 | Manufacturing (D) | Manufactured_products |
| 93 | Manufacture of furniture; manufacturing n.e.c. (36) | i36 | Manufacturing (D) | Manufactured_products |
| 94 | Recycling of waste and scrap | i37 | Manufacturing (D) | Manufactured_products |
| 95 | Recycling of bottles by direct reuse | i37.w.1 | Manufacturing (D) | Manufactured_products |
| 96 | Production of electricity by coal | i40.11.a | Electricity, gas and water supply (E) | Shelter |
| 97 | Production of electricity by gas | i40.11.b | Electricity, gas and water supply (E) | Shelter |
| 98 | Production of electricity by nuclear | i40.11.c | Electricity, gas and water supply (E) | Shelter |
| 99 | Production of electricity by hydro | i40.11.d | Electricity, gas and water supply (E) | Shelter |
| 100 | Production of electricity by wind | i40.11.e | Electricity, gas and water supply (E) | Shelter |
| 101 | Production of electricity by petroleum and other oil derivatives | i40.11.f | Electricity, gas and water supply (E) | Shelter |
| 102 | Production of electricity by biomass and waste | i40.11.g | Electricity, gas and water supply (E) | Shelter |
| 103 | Production of electricity by solar photovoltaic | i40.11.h | Electricity, gas and water supply (E) | Shelter |
| 104 | Production of electricity by solar thermal | i40.11.i | Electricity, gas and water supply (E) | Shelter |
| 105 | Production of electricity by tide, wave, ocean | i40.11.j | Electricity, gas and water supply (E) | Shelter |
| 106 | Production of electricity by Geothermal | i40.11.k | Electricity, gas and water supply (E) | Shelter |
| 107 | Production of electricity nec | i40.11.l | Electricity, gas and water supply (E) | Shelter |
| 108 | Transmission of electricity | i40.12 | Electricity, gas and water supply (E) | Shelter |
| 109 | Distribution and trade of electricity | i40.13 | Electricity, gas and water supply (E) | Shelter |
| 110 | Manufacture of gas; distribution of gaseous fuels through mains | i40.2 | Electricity, gas and water supply (E) | Shelter |
| 111 | Steam and hot water supply | i40.3 | Electricity, gas and water supply (E) | Shelter |
| 112 | Collection, purification and distribution of water (41) | i41 | Electricity, gas and water supply (E) | Shelter |
| 113 | Construction (45) | i45 | Construction (F) | Construction |
| 114 | Re-processing of secondary construction material into aggregates | i45.w | Construction (F) | Construction |
| 115 | Sale, maintenance, repair of motor vehicles, motor vehicles parts, motorcycles, motor cycles parts and accessoiries | i50.a | Wholesale retail trade, repair of motor vehicles, motorcycles, etc.; hotels and restaurants (G+H) | Trade |
| 116 | Retail sale of automotive fuel | i50.b | Wholesale retail trade, repair of motor vehicles, motorcycles, etc.; hotels and restaurants (G+H) | Trade |
| 117 | Wholesale trade and commission trade, except of motor vehicles and motorcycles (51) | i51 | Wholesale retail trade, repair of motor vehicles, motorcycles, etc.; hotels and restaurants (G+H) | Trade |
| 118 | Retail trade, except of motor vehicles and motorcycles; repair of personal and household goods (52) | i52 | Wholesale retail trade, repair of motor vehicles, motorcycles, etc.; hotels and restaurants (G+H) | Trade |
| 119 | Hotels and restaurants (55) | i55 | Wholesale retail trade, repair of motor vehicles, motorcycles, etc.; hotels and restaurants (G+H) | Services |
| 120 | Transport via railways | i60.1 | Transport, storage and communications (I) | Mobility |
| 121 | Other land transport | i60.2 | Transport, storage and communications (I) | Mobility |
| 122 | Transport via pipelines | i60.3 | Transport, storage and communications (I) | Mobility |
| 123 | Sea and coastal water transport | i61.1 | Transport, storage and communications (I) | Mobility |
| 124 | Inland water transport | i61.2 | Transport, storage and communications (I) | Mobility |
| 125 | Air transport (62) | i62 | Transport, storage and communications (I) | Mobility |
| 126 | Supporting and auxiliary transport activities; activities of travel agencies (63) | i63 | Transport, storage and communications (I) | Mobility |
| 127 | Post and telecommunications (64) | i64 | Transport, storage and communications (I) | Mobility |
| 128 | Financial intermediation, except insurance and pension funding (65) | i65 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 129 | Insurance and pension funding, except compulsory social security (66) | i66 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 130 | Activities auxiliary to financial intermediation (67) | i67 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 131 | Real estate activities (70) | i70 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 132 | Renting of machinery and equipment without operator and of personal and household goods (71) | i71 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 133 | Computer and related activities (72) | i72 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 134 | Research and development (73) | i73 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 135 | Other business activities (74) | i74 | Financial intermediation; real estate, renting and business activities (J+K) | Services |
| 136 | Public administration and defence; compulsory social security (75) | i75 | Public administration and defense; compulsory social security (L) | Services |
| 137 | Education (80) | i80 | Education; health and social work; other community, social and personal services (M+N+O) | Services |
| 138 | Health and social work (85) | i85 | Education; health and social work; other community, social and personal services (M+N+O) | Services |
| 139 | Incineration of waste: Food | i90.1.a | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 140 | Incineration of waste: Paper | i90.1.b | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 141 | Incineration of waste: Plastic | i90.1.c | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 142 | Incineration of waste: Metals and Inert materials | i90.1.d | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 143 | Incineration of waste: Textiles | i90.1.e | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 144 | Incineration of waste: Wood | i90.1.f | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 145 | Incineration of waste: Oil/Hazardous waste | i90.1.g | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 146 | Biogasification of food waste, incl. land application | i90.2.a | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 147 | Biogasification of paper, incl. land application | i90.2.b | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 148 | Biogasification of sewage slugde, incl. land application | i90.2.c | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 149 | Composting of food waste, incl. land application | i90.3.a | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 150 | Composting of paper and wood, incl. land application | i90.3.b | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 151 | Waste water treatment, food | i90.4.a | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 152 | Waste water treatment, other | i90.4.b | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 153 | Landfill of waste: Food | i90.5.a | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 154 | Landfill of waste: Paper | i90.5.b | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 155 | Landfill of waste: Plastic | i90.5.c | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 156 | Landfill of waste: Inert/metal/hazardous | i90.5.d | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 157 | Landfill of waste: Textiles | i90.5.e | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 158 | Landfill of waste: Wood | i90.5.f | Education; health and social work; other community, social and personal services (M+N+O) | Shelter |
| 159 | Activities of membership organisation n.e.c. (91) | i91 | Education; health and social work; other community, social and personal services (M+N+O) | Services |
| 160 | Recreational, cultural and sporting activities (92) | i92 | Education; health and social work; other community, social and personal services (M+N+O) | Services |
| 161 | Other service activities (93) | i93 | Education; health and social work; other community, social and personal services (M+N+O) | Services |
| 162 | Private households with employed persons (95) | i95 | Private households with employed persons (P) | Shelter |
| 163 | Extra-territorial organizations and bodies | i99 | Public administration and defense; compulsory social security (L) | Services |
