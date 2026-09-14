# Tagging Scheme

*Controlled vocabulary and inline markup for the Spirit project. Research frame: `background.md`. Tagged corpus: `resources.md`.*

Status: rev. 3, 2026-08-25.

---

## 1. Design rationale

The scheme is a **faceted folksonomy**: a small set of fixed facets (the taxonomy part, which prevents drift) filled by a growing but curated term list (the folksonomy part, which keeps it usable). This hybrid is the standard recommendation in the tagging literature — pure folksonomies suffer polysemy, homonymy and base-level inconsistency; pure controlled vocabularies are too rigid for an inquiry whose categories are still forming. Facets disambiguate the tags and give the whole thing an information architecture.

Three constraints shape it, and all three come from the project rather than from library science:

- **Tag budget of 3.** A budget forces a judgement about what an item is *for*. Twelve tags per item is the same as no tags: nothing is discriminated. Three means every tag was chosen against a rival.
- **One facet encodes the genealogy/analogy distinction.** J. Z. Smith's charge is that comparative religion collapses *genealogy* (historical descent or contact) into *analogy* (structural similarity). The `#r/` facet makes every item declare which it claims.
- **One facet encodes epistemic status separately from topic — and with it, the emic/etic line.** A hagiography and a peer-reviewed article can be about the same event. `#e/` keeps "what it is about" apart from "what it can be used to establish." This is where `background.md` §2.2 becomes operational: `#e/devotional` marks emic material, the `#e/attested`–`#e/inferred` range marks etic material, and the two never occupy the same slot.

## 2. Facets

Five facets, prefix-coded. Single-letter prefixes keep tags short and greppable.

| Prefix | Facet | Answers | Required? |
|---|---|---|---|
| `#d/` | **Domain** | Which tradition, corpus, or field? | at least one of `#d/` or `#c/` |
| `#c/` | **Concept** | Which motif, doctrine, practice, or evidence-type? | at least one of `#d/` or `#c/` |
| `#r/` | **Relation-claim** | What kind of comparative claim, if any? | on any comparative item |
| `#e/` | **Evidential status** | What can it be used to establish? | **always** |
| `#f/` | **Form** | What kind of object is it? | optional |

### Rules

1. **Maximum 3 tags per item.** Fewer is fine.
2. **`#e/` is mandatory.** No exceptions.
3. **`#r/` is mandatory on any item asserting or evaluating a cross-tradition link.** Single-tradition description omits it.
4. **No facet repeats within an item.** Two `#d/` tags means the item should be split, or that `#r/` is the honest third tag.
5. **New terms go into this file before use.** An undefined term is a typo until proven otherwise.
6. **Lowercase, hyphenated, singular.** `#c/rainbow-body`, never `#c/Rainbow_Bodies`.

## 3. Controlled vocabulary

### `#d/` — Domain / tradition / corpus

```
#d/dzogchen        Great Perfection, Buddhist (Nyingma) and general
#d/bon             Bön, incl. Bön Dzogchen and Zhang Zhung material
#d/nyingma         Nyingma more broadly; tantra, terma
#d/tibetan         Tibetan Buddhism generally, where no narrower term fits
#d/nikaya          Mainstream / early Buddhism: the Nikāya schools, incl. Theravāda,
                   Mahāsāṃghika, Sarvāstivāda. NOT a synonym for Theravāda.
#d/mahayana        Indian and pan-Asian Mahāyāna
#d/chan            Chan / Zen, incl. Tibetan Zen
#d/christian       Christianity generally, where no narrower term fits
#d/gnostic         So-called Gnostic corpora (Nag Hammadi, BG 8502, Sethian, Valentinian)
#d/syriac          Syriac Christianity; Ephrem, Church of the East
#d/orthodox        Eastern Orthodox, esp. Hesychasm and Palamite theology
#d/catholic        Latin/magisterial Christianity
#d/manichaean      Manichaeism, Roman through Central Asian
#d/iranian         Zoroastrian, Achaemenid, Parthian, Sasanian; Iranian religion and art
#d/hellenistic     Greco-Roman religion, mystery cults, Middle Platonism, Gandhāran Greek
#d/indo-european   Comparative IE linguistics, mythology, and dispersal
#d/central-asia    The Silk Road contact zone as an object of study
#d/method          Theory and method in comparative and historical study
```

### `#c/` — Concept / motif / practice / evidence-type

