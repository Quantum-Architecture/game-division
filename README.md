[![CI](https://github.com/Quantum-Architecture/game-division/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/Quantum-Architecture/game-division/actions/workflows/verify.yml)

# Game Division — sixteen interactive worlds
**Quantum Excellium Marango.** Serious games and philosophical worlds, each delivered as **one self-contained HTML file**: playable offline, no account, no data transmitted, with a chained journal that attests the integrity of every session.

## The collection
| # | World | Theme | Languages |
|---|---|---|---|
| 1 | Quantum Übermensch — Enterprise | leadership, transformation, responsibility | FR · EN |
| 2 | Quantum Übermensch — Statecraft | power, strategy, reason of state | FR · EN |
| 3 | Quantum Übermensch — Night Edition | choice, confrontation, creativity | FR · EN |
| 4 | Q Spectrum | observe, superpose, decide — a strategic decision chamber | FR · EN |
| 5 | Onyrium — The Three Ubiquities | memory, absence, timelines | FR |
| 6 | Entropy & Resilience Lab | complexity, resources, resilience | FR |
| 7 | Quantum Fitness | effort, will, progression | FR |
| 8 | Axiom 12 | arithmetic, geometry, proportions — six mathematical worlds | FR · EN |
| 9 | Delta Pyramid | volatility, risk, rebalancing on synthetic markets | FR · EN |
| 10 | Noumenara | music, colour, philosophy — a playable symphony | FR · EN |
| 11 | Corpus Futurum | biology, augmentation, ethics | FR · EN |
| 12 | Arca Vitae | preserve, adapt, let evolve | FR · EN |
| 13 | Dialyrium | thesis, antithesis, synthesis — a Hegelian fashion museum | FR · EN |
| 14 | Hodarium — The Motionless Journey | places, fates, a sealed story | FR · EN |
| 15 | Devenium | Leibniz's world of possibles | FR · EN |
| 16 | Quantum Chess | energy, fields, multiple strategies | FR · EN |

Playable demos for every world: **Simulations** on [quantumexcellium.com](https://quantumexcellium.com).

## Proofs
- `preuves/SMOKE_REPORT.md` + `preuves/smoke_result.json` — published evidence from the headless smoke campaign: files loaded without recorded JavaScript errors, with title and controls present. The public CI validates the evidence structure and the smoke harness syntax; it does **not** re-run product HTML files because those files are not committed in this repository.
- Deeper playthrough tests drive full sessions programmatically for Syngnosium, Parcivium, Devenium, Hodarium, Ludonirium and Dialyrium, and verify their journals.
- Every game exports its session as a chained journal; the public verifier is [ledger-verify](https://github.com/Quantum-Architecture/ledger-verify).

## What is, and is not, in this repository
Here: the catalogue, the test methodology and its results. Not here: the games' source files, which are the product (personal, collector and B2B editions — see the site). Philosophical worlds are allegories, not courses; business simulations are training tools, not advice.
