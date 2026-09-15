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
| `#e/` | **Evidential role** | What kind of thing is it, and how does it bear on a claim? | **always** |
| `#v/` | **Point of view** | Whose frame does it speak from, if not the analyst's? | optional |
| `#s/` | **Standing** | How does the literature regard it, if not unremarkably? | optional |
| `#f/` | **Form** | What kind of object is it? | optional |

### Rules

1. **Maximum 3 tags per item.** Fewer is fine.
2. **`#e/` is mandatory.** No exceptions.
3. **`#r/` is mandatory on any item asserting or evaluating a cross-tradition link.** Single-tradition description omits it.
4. **No facet repeats within an item.** Two `#d/` tags means the item should be split, or that `#r/` is the honest third tag.
5. **New terms go into this file before use.** An undefined term is a typo until proven otherwise.
6. **Lowercase, hyphenated, singular.** `#c/rainbow-body`, never `#c/Rainbow_Bodies`.
7. **The cap applies to the descriptive facets.** At most three of `#d/ #c/ #r/ #f/`; exactly one
   `#e/`; at most one each of `#v/` and `#s/`. The old flat cap of three forced a choice between
   facts that answer different questions, which is how the register lost one answer per entry for
   257 entries — see §5.
8. **Verification and strength are fields, not tags.** `[unverified]` records whether *we* have
   checked the item; `rung:` records the strength of a comparative claim against the `methods.md`
   §5 ladder. Neither is a property of the source, so neither is a tag.

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

### `#e/` — Evidential role

What kind of thing the entry is, and how it can bear on a claim. Exactly one, always.

```
#e/primary      A source text, artefact, dataset or first-hand report
#e/secondary    Scholarship about such material. The unmarked default for a bibliography
#e/inferred     A claim derived by reasoning from other evidence, not directly attested
#e/heuristic    Not evidence. Generates questions and leads; never cited in support
```

### `#v/` — Point of view

Whose frame the item speaks from. **Optional, and absent means the analyst's own** — an
unmarked entry is etic, which is what most scholarship is. Tag only the informative case.

```
#v/emic         The tradition's own categories, as its participants operate them
#v/polemical    An opponent's frame. The heresiologists on "Gnosticism" is the type case
#v/apologetic   A defence pitched at an outside audience, and shaped by that audience
```

`#v/` is independent of `#e/`, which is why it is a separate facet: Norbu's *Talks* is a
primary source **and** the tradition speaking about itself, and both facts are worth keeping.

> **`#v/polemical` matters more than its count suggests.** For some traditions the hostile
> witness is the only witness — "Gnosticism" before Nag Hammadi was known almost entirely
> through Irenaeus and Epiphanius. Such sources cannot be discarded, so they must be marked
> and corrected for. Leaving them untagged is how an opponents' frame gets naturalised into a
> neutral-seeming analytic category, which is `methods.md` §2.5's first failure mode.

### `#s/` — Standing

How the literature regards the item. **Optional, and absent means unremarkable.** This replaces
the old `#e/attested`, which ran at half the register and so discriminated nothing.

```
#s/contested    Live scholarly dispute; name the opponent in the `against:` field
#s/fringe       Outside scholarly consensus, and recorded as such rather than excluded
#s/speculative  Unreviewed — preprint, or an author writing outside their field
```

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
  #c/rainbow-body #r/genealogy #e/secondary #s/contested

- Gandhāran Buddha with nimbus, 1st c. CE, Kushan. @gandhara-nimbus
  #c/iconography #r/homology #e/primary          ← tests H5

- Bön origin in Tazig / Olmo Lungring. @bon-tazig
  #c/emic-etic #r/genealogy #e/primary #v/emic   ← the tradition's own contact claim

- Smith, Jonathan Z. *Drudgery Divine* (1990). @smith-1990
  #d/method #r/deflation #e/secondary            ← standing unremarkable, so no #s/

- Namkhai Norbu. *Talks in California, USA 1982*. @norbu-1988
  #d/dzogchen #c/rainbow-body #e/primary #v/emic

- Irenaeus, *Adversus Haereses*, on the Valentinians. @irenaeus
  #d/gnostic #e/primary #v/polemical             ← a hostile witness, and often the only one
```

### 5.1 What the old scheme could not say, and why it was changed

Until 2026-09-14 these were one facet, `#e/`, with exactly one value per entry. The Norbu line was
carried in this file as the worked example of an **invalid** entry:

```markdown
  #d/dzogchen #e/primary #e/devotional    ← INVALID: two #e/ tags
```

and the guidance was to "choose the one that governs how you will *use* it."

That was a rule for living with a defect. Both statements are true, and they answer different
questions: Norbu's *Talks* **is** a primary source, and it **is** the tradition speaking about
itself. Being emic is independent of being first-hand, so no single value can carry both.

A census settled it. Across 258 tagged entries, **not one** carried both a kind value
(`primary`, `devotional`, `inferred`, `heuristic`) and a standing value (`attested`, `contested`,
`fringe`, `speculative`) — because the schema forbade it. So for every primary source the register
had no record of its standing, and for every attested item no record of what kind of thing it was.
The facet was not merely imprecise; it discarded one answer per entry, 258 times.

Splitting it also gave `methods.md` §2.8's conclusion somewhere to live. That decision held that
emic testimony is evidence differing in **type** rather than degree — which a single ordering
cannot express, and which `#v/emic` states directly.

### 5a. Notes from the 2026-08-25 census, and what came of them

Two findings worth recording, because they change how the facets should be read.

- **`#e/attested` was the unmarked default.** It ran at roughly half of all entries, past the
  threshold §6 sets for promoting a tag to a heading, and the census concluded it meant "nothing
  unusual here." **Acted on 2026-09-14**: a value carried by half the register discriminates
  nothing, so standing became its own optional facet, absent by default. `#e/attested` no longer
  exists; an entry with no `#s/` tag is unremarkable in the literature. See §5.1.
- **`#f/` has been largely superseded by the field line.** It appears on under a tenth of entries,
  because `access:`, `src` and the entry prose already say what kind of object something is. It
  remains optional and legitimate — `#f/manuscript`, `#f/dataset` and `#f/reference` still earn their
  place — but it should not be reached for when a `#c/` tag would be more informative. `#f/monograph`
  was pruned as never used.

## 6. Maintenance

- **Review the vocabulary past ~50 terms.** Merge near-synonyms. Promote any tag applied to more than a quarter of items into a section heading instead: a tag that applies to everything discriminates nothing.
- **Prune single-use tags** once the corpus stabilises, unless the single use is a deliberate placeholder for a thread not yet followed.
- **A tag is also a prompt to notice.** A category with no entries yet may still earn its place, because having the name in the vocabulary is what makes instances visible. `#v/apologetic` was added before any entry used it; inspecting the register immediately turned up three that had been filed as `#e/devotional` for want of anywhere better. Bound this by the rule above: anticipatory tags are for **named failure modes the project already tracks**, not for speculation.
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