```
#c/rainbow-body      'ja' lus and its subtypes
#c/great-transfer    'pho ba chen po; transformation without death
#c/light-body        'od kyi sku / 'od lus; and non-Tibetan light-body notions
#c/glory             The khvarenah / farr / robe-of-glory / nimbus radiance complex (H5)
#c/resurrection      Bodily rising after death, and post-resurrection persistence
#c/transfiguration   Tabor; uncreated light
#c/assumption        Translation/assumption without death (Enoch, Elijah, Mary)
#c/relics            ring bsrel, incorruptibility, hair-and-nails remainder
#c/thodgal           thod rgal, dark retreat, the four visions
#c/gnosis            Salvific knowledge; rig pa / jñāna / gnōsis compared
#c/primordial-basis  gzhi, ka dag, lhun grub; pleroma; ground-of-being motifs
#c/death-process     Bardo, dying, post-mortem states
#c/asceticism        Renunciation, forest-dwelling, monastic vs. lay questions
#c/lineage-narrative Origin stories, transmission accounts, hagiography as genre (H6)
#c/terma             gter ma revelation; revealed-text claims and their dating problem
#c/emic-etic         The self-description / observable-record interface itself
#c/translation-layer Distortion from translation, transcription, reception, or framing
#c/contact-route     Trade, migration, mission, manuscript transmission
#c/nexus             Contact-zone generativity: preconditions, comparison cases, and
                     the transmitter/innovator distinction (Q8)
#c/iconography       Visual motif as evidence: halos, gesture, composition, attributes
#c/material-culture  Art, architecture, archaeology, technology, coins as evidence
#c/loanword          Lexical and calque evidence for contact
#c/genetics          Population-genetic and ancient-DNA evidence
#c/canon-formation   How texts became authoritative or were excluded
#c/historical-jesus  The historical / ecclesiastical Jesus problem
#c/diaspora          Dispersed communities as a transmission mechanism in their own
                     right, and the transmitter/innovator distinction within them (H11)
#c/household-channel Transmission across a generational rather than a transactional
                     boundary: childcare, domestic service, kitchen and nursery
```

### `#r/` — Relation-claim (the Smith facet)

```
#r/genealogy    Asserts historical descent or contact between traditions
#r/analogy      Asserts structural or phenomenological similarity; no contact claimed
#r/homology     Asserts shared descent from a common source — stronger than analogy,
                different from genealogy. The H5 tag.
#r/vector       Documents a concrete contact mechanism (route, manuscript, mission, coin)
#r/deflation    Argues *against* a proposed link, or explains it away
#r/none         Single-tradition description; no comparative claim
```

`#r/deflation` is deliberately available. Arguments that dissolve a parallel are findings, and must be as tagged, findable and countable as arguments that build one.

`#r/homology` is the facet's most useful distinction for this project. Buddhist and Christian halos are probably not a case of one borrowing from the other (`#r/genealogy`) nor of independent invention (`#r/analogy`), but of both inheriting an Iranian–Hellenistic convention. Tagging that correctly is most of the analysis.

### `#e/` — Evidential status

```
#e/primary      A source text of the tradition itself
#e/attested     Well-evidenced scholarly claim; documentary or material backing
#e/inferred     Reasonable scholarly inference beyond direct evidence
#e/contested    Live scholarly disagreement; cite the disagreement, not one side of it
#e/speculative  Proposed but thinly supported; interesting, not loadbearing
#e/fringe       Outside scholarly consensus or methodologically unsound; read with care
#e/devotional   Insider / confessional / self-descriptive — EMIC. Evidence of what a
                tradition holds, not of what happened.
#e/heuristic    NOT evidence. A source of hypotheses, framings and questions — fiction,
                thought experiments, analogies. Generative, never citable in support of
                a claim. Kept distinct from #e/speculative, which IS a weak factual claim.
#e/unverified   Not yet checked against the source by us
```

`#e/devotional` is not a demerit; it is a slot assignment. Norbu's talks are the best possible evidence for what the tradition teaches and no evidence at all for the eighth century. Bön's Tazig origin claim is `#e/devotional` — and is *interesting precisely as such*, because `background.md` §11 proposes testing it against material evidence. Keeping the emic claim tagged as emic is what makes that test possible rather than circular.

### `#f/` — Form

```
#f/article  #f/edited-volume  #f/translation
#f/manuscript #f/reference #f/dataset  #f/popular  #f/lecture  #f/web
#f/object     Artefact, image, sculpture, coin, inscription
```

## 4. Inline markup beyond tags

