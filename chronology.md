# chronology.md — dated claims and the notation that governs them

Companion index to `geography.md`. One schema on two axes: chronology indexes time, geography
indexes place. **The notation below binds both files.**

Decided `methods.md` §9.2 item 3, constraints at §9.3 · created 2026-08-27 · rev. 1

---

## 1. Why this file exists

`background.md` §7 sets a dating discipline; until now it was a rule with no instrument. A date
asserted inside a prose paragraph cannot be sorted, compared, or checked for the one error that
matters most here — conflating the date of a text with the date of its manuscript with the date of
the events it narrates.

**A date is a claim.** It therefore carries an evidential tag, exactly like any register entry, and
is subject to the same discipline.

## 2. Notation

### 2.1 Era

**BCE/CE only. Never BC/AD.** A project whose method turns on the emic/etic distinction (`methods.md`
§2) cannot adopt a confessional era notation as its neutral default without contradicting itself.
This applies to the project's own prose; quoted sources keep their own usage.

### 2.2 Qualifiers

| Form | Means | Example |
|---|---|---|
| `1048 CE` | a date the sources give exactly | Latin translation of *Barlaam* |
| `c. 375 CE` | approximate; the source itself hedges | Kushan collapse |
| `[30–375 CE]` | a span, both ends asserted | Kushan Empire |
| `t.p.q. 1048 CE` | *terminus post quem* — not before this | a copy citing a dated work |
| `t.a.q. 1028 CE` | *terminus ante quem* — not after this | Euthymius's Greek text, from his death |
| `fl. 1010–1028 CE` | floruit; only activity is datable, not birth or death | Euthymius of Athos |
| `C6 CE` | century-level precision, and no more | the Middle Persian *Bodisav* |

The termini are standard archaeological usage and map onto `methods.md` §5: a *t.p.q.* from a
datable object is rung 4 evidence, while a *t.p.q.* from a stylistic judgement is not.

### 2.3 The three date-kinds — the discipline this file exists to enforce

`background.md` §7's dating obstacle, in miniature. Every row declares which it is:

| Kind | Dates | Failure if conflated |
|---|---|---|
| `comp` | composition of the work | a 14th-c. composition read as an 8th-c. witness |
| `ms` | the surviving manuscript witness | a late copy taken to date its content |
| `ev` | the events narrated | a tradition's internal chronology read as history |

A Dunhuang manuscript has all three and they can differ by centuries. **A row with an undeclared
kind is malformed**, not merely incomplete: the terma question (`resources.md` §14.5a) is exactly a
dispute about which kind a given date is.

### 2.4 Evidential tag

Every row carries the evidential tags of `tags.md` §3, which apply to a dated claim exactly as they
apply to a source. `#e/` says how the date was established: `primary` for a direct measurement such
as a radiocarbon determination, `secondary` for a date reported in scholarship, `inferred` for one
derived from a synchronism. `#v/emic` marks a tradition's own reckoning of its past. `#s/contested`
marks a date under active dispute — and being independent of how the date was established, it says
something the old single-facet scheme could not. `[unverified]` marks a row not checked against its
source, including every row taken from a tertiary index.

### 2.5 Machine form — derived, not stored

`methods.md` §9.3 called for "a sortable machine form alongside the display form." **Refined in
practice to *derived from* the display form**, by `scripts/build_tables.py`. Storing both invites
drift between them, and a drifting date is worse than an unsorted one.

Two consequences worth stating:

- **The display form must be machine-parseable.** That is the real constraint the table rows are
  obeying, and why the qualifier vocabulary in §2.2 is closed rather than free text.
- **Arithmetic uses astronomical year numbering, display does not.** Historians' BCE/CE has no year
  zero, so naively mapping `550 BCE → -550` and subtracting overstates every span crossing the
  epoch by one year. Internally `1 BCE = 0`, `2 BCE = -1`, i.e. `astronomical = 1 − BCE`. The CSV
  carries `year_astronomical` for arithmetic and the original string for reading. The Indo-Greek
  Kingdom, 200 BCE to 10 CE, is 209 years and not 210.

---

## 3. The table

`bears-on` uses the project's question and hypothesis labels. Rows sourced only from a tertiary
index are `#e/secondary` [unverified] regardless of how confident the source sounded.

