# Smoke report — 2026-09-26

Each file is loaded in a headless browser (jsdom): the page must initialise without a JavaScript error, expose a title and interactive controls. Rendering-only APIs absent from the test browser (canvas, WebGL, matchMedia) are not counted as errors.

| Game | File | Controls | Size | Result |
|---|---|---|---|---|
| Surhomme Quantique — Raison d'État (FR) | `Surhomme_Quantique_RAISON_DETAT_V2_1.html` | 21 | 7450 KB | ✓ loads |
| Quantum Übermensch — Reason of State (EN) | `Surhomme_Quantique_REASON_OF_STATE_V2_1_EN.html` | 21 | 7443 KB | ✓ loads |
| Soirée Surhomme (FR) | `Soiree_Surhomme_Quantique_V1.html` | 6 | 1740 KB | ✓ loads |
| Quantum Übermensch Night (EN) | `Quantum_Ubermensch_Night_V1_EN.html` | 6 | 1739 KB | ✓ loads |
| Axiom 12 (FR) | `AXIOM12_V5_PRODUCTION.html` | 17 | 4491 KB | ✓ loads |
| Axiom 12 (EN) | `AXIOM12_V5_PRODUCTION_EN.html` | 17 | 4491 KB | ✓ loads |
| Delta Pyramid (FR) | `DELTA_PYRAMID_V2_MASTER.html` | 21 | 3681 KB | ✓ loads |
| Delta Pyramid (EN) | `DELTA_PYRAMID_V2_MASTER_EN.html` | 21 | 3681 KB | ✓ loads |
| Dialyrium (FR) | `DIALYRIUM_V1_1.html` | 7 | 3770 KB | ✓ loads |
| Dialyrium (EN) | `DIALYRIUM_V1_1_EN.html` | 7 | 3770 KB | ✓ loads |
| Noumenara (FR) | `NOUMENARA_V1_0_SYMPHONIE.html` | 18 | 4315 KB | ✓ loads |
| Noumenara (EN) | `NOUMENARA_V1_0_SYMPHONY_EN.html` | 18 | 4314 KB | ✓ loads |
| Quantum Chess (FR) | `QUANTUM_CHESS_EDITION_JOUEUR_V2_1.html` | 5 | 2045 KB | ✓ loads |
| Quantum Chess (EN) | `QUANTUM_CHESS_PLAYER_EDITION_V2_1_EN.html` | 5 | 2722 KB | ✓ loads |
| Arca Vitae (FR) | `ARCA_VITAE_V1_1.html` | 13 | 1976 KB | ✓ loads |
| Arca Vitae (EN) | `ARCA_VITAE_V1_1_EN.html` | 13 | 1975 KB | ✓ loads |
| Corpus Futurum (FR) | `CORPUS_FUTURUM_V1_1_ATELIER.html` | 14 | 7387 KB | ✓ loads |
| Corpus Futurum (EN) | `CORPUS_FUTURUM_V1_1_WORKSHOP_EN.html` | 14 | 7386 KB | ✓ loads |
| Hodarium (FR) | `HODARIUM_V1_1.html` | 7 | 5580 KB | ✓ loads |
| Hodarium (EN) | `HODARIUM_V1_1_EN.html` | 7 | 5580 KB | ✓ loads |
| Devenium (FR) | `DEVENIUM_V1_1.html` | 4 | 4773 KB | ✓ loads |
| Devenium (EN) | `DEVENIUM_V1_1_EN.html` | 4 | 4772 KB | ✓ loads |
| Q Spectrum (FR) | `Q_SPECTRUM_HTML_V3_QUANTUM_EXCELLIUM.html` | 21 | 1215 KB | ✓ loads |
| Q Spectrum (EN) | `Q_SPECTRUM_HTML_V3_EN_QUANTUM_EXCELLIUM.html` | 21 | 1212 KB | ✓ loads |
| Morpheus — Les Trois Ubiquités (FR) | `MORPHEUS_V3_LES_TROIS_UBIQUITES.html` | 30 | 2249 KB | ✓ loads |
| Ludonirium (FR/EN) | `LUDONIRIUM_DEMO_SANCTUAIRE_DES_DOUZE_FR_EN.html` | 10 | 7517 KB | ✓ loads |
| Parcivium (FR) | `PARCIVIUM_DEMO.html` | 16 | 1161 KB | ✓ loads |
| Parcivium (EN) | `PARCIVIUM_DEMO_EN.html` | 16 | 1161 KB | ✓ loads |
| Syngnosium (FR) | `SYNGNOSIUM_DEMO.html` | 18 | 1518 KB | ✓ loads |
| Syngnosium (EN) | `SYNGNOSIUM_DEMO_EN.html` | 18 | 1517 KB | ✓ loads |

**30 / 30 files load cleanly.** Deeper playthrough tests exist for Syngnosium, Parcivium, Devenium, Hodarium, Ludonirium and Dialyrium (full sessions driven programmatically, journals verified).
