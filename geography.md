# geography.md — places, regions and polities

Companion index to `chronology.md`. One schema on two axes: **chronology indexes time, geography
indexes place**, and both carry entity identity, a period, and an evidential tag. Notation is
specified once, in `chronology.md` §2, and binds both files.

Decided `methods.md` §9.2 item 6 · created 2026-08-27 · rev. 1

---

## 1. Why this file exists

Q8 is a question about contact zones; H9's typology is about channels between places; the nexus
material (`background.md` §5.3) is indexed by site before it is indexed by date. Place was already
doing the work — it just had nowhere to live.

The register's `#d/` domain facet is not a substitute. `#d/central-asia` groups sources; this file
identifies *entities*, so that two entries about Gandhāra are known to be about the same Gandhāra,
and so that the duration table has something to count.

## 2. Entity identity: the Wikidata Q-id

**Every entity carries a Q-id, and the Q-id is the key — not the name.**

Gandhāra, Bactria and Sogdia change name, language and extent across the period this project
covers. Bāmiyān is Bamyan is Bamian; Begram is Bagram; Khotan is Hotan; Turfan is Turpan. A file
keyed on names accumulates duplicates that look like distinct places, which is precisely the error
this project exists to detect in other domains.

The Q-id is language-independent, survives renaming, and is the join key to any other
Wikidata-linked dataset. Q-ids below were retrieved with the `/wikipedia` skill
(`page --fields coordinates,wikidata`) on 2026-08-27.

> **The Q-id identifies the entity, not the claim.** That a Q-id is recorded says nothing about
> whether any assertion here is true. Evidential tags do that work, as everywhere else.

## 3. Three object types, because the data has three

`methods.md` §9.2 anticipated two — sites and polities — on the ground that a site has coordinates
while a polity has shifting borders and a lifespan. Populating the file forced a third.

| Type | Has | Lacks | Example |
|---|---|---|---|
| **site** | a point coordinate | a lifespan of its own | Taxila, Dunhuang |
| **region** | a representative coordinate, but a fuzzy and contested extent | a boundary that would make the coordinate mean what it means for a site | Gandhāra, Sogdia |
| **polity** | a lifespan, a claim to territory | a single coordinate | Kushan Empire |

**Regions are the trap.** A region gets a coordinate from the API exactly as a site does, and the
number looks identical. It does not mean the same thing: Gandhāra's `33.756, 72.829` is a
centroid-ish gesture at a contested extent, and treating it as a location is the kind of false
precision the project's own §5 ladder is built to resist. Regions are therefore marked, and their
coordinates are flagged `~`.

**Sites and polities must not be conflated in counting.** The duration table counts polities. A
site has no lifespan to contribute, and mixing the two would quietly measure two different things —
which matters because `background.md` §5.3 leans on that table.

---

## 4. Places — sites and regions

`rel` is period of relevance *to this project*, not the entity's full existence. `~` on a
coordinate marks a region centroid rather than a location.

| id | name | kind | qid | lat | lon | modern | rel | tag | bears-on |
|---|---|---|---|---|---|---|---|---|---|
| gandhara | Gandhāra | region | Q213651 | ~33.756 | ~72.829 | PK/AF | [c. 500 BCE–c. 1000 CE] | `#e/attested` | Q8, H5, H7 |
| taxila | Taxila | site | Q156093 | 33.7458 | 72.7875 | PK | [c. 500 BCE–c. 500 CE] | `#e/attested` | Q8 |
| bagram | Bagram (Begram) | site | Q814388 | 34.9403 | 69.2550 | AF | [c. 100 BCE–c. 300 CE] | `#e/attested` | Q8, H7 |
| bamyan | Bāmiyān | site | Q214495 | 34.8250 | 67.8333 | AF | [c. 500–c. 900 CE] | `#e/attested` | Q8, H5 |
| dunhuang | Dunhuang | site | Q319114 | 40.1411 | 94.6639 | CN | [c. 400–c. 1000 CE] | `#e/attested` | Q8a, H7 |
| turpan | Turpan | site | Q868527 | 42.9512 | 89.1895 | CN | [c. 400–c. 900 CE] | `#e/unverified` | Q8a |
| kucha | Kucha | site | Q1328546 | 41.7156 | 82.9322 | CN | [c. 300–c. 800 CE] | `#e/unverified` | Q8a |
| hotan | Hotan (Khotan) | site | Q235389 | 37.1172 | 79.9344 | CN | [c. 200–c. 1000 CE] | `#e/unverified` | Q8a |
| sogdia | Sogdia | region | Q486244 | ~40.400 | ~69.400 | UZ/TJ | [c. 500 BCE–c. 800 CE] | `#e/attested` | H9, H11 |
| samarkand | Samarkand | site | Q5753 | 39.6506 | 66.9653 | UZ | [c. 700 BCE–present] | `#e/attested` | Q8, H11 |
| merv | Merv | site | Q193325 | 37.6628 | 62.1925 | TM | [c. 500 BCE–c. 1300 CE] | `#e/unverified` | Q8, H5 |
| palmyra | Palmyra | site | Q5747 | 34.5514 | 38.2681 | SY | [c. 100 BCE–c. 300 CE] | `#e/attested` | Q8 |
| ctesiphon | Ctesiphon | site | Q192541 | 33.0936 | 44.5806 | IQ | [c. 100 BCE–c. 650 CE] | `#e/unverified` | H5 |
| baghdad | Baghdad | site | Q1530 | 33.3153 | 44.3661 | IQ | [762 CE–present] | `#e/attested` | §14.8, H5 |
| alexandria | Alexandria | site | Q87 | 31.1975 | 29.8925 | EG | [c. 331 BCE–present] | `#e/attested` | Q8, §14.6 |
| aksum | Aksum (kingdom seat) | site | Q139377 | — | — | ET/ER | [c. 100–c. 960 CE] | `#e/unverified` | Q8 |
| constantinople | Constantinople | site | Q16869 | 41.0125 | 28.9800 | TR | [330 CE–present] | `#e/attested` | §14.8 |
| athos | Mount Athos | site | Q130321 | 40.1583 | 24.3272 | GR | [c. 900 CE–present] | `#e/attested` | §14.8 |
| florence | Florence | site | Q2044 | 43.7714 | 11.2542 | IT | [c. 1100–c. 1600 CE] | `#e/attested` | Q8, §11.4 |
| venice | Venice | site | Q641 | 45.4375 | 12.3358 | IT | [c. 700–1797 CE] | `#e/attested` | §14.8 |