| id | date | kind | entity | bears-on | tag | rung |
|---|---|---|---|---|---|---|
| buddha-life | [c. 480–c. 400 BCE] | ev | Life of Siddhārtha Gautama — dating heavily disputed | Q2, §14.8 | `#e/secondary #s/contested` | — |
| lalitavistara | [C1–C3 CE] | comp | *Lalitavistara Sūtra*, candidate source of the Barlaam chain | §14.8 | `#e/secondary` [unverified] | — |
| bj-sanskrit | [C2–C4 CE] | comp | Sanskrit Mahāyāna source text of the Barlaam material | §14.8 | `#e/secondary` [unverified] | 2 |
| bj-persian | [C6–C7 CE] | comp | Middle Persian *Bodisav* — the step the popular retelling drops | §14.8 | `#e/secondary` | 1 |
| bj-arabic | C8 CE | comp | Arabic *Kitāb Bilawhar wa-Būd̠āsaf*, current in Baghdad | §14.8, H5 | `#e/secondary` | 1 |
| bj-georgian | C10 CE | comp | Georgian *Balavariani* — first Christianised adaptation | §14.8 | `#e/secondary` | 2 |
| euthymius | t.a.q. 1028 CE | comp | Greek *Barlaam and Ioasaph*, by Euthymius of Athos | §14.8 | `#e/secondary` | 2 |
| bj-latin | 1048 CE | comp | Latin translation; the name enters Western Europe | §14.8 | `#e/secondary` | 1 |
| bj-relic | 1571 CE | ev | Josaphat relic presented to King Sebastian of Portugal | §14.8, Q5 | `#e/secondary` [unverified] | 4 |
| bj-refuted | [C19–C20 CE] | ev | Conybeare and Peeters establish the Georgian/Arabic descent | §14.8, §7.2 | `#e/secondary` | — |
| kuntsevych | 1960 CE | ev | Josaphat Kuntsevych set at 16 Nov — *not* a removal of Barlaam/Josaphat | §14.8 | `#e/secondary` | — |
| gandharan-art | [c. 100 BCE–c. 400 CE] | ev | Gandhāran sculptural production | Q8, H5, H7 | `#e/secondary` | 4 |
| halo-gandhara | c. C1 CE | ev | Earliest nimbate Buddha images — H5's anchor | H5 | `#e/secondary #s/contested` | 4 |
| dunhuang-caves | [c. 366–c. 1000 CE] | ev | Mogao cave excavation and use | Q8a | `#e/secondary` | 4 |
| dunhuang-sealed | c. 1000 CE | ev | Cave 17 sealed — the reason the archive survives | Q8a, §14.7 | `#e/secondary #s/contested` | 4 |
| dunhuang-opened | 1900 CE | ev | Wang Yuanlu opens Cave 17 | Q8a, §14.7 | `#e/secondary` | — |
| nubchen | c. C10 CE | comp | Nubchen Sangye Yeshe, *bSam gtan mig sgron* | Q4 | `#e/secondary` | 2 |
| terma-tradition | t.p.q. C11 CE | ev | Treasure revelation as an established Nyingma practice | H7, §14.5a | `#e/secondary #s/contested` | — |
| rainbow-body-doc | t.p.q. C11 CE | comp | Earliest datable rainbow-body doctrinal material | Q1, H2 | `#e/secondary #s/contested` | 2 |
| pema-dudul | 1872 CE | ev | Death of Nyagla Pema Dündul | Q1 | `#e/secondary` [unverified] | — |
| khenpo-acho | 1998 CE | ev | Death of Khenpo A Chö — **1998 vs 1999 unresolved (C7)** | Q1 | `#e/secondary #s/contested` | — |
| norbu-talks | 1982 CE | ev | Norbu's California talks, as delivered | Q1, H4 | `#e/secondary` | — |
| norbu-print | 1988 CE | ms | *Talks in California, USA 1982*, first printing Sept 1988 | Q1, H4 | `#e/secondary` | — |
| tiso-book | 2016 CE | comp | Tiso, *Rainbow Body and Resurrection* | Q3, H2 | `#e/secondary` | — |
| gutenberg | c. 1450 CE | ev | Movable type in Europe — §14.6's substrate change | §14.6 | `#e/secondary` | 4 |

? **`buddha-life` is the project's own worked example of §2.3.** The long and short chronologies
differ by roughly a century, and the traditional dates differ from both. Three date-kinds and three
evidential regimes in one row; it should probably be split into three.
? **`rainbow-body-doc` is the most consequential row here.** Q1 and H2 turn on it, and it currently
carries a *t.p.q.* rather than a date. Germano is the source to work it from.
? **`halo-gandhara` is tagged `#e/secondary #s/contested` deliberately** — whether the earliest nimbate images
are 1st century is exactly what H5 needs and exactly what is disputed.

---

## 4. Gaps

- **Thin before the common era, and thin outside the two founding cases.** The table serves Q8,
  §14.8 and Q1 well and everything else barely.
- **No Bön chronology at all.** `background.md` §11 makes Bön the sharpest available test of the
  whole method, and it has no dated anchors here. The Tazig circularity check needs them.
- **`rung` is empty for most rows.** Where a date rests on stylistic judgement rather than a datable
  object, the rung is the honest answer and is being deferred rather than recorded.
- **No Christian-side sequence.** §14.6 tracks canon, scriptorium, pecia and press; only the press
  has a row.