Minimal and greppable; no tooling required.

| Markup | Meaning | Example |
|---|---|---|
| `#f/term` | Faceted tag | `#c/rainbow-body` |
| `[[concept]]` | Cross-document concept link | `[[great-transfer]]` |
| `@author-year` | Citekey resolving to a `resources.md` entry | `@tiso-2016` |
| `?` at line start | Open question | `? Wylie for the Pema Dündul terma?` |
| `!` at line start | Flag: unreliable, disputed, needs care | `! Hirakawa's lay-origins thesis is displaced` |
| `→` | Consequence or next step | `→ check against Sasanian coin evidence` |
| `[unverified]` | Written from memory; not source-checked | inline, anywhere |
| `H1`–`H6` | Reference to a `background.md` hypothesis | `tests H5 directly` |

`?` and `!` at line start make open questions and warnings greppable project-wide without a database.

## 5. Worked examples

```markdown
- Tiso, Francis V. *Rainbow Body and Resurrection* (2016). @tiso-2016
  #c/rainbow-body #r/genealogy #e/contested

- Gandhāran Buddha with nimbus, 1st c. CE, Kushan. @gandhara-nimbus
  #c/iconography #r/homology #e/primary        ← tests H5

- Bön origin in Tazig / Olmo Lungring. @bon-tazig
  #c/emic-etic #r/genealogy #e/devotional      ← the tradition's own contact claim

- Smith, Jonathan Z. *Drudgery Divine* (1990). @smith-1990
  #d/method #r/deflation #e/attested

- Namkhai Norbu. *Talks in California, USA 1982*. @norbu-1988
  #d/dzogchen #e/primary #e/devotional         ← INVALID: two #e/ tags

- Namkhai Norbu. *Talks in California, USA 1982*. @norbu-1988
  #d/dzogchen #c/rainbow-body #e/devotional    ← valid
```

The invalid case is instructive. When an item genuinely straddles two `#e/` values, choose the one that governs how you will *use* it. We read Norbu for what the tradition says about itself, so `#e/devotional` governs — and that is the emic/etic discipline doing its work at the level of a single tag.

### 5a. Notes from the 2026-08-25 census

Two findings worth recording, because they change how the facets should be read.

- **`#e/attested` is the unmarked default.** It runs at roughly half of all entries, past the
  threshold §6 sets for promoting a tag to a heading. But the right reading is not that it should be
  split: for a bibliography of scholarship, "well-evidenced" *is* the expected value. **The
  information is in the other seven** — `#e/contested`, `#e/devotional`, `#e/heuristic` and the rest
  are what discriminate. Treat `#e/attested` as "nothing unusual here."
- **`#f/` has been largely superseded by the field line.** It appears on under a tenth of entries,
  because `access:`, `src` and the entry prose already say what kind of object something is. It
  remains optional and legitimate — `#f/manuscript`, `#f/dataset` and `#f/reference` still earn their
  place — but it should not be reached for when a `#c/` tag would be more informative. `#f/monograph`
  was pruned as never used.

## 6. Maintenance

- **Review the vocabulary past ~50 terms.** Merge near-synonyms. Promote any tag applied to more than a quarter of items into a section heading instead: a tag that applies to everything discriminates nothing.
- **Prune single-use tags** once the corpus stabilises, unless the single use is a deliberate placeholder for a thread not yet followed.
- **Never retag to make a pattern come out.** If `#r/genealogy` items keep resolving to `#e/speculative`, that is the result.

## 7. Grep recipes

```bash
# Everything claiming actual historical contact
grep -n '#r/genealogy' resources.md

# Genealogical claims that are NOT well-evidenced — the project's soft underbelly
grep -n '#r/genealogy' resources.md | grep -E '#e/(speculative|fringe|contested)'

# The H5 thread: common-ancestry claims and the glory complex
grep -n '#r/homology\|#c/glory' resources.md

# Emic material — what traditions say about themselves
grep -n '#e/devotional' resources.md

# Emic claims that make historical assertions: the §2.2 test cases
grep -n '#e/devotional' resources.md | grep -E '#r/(genealogy|vector)'

# All open questions and all warnings, project-wide
grep -rn '^\s*[?!]' *.md notes/ 2>/dev/null

# Everything still unchecked
grep -rn '\[unverified\]\|#e/unverified' *.md

# Tag frequency census (for the §6 review)
grep -o '#[dcref]/[a-z-]*' *.md | cut -d: -f2 | sort | uniq -c | sort -rn
```
