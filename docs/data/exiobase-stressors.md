# EXIOBASE 3 — all satellite-account stressors (exhaustive)

Every indicator in every EXIOBASE 3 satellite account (2022, pxp), with its unit. Each attaches to all 49 regions × 200 products. See also the [sector lists](exiobase-sectors.md) and the [data catalog](datasets.md).

**Source:** read directly from `IOT_2022_pxp.zip` (Zenodo DOI [10.5281/zenodo.3583070](https://doi.org/10.5281/zenodo.3583070)) via pymrio 0.6.3. Generated from the data.


| Extension | # | Units |
| --- | ---: | --- |
| [employment](#employment) | 12 | 1000 p ×6, M.hr ×6 |
| [air_emissions](#air_emissions) | 420 | kg ×418, kg CO2-eq ×2 |
| [energy](#energy) | 4 | TJ ×4 |
| [material](#material) | 62 | kt ×62 |
| [water](#water) | 194 | Mm3 ×194 |
| [land](#land) | 26 | km2 ×26 |
| [nutrients](#nutrients) | 6 | kg ×6 |
| [factor_inputs](#factor_inputs) | 9 | M.EUR ×9 |

## employment

<a id="employment"></a>Jobs **and** hours worked, split by skill (low / medium / high) × sex. 6 rows in `1000 p` (thousand persons) and 6 in `M.hr` (million hours).

- 12 stressors · units: 1000 p ×6, M.hr ×6

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Employment people: Low-skilled male | 1000 p |
| 2 | Employment people: Low-skilled female | 1000 p |
| 3 | Employment people: Medium-skilled male | 1000 p |
| 4 | Employment people: Medium-skilled female | 1000 p |
| 5 | Employment people: High-skilled male | 1000 p |
| 6 | Employment people: High-skilled female | 1000 p |
| 7 | Employment hours: Low-skilled male | M.hr |
| 8 | Employment hours: Low-skilled female | M.hr |
| 9 | Employment hours: Medium-skilled male | M.hr |
| 10 | Employment hours: Medium-skilled female | M.hr |
| 11 | Employment hours: High-skilled male | M.hr |
| 12 | Employment hours: High-skilled female | M.hr |

## air_emissions

<a id="air_emissions"></a>Pattern `Substance - Source - air` (e.g. `CO2 - combustion - air`); a few gases have no source token. The two `kg CO2-eq` rows are GWP-weighted GHG totals.

- 420 stressors · units: kg ×418, kg CO2-eq ×2
- By source: non combustion (373), combustion (31), waste (8), agriculture (5), (unspecified) (3)

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | As - combustion - air | kg |
| 2 | B(a)P - combustion - air | kg |
| 3 | B(b)F - combustion - air | kg |
| 4 | B(k)F - combustion - air | kg |
| 5 | CH4 - combustion - air | kg |
| 6 | CH4_bio - combustion - air | kg |
| 7 | CO - combustion - air | kg |
| 8 | CO2 - combustion - air | kg |
| 9 | CO2_bio - combustion - air | kg |
| 10 | Cd - combustion - air | kg |
| 11 | Cr - combustion - air | kg |
| 12 | Cu - combustion - air | kg |
| 13 | HCB - combustion - air | kg |
| 14 | Hg - combustion - air | kg |
| 15 | Indeno - combustion - air | kg |
| 16 | N2O - combustion - air | kg |
| 17 | N2O_bio - combustion - air | kg |
| 18 | NH3 - combustion - air | kg |
| 19 | NMVOC - combustion - air | kg |
| 20 | NOx - combustion - air | kg |
| 21 | Ni - combustion - air | kg |
| 22 | PCB - combustion - air | kg |
| 23 | PCDD/F - combustion - air | kg |
| 24 | PM10 - combustion - air | kg |
| 25 | PM2_5 - combustion - air | kg |
| 26 | Pb - combustion - air | kg |
| 27 | SO2 - combustion - air | kg |
| 28 | SOx - combustion - air | kg |
| 29 | Se - combustion - air | kg |
| 30 | TSP - combustion - air | kg |
| 31 | Zn - combustion - air | kg |
| 32 | As - non combustion - Agglomeration plant - pellets - air | kg |
| 33 | As - non combustion - Agglomeration plant - sinter - air | kg |
| 34 | As - non combustion - Glass production - air | kg |
| 35 | As - non combustion - Production of coke oven coke - air | kg |
| 36 | As - non combustion - Production of gascoke - air | kg |
| 37 | As - non combustion - Steel production: basic oxygen furnace - air | kg |
| 38 | As - non combustion - Steel production: electric arc furnace - air | kg |
| 39 | As - non combustion - Steel production: open hearth furnace - air | kg |
| 40 | B(a)P - non combustion - Primary aluminium production - air | kg |
| 41 | B(a)P - non combustion - Production of coke oven coke - air | kg |
| 42 | B(a)P - non combustion - Production of gascoke - air | kg |
| 43 | B(b)F - non combustion - Primary aluminium production - air | kg |
| 44 | B(b)F - non combustion - Production of coke oven coke - air | kg |
| 45 | B(b)F - non combustion - Production of gascoke - air | kg |
| 46 | B(k)F - non combustion - Primary aluminium production - air | kg |
| 47 | B(k)F - non combustion - Production of coke oven coke - air | kg |
| 48 | B(k)F - non combustion - Production of gascoke - air | kg |
| 49 | CH4 - non combustion - Extraction/production of (natural) gas - air | kg |
| 50 | CH4 - non combustion - Extraction/production of crude oil - air | kg |
| 51 | CH4 - non combustion - Mining of antracite - air | kg |
| 52 | CH4 - non combustion - Mining of bituminous coal - air | kg |
| 53 | CH4 - non combustion - Mining of coking coal - air | kg |
| 54 | CH4 - non combustion - Mining of lignite (brown coal) - air | kg |
| 55 | CH4 - non combustion - Mining of sub-bituminous coal - air | kg |
| 56 | CH4 - non combustion - Oil refinery - air | kg |
| 57 | CO - non combustion - Agglomeration plant - sinter - air | kg |
| 58 | CO - non combustion - Bricks production - air | kg |
| 59 | CO - non combustion - Carbon black production - air | kg |
| 60 | CO - non combustion - Cement production - air | kg |
| 61 | CO - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 62 | CO - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 63 | CO - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 64 | CO - non combustion - Glass production - air | kg |
| 65 | CO - non combustion - Lime production - air | kg |
| 66 | CO - non combustion - Oil refinery - air | kg |
| 67 | CO - non combustion - Pig iron production, blast furnace - air | kg |
| 68 | CO - non combustion - Primary aluminium production - air | kg |
| 69 | CO - non combustion - Production of coke oven coke - air | kg |
| 70 | CO - non combustion - Production of gascoke - air | kg |
| 71 | CO - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 72 | CO - non combustion - Steel production: basic oxygen furnace - air | kg |
| 73 | CO - non combustion - Steel production: electric arc furnace - air | kg |
| 74 | CO2 - non combustion - Cement production - air | kg |
| 75 | CO2 - non combustion - Lime production - air | kg |
| 76 | Cd - non combustion - Agglomeration plant - pellets - air | kg |
| 77 | Cd - non combustion - Agglomeration plant - sinter - air | kg |
| 78 | Cd - non combustion - Glass production - air | kg |
| 79 | Cd - non combustion - Nickel, unwrought - air | kg |
| 80 | Cd - non combustion - Production of coke oven coke - air | kg |
| 81 | Cd - non combustion - Production of gascoke - air | kg |
| 82 | Cd - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 83 | Cd - non combustion - Refined lead, unwrought - air | kg |
| 84 | Cd - non combustion - Steel production: basic oxygen furnace - air | kg |
| 85 | Cd - non combustion - Steel production: electric arc furnace - air | kg |
| 86 | Cd - non combustion - Steel production: open hearth furnace - air | kg |
| 87 | Cd - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 88 | Cd - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 89 | Cr - non combustion - Agglomeration plant - pellets - air | kg |
| 90 | Cr - non combustion - Agglomeration plant - sinter - air | kg |
| 91 | Cr - non combustion - Glass production - air | kg |
| 92 | Cr - non combustion - Pig iron production, blast furnace - air | kg |
| 93 | Cr - non combustion - Steel production: basic oxygen furnace - air | kg |
| 94 | Cr - non combustion - Steel production: electric arc furnace - air | kg |
| 95 | Cr - non combustion - Steel production: open hearth furnace - air | kg |
| 96 | Cu - non combustion - Agglomeration plant - pellets - air | kg |
| 97 | Cu - non combustion - Agglomeration plant - sinter - air | kg |
| 98 | Cu - non combustion - Glass production - air | kg |
| 99 | Cu - non combustion - Pig iron production, blast furnace - air | kg |
| 100 | Cu - non combustion - Steel production: basic oxygen furnace - air | kg |
| 101 | Cu - non combustion - Steel production: electric arc furnace - air | kg |
| 102 | Cu - non combustion - Steel production: open hearth furnace - air | kg |
| 103 | HCB - non combustion - Agglomeration plant - pellets - air | kg |
| 104 | HCB - non combustion - Agglomeration plant - sinter - air | kg |
| 105 | Hg - non combustion - Agglomeration plant - pellets - air | kg |
| 106 | Hg - non combustion - Agglomeration plant - sinter - air | kg |
| 107 | Hg - non combustion - Glass production - air | kg |
| 108 | Hg - non combustion - Nickel, unwrought - air | kg |
| 109 | Hg - non combustion - Pig iron production, blast furnace - air | kg |
| 110 | Hg - non combustion - Production of coke oven coke - air | kg |
| 111 | Hg - non combustion - Production of gascoke - air | kg |
| 112 | Hg - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 113 | Hg - non combustion - Refined lead, unwrought - air | kg |
| 114 | HCB - non combustion - Secondary aluminium production - air | kg |
| 115 | Hg - non combustion - Steel production: basic oxygen furnace - air | kg |
| 116 | Hg - non combustion - Steel production: electric arc furnace - air | kg |
| 117 | Hg - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 118 | Hg - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 119 | Indeno - non combustion - Primary aluminium production - air | kg |
| 120 | Indeno - non combustion - Production of coke oven coke - air | kg |
| 121 | Indeno - non combustion - Production of gascoke - air | kg |
| 122 | NH3 - non combustion - N- fertilizer production - air | kg |
| 123 | NMVOC - non combustion - Beef and veal - air | kg |
| 124 | NMVOC - non combustion - Coil coating (coating of aluminum and steel) - air | kg |
| 125 | NMVOC - non combustion - Decorative paint applicatoin - air | kg |
| 126 | NMVOC - non combustion - Degreasing - air | kg |
| 127 | NMVOC - non combustion - Diesel distribution - transport and depots (used in mobile sources) - air | kg |
| 128 | NMVOC - non combustion - Diesel distribution - transport and depots (used in stationary sources) - air | kg |
| 129 | NMVOC - non combustion - Dry cleaning - air | kg |
| 130 | NMVOC - non combustion - Extraction, proc. and distribution of gaseous fuels - air | kg |
| 131 | NMVOC - non combustion - Extraction, proc. and distribution of liquid fuels - air | kg |
| 132 | NMVOC - non combustion - Extraction/production of (natural) gas - air | kg |
| 133 | NMVOC - non combustion - Extraction/production of crude oil - air | kg |
| 134 | NMVOC - non combustion - Fat, edible and non-edible oil extraction - air | kg |
| 135 | NMVOC - non combustion - Fish, dried, salted or in brine; smoked fish; edible fish meal - air | kg |
| 136 | NMVOC - non combustion - Fish, fish fillets, other fish meat and fish livers and roes, frozen - air | kg |
| 137 | NMVOC - non combustion - Fish, otherwise prepared or preserved; caviar - air | kg |
| 138 | NMVOC - non combustion - Flexography and rotogravure in packaging - air | kg |
| 139 | NMVOC - non combustion - Gasoline distribution - service stations - air | kg |
| 140 | NMVOC - non combustion - Gasoline distribution - transport and depots (used in mobile sources) - air | kg |
| 141 | NMVOC - non combustion - Gasoline distribution - transport and depots (used in stationary sources) - air | kg |
| 142 | NMVOC - non combustion - Industrial application of adhesives (use of high performance solvent based adhesives) - air | kg |
| 143 | NMVOC - non combustion - Industrial application of adhesives (use of traditional solvent based adhesives) - air | kg |
| 144 | NMVOC - non combustion - Industrial paint application, general industry (continuous processes) - air | kg |
| 145 | NMVOC - non combustion - Industrial paint application, general industry (plastic parts) - air | kg |
| 146 | NMVOC - non combustion - Industrial paint application, general industry - air | kg |
| 147 | NMVOC - non combustion - Inorganic chemical industry, fertilizers and other - air | kg |
| 148 | NMVOC - non combustion - Leather coating - air | kg |
| 149 | NMVOC - non combustion - Manufacture of automobiles - air | kg |
| 150 | NMVOC - non combustion - Mutton and lamb - air | kg |
| 151 | NMVOC - non combustion - Oil refinery - air | kg |
| 152 | NMVOC - non combustion - Organic chemical industry - downstream units - air | kg |
| 153 | NMVOC - non combustion - Organic chemical industry, storage - air | kg |
| 154 | NMVOC - non combustion - Other industrial use of solvents - air | kg |
| 155 | NMVOC - non combustion - Pharmaceutical industry - air | kg |
| 156 | NMVOC - non combustion - Polystyrene processing - air | kg |
| 157 | NMVOC - non combustion - Polyvinylchloride produceduction by suspension process - air | kg |
| 158 | NMVOC - non combustion - Pork - air | kg |
| 159 | NMVOC - non combustion - Poultry, dressed - air | kg |
| 160 | NMVOC - non combustion - Printing, offset - air | kg |
| 161 | NMVOC - non combustion - Products incorporating solvents - air | kg |
| 162 | NMVOC - non combustion - Raw sugar - air | kg |
| 163 | NMVOC - non combustion - Rotogravure in publication - air | kg |
| 164 | NMVOC - non combustion - Screen printing - air | kg |
| 165 | NMVOC - non combustion - Steam cracking (ethylene and propylene production) - air | kg |
| 166 | NMVOC - non combustion - Synthetic rubber - air | kg |
| 167 | NMVOC - non combustion - Tyre production - air | kg |
| 168 | NMVOC - non combustion - Vehicle refinishing - air | kg |
| 169 | NMVOC - non combustion - Wire coating - air | kg |
| 170 | NOx - non combustion - Agglomeration plant - pellets - air | kg |
| 171 | NOx - non combustion - Agglomeration plant - sinter - air | kg |
| 172 | NOx - non combustion - Bricks production - air | kg |
| 173 | NOx - non combustion - Cement production - air | kg |
| 174 | NOx - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 175 | NOx - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 176 | NOx - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 177 | NOx - non combustion - Glass production - air | kg |
| 178 | NOx - non combustion - Lime production - air | kg |
| 179 | NOx - non combustion - Nickel, unwrought - air | kg |
| 180 | NOx - non combustion - Oil refinery - air | kg |
| 181 | NOx - non combustion - Pig iron production, blast furnace - air | kg |
| 182 | NOx - non combustion - Production of coke oven coke - air | kg |
| 183 | NOx - non combustion - Production of gascoke - air | kg |
| 184 | NOx - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 185 | NOx - non combustion - Refined lead, unwrought - air | kg |
| 186 | NOx - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 187 | NOx - non combustion - Steel production: basic oxygen furnace - air | kg |
| 188 | NOx - non combustion - Steel production: electric arc furnace - air | kg |
| 189 | NOx - non combustion - Sulphuric acid production - air | kg |
| 190 | NOx - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 191 | NOx - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 192 | Ni - non combustion - Agglomeration plant - pellets - air | kg |
| 193 | Ni - non combustion - Agglomeration plant - sinter - air | kg |
| 194 | Ni - non combustion - Glass production - air | kg |
| 195 | Ni - non combustion - Production of coke oven coke - air | kg |
| 196 | Ni - non combustion - Production of gascoke - air | kg |
| 197 | Ni - non combustion - Steel production: basic oxygen furnace - air | kg |
| 198 | Ni - non combustion - Steel production: electric arc furnace - air | kg |
| 199 | Ni - non combustion - Steel production: open hearth furnace - air | kg |
| 200 | PAH - non combustion - Agglomeration plant - pellets - air | kg |
| 201 | PAH - non combustion - Agglomeration plant - sinter - air | kg |
| 202 | PAH - non combustion - Pig iron production, blast furnace - air | kg |
| 203 | PAH - non combustion - Production of coke oven coke - air | kg |
| 204 | PAH - non combustion - Production of gascoke - air | kg |
| 205 | PAH - non combustion - Steel production: basic oxygen furnace - air | kg |
| 206 | PAH - non combustion - Steel production: electric arc furnace - air | kg |
| 207 | PCB - non combustion - Agglomeration plant - pellets - air | kg |
| 208 | PCB - non combustion - Agglomeration plant - sinter - air | kg |
| 209 | PCB - non combustion - Pig iron production, blast furnace - air | kg |
| 210 | PCB - non combustion - Steel production: basic oxygen furnace - air | kg |
| 211 | PCB - non combustion - Steel production: electric arc furnace - air | kg |
| 212 | PCDD/F - non combustion - Agglomeration plant - pellets - air | kg |
| 213 | PCDD/F - non combustion - Agglomeration plant - sinter - air | kg |
| 214 | PCDD/F - non combustion - Pig iron production, blast furnace - air | kg |
| 215 | PCDD/F - non combustion - Secondary aluminium production - air | kg |
| 216 | PCDD/F - non combustion - Steel production: basic oxygen furnace - air | kg |
| 217 | PCDD/F - non combustion - Steel production: electric arc furnace - air | kg |
| 218 | PM10 - non combustion - Agglomeration plant - pellets - air | kg |
| 219 | PM10 - non combustion - Agglomeration plant - sinter - air | kg |
| 220 | PM10 - non combustion - Aluminium ores and concentrates (Bauxite) - air | kg |
| 221 | PM10 - non combustion - Bricks production - air | kg |
| 222 | PM10 - non combustion - Briquettes production - air | kg |
| 223 | PM10 - non combustion - Carbon black production - air | kg |
| 224 | PM10 - non combustion - Cast iron production (grey iron foundries) - air | kg |
| 225 | PM10 - non combustion - Cement production - air | kg |
| 226 | PM10 - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 227 | PM10 - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 228 | PM10 - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 229 | PM10 - non combustion - Chromium ores and concentrates - air | kg |
| 230 | PM10 - non combustion - Copper ores and concentrates - air | kg |
| 231 | PM10 - non combustion - Fertilizer production (N-fertilizer) - air | kg |
| 232 | PM10 - non combustion - Glass production - air | kg |
| 233 | PM10 - non combustion - Gold ores and concentrates - air | kg |
| 234 | PM10 - non combustion - Iron ores and concentrates - air | kg |
| 235 | PM10 - non combustion - Lead ores and concentrates - air | kg |
| 236 | PM10 - non combustion - Lime production - air | kg |
| 237 | PM10 - non combustion - Mining of antracite - air | kg |
| 238 | PM10 - non combustion - Mining of bituminous coal - air | kg |
| 239 | PM10 - non combustion - Mining of coking coal - air | kg |
| 240 | PM10 - non combustion - Mining of lignite (brown coal) - air | kg |
| 241 | PM10 - non combustion - Mining of sub-bituminous coal - air | kg |
| 242 | PM10 - non combustion - Molybdenum ores and concentrates - air | kg |
| 243 | PM10 - non combustion - N- fertilizer production - air | kg |
| 244 | PM10 - non combustion - Nickel ores and concentrates - air | kg |
| 245 | PM10 - non combustion - Nickel, unwrought - air | kg |
| 246 | PM10 - non combustion - Oil refinery - air | kg |
| 247 | PM10 - non combustion - Pig iron production, blast furnace - air | kg |
| 248 | PM10 - non combustion - Platinum ores and concentrates - air | kg |
| 249 | PM10 - non combustion - Primary aluminium production - air | kg |
| 250 | PM10 - non combustion - Production of coke oven coke - air | kg |
| 251 | PM10 - non combustion - Production of gascoke - air | kg |
| 252 | PM10 - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 253 | PM10 - non combustion - Refined lead, unwrought - air | kg |
| 254 | PM10 - non combustion - Secondary aluminium production - air | kg |
| 255 | PM10 - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 256 | PM10 - non combustion - Silver ores and concentrates - air | kg |
| 257 | PM10 - non combustion - Steel production: basic oxygen furnace - air | kg |
| 258 | PM10 - non combustion - Steel production: electric arc furnace - air | kg |
| 259 | PM10 - non combustion - Steel production: open hearth furnace - air | kg |
| 260 | PM10 - non combustion - Tin ores and concentrates - air | kg |
| 261 | PM10 - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 262 | PM10 - non combustion - Zinc ores and concentrates - air | kg |
| 263 | PM10 - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 264 | PM2.5 - non combustion - Agglomeration plant - pellets - air | kg |
| 265 | PM2.5 - non combustion - Agglomeration plant - sinter - air | kg |
| 266 | PM2.5 - non combustion - Aluminium ores and concentrates (Bauxite) - air | kg |
| 267 | PM2.5 - non combustion - Bricks production - air | kg |
| 268 | PM2.5 - non combustion - Briquettes production - air | kg |
| 269 | PM2.5 - non combustion - Carbon black production - air | kg |
| 270 | PM2.5 - non combustion - Cast iron production (grey iron foundries) - air | kg |
| 271 | PM2.5 - non combustion - Cement production - air | kg |
| 272 | PM2.5 - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 273 | PM2.5 - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 274 | PM2.5 - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 275 | PM2.5 - non combustion - Chromium ores and concentrates - air | kg |
| 276 | PM2.5 - non combustion - Copper ores and concentrates - air | kg |
| 277 | PM2.5 - non combustion - Fertilizer production (N-fertilizer) - air | kg |
| 278 | PM2.5 - non combustion - Glass production - air | kg |
| 279 | PM2.5 - non combustion - Gold ores and concentrates - air | kg |
| 280 | PM2.5 - non combustion - Iron ores and concentrates - air | kg |
| 281 | PM2.5 - non combustion - Lead ores and concentrates - air | kg |
| 282 | PM2.5 - non combustion - Lime production - air | kg |
| 283 | PM2.5 - non combustion - Mining of antracite - air | kg |
| 284 | PM2.5 - non combustion - Mining of bituminous coal - air | kg |
| 285 | PM2.5 - non combustion - Mining of coking coal - air | kg |
| 286 | PM2.5 - non combustion - Mining of lignite (brown coal) - air | kg |
| 287 | PM2.5 - non combustion - Mining of sub-bituminous coal - air | kg |
| 288 | PM2.5 - non combustion - Molybdenum ores and concentrates - air | kg |
| 289 | PM2.5 - non combustion - N- fertilizer production - air | kg |
| 290 | PM2.5 - non combustion - Nickel ores and concentrates - air | kg |
| 291 | PM2.5 - non combustion - Nickel, unwrought - air | kg |
| 292 | PM2.5 - non combustion - Oil refinery - air | kg |
| 293 | PM2.5 - non combustion - Pig iron production, blast furnace - air | kg |
| 294 | PM2.5 - non combustion - Platinum ores and concentrates - air | kg |
| 295 | PM2.5 - non combustion - Primary aluminium production - air | kg |
| 296 | PM2.5 - non combustion - Production of coke oven coke - air | kg |
| 297 | PM2.5 - non combustion - Production of gascoke - air | kg |
| 298 | PM2.5 - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 299 | PM2.5 - non combustion - Refined lead, unwrought - air | kg |
| 300 | PM2.5 - non combustion - Secondary aluminium production - air | kg |
| 301 | PM2.5 - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 302 | PM2.5 - non combustion - Silver ores and concentrates - air | kg |
| 303 | PM2.5 - non combustion - Steel production: basic oxygen furnace - air | kg |
| 304 | PM2.5 - non combustion - Steel production: electric arc furnace - air | kg |
| 305 | PM2.5 - non combustion - Steel production: open hearth furnace - air | kg |
| 306 | PM2.5 - non combustion - Tin ores and concentrates - air | kg |
| 307 | PM2.5 - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 308 | PM2.5 - non combustion - Zinc ores and concentrates - air | kg |
| 309 | PM2.5 - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 310 | Pb - non combustion - Agglomeration plant - pellets - air | kg |
| 311 | Pb - non combustion - Agglomeration plant - sinter - air | kg |
| 312 | Pb - non combustion - Glass production - air | kg |
| 313 | Pb - non combustion - Nickel, unwrought - air | kg |
| 314 | Pb - non combustion - Pig iron production, blast furnace - air | kg |
| 315 | Pb - non combustion - Production of coke oven coke - air | kg |
| 316 | Pb - non combustion - Production of gascoke - air | kg |
| 317 | Pb - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 318 | Pb - non combustion - Refined lead, unwrought - air | kg |
| 319 | Pb - non combustion - Steel production: basic oxygen furnace - air | kg |
| 320 | Pb - non combustion - Steel production: electric arc furnace - air | kg |
| 321 | Pb - non combustion - Steel production: open hearth furnace - air | kg |
| 322 | Pb - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 323 | Pb - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 324 | SOx - non combustion - Agglomeration plant - sinter - air | kg |
| 325 | SOx - non combustion - Bricks production - air | kg |
| 326 | SOx - non combustion - Cement production - air | kg |
| 327 | SOx - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 328 | SOx - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 329 | SOx - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 330 | SOx - non combustion - Glass production - air | kg |
| 331 | SOx - non combustion - Lime production - air | kg |
| 332 | SOx - non combustion - Nickel, unwrought - air | kg |
| 333 | SOx - non combustion - Oil refinery - air | kg |
| 334 | SOx - non combustion - Pig iron production, blast furnace - air | kg |
| 335 | SOx - non combustion - Production of coke oven coke - air | kg |
| 336 | SOx - non combustion - Production of gascoke - air | kg |
| 337 | SOx - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 338 | SOx - non combustion - Refined lead, unwrought - air | kg |
| 339 | SOx - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 340 | SOx - non combustion - Sulphuric acid production - air | kg |
| 341 | SOx - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 342 | SOx - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 343 | Se - non combustion - Agglomeration plant - pellets - air | kg |
| 344 | Se - non combustion - Agglomeration plant - sinter - air | kg |
| 345 | Se - non combustion - Glass production - air | kg |
| 346 | Se - non combustion - Steel production: basic oxygen furnace - air | kg |
| 347 | TSP - non combustion - Agglomeration plant - pellets - air | kg |
| 348 | TSP - non combustion - Agglomeration plant - sinter - air | kg |
| 349 | TSP - non combustion - Aluminium ores and concentrates (Bauxite) - air | kg |
| 350 | TSP - non combustion - Bricks production - air | kg |
| 351 | TSP - non combustion - Briquettes production - air | kg |
| 352 | TSP - non combustion - Carbon black production - air | kg |
| 353 | TSP - non combustion - Cast iron production (grey iron foundries) - air | kg |
| 354 | TSP - non combustion - Cement production - air | kg |
| 355 | TSP - non combustion - Chemical wood pulp, dissolving grades - air | kg |
| 356 | TSP - non combustion - Chemical wood pulp, soda and sulphate, other than dissolving grades - air | kg |
| 357 | TSP - non combustion - Chemical wood pulp, sulphite, other than dissolving grades - air | kg |
| 358 | TSP - non combustion - Chromium ores and concentrates - air | kg |
| 359 | TSP - non combustion - Copper ores and concentrates - air | kg |
| 360 | TSP - non combustion - Fertilizer production (N-fertilizer) - air | kg |
| 361 | TSP - non combustion - Glass production - air | kg |
| 362 | TSP - non combustion - Gold ores and concentrates - air | kg |
| 363 | TSP - non combustion - Iron ores and concentrates - air | kg |
| 364 | TSP - non combustion - Lead ores and concentrates - air | kg |
| 365 | TSP - non combustion - Lime production - air | kg |
| 366 | TSP - non combustion - Mining of antracite - air | kg |
| 367 | TSP - non combustion - Mining of bituminous coal - air | kg |
| 368 | TSP - non combustion - Mining of coking coal - air | kg |
| 369 | TSP - non combustion - Mining of lignite (brown coal) - air | kg |
| 370 | TSP - non combustion - Mining of sub-bituminous coal - air | kg |
| 371 | TSP - non combustion - Molybdenum ores and concentrates - air | kg |
| 372 | TSP - non combustion - N- fertilizer production - air | kg |
| 373 | TSP - non combustion - Nickel ores and concentrates - air | kg |
| 374 | TSP - non combustion - Nickel, unwrought - air | kg |
| 375 | TSP - non combustion - Oil refinery - air | kg |
| 376 | TSP - non combustion - Pig iron production, blast furnace - air | kg |
| 377 | TSP - non combustion - Platinum ores and concentrates - air | kg |
| 378 | TSP - non combustion - Primary aluminium production - air | kg |
| 379 | TSP - non combustion - Production of coke oven coke - air | kg |
| 380 | TSP - non combustion - Production of gascoke - air | kg |
| 381 | TSP - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 382 | TSP - non combustion - Refined lead, unwrought - air | kg |
| 383 | TSP - non combustion - Secondary aluminium production - air | kg |
| 384 | TSP - non combustion - Semi-chemical wood pulp, pulp of fibers other than wood - air | kg |
| 385 | TSP - non combustion - Silver ores and concentrates - air | kg |
| 386 | TSP - non combustion - Steel production: basic oxygen furnace - air | kg |
| 387 | TSP - non combustion - Steel production: electric arc furnace - air | kg |
| 388 | TSP - non combustion - Steel production: open hearth furnace - air | kg |
| 389 | TSP - non combustion - Tin ores and concentrates - air | kg |
| 390 | TSP - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 391 | TSP - non combustion - Zinc ores and concentrates - air | kg |
| 392 | TSP - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 393 | Zn - non combustion - Agglomeration plant - pellets - air | kg |
| 394 | Zn - non combustion - Agglomeration plant - sinter - air | kg |
| 395 | Zn - non combustion - Glass production - air | kg |
| 396 | Zn - non combustion - Nickel, unwrought - air | kg |
| 397 | Zn - non combustion - Pig iron production, blast furnace - air | kg |
| 398 | Zn - non combustion - Refined copper; unwrought, not alloyed - air | kg |
| 399 | Zn - non combustion - Refined lead, unwrought - air | kg |
| 400 | Zn - non combustion - Steel production: basic oxygen furnace - air | kg |
| 401 | Zn - non combustion - Steel production: electric arc furnace - air | kg |
| 402 | Zn - non combustion - Steel production: open hearth furnace - air | kg |
| 403 | Zn - non combustion - Unrefined copper; copper anodes for electrolytic refining - air | kg |
| 404 | Zn - non combustion - Zinc, unwrought, not alloyed - air | kg |
| 405 | SF6 - air | kg |
| 406 | HFC - air | kg CO2-eq |
| 407 | PFC - air | kg CO2-eq |
| 408 | CH4 - agriculture - air | kg |
| 409 | CO2 - agriculture - peat decay - air | kg |
| 410 | N2O - agriculture - air | kg |
| 411 | NH3 - agriculture - air | kg |
| 412 | NOX - agriculture - air | kg |
| 413 | CH4 - waste - air | kg |
| 414 | CO - waste - air | kg |
| 415 | CO2 - waste - biogenic - air | kg |
| 416 | CO2 - waste - fossil - air | kg |
| 417 | NH3 - waste - air | kg |
| 418 | NOX - waste - air | kg |
| 419 | PM2.5 - waste - air | kg |
| 420 | SOx - waste - air | kg |

## energy

<a id="energy"></a>Total energy use at four accounting boundaries: Emission-relevant / Final / Gross / Net.

- 4 stressors · units: TJ ×4

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Energy use - Emission relevant | TJ |
| 2 | Energy use - Final | TJ |
| 3 | Energy use - Gross | TJ |
| 4 | Energy use - Net | TJ |

## material

<a id="material"></a>Domestic Extraction Used (DEU): biomass (crops, residues, grazing, wood, fish), metal ores, non-metallic minerals, fossil fuels.

- 62 stressors · units: kt ×62

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Domestic Extraction Used - Primary Crops - Rice | kt |
| 2 | Domestic Extraction Used - Primary Crops - Wheat | kt |
| 3 | Domestic Extraction Used - Primary Crops - Cereals n.e.c. | kt |
| 4 | Domestic Extraction Used - Primary Crops - Roots and tubers | kt |
| 5 | Domestic Extraction Used - Primary Crops - Pulses | kt |
| 6 | Domestic Extraction Used - Primary Crops - Nuts | kt |
| 7 | Domestic Extraction Used - Primary Crops - Vegetables | kt |
| 8 | Domestic Extraction Used - Primary Crops - Fruits | kt |
| 9 | Domestic Extraction Used - Primary Crops - Oil bearing crops | kt |
| 10 | Domestic Extraction Used - Primary Crops - Sugar crops | kt |
| 11 | Domestic Extraction Used - Primary Crops - Fibres | kt |
| 12 | Domestic Extraction Used - Primary Crops - Spice - beverage - pharmaceutical crops | kt |
| 13 | Domestic Extraction Used - Primary Crops - Tobacco | kt |
| 14 | Domestic Extraction Used - Crop residues - Straw | kt |
| 15 | Domestic Extraction Used - Crop residues - Other crop residues (sugar and fodder beet leaves etc) | kt |
| 16 | Domestic Extraction Used - Fodder crops (including biomass harvest from grassland) | kt |
| 17 | Domestic Extraction Used - Grazed biomass | kt |
| 18 | Domestic Extraction Used - Forestry - Other crops n.e.c | kt |
| 19 | Domestic Extraction Used - Forestry - Timber (Industrial roundwood) | kt |
| 20 | Domestic Extraction Used - Forestry - Wood fuel and other extraction | kt |
| 21 | Domestic Extraction Used - Fishery - Wild fish catch | kt |
| 22 | Domestic Extraction Used - Fishery - All other aquatic animals | kt |
| 23 | Domestic Extraction Used - Fishery - Aquatic plants | kt |
| 24 | Domestic Extraction Used - Fossil Fuels - Anthracite | kt |
| 25 | Domestic Extraction Used - Fossil Fuels - Coking Coal | kt |
| 26 | Domestic Extraction Used - Fossil Fuels - Other Bituminous Coal | kt |
| 27 | Domestic Extraction Used - Fossil Fuels - Other Sub-Bituminous Coal | kt |
| 28 | Domestic Extraction Used - Fossil Fuels - Lignite (brown coal) | kt |
| 29 | Domestic Extraction Used - Fossil Fuels - Peat | kt |
| 30 | Domestic Extraction Used - Fossil Fuels - Crude oil | kt |
| 31 | Domestic Extraction Used - Fossil Fuels - Oil shale and tar sands | kt |
| 32 | Domestic Extraction Used - Fossil Fuels - Natural gas | kt |
| 33 | Domestic Extraction Used - Fossil Fuels - Natural gas liquids | kt |
| 34 | Domestic Extraction Used - Metal Ores - Uranium ores | kt |
| 35 | Domestic Extraction Used - Metal Ores - Iron ores | kt |
| 36 | Domestic Extraction Used - Metal Ores - Copper ores | kt |
| 37 | Domestic Extraction Used - Metal Ores - Nickel ores | kt |
| 38 | Domestic Extraction Used - Metal Ores - Bauxite and other aluminium ores - gross ore | kt |
| 39 | Domestic Extraction Used - Metal Ores - Silver ores | kt |
| 40 | Domestic Extraction Used - Metal Ores - Gold ores | kt |
| 41 | Domestic Extraction Used - Metal Ores - Platinum group metal ores | kt |
| 42 | Domestic Extraction Used - Metal Ores - Lead ores | kt |
| 43 | Domestic Extraction Used - Metal Ores - Tin ores | kt |
| 44 | Domestic Extraction Used - Metal Ores - Zinc ores | kt |
| 45 | Domestic Extraction Used - Metal Ores - Chromium ores | kt |
| 46 | Domestic Extraction Used - Metal Ores - Manganese ores | kt |
| 47 | Domestic Extraction Used - Metal Ores - Other metal ores | kt |
| 48 | Domestic Extraction Used - Metal Ores - Titanium ores | kt |
| 49 | Domestic Extraction Used - Non-Metallic Minerals - Ornamental or building stone | kt |
| 50 | Domestic Extraction Used - Non-Metallic Minerals - Chalk | kt |
| 51 | Domestic Extraction Used - Non-Metallic Minerals - Dolomite | kt |
| 52 | Domestic Extraction Used - Non-Metallic Minerals - Limestone | kt |
| 53 | Domestic Extraction Used - Non-Metallic Minerals - Gypsum | kt |
| 54 | Domestic Extraction Used - Non-Metallic Minerals - Structural clays | kt |
| 55 | Domestic Extraction Used - Non-Metallic Minerals - Specialty clays | kt |
| 56 | Domestic Extraction Used - Non-Metallic Minerals - Industrial sand and gravel | kt |
| 57 | Domestic Extraction Used - Non-Metallic Minerals - Sand gravel and crushed rock for construction | kt |
| 58 | Domestic Extraction Used - Non-Metallic Minerals - Fertilizer minerals n.e.c. | kt |
| 59 | Domestic Extraction Used - Non-Metallic Minerals - Chemical minerals n.e.c. | kt |
| 60 | Domestic Extraction Used - Non-Metallic Minerals - Industrial minerals n.e.c | kt |
| 61 | Domestic Extraction Used - Non-Metallic Minerals - Salt | kt |
| 62 | Domestic Extraction Used - Non-Metallic Minerals - Other non-metallic minerals n.e.c. | kt |

## water

<a id="water"></a>Pattern `Water <Metric> <Colour> - Use - detail`. *Consumption* = water not returned; *Withdrawal* = abstracted (partly returned). *Green* = soil rainwater; *Blue* = surface/ground water.

- 194 stressors · units: Mm3 ×194
- By metric/colour: Water Consumption Blue (103), Water Withdrawal Blue (78), Water Consumption Green (13)
- By use: Manufacturing (106), Electricity (48), Agriculture (26), Livestock (12), Domestic (2)

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Water Consumption Green - Agriculture - rice | Mm3 |
| 2 | Water Consumption Green - Agriculture - wheat | Mm3 |
| 3 | Water Consumption Green - Agriculture - other cereals | Mm3 |
| 4 | Water Consumption Green - Agriculture - roots and tubers | Mm3 |
| 5 | Water Consumption Green - Agriculture - sugar crops | Mm3 |
| 6 | Water Consumption Green - Agriculture - pulses | Mm3 |
| 7 | Water Consumption Green - Agriculture - nuts | Mm3 |
| 8 | Water Consumption Green - Agriculture - oil crops | Mm3 |
| 9 | Water Consumption Green - Agriculture - vegetables | Mm3 |
| 10 | Water Consumption Green - Agriculture - fruits | Mm3 |
| 11 | Water Consumption Green - Agriculture - fibres | Mm3 |
| 12 | Water Consumption Green - Agriculture - other crops | Mm3 |
| 13 | Water Consumption Green - Agriculture - fodder crops | Mm3 |
| 14 | Water Consumption Blue - Agriculture - rice | Mm3 |
| 15 | Water Consumption Blue - Agriculture - wheat | Mm3 |
| 16 | Water Consumption Blue - Agriculture - other cereals | Mm3 |
| 17 | Water Consumption Blue - Agriculture - roots and tubers | Mm3 |
| 18 | Water Consumption Blue - Agriculture - sugar crops | Mm3 |
| 19 | Water Consumption Blue - Agriculture - pulses | Mm3 |
| 20 | Water Consumption Blue - Agriculture - nuts | Mm3 |
| 21 | Water Consumption Blue - Agriculture - oil crops | Mm3 |
| 22 | Water Consumption Blue - Agriculture - vegetables | Mm3 |
| 23 | Water Consumption Blue - Agriculture - fruits | Mm3 |
| 24 | Water Consumption Blue - Agriculture - fibres | Mm3 |
| 25 | Water Consumption Blue - Agriculture - other crops | Mm3 |
| 26 | Water Consumption Blue - Agriculture - fodder crops | Mm3 |
| 27 | Water Consumption Blue - Livestock - dairy cattle | Mm3 |
| 28 | Water Consumption Blue - Livestock - nondairy cattle | Mm3 |
| 29 | Water Consumption Blue - Livestock - pigs | Mm3 |
| 30 | Water Consumption Blue - Livestock - sheep | Mm3 |
| 31 | Water Consumption Blue - Livestock - goats | Mm3 |
| 32 | Water Consumption Blue - Livestock - buffaloes | Mm3 |
| 33 | Water Consumption Blue - Livestock - camels | Mm3 |
| 34 | Water Consumption Blue - Livestock - horses | Mm3 |
| 35 | Water Consumption Blue - Livestock - chicken | Mm3 |
| 36 | Water Consumption Blue - Livestock - turkeys | Mm3 |
| 37 | Water Consumption Blue - Livestock - ducks | Mm3 |
| 38 | Water Consumption Blue - Livestock - geese | Mm3 |
| 39 | Water Consumption Blue - Manufacturing - Products of meat cattle | Mm3 |
| 40 | Water Consumption Blue - Manufacturing - Products of meat pigs | Mm3 |
| 41 | Water Consumption Blue - Manufacturing - Products of meat poultry | Mm3 |
| 42 | Water Consumption Blue - Manufacturing - Meat products nec | Mm3 |
| 43 | Water Consumption Blue - Manufacturing - products of Vegetable oils and fats | Mm3 |
| 44 | Water Consumption Blue - Manufacturing - Dairy products | Mm3 |
| 45 | Water Consumption Blue - Manufacturing - Processed rice | Mm3 |
| 46 | Water Consumption Blue - Manufacturing - Sugar | Mm3 |
| 47 | Water Consumption Blue - Manufacturing - Food products nec | Mm3 |
| 48 | Water Consumption Blue - Manufacturing - Beverages | Mm3 |
| 49 | Water Consumption Blue - Manufacturing - Fish products | Mm3 |
| 50 | Water Consumption Blue - Manufacturing - Tobacco products (16) | Mm3 |
| 51 | Water Consumption Blue - Manufacturing - Textiles (17) | Mm3 |
| 52 | Water Consumption Blue - Manufacturing - Wearing apparel; furs (18) | Mm3 |
| 53 | Water Consumption Blue - Manufacturing - Leather and leather products (19) | Mm3 |
| 54 | Water Consumption Blue - Manufacturing - Pulp | Mm3 |
| 55 | Water Consumption Blue - Manufacturing - Secondary paper for treatment, Re-processing of secondary paper into new pulp | Mm3 |
| 56 | Water Consumption Blue - Manufacturing - Paper and paper products | Mm3 |
| 57 | Water Consumption Blue - Manufacturing - Printed matter and recorded media (22) | Mm3 |
| 58 | Water Consumption Blue - Manufacturing - Plastics, basic | Mm3 |
| 59 | Water Consumption Blue - Manufacturing - Secondary plastic for treatment, Re-processing of secondary plastic into new plastic | Mm3 |
| 60 | Water Consumption Blue - Manufacturing - N-fertiliser | Mm3 |
| 61 | Water Consumption Blue - Manufacturing - P- and other fertiliser | Mm3 |
| 62 | Water Consumption Blue - Manufacturing - Chemicals nec | Mm3 |
| 63 | Water Consumption Blue - Manufacturing - Rubber and plastic products (25) | Mm3 |
| 64 | Water Consumption Blue - Manufacturing - Glass and glass products | Mm3 |
| 65 | Water Consumption Blue - Manufacturing - Secondary glass for treatment, Re-processing of secondary glass into new glass | Mm3 |
| 66 | Water Consumption Blue - Manufacturing - Ceramic goods | Mm3 |
| 67 | Water Consumption Blue - Manufacturing - Bricks, tiles and construction products, in baked clay | Mm3 |
| 68 | Water Consumption Blue - Manufacturing - Cement, lime and plaster | Mm3 |
| 69 | Water Consumption Blue - Manufacturing - Ash for treatment, Re-processing of ash into clinker | Mm3 |
| 70 | Water Consumption Blue - Manufacturing - Other non-metallic mineral products | Mm3 |
| 71 | Water Consumption Blue - Manufacturing - Basic iron and steel and of ferro-alloys and first products thereof | Mm3 |
| 72 | Water Consumption Blue - Manufacturing - Secondary steel for treatment, Re-processing of secondary steel into new steel | Mm3 |
| 73 | Water Consumption Blue - Manufacturing - Precious metals | Mm3 |
| 74 | Water Consumption Blue - Manufacturing - Secondary preciuos metals for treatment, Re-processing of secondary preciuos metals into new preciuos metals | Mm3 |
| 75 | Water Consumption Blue - Manufacturing - Aluminium and aluminium products | Mm3 |
| 76 | Water Consumption Blue - Manufacturing - Secondary aluminium for treatment, Re-processing of secondary aluminium into new aluminium | Mm3 |
| 77 | Water Consumption Blue - Manufacturing - Lead, zinc and tin and products thereof | Mm3 |
| 78 | Water Consumption Blue - Manufacturing - Secondary lead for treatment, Re-processing of secondary lead into new lead | Mm3 |
| 79 | Water Consumption Blue - Manufacturing - Copper products | Mm3 |
| 80 | Water Consumption Blue - Manufacturing - Secondary copper for treatment, Re-processing of secondary copper into new copper | Mm3 |
| 81 | Water Consumption Blue - Manufacturing - Other non-ferrous metal products | Mm3 |
| 82 | Water Consumption Blue - Manufacturing - Secondary other non-ferrous metals for treatment, Re-processing of secondary other non-ferrous metals into new other non-ferrous metals | Mm3 |
| 83 | Water Consumption Blue - Manufacturing - Fabricated metal products, except machinery and equipment (28) | Mm3 |
| 84 | Water Consumption Blue - Manufacturing - Machinery and equipment n.e.c. (29) | Mm3 |
| 85 | Water Consumption Blue - Manufacturing - Office machinery and computers (30) | Mm3 |
| 86 | Water Consumption Blue - Manufacturing - Electrical machinery and apparatus n.e.c. (31) | Mm3 |
| 87 | Water Consumption Blue - Manufacturing - Radio, television and communication equipment and apparatus (32) | Mm3 |
| 88 | Water Consumption Blue - Manufacturing - Medical, precision and optical instruments, watches and clocks (33) | Mm3 |
| 89 | Water Consumption Blue - Manufacturing - Motor vehicles, trailers and semi-trailers (34) | Mm3 |
| 90 | Water Consumption Blue - Manufacturing - Other transport equipment (35) | Mm3 |
| 91 | Water Consumption Blue - Manufacturing - Furniture; other manufactured goods n.e.c. (36) | Mm3 |
| 92 | Water Consumption Blue - Electricity - tower - Electricity by coal | Mm3 |
| 93 | Water Consumption Blue - Electricity - tower - Electricity by gas | Mm3 |
| 94 | Water Consumption Blue - Electricity - tower - Electricity by nuclear | Mm3 |
| 95 | Water Consumption Blue - Electricity - tower - Electricity by hydro | Mm3 |
| 96 | Water Consumption Blue - Electricity - tower - Electricity by wind | Mm3 |
| 97 | Water Consumption Blue - Electricity - tower - Electricity by petroleum and other oil derivatives | Mm3 |
| 98 | Water Consumption Blue - Electricity - tower - Electricity by biomass and waste | Mm3 |
| 99 | Water Consumption Blue - Electricity - tower - Electricity by solar photovoltaic | Mm3 |
| 100 | Water Consumption Blue - Electricity - tower - Electricity by solar thermal | Mm3 |
| 101 | Water Consumption Blue - Electricity - tower - Electricity by tide, wave, ocean | Mm3 |
| 102 | Water Consumption Blue - Electricity - tower - Electricity by Geothermal | Mm3 |
| 103 | Water Consumption Blue - Electricity - tower - Electricity nec | Mm3 |
| 104 | Water Consumption Blue - Electricity - once-through - Electricity by coal | Mm3 |
| 105 | Water Consumption Blue - Electricity - once-through - Electricity by gas | Mm3 |
| 106 | Water Consumption Blue - Electricity - once-through - Electricity by nuclear | Mm3 |
| 107 | Water Consumption Blue - Electricity - once-through - Electricity by hydro | Mm3 |
| 108 | Water Consumption Blue - Electricity - once-through - Electricity by wind | Mm3 |
| 109 | Water Consumption Blue - Electricity - once-through - Electricity by petroleum and other oil derivatives | Mm3 |
| 110 | Water Consumption Blue - Electricity - once-through - Electricity by biomass and waste | Mm3 |
| 111 | Water Consumption Blue - Electricity - once-through - Electricity by solar photovoltaic | Mm3 |
| 112 | Water Consumption Blue - Electricity - once-through - Electricity by solar thermal | Mm3 |
| 113 | Water Consumption Blue - Electricity - once-through - Electricity by tide, wave, ocean | Mm3 |
| 114 | Water Consumption Blue - Electricity - once-through - Electricity by Geothermal | Mm3 |
| 115 | Water Consumption Blue - Electricity - once-through - Electricity nec | Mm3 |
| 116 | Water Consumption Blue - Domestic - domestic Water Consumption Blue | Mm3 |
| 117 | Water Withdrawal Blue - Manufacturing - Products of meat cattle | Mm3 |
| 118 | Water Withdrawal Blue - Manufacturing - Products of meat pigs | Mm3 |
| 119 | Water Withdrawal Blue - Manufacturing - Products of meat poultry | Mm3 |
| 120 | Water Withdrawal Blue - Manufacturing - Meat products nec | Mm3 |
| 121 | Water Withdrawal Blue - Manufacturing - products of Vegetable oils and fats | Mm3 |
| 122 | Water Withdrawal Blue - Manufacturing - Dairy products | Mm3 |
| 123 | Water Withdrawal Blue - Manufacturing - Processed rice | Mm3 |
| 124 | Water Withdrawal Blue - Manufacturing - Sugar | Mm3 |
| 125 | Water Withdrawal Blue - Manufacturing - Food products nec | Mm3 |
| 126 | Water Withdrawal Blue - Manufacturing - Beverages | Mm3 |
| 127 | Water Withdrawal Blue - Manufacturing - Fish products | Mm3 |
| 128 | Water Withdrawal Blue - Manufacturing - Tobacco products (16) | Mm3 |
| 129 | Water Withdrawal Blue - Manufacturing - Textiles (17) | Mm3 |
| 130 | Water Withdrawal Blue - Manufacturing - Wearing apparel; furs (18) | Mm3 |
| 131 | Water Withdrawal Blue - Manufacturing - Leather and leather products (19) | Mm3 |
| 132 | Water Withdrawal Blue - Manufacturing - Pulp | Mm3 |
| 133 | Water Withdrawal Blue - Manufacturing - Secondary paper for treatment, Re-processing of secondary paper into new pulp | Mm3 |
| 134 | Water Withdrawal Blue - Manufacturing - Paper and paper products | Mm3 |
| 135 | Water Withdrawal Blue - Manufacturing - Printed matter and recorded media (22) | Mm3 |
| 136 | Water Withdrawal Blue - Manufacturing - Plastics, basic | Mm3 |
| 137 | Water Withdrawal Blue - Manufacturing - Secondary plastic for treatment, Re-processing of secondary plastic into new plastic | Mm3 |
| 138 | Water Withdrawal Blue - Manufacturing - N-fertiliser | Mm3 |
| 139 | Water Withdrawal Blue - Manufacturing - P- and other fertiliser | Mm3 |
| 140 | Water Withdrawal Blue - Manufacturing - Chemicals nec | Mm3 |
| 141 | Water Withdrawal Blue - Manufacturing - Rubber and plastic products (25) | Mm3 |
| 142 | Water Withdrawal Blue - Manufacturing - Glass and glass products | Mm3 |
| 143 | Water Withdrawal Blue - Manufacturing - Secondary glass for treatment, Re-processing of secondary glass into new glass | Mm3 |
| 144 | Water Withdrawal Blue - Manufacturing - Ceramic goods | Mm3 |
| 145 | Water Withdrawal Blue - Manufacturing - Bricks, tiles and construction products, in baked clay | Mm3 |
| 146 | Water Withdrawal Blue - Manufacturing - Cement, lime and plaster | Mm3 |
| 147 | Water Withdrawal Blue - Manufacturing - Ash for treatment, Re-processing of ash into clinker | Mm3 |
| 148 | Water Withdrawal Blue - Manufacturing - Other non-metallic mineral products | Mm3 |
| 149 | Water Withdrawal Blue - Manufacturing - Basic iron and steel and of ferro-alloys and first products thereof | Mm3 |
| 150 | Water Withdrawal Blue - Manufacturing - Secondary steel for treatment, Re-processing of secondary steel into new steel | Mm3 |
| 151 | Water Withdrawal Blue - Manufacturing - Precious metals | Mm3 |
| 152 | Water Withdrawal Blue - Manufacturing - Secondary preciuos metals for treatment, Re-processing of secondary preciuos metals into new preciuos metals | Mm3 |
| 153 | Water Withdrawal Blue - Manufacturing - Aluminium and aluminium products | Mm3 |
| 154 | Water Withdrawal Blue - Manufacturing - Secondary aluminium for treatment, Re-processing of secondary aluminium into new aluminium | Mm3 |
| 155 | Water Withdrawal Blue - Manufacturing - Lead, zinc and tin and products thereof | Mm3 |
| 156 | Water Withdrawal Blue - Manufacturing - Secondary lead for treatment, Re-processing of secondary lead into new lead | Mm3 |
| 157 | Water Withdrawal Blue - Manufacturing - Copper products | Mm3 |
| 158 | Water Withdrawal Blue - Manufacturing - Secondary copper for treatment, Re-processing of secondary copper into new copper | Mm3 |
| 159 | Water Withdrawal Blue - Manufacturing - Other non-ferrous metal products | Mm3 |
| 160 | Water Withdrawal Blue - Manufacturing - Secondary other non-ferrous metals for treatment, Re-processing of secondary other non-ferrous metals into new other non-ferrous metals | Mm3 |
| 161 | Water Withdrawal Blue - Manufacturing - Fabricated metal products, except machinery and equipment (28) | Mm3 |
| 162 | Water Withdrawal Blue - Manufacturing - Machinery and equipment n.e.c. (29) | Mm3 |
| 163 | Water Withdrawal Blue - Manufacturing - Office machinery and computers (30) | Mm3 |
| 164 | Water Withdrawal Blue - Manufacturing - Electrical machinery and apparatus n.e.c. (31) | Mm3 |
| 165 | Water Withdrawal Blue - Manufacturing - Radio, television and communication equipment and apparatus (32) | Mm3 |
| 166 | Water Withdrawal Blue - Manufacturing - Medical, precision and optical instruments, watches and clocks (33) | Mm3 |
| 167 | Water Withdrawal Blue - Manufacturing - Motor vehicles, trailers and semi-trailers (34) | Mm3 |
| 168 | Water Withdrawal Blue - Manufacturing - Other transport equipment (35) | Mm3 |
| 169 | Water Withdrawal Blue - Manufacturing - Furniture; other manufactured goods n.e.c. (36) | Mm3 |
| 170 | Water Withdrawal Blue - Electricity - tower - Electricity by coal | Mm3 |
| 171 | Water Withdrawal Blue - Electricity - tower - Electricity by gas | Mm3 |
| 172 | Water Withdrawal Blue - Electricity - tower - Electricity by nuclear | Mm3 |
| 173 | Water Withdrawal Blue - Electricity - tower - Electricity by hydro | Mm3 |
| 174 | Water Withdrawal Blue - Electricity - tower - Electricity by wind | Mm3 |
| 175 | Water Withdrawal Blue - Electricity - tower - Electricity by petroleum and other oil derivatives | Mm3 |
| 176 | Water Withdrawal Blue - Electricity - tower - Electricity by biomass and waste | Mm3 |
| 177 | Water Withdrawal Blue - Electricity - tower - Electricity by solar photovoltaic | Mm3 |
| 178 | Water Withdrawal Blue - Electricity - tower - Electricity by solar thermal | Mm3 |
| 179 | Water Withdrawal Blue - Electricity - tower - Electricity by tide, wave, ocean | Mm3 |
| 180 | Water Withdrawal Blue - Electricity - tower - Electricity by Geothermal | Mm3 |
| 181 | Water Withdrawal Blue - Electricity - tower - Electricity nec | Mm3 |
| 182 | Water Withdrawal Blue - Electricity - once-through - Electricity by coal | Mm3 |
| 183 | Water Withdrawal Blue - Electricity - once-through - Electricity by gas | Mm3 |
| 184 | Water Withdrawal Blue - Electricity - once-through - Electricity by nuclear | Mm3 |
| 185 | Water Withdrawal Blue - Electricity - once-through - Electricity by hydro | Mm3 |
| 186 | Water Withdrawal Blue - Electricity - once-through - Electricity by wind | Mm3 |
| 187 | Water Withdrawal Blue - Electricity - once-through - Electricity by petroleum and other oil derivatives | Mm3 |
| 188 | Water Withdrawal Blue - Electricity - once-through - Electricity by biomass and waste | Mm3 |
| 189 | Water Withdrawal Blue - Electricity - once-through - Electricity by solar photovoltaic | Mm3 |
| 190 | Water Withdrawal Blue - Electricity - once-through - Electricity by solar thermal | Mm3 |
| 191 | Water Withdrawal Blue - Electricity - once-through - Electricity by tide, wave, ocean | Mm3 |
| 192 | Water Withdrawal Blue - Electricity - once-through - Electricity by Geothermal | Mm3 |
| 193 | Water Withdrawal Blue - Electricity - once-through - Electricity nec | Mm3 |
| 194 | Water Withdrawal Blue - Domestic - domestic Water Withdrawal Blue | Mm3 |

## land

<a id="land"></a>Land occupation by type: artificial surfaces, cropland (per crop), pasture, forest, etc.

- 26 stressors · units: km2 ×26

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Artificial Surfaces | km2 |
| 2 | Cropland - cropped area - Cereal grains nec | km2 |
| 3 | Cropland - cropped area - Crops nec | km2 |
| 4 | Cropland - cropped area - Oil seeds | km2 |
| 5 | Cropland - cropped area - Paddy rice | km2 |
| 6 | Cropland - cropped area - Plant-based fibers | km2 |
| 7 | Cropland - cropped area - Sugar cane, sugar beet | km2 |
| 8 | Cropland - cropped area - Vegetables, fruit, nuts | km2 |
| 9 | Cropland - cropped area - Wheat | km2 |
| 10 | Cropland - fallowed area - Cereal grains nec | km2 |
| 11 | Cropland - fallowed area - Crops nec | km2 |
| 12 | Cropland - fallowed area - Oil seeds | km2 |
| 13 | Cropland - fallowed area - Paddy rice | km2 |
| 14 | Cropland - fallowed area - Plant-based fibers | km2 |
| 15 | Cropland - fallowed area - Sugar cane, sugar beet | km2 |
| 16 | Cropland - fallowed area - Vegetables, fruit, nuts | km2 |
| 17 | Cropland - fallowed area - Wheat | km2 |
| 18 | Cropland - fallowed area-Cattle | km2 |
| 19 | Cropland - fallowed area-Meat animals nec | km2 |
| 20 | Cropland - fallowed area-Pigs | km2 |
| 21 | Cropland - fallowed area-Poultry | km2 |
| 22 | Cropland - fallowed area-Raw milk | km2 |
| 23 | Forest | km2 |
| 24 | Permanent pastures - Grazing-Cattle | km2 |
| 25 | Permanent pastures - Grazing-Meat animals nec | km2 |
| 26 | Permanent pastures - Grazing-Raw milk | km2 |

## nutrients

<a id="nutrients"></a>Nitrogen (N) and phosphorus (P) releases to soil and water (agriculture).

- 6 stressors · units: kg ×6

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | N - agriculture - water | kg |
| 2 | P - agriculture - soil | kg |
| 3 | P - agriculture - water | kg |
| 4 | Pxx - agriculture - soil | kg |
| 5 | N - waste - water | kg |
| 6 | P - waste - water | kg |

## factor_inputs

<a id="factor_inputs"></a>Monetary value-added components: taxes less subsidies on products, other net taxes on production, compensation of employees (by skill), operating surplus & mixed income.

- 9 stressors · units: M.EUR ×9

| # | Stressor | Unit |
| ---: | --- | --- |
| 1 | Taxes less subsidies on products purchased: Total | M.EUR |
| 2 | Other net taxes on production | M.EUR |
| 3 | Compensation of employees; wages, salaries, & employers' social contributions: Low-skilled | M.EUR |
| 4 | Compensation of employees; wages, salaries, & employers' social contributions: Medium-skilled | M.EUR |
| 5 | Compensation of employees; wages, salaries, & employers' social contributions: High-skilled | M.EUR |
| 6 | Operating surplus: Consumption of fixed capital | M.EUR |
| 7 | Operating surplus: Rents on land | M.EUR |
| 8 | Operating surplus: Royalties on resources | M.EUR |
| 9 | Operating surplus: Remaining net operating surplus | M.EUR |