? **Aksum has no coordinate** from the retrieval — the article resolved to the kingdom, not the
city. Needs the site's own Q-id if Aksum is to enter the comparison class as a place.

## 5. Polities — the comparison class

`from`/`to` are the entity's own lifespan. **Source for every row: the `{{Infobox}}`
`year_start`/`year_end` fields of the corresponding English Wikipedia article, parsed 2026-08-27.**
That is a tertiary source, so every row is `#e/unverified` until checked against scholarship —
see §7. Durations are *not* stored here; they are derived by `scripts/build_tables.py`, so that
the arithmetic has exactly one home.

| id | name | qid | from | to | tag | note |
|---|---|---|---|---|---|---|
| achaemenid | Achaemenid Empire | Q389688 | 550 BCE | 330 BCE | `#e/unverified` | H5's Iranian substrate |
| greco-bactrian | Greco-Bactrian Kingdom | Q488880 | 256 BCE | c. 120 BCE | `#e/unverified` | Hellenistic Central Asia |
| indo-greek | Indo-Greek Kingdom | Q215643 | 200 BCE | 10 CE | `#e/unverified` | the Greco-Buddhist interface |
| kushan | Kushan Empire | Q25979 | c. 30 CE | c. 375 CE | `#e/unverified` | **Q8's type specimen** |
| palmyrene | Palmyrene Empire | Q877875 | 260 CE | 273 CE | `#e/unverified` | the short-lived limit case |
| sasanian | Sasanian Empire | Q83891 | 224 CE | 651 CE | `#e/unverified` | H5's corridor |
| tang | Tang dynasty | Q9683 | 618 CE | 907 CE | `#e/unverified` | Dunhuang's sovereign for most of Q8a |
| tibetan-empire | Tibetan Empire | Q2431480 | 618 CE | 842 CE | `#e/unverified` | Dunhuang's other sovereign |
| abbasid | Abbasid Caliphate | Q12536 | 750 CE | 1517 CE | `#e/unverified` | §14.8's Baghdad translation milieu |
| aksum-k | Kingdom of Aksum | Q139377 | c. 100 CE | 960 CE | `#e/unverified` | comparison class, Red Sea |
| florence-r | Republic of Florence | Q148540 | 1115 CE | 1569 CE | `#e/unverified` | §11.4's household channels |
| venice-r | Republic of Venice | Q4948 | 697 CE | 1797 CE | `#e/unverified` | the long-duration outlier |

? **Tibetan Empire's end is given as "842/848"** in the infobox. 842 is recorded; the ambiguity is
real and should be resolved from Tibetological scholarship, not from the infobox.
? **Abbasid 750–1517 spans an interregnum** (1258–1261, Baghdad to Cairo). A single duration
misrepresents it. The duration table flags this row; whether a broken polity counts as one entity
or two is a modelling question, not a data question.
? **Aksum's start is "1st century"**, recorded as `c. 100 CE`. The century-level precision is real
and the conversion to a year is the file's, not the source's.

---

## 6. What this file does not do

- **No borders.** A polity is a name, a lifespan and a claim; its extent is not modelled. Anything
  needing extent needs a map, and a map needs a projection and a date, which is a larger commitment.
- **No routes.** H9's channels connect places, but the edges are not recorded here. If the diaspora
  work (`resources.md` §11.6) needs them, they belong in their own table.
- **No settlement continuity.** "Dunhuang" the Tang garrison and "Dunhuang" the modern city share a
  Q-id and very little else. `rel` bounds what this project means; it does not assert continuity.

## 7. Gaps

- **Every polity date is tertiary.** Wikipedia infoboxes, parsed once. They are good enough to
  compute a first duration table and not good enough to publish. Verification is per-row and
  cheap for the well-studied ones.
- **The comparison class is incomplete.** `background.md` §5.3 names Palmyra, Samarkand,
  Alexandria, Dunhuang and Aksum; the polities above cover them unevenly, and several nexus sites
  (Samarkand, Alexandria, Dunhuang) sit inside polities rather than being polities. **Whether the
  duration table should count polities, cities, or periods-of-florescence is unresolved**, and it
  is the substantive question hiding inside a bookkeeping one. → `background.md` §11.
- **No non-Eurasian control.** Every entity here lies on one connected landmass. A comparison class
  with no independent case cannot distinguish "contact zones are generative" from "Eurasia is
  generative."
