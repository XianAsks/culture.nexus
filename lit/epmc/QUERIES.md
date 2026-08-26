# Europe PMC — query log

Run 2026-08-23. The Europe PMC API does **not** echo the query, so the text
below is transcribed from the invoking commands. `OPEN_ACCESS:y` is appended
automatically by the skill to every query. Raw responses in `queries/`.

| # | Query | Hits |
|---|---|---|
| `20-thukdam` | `thukdam OR "post-mortem meditation" OR "meditative state after death" Tibetan` | 2310 |
| `21-tarim` | `Tarim Basin mummies genomic Bronze Age` | 7 |
| `22-tibet-adapt` | `EPAS1 Denisovan Tibetan high altitude adaptation` | 69 |
| `23-tibet-people` | `peopling Tibetan Plateau archaeology ancient DNA` | 12 |
| `24-silkroad-dna` | `ancient DNA Silk Road Central Asia population history` | 335 |
| `25-mummify` | `self-mummification sokushinbutsu Buddhist mummy preservation` | **0** |
| `26-relics` | `radiocarbon dating relics saint authentication` | **0** |
| `27-thukdam2` | `TITLE:thukdam` | **0** |
| `28-postmortem` | `TITLE:"postmortem meditation" OR TITLE:"post-mortem meditative"` | 3 |
| `29-monks-eeg` | `TITLE:meditation AND TITLE:Tibetan AND TITLE:monks` | 1 |
| `30-mummy` | `TITLE:mummification AND (Buddhist OR monk OR ascetic)` | **0** |
| `31-xiaohe` | `Xiaohe cemetery Tarim mitochondrial DNA` | 9 |
| `32-anthro` | `TITLE:archaeology AND (Tibet OR Xinjiang OR "Central Asia")` | 8 |
| `33-contempl` | `contemplative practitioners death dying Tibetan Buddhist monastery` | 4 |
| `34-eeg-death` | `TITLE:"clinical death" OR TITLE:"brain death" meditation practitioners` | 7704 |
| `35-mummies-gen` | `mummy ancient DNA preservation archaeology Asia` | 35 |

## Zero-hit queries — negative results

Recorded per `methods.md` §7.

- `25-mummify` — `self-mummification sokushinbutsu Buddhist mummy preservation`
- `26-relics` — `radiocarbon dating relics saint authentication`
- `27-thukdam2` — `TITLE:thukdam`
- `30-mummy` — `TITLE:mummification AND (Buddhist OR monk OR ascetic)`

## Queries that returned hits but no usable results

Broad boolean queries where the engine ignored the intended scoping and returned
high-volume clinical noise. Retained as evidence of method, not as findings.

- `20-thukdam` (2310 hits) — boolean swallowed; superseded by `27-thukdam2`, `28-postmortem`
- `34-eeg-death` (7704 hits) — same failure mode
- `24-silkroad-dna` (335 hits) — returned epidemiology, not population history
