# Resource Register

*Topical catalogue of sources. Reasoning: `methods.md`. Questions and findings: `background.md`. Markup: `tags.md`.*

Status: rev. 4, 2026-08-25. Validate with `./validate.sh`.

---

## 0. How to read an entry

```
- Author, *Title* — one line on what it establishes. @citekey
  `#tags` · subj <period it is about> · src <year written> · <Q/H it bears on>
  · access: <status> · chain: <transmission> · against: @citekey · [unverified]
```

**Fields.** `subj` and `src` are separate because a 1990 book about the first century must never be dated by its publication (`methods.md` §4). `bears-on` names the question or hypothesis the source can actually settle, so the register stays actionable rather than decorative. `chain` records the transmission path for anything translated — the §14 problem made visible per item. `against` points to the entry it contradicts; both then appear in the controversy register (§16).

**Access.** `open` (free online) · `library` · `purchase` · `unlocated` (exists, not yet found) · `held` (we have it).

**Evidential tags.** `#e/` says what kind of thing an entry is — `primary` a source text, `secondary` scholarship about it, `inferred` a claim derived by reasoning, `heuristic` not evidence at all. `#v/` marks whose frame it speaks from when that is not the analyst's — `emic` the tradition's own, `polemical` an opponent's, `apologetic` a defence pitched outward. `#s/` marks standing in the literature when it is not unremarkable — `contested`, `fringe`, `speculative`. Strength of a comparative claim is the `rung:` field, governed by the ladder in `methods.md` §5. See `tags.md`.

`[unverified]` on an entry means compiled from prior knowledge, not checked against the source. Substance reliable, citation details provisional.

**Held locally.** Entries marked `access: held` have a PDF under `lit/` — see
`lit/openalex/MANIFEST.md` and `lit/epmc/MANIFEST.md` for licenses and filenames, and the
`QUERIES.md` files for what was searched. `lit/WANTED.md` lists items verified to exist but
not held. Retrieval coverage limits are recorded in §17.

Each topic splits into **Primary references** (the texts and objects themselves) and **Potential sources** (scholarship about them).

---

## 1. Dzogchen: the tradition's own texts

Norbu's *Talks* is oral teaching in an acquired language, transcribed, translated, and published by the teacher's own institution — excellent evidence for what the tradition presents to a late-twentieth-century Western audience, none for the eighth century. Behind it stand the datable textual strata where historical questions must be settled. Norbu occupies both sides of the emic/etic seam (`methods.md` §2.3), which makes his corpus a working demonstration as well as a source.

### Primary references

- Namkhai Norbu, *Talks in California, USA 1982* — **the project text**; source of the Pema Dündul passage. @norbu-1988
  `#d/dzogchen #c/rainbow-body #e/primary #v/emic` · subj 1982 · src 1988 (© 1982) · Q1 Q3 · access: held · chain: Tib→It (oral)→En (Barry Simmons)
- ——, *Talks in Conway, USA, July 1982 & January 1983* — same translator and period, different audience. Control for audience-driven vocabulary shift. @norbu-conway
  `#d/dzogchen #c/translation-layer #e/primary #v/emic` · subj 1982–83 · src n.d. · H4 · access: purchase · chain: Tib→It→En (Simmons)
- ——, *The Cycle of Day and Night* — carries the lineage-origin narrative behind H6. @norbu-cycle
  `#d/dzogchen #c/lineage-narrative #e/primary #v/emic` · subj mythic/8c · src 1984 · Q4 H6 · access: purchase · chain: Tib→En (J. M. Reynolds) · [unverified]
- ——, *The Crystal and the Way of Light* — general introduction; also where Norbu writes on Changchub Dorje. @norbu-crystal
  `#d/dzogchen #c/primordial-basis #e/primary #v/emic` · subj 20c · src 1986 · Q1 · access: purchase · chain: →En (ed. John Shane)
- ——, with Adriano Clemente, *The Supreme Source: … Kunjed Gyalpo* — the root Mind Series tantra in English. @norbu-supreme
  `#d/dzogchen #c/primordial-basis #e/primary` · subj 9–10c · src 1999 · Q1 · access: purchase · chain: Tib→It→En (Clemente/Lukianowicz) · [unverified]
- ——, *Drung, Deu and Bön* — Norbu as historian of pre-Buddhist Tibet. @norbu-drung
  `#d/bon #c/lineage-narrative #e/secondary #s/contested` · subj pre-7c · src 1995 · Q4 · access: purchase · [unverified]
- ——, *The Light of Kailash*, 3 vols — Norbu's major historical work; strong Zhang Zhung antiquity claims. **The clearest case of a lineage holder doing etic work.** @norbu-kailash
  `#d/bon #c/emic-etic #e/secondary #s/contested` · subj pre-7c–17c · src 2009–15 · Q4 · access: purchase · chain: Tib→En (Rossi, N. Simmons) · against: @bon-scholarship
- `Kun byed rgyal po` and the Eighteen Texts of the Mind Series. @kunjed
  `#d/dzogchen #c/primordial-basis #e/primary` · subj 9–10c · Q1 · access: purchase · [unverified]
- *Seventeen Tantras* of the Seminal Heart (`snying thig`) — where `thod rgal` and the light-body material concentrate. @seventeen-tantras
  `#d/dzogchen #c/thodgal #e/primary` · subj 11c+ · Q1 Q3 · access: unlocated · [unverified]
- *Zhang Zhung Nyen Gyud* — Bön aural transmission; its rainbow-body lineage incl. Tapihritsa. @zznyengyud
  `#d/bon #c/rainbow-body #e/primary` · subj claimed pre-7c · Q1 · access: unlocated · [unverified]
- Dunhuang Tibetan manuscripts (IOL Tib J; Pelliot tibétain) — **the only genuinely 8th–10th c. Tibetan witnesses; the evidentiary floor under every dating claim here.** @dunhuang-tib
  `#d/central-asia #c/contact-route #e/primary` · subj 8–10c · Q6 · access: open (IDP)
- `gter ma` literature generally — revealed texts attributed to earlier concealment. The sharpest emic/etic problem in Tibetan studies. @terma **A stronger reading follows from `methods.md` §1.2b**: Tibetan transmission requires `lung` and `dbang` — you cannot legitimately pass on what you have not received — which is institutional error-correction of the Vedic type. **Terma is a sanctioned *bypass* of that apparatus**, routing legitimacy through Padmasambhava rather than through living teachers, and so admitting novelty without breaking the chain. Not merely "legitimating innovation by attributing it to the past" but **reopening design space without requiring the institution to collapse** — the H13 mechanism, available from inside.
  `#c/emic-etic #d/nyingma #e/secondary #s/contested` · subj 11c+ (claimed 8c) · Q4 · access: n/a

? Does the ebook carry a series number, and is it the Sept. 1988 first printing? — **resolved: © 1982, 1st ed. 1st printing Sept 1988.**
→ Cross-translator comparison (Simmons / Reynolds / Clemente / Shane / Lukianowicz) is the practicable H4 instrument absent Italian. `methods.md` §3.2 step 4.

---

## 2. Dzogchen studies

The field has moved from Karmay's founding survey toward the Dunhuang manuscripts and the Seminal Heart's visionary and funerary material. Central finding for us: the earliest layer (Mind Series, 9th–10th c.) differs markedly from the later one (Seminal Heart, 11th c.+), and **the rainbow body belongs to the later layer** — the load-bearing objection to H2.

### Potential sources

- Karmay, Samten G., *The Great Perfection (rDzogs chen)* — the founding philological survey; still baseline. @karmay-1988
  `#d/dzogchen #r/none #e/secondary` · subj 8–14c · src 1988 · Q1 · access: library · [unverified]
- van Schaik, Sam, *Approaching the Great Perfection* @vanschaik-2004
  `#d/dzogchen #r/none #e/secondary` · subj 14c · src 2004 · Q1 · access: purchase · [unverified]
- ——, "The Early Days of the Great Perfection," *JIABS* 27.1 — dates the earliest stratum from Dunhuang. **Governs the §4 dating obstacle.** @vanschaik-2004b
  `#d/dzogchen #c/contact-route #e/secondary` · subj 9–10c · src 2004 · Q6 H2 · access: open · [unverified]
- ——, *earlytibet.com* — research blog citing manuscripts directly. @earlytibet
  `#d/dzogchen #f/web #e/secondary` · subj 8–11c · src 2007– · Q1 Q6 · access: open
- Germano, David, "Architecture and Absence in the Secret Tantric History of rDzogs Chen," *JIABS* 17.2 — locates the Seminal Heart in a **Tibetan mortuary substrate**, not an imported one. @germano-1994
  `#d/dzogchen #c/death-process #e/secondary` · subj 11–14c · src 1994 · H2 · access: open · against: @tiso-2016 · [unverified]
- Hatchell, Christopher, *Naked Seeing* — `thod rgal` across Dzogchen, Kālacakra and Bön. Best entry to the practice side. @hatchell-2014
  `#d/dzogchen #c/thodgal #e/secondary` · subj 11–15c · src 2014 · Q1 · access: purchase
- Achard, Jean-Luc, *L'Essence perlée du secret* — Bön Dzogchen and light-body doctrine. @achard-1999
  `#d/bon #c/light-body #e/secondary` · subj 11–14c · src 1999 · Q1 · access: library · [unverified]
- Klein, Anne C., & Tenzin Wangyal, *Unbounded Wholeness* @klein-2006
  `#d/bon #c/primordial-basis #e/secondary` · subj 11c+ · src 2006 · Q1 · access: purchase · [unverified]
- Rossi, Donatella, *The Philosophical View of the Great Perfection in the Tibetan Bon Religion* — Rossi also translated Norbu; note how often scholarly and community roles overlap here. @rossi-1999
  `#d/bon #c/emic-etic #e/secondary` · subj 11c+ · src 1999 · Q1 · access: purchase · [unverified]

- Baker, Ian, "Embodying Enlightenment: Physical Culture in Dzogchen as revealed in Tibet's Lukhang Murals," *Asian Medicine* 7 (2012) — `thod rgal` and the body in a datable visual source. Bridges §2 and §6: Dzogchen practice *as depicted*, i.e. iconographic evidence rather than doctrinal assertion. @baker-2012
  `#d/dzogchen #c/iconography #e/secondary` · subj 17c · src 2012 · Q1 H5 · access: held · license: unspecified
- Chaoul, M. Alejandro, "Magical Movement (`'phrul 'khor`): Ancient Tibetan Yogic Practices from the Bön Religion," *Asian Medicine* 3 (2007). Chaoul has worked closely with Bön lineage holders — read with §14 in view. @chaoul-2007
  `#d/bon #c/thodgal #e/secondary` · subj 11c+ · src 2007 · Q1 · access: held · license: unspecified
- Roberti di Sarsina, Paolo, "Chögyal Namkhai Norbu Rinpoche: Dzogchen and Tibetan Tradition. From Shang Shung into the Modern World," *Religions* 3 (2012) — the only peer-reviewed treatment of the project's primary author located so far. **The author is a physician writing on integrative medicine, not a Tibetologist**; sympathetic presentation, not independent scholarship. @robertidisarsina-2012
  `#d/dzogchen #c/emic-etic #e/secondary #v/apologetic` · subj 20c · src 2012 · Q1 · access: held · license: cc-by

### Bön as the double test case

- **As control**: an independent rainbow-body lineage in a tradition Christianity had no route to. If the doctrine appears there too, Christian influence loses its explanatory advantage. @bon-control
  `#d/bon #r/deflation #e/inferred` · subj 11c+ · H1 H2 · access: n/a
- **As emic westward claim**: Bön's origin account places its source in **Tazig** (`sTag gzig`) and Olmo Lungring, conventionally identified with Iranian lands. @bon-tazig
  `#c/emic-etic #r/genealogy #e/primary #v/emic` · subj claimed pre-7c · H5 · access: n/a
- Martin, Dan; Kvaerne, Per; Karmay — standard scholarship on Bön origins and the Tazig identification. @bon-scholarship
  `#d/bon #r/genealogy #e/secondary #s/contested` · subj pre-7c–11c · src 1985–2010 · H5 · access: library · against: @norbu-kailash · [unverified]

? **Circularity check required** (`methods.md` §2.6): is the Tazig↔Iran identification the tradition's own, or a scholarly gloss the tradition later absorbed? H5 cannot lean on the Bön convergence until this is settled.

---

## 3. The rainbow body

Not one claim but a graded family; typology in `background.md` §4. Only type (a) leaves physical evidence; only type (c), the great transfer, resembles the Christian assumption family — and it does so by *skipping* death. The modern evidentiary centre is Khenpo A Chö, investigated by Tiso, who is simultaneously the best resource and a specimen of the §1.1 problem.

### Primary references

- **Type (a): `ring bsrel`** — relics reported in the cremation remains of realized practitioners; `'phags pa'i ring bsrel` for those of an ārya. **The only branch of the typology that leaves physical evidence**, and the one with a genuine Christian counterpart in relic culture and incorruptibility. §8's judgement stands: the relic parallel is less glamorous than the resurrection parallel and probably more real. @ring-bsrel
  `#c/relics #d/tibetan #e/primary #v/emic` · subj 11c– · Q1 Q3 · access: n/a
- **Type (c): `'ja' lus 'pho ba chen po`, the great transfer** — transformation without passing through death, the adept remaining available; ascribed to Padmasambhava, Vimalamitra, and in Bön to Tapihritsa. **The only branch with a Christian structural analogue** — assumption and translation (Enoch, Elijah), not resurrection — because it skips death, which is exactly what resurrection does not do. The H1 pivot. @great-transfer
  `#c/great-transfer #r/analogy #e/primary #v/emic` · subj 8c– · Q3 H1 · access: n/a


- Nyala Pema Dündul (`Nyag bla Padma bdud 'dul`), 1816–1872 — tertön of Nyarong; founded Kalzang Monastery 1860; teacher of Tertön Sogyal; rainbow body in Saga Dawa 1872 with the standard apparatus (rainbows, three earth-tremors, music, spheres of light, fragrance). **Type (b).** Norbu's "master of my master"; the intermediate is Changchub Dorje (d. 1978). @pema-dundul
  `#c/rainbow-body #d/nyingma #e/primary #v/emic` · subj 1816–72 · Q1 Q3 · access: n/a
- Pema Dündul's terma: Guru Amitāyus long-life practice, "Union of Primordial Essences"; plus the cycle Norbu transcribes as **"Dzogchen Kazhag Rangdrol."** @pema-dundul-terma
  `#c/terma #f/manuscript #e/secondary` · subj 19c · Q1 · access: unlocated · chain: Tib→spoken It→En transcription
- Khenpo A Chö, d. **1998 or 1999**, Kham — the best-documented modern case. @khenpo-acho
  `#c/rainbow-body #d/tibetan #e/secondary #s/contested` · subj 1998/99 · Q1 · access: n/a

### Potential sources

- Tiso, Francis V., *Rainbow Body and Resurrection* — field interviews, textual history, and an explicit Central Asian contact hypothesis. **Read evidence chapters and hypothesis chapters as separate documents.** @tiso-2016
  `#c/rainbow-body #r/genealogy #e/secondary #s/contested` · subj 8c–1999 · src 2016 · Q3 Q6 H2 · access: purchase · against: @germano-1994
- ——, pre-2016 articles on the rainbow body in early Dzogchen texts; doctoral work on Milarepa. → Show whether the contact hypothesis grew from the evidence or preceded it. @tiso-articles
  `#c/rainbow-body #r/genealogy #e/secondary` · src pre-2016 · Q6 · access: unlocated
- *Treasury of Lives*, "Nyakla Pema Dudul" — peer-reviewed biography; the etic counterpart to the hagiography. @tol-pemadudul
  `#d/tibetan #f/reference #e/secondary` · subj 1816–72 · Q1 · access: open
- Rigpa Wiki / Rangjung Yeshe Wiki entries — useful for Tibetan orthography, unreliable for citation. @rywiki
  `#d/tibetan #f/reference #e/secondary #v/emic` · access: open
- "Investigating the Rainbow Body," *Lion's Roar* — reportage on the Tiso investigation. @lionsroar-rainbow
  `#c/rainbow-body #f/popular #e/secondary #v/apologetic` · src c. 2017 · access: open
- Pistono, Matteo, *In the Shadow of the Buddha* — biographical material on Tertön Sogyal and the Nyarong lineage. Leads, not citations. @pistono
  `#d/tibetan #f/popular #e/secondary #v/apologetic` · subj 19–20c · src 2011 · access: purchase · [unverified]
- Steindl-Rast, Br. David — reportedly the origin of Tiso's inquiry. → Verify; if so the comparison was framed emically before evidence was gathered. @steindlrast
  `#d/catholic #r/analogy #e/secondary` · Q6 · access: unlocated

? **Wylie for "Kazhag Rangdrol."** Candidates: `dka' zhag rang grol`, `bka' bzhag rang grol`. The `methods.md` §3.3 micro-case.
? **1998 vs 1999** for Khenpo A Chö's death. Resolve from Tiso's own text; a one-year discrepancy in the best-documented case indicates whether it is documentary or hagiographic.
? Type (b) is *maximally testable* — a vanished body leaves an attestable absence, and 1872 is recent. What documentary base exists beyond hagiography? Qing administrative records, monastery inventories, travellers' accounts?

### The tukdam research programme — the nearest thing to a test

An instrumented research programme on **tukdam** (`thugs dam`): practitioners reported to remain
in meditative state after clinical death without the expected decomposition. Conducted with
monastic cooperation, largely by one group. It matters more than its size suggests, because it is
the **same class of claim as the rainbow body** — a bodily anomaly after death, asserted by a
tradition, in principle checkable — but recent enough to instrument. The closest available
analogue to the "maximally testable" type (b) claim.

**The headline result is negative.** That makes the programme a specimen for `methods.md` §2.6
(divergence) and §7 (negative results), not support for the tradition's claim. Note also what it
models procedurally: researchers measuring an emic claim etically, *with* the tradition's
cooperation rather than against it.

- Lott, D. T., et al. (25 authors), "No Detectable Electroencephalographic Activity After Clinical Declaration of Death Among Tibetan Buddhist Meditators in Apparent Tukdam," *Frontiers in Psychology* 11 (2020). @lott-2020
  `#c/death-process #r/deflation #e/secondary` · subj 2015–19 · src 2020 · Q1 Q3 Q5 · access: held · license: cc-by · doi 10.3389/fpsyg.2020.599190
- Tidwell, Tawni L., "Life in Suspension with Death: Biocultural Ontologies, Perceptual Cues, and Biomarkers for the Tibetan Tukdam Postmortem Meditative State," *Culture, Medicine and Psychiatry* (2025) — Tidwell is trained in both Tibetan medicine and anthropology, so this sits *on* the emic/etic seam rather than on one side of it. @tidwell-2025
  `#c/emic-etic #d/tibetan #e/secondary` · subj 2015–24 · src 2025 · Q5 · access: held · license: cc-by
- Namdul, Tenzin, "Death and Happiness: Exploring the Temporalities of the Meditated Death and Everyday Life in Tibetan Buddhist Communities," *Culture, Medicine and Psychiatry* (2025). @namdul-2025
  `#c/death-process #d/tibetan #e/secondary` · subj 2015–24 · src 2025 · Q5 · access: held · license: cc-by

? Does the tukdam literature engage the rainbow body, and if so how does it handle the difference —
a body that fails to decompose versus a body that disappears? Adjacent claims, not identical ones;
how these researchers separate them is directly instructive for §3.

### Terminology (→ `terms.md`)

`'ja' lus` rainbow body · `'od kyi sku` / `'od lus` body of light · `'ja' lus 'pho ba chen po` great transfer · `ring bsrel` relics · `thod rgal` leaping-over · `gzhi` / `ka dag` / `lhun grub` basis, primordial purity, spontaneous presence · `gter ma` treasure.
`#d/dzogchen #c/light-body #e/primary` · Q1 H4

---

## 4. Dzogchen and Chan/Zen

The best-developed contact question in the field, and a rehearsal for the harder ones — because here contact is *undisputed* and only influence is argued. Older scholarship read Dzogchen as Chan-derived; the corrective is a native witness distinguishing them at the moment they were in contact. **Transferable lesson: proximity plus resemblance did not equal derivation.**

### Primary references

- Nubchen Sangye Yeshe, *bSam gtan mig sgron* — distinguishes Chan from Dzogchen doctrinally and soteriologically. @nubchen
  `#d/dzogchen #r/deflation #e/primary` · subj 10c · Q4 · access: unlocated
- Tibetan-language Chan manuscripts from Dunhuang. @dunhuang-chan
  `#d/chan #c/contact-route #e/primary` · subj 8–10c · Q6 · access: open (IDP)

### Potential sources

- van Schaik, Sam, *Tibetan Zen: Discovering a Lost Tradition* @vanschaik-2015
  `#d/chan #r/vector #e/secondary` · subj 8–10c · src 2015 · Q6 · access: purchase
- ——, "Dzogchen, Chan and the Question of Influence" — addresses the methodological question directly. @vanschaik-influence
  `#d/chan #r/deflation #e/secondary` · subj 8–10c · src n.d. · Q4 Q7 · access: open · against: @demieville-1952
- Meinert, Carmen — Chan–Dzogchen Dunhuang manuscript studies. @meinert
  `#d/chan #r/genealogy #e/secondary` · subj 8–10c · src 2002–07 · Q6 · access: library · [unverified]
- Demiéville, Paul, *Le concile de Lhasa* — the classic Samye study; source of the older derivation thesis and a specimen of its period's assumptions. @demieville-1952
  `#d/chan #r/genealogy #e/secondary #s/contested` · subj 792–94 · src 1952 · Q4 · access: library · against: @vanschaik-influence · [unverified]
- Broughton, Jeffrey — early Chan; the *bSam gtan mig sgron*'s doxography. @broughton
  `#d/chan #r/analogy #e/secondary` · subj 8–10c · src 1983–2009 · Q4 · access: library · [unverified]

- Ying, Chinghui Jianying, *Being and Knowing in Wholeness: Chinese Chan, Tibetan Dzogchen, and the Logic of Immediacy in Contemplation* (Rice PhD thesis, 2010) — book-length comparative treatment. A doctoral thesis; weight accordingly. @ying-2010
  `#d/chan #r/analogy #e/inferred` · subj 8–14c · src 2010 · Q4 · access: held · license: public-domain
- Del Toso, Krishna, "sLob dpon gyis bśad pa: Explanation by the Master — The Teachings on Meditation…" (2016) — a Dunhuang-adjacent meditation text in translation. @deltoso-2016
  `#d/chan #f/translation #e/primary` · subj 8–10c · src 2016 · Q4 · access: held · license: unspecified

---

## 5. Nikāya → Mahāyāna

**The cross-check is in `background.md` §5.1** — three corrections (the predecessor is misnamed; the date splits into textual-early and institutional-late; the ascetic→devotional direction is probably inverted) and one confirmation (Kushan/Gandhāra is a real inflection).

### Primary references

- Gāndhārī birchbark manuscripts — oldest surviving Buddhist manuscripts, incl. early Mahāyāna material. **The hard evidentiary floor for the dating.** @gandhari-mss
  `#d/mahayana #f/manuscript #e/primary` · subj 1–2c CE · Q2 · access: open (Gandhāran Buddhist Texts project)
- Lokakṣema's Chinese translations, Luoyang c. 179 CE — the terminus ante quem. @lokaksema
  `#d/mahayana #c/contact-route #e/primary` · subj 179 CE · Q2 · access: library
- Aṣṭasāhasrikā Prajñāpāramitā — the earliest Mahāyāna sūtra layer; Conze's Sophia parallel attaches here. @asta
  `#d/mahayana #c/gnosis #e/primary` · subj 1c BCE–1c CE · Q2 H3 · access: purchase
- *Rāṣṭrapālaparipṛcchā*; *Ugraparipṛcchā* — the ascetic, anti-establishment early Mahāyāna texts. @rastrapala
  `#d/mahayana #c/asceticism #e/primary` · subj 1–2c CE · Q2 · access: purchase
- *Milindapañha* — Indo-Greek and Buddhist exchange in literary form. @milindapanha
  `#d/hellenistic #r/vector #e/primary` · subj c. 100 BCE · Q6 · access: open · [unverified]
- Aśoka, Rock Edict XIII — westward dharma missions. Evidence of *intent*, none of receipt. @asoka-re13
  `#d/nikaya #r/vector #e/primary` · subj c. 250 BCE · Q6 · access: open · [unverified]

### Potential sources

- Drewes, David, "Early Indian Mahayana Buddhism I & II," *Religion Compass* — best short survey of the debate. **Start here.** @drewes-2010
  `#d/mahayana #f/article #e/secondary` · subj 1c BCE–5c CE · src 2010 · Q2 · access: library · [unverified]
- Harrison, Paul (ed.), *Setting Out on the Great Way* — incl. "The Forest Hypothesis." Current state of the question. @harrison-2018
  `#d/mahayana #c/asceticism #e/secondary` · subj 1–3c CE · src 2018 · Q2 · access: purchase · against: @hirakawa-1963
- Nattier, Jan, *A Few Good Men* — close reading of the *Ugraparipṛcchā* against lay-origins. @nattier-2003
  `#d/mahayana #c/asceticism #e/secondary` · subj 1–2c CE · src 2003 · Q2 · access: purchase · against: @hirakawa-1963 · [unverified]
- Boucher, Daniel, *Bodhisattvas of the Forest and the Formation of the Mahāyāna* @boucher-2008
  `#d/mahayana #c/asceticism #e/secondary` · subj 1–3c CE · src 2008 · Q2 · access: purchase
- Schopen, Gregory, *Bones, Stones, and Buddhist Monks* — **the methodological model for this project**; inscriptions and archaeology against normative texts. @schopen-1997
  `#d/nikaya #c/emic-etic #e/secondary` · subj 2c BCE–5c CE · src 1997 · Q2 Q5 · access: purchase
- ——, *Figments and Fragments of Mahāyāna Buddhism in India* @schopen-2005
  `#d/mahayana #c/emic-etic #e/secondary` · subj 2–7c CE · src 2005 · Q2 · access: purchase · [unverified]
- ——, "Mahāyāna in Indian Inscriptions," *IIJ* — the epigraphic-invisibility finding. @schopen-1979
  `#d/mahayana #c/material-culture #e/secondary` · subj 2–8c CE · src 1979 · Q2 · access: library · [unverified]
- ! Hirakawa, Akira, "The Rise of Mahāyāna Buddhism and Its Relationship to the Worship of Stūpas" — the lay-devotional origins thesis. **Displaced, and retained deliberately**: it is the source of the received popular picture, and its persistence is itself a transmission-distortion phenomenon. @hirakawa-1963
  `#d/mahayana #c/asceticism #e/secondary #s/contested` · subj 1–3c CE · src 1963 · Q2 · access: library · against: @harrison-2018
- "Origins of the Mahāyāna," *Indo-Iranian Journal* 63.4 — recent review. @iij-2020
  `#d/mahayana #f/article #e/secondary` · subj 1c BCE–5c CE · src 2020 · Q2 · access: library
- Walser, Joseph, *Nāgārjuna in Context* — Mahāyāna's social and institutional setting. @walser-2005
  `#d/mahayana #c/material-culture #e/secondary` · subj 2–3c CE · src 2005 · Q2 · access: purchase · [unverified]
- Salomon, Richard, *Ancient Buddhist Scrolls from Gandhāra*; *The Buddhist Literature of Ancient Gandhāra* @salomon
  `#d/mahayana #f/manuscript #e/secondary` · subj 1–2c CE · src 1999, 2018 · Q2 · access: purchase · [unverified]

---

## 6. Iconography and the glory complex (H5)

The project's most tractable thread: physical, datable, geographically located. Gandhāran nimbus 1st c. CE; Christian halo only 4th c. CE. The better reading is not Buddhist→Christian transmission but a **shared Iranian–Hellenistic glory complex** feeding both — `#r/homology`, and with no dating obstacle. **Method caution** (`methods.md` §5): a shared visual convention shows contact between *workshops*, not that the doctrines the images illustrate travelled with them.

### Primary references

- Gandhāran Buddha with nimbus, Kushan schist — the object raised in the brief. @gandhara-nimbus
  `#c/iconography #r/homology #e/primary` · subj 1c CE · H5 · access: open (Wikimedia Commons)
- Kaniṣka coinage with haloed Buddha, Bactrian legend *BODDO* — datable, portable, state-issued. **The strongest single evidence class for the motif's currency along trade routes.** @kanishka-coins
  `#d/hellenistic #c/iconography #e/secondary` · subj 2c CE · H5 · access: open (British Museum) · [unverified]
- Sasanian rock reliefs and silver: the ruler's circular nimbus — where *khvarenah* becomes a halo. @sasanian-nimbus
  `#d/iranian #c/iconography #e/secondary` · subj 3–7c CE · H5 · access: open · [unverified]
- "Flaming shoulders" motif, Kushan royal and Buddhist imagery — an Iranian radiance convention entering Buddhist art. **A shared *arbitrary* detail**, which per the §5 ladder counts for more than a shared plausible one. @flaming-shoulders
  `#c/iconography #r/genealogy #e/inferred` · subj 1–3c CE · H5 Q7 · access: open · [unverified]
- Manichaean book illumination, Turfan — documented connection to Syriac and Armenian Gospel illumination. @manichaean-art
  `#d/manichaean #c/iconography #e/secondary` · subj 8–11c · H5 Q6 · access: open (Iranica)

### Potential sources

- *Encyclopaedia Iranica*, "FARR(AH)"; Wikipedia, "Khvarenah" — the Iranian glory concept, Avestan through Middle Persian, and its Sasanian visual expression. @farrah
  `#d/iranian #c/glory #e/secondary` · subj 1200 BCE–7c CE · H5 · access: open
- Wikipedia, "Halo (religious iconography)"; Britannica, "halo (art)" — orientation and starting chronology; follow to specialists before citing. @halo-ref
  `#c/iconography #f/reference #e/inferred` · subj 5c BCE–15c CE · H5 · access: open
- Greco-Buddhist art of Gandhāra; the first anthropomorphic Buddha images. **Calibration case: this is what demonstrable cultural contact leaves behind.** @greco-buddhist
  `#d/hellenistic #c/material-culture #e/secondary` · subj 1–5c CE · Q5 Q7 · access: library

- **Pons, Jessie, "The Buddha and the Sun Disk: Some Reflections on the Dialectics of Light in Gandhāran Art," *Acta Asiatica Varsoviensia* 38 (2025)** — the closest thing yet located to a direct treatment of H5: light as a visual and conceptual problem in Gandhāran art, by a Gandhāra specialist. **Read first.** @pons-2025
  `#d/hellenistic #c/glory #e/secondary` · subj 1–5c CE · src 2025 · H5 · access: held · license: cc-by-nc-sa · doi 10.60018/acasva.xbmi1252
- Tanabe, Katsumi, "Gandhāran Smiling Buddhas Revisited — Farewell to the so-called Archaic Smile" (2023) — a specialist undoing a long-standing misreading of a Gandhāran convention. Method value beyond its subject: a worked case of iconographic over-interpretation being corrected. @tanabe-2023
  `#c/iconography #r/deflation #e/secondary` · subj 1–4c CE · src 2023 · H5 Q7 · access: held · license: cc-by-nc-nd
- Faresin, Emanuela, & G. Salemi, "Buddhist Stele of Swat Valley: Point Cloud Analysis and Interpretation" (2019) — 3D documentation of a Gandhāran stele; method rather than argument. @faresin-2019
  `#c/material-culture #d/hellenistic #e/secondary` · subj 1–5c CE · src 2019 · H5 · access: held · license: cc-by
- Hauser-Ulrich, Johann G., *Deconstructing the Sikri Fasting Buddha: Buddhist Aniconism and…* (MA thesis, Wisconsin–Milwaukee, 2026) — aniconism and its abandonment: when and why the Buddha became depictable. @hauserulrich-2026
  `#d/hellenistic #c/iconography #e/inferred` · subj 1–3c CE · src 2026 · H5 Q2 · access: held · license: unspecified
- Mackenthun, Tamara C., *Continuity in Iranian Leadership Legitimization: Farr-i Izadi, Shi'ism, and…* (Boise State thesis, 2009) — traces *farr* across a very long span. A thesis, and the continuity claim is ambitious; orientation, not authority. @mackenthun-2009
  `#d/iranian #c/glory #e/inferred` · subj 1200 BCE–20c · src 2009 · H5 · access: held · license: unspecified

- **Ravenna** — San Vitale and Sant'Apollinare Nuovo; 6th-c. mosaic programmes executed in Italy under Byzantine patronage. **A documented instance of the artisan channel**: technique and workshop practice moving with craftsmen between Constantinople and the Exarchate. The nearest well-evidenced European analogue to the Gandhāran case, and reached via the *Sarantine Mosaic* lead (§14.4). @ravenna
  `#c/iconography #d/orthodox #e/secondary` · subj 6c CE · H8 H5 · access: open (images) · [unverified]

? Does any Tibetan visual convention for the rainbow body descend from this complex, or is it independent? Tibetan nimbus conventions arrive via India and Central Asia, so the *image* has a traceable route even where the *doctrine* does not — a direct test of the §5 method caution.

---

## 7. Christian primary sources

"Resurrection" is not one doctrine. Pauline `sōma pneumatikon`, the empty-tomb narratives, the Transfiguration, and **post-resurrection persistence** are four distinct things. The persistence material is closest to the great transfer: Jesus repeatedly unrecognised, told not to be held, appearing and vanishing, departing while remaining present. Note the asymmetry (`background.md` §3 Q3): the rainbow body concerns the *material* body's transformation, while the Gospel of Mary's soteriology concerns escaping it — **the two proposed parallels pull in opposite directions.**

### Primary references

- *Gospel of Mary* — BG 8502 (Coptic, incomplete), P.Ryl. 463, P.Oxy. 3525. **Pages 1–6 and 11–14 are missing**; much of any argument built on it is reconstruction. @gosmary
  `#d/gnostic #c/historical-jesus #e/primary` · subj 2c CE · Q1 Q3 · access: open
- 1 Corinthians 15 — `sōma psychikon` / `sōma pneumatikon`. The most philosophically precise Christian statement. @1cor15
  `#d/christian #c/resurrection #e/primary` · subj c. 55 CE · Q1 Q3 · access: open
- Luke 24 (Emmaus, non-recognition); John 20 (*noli me tangere*); Acts 1 (ascension); 1 Cor 15:5–8 — the persistence material. @persistence-texts
  `#d/christian #c/resurrection #e/primary` · subj 1c CE · Q3 · access: open
- Mark 9:2–8 // Matt 17:1–8 // Luke 9:28–36 — the Transfiguration. @transfiguration
  `#d/christian #c/transfiguration #e/primary` · subj 1c CE · Q3 · access: open
- Genesis 5:24 (Enoch); 2 Kings 2:11 (Elijah) — translation without death; the structural analogue to `'pho ba chen po`. @enoch-elijah
  `#d/christian #c/assumption #e/primary` · subj 6c BCE (text) · Q3 · access: open
- *Acts of Thomas*, incl. the *Hymn of the Pearl* — Syriac; the robe of glory; the Thomas-in-India tradition. @acts-thomas
  `#d/syriac #c/glory #e/primary` · subj 3c CE · H5 Q6 · access: open
- Ephrem the Syrian, hymns — Syriac light-and-clothing theology at its richest. @ephrem
  `#d/syriac #c/glory #e/primary` · subj 4c CE · H5 · access: library
- Gregory Palamas, *Triads* — Hesychast defence of the vision of uncreated light; **the closest Christian *practice* tradition to `thod rgal`.** @palamas
  `#d/orthodox #c/transfiguration #e/primary` · subj 14c · Q3 · access: purchase · [unverified]
- *Gospel of Thomas*, *Philip*, *Apocryphon of John*, *Zostrianos*, *Allogenes* — the texts most often invoked in Buddhism comparisons. @nhc-texts
  `#d/gnostic #r/analogy #e/primary` · subj 2–3c CE · H3 · access: open
- Meyer, Marvin (ed.), *The Nag Hammadi Scriptures* — current standard one-volume English collection. @meyer-2007
  `#d/gnostic #f/translation #e/primary` · subj 2–4c CE · src 2007 · H3 · access: purchase · chain: Coptic→En · [unverified]

### Potential sources

- King, Karen L., *The Gospel of Mary of Magdala* — the standard critical treatment with translation. @king-2003
  `#d/gnostic #c/canon-formation #e/secondary` · subj 2c CE · src 2003 · Q1 · access: purchase · [unverified]
- Watterson, Meggan, *Mary Magdalene Revealed* — named in the brief for its account of Jesus's persistence. MTS (Harvard Div.), MDiv (Union); the book sits deliberately between theology and spiritual memoir, and reception splits on exactly that (thin referencing, limited engagement with the text itself, large memoir component). **Read as a contemporary theological reading and a reception document, not as the critical treatment.** Pair with @king-2003. @watterson-2019
  `#d/christian #c/historical-jesus #e/secondary #v/apologetic` · subj 1c CE / 2019 · src 2019 · Q3 · access: purchase
- Pagels, Elaine, *The Gnostic Gospels*; *Beyond Belief* — where the popular framing originates; Pagels was more cautious about Buddhist parallels than her readers. @pagels-1979
  `#d/gnostic #r/analogy #e/secondary` · subj 2–4c CE · src 1979, 2003 · H3 · access: purchase · [unverified]
- de Boer, Esther, *The Gospel of Mary: Beyond a Gnostic and a Biblical Mary Magdalene* @deboer
  `#d/gnostic #c/canon-formation #e/secondary` · subj 2c CE · src 2004 · Q1 · access: library · [unverified]

- Kateusz, Ally, *Mary and Early Christian Women: Hidden Leadership* (Palgrave, 2019) — argues from **art and material evidence** as well as texts, which puts it methodologically closer to §6 than to §7. Open access via OAPEN. @kateusz-2019
  `#d/christian #c/iconography #e/secondary` · subj 1–6c CE · src 2019 · Q1 Q3 · access: held · license: cc-by-nc-nd
- Smith, Daniel A., "Revisiting the Empty Tomb: The Early History of Easter" (2010) — the development of the empty-tomb tradition, i.e. precisely the strand Q3 argues has *no* Dzogchen analogue. @dasmith-2010
  `#d/christian #c/resurrection #e/secondary` · subj 1–2c CE · src 2010 · Q3 H1 · access: held · license: cc-by-nc-nd

? Does the Gospel of Mary actually contain a doctrine of Jesus's continuing presence, or is that supplied by later reading? With pages 1–6 and 11–14 missing this may be undecidable — which would itself be a §14 finding.

---

## 8. Christian scholarship on body, light, and resurrection

Bynum's finding is the indispensable move: Christian resurrection doctrine was for over a millennium preoccupied with *material* continuity, and that preoccupation is what the doctrine is about. It cuts both ways — sharpening the contrast with a rainbow body that dissolves matter, and opening an unexpected convergence with relic culture, incorruptibility and `ring bsrel`. **The relic parallel is less glamorous than the resurrection parallel and probably more real.**

### Potential sources

- Bynum, Caroline Walker, *The Resurrection of the Body in Western Christianity, 200–1336* — **essential**; establishes what the doctrine claimed, the precondition for comparing it. @bynum-1995
  `#d/christian #c/resurrection #e/secondary` · subj 200–1336 · src 1995 · Q1 Q3 H1 · access: purchase · [unverified]
- Martin, Dale B., *The Corinthian Body* — Pauline body-language against Greco-Roman physiology. @martin-1995
  `#d/christian #c/resurrection #e/secondary` · subj 1c CE · src 1995 · Q1 · access: purchase · [unverified]
- Brock, Sebastian, *The Luminous Eye* — Syriac light-theology and the robe of glory; entry point to Syriac studies. @brock
  `#d/syriac #c/glory #e/secondary` · subj 4c CE · src 1985 · H5 · access: purchase · [unverified]
- Williams, Michael A., *Rethinking "Gnosticism"* @williams-1996
  `#d/gnostic #r/deflation #e/secondary` · subj 2–4c CE · src 1996 · H3 · access: purchase · [unverified]
- King, Karen L., *What Is Gnosticism?* — with Williams, the reason "Gnostic" keeps its scare quotes. Both are also case studies in category construction from heresiological polemic. @king-2003b
  `#d/gnostic #r/deflation #e/secondary` · subj 2–4c CE · src 2003 · H3 · access: purchase · [unverified]
- Lossky, Vladimir; Meyendorff, John — Palamism and the uncreated light. @lossky-meyendorff
  `#d/orthodox #c/transfiguration #e/secondary` · subj 14c · src 1944–74 · Q3 · access: library · [unverified]

---

## 9. The Buddhism–"Gnosticism" comparison literature

Conze is the respectable representative: his 1967 *Numen* paper grew from a 1960 Moscow lecture that met such hostility from Indian delegates it reached the front page of *Pravda*. His framing is more careful than his reputation — he compared Mahāyāna to **gnosis**, explicitly not to the Gnostics as a social group. Below him quality falls sharply. Against all of it stands **Barlaam and Josaphat**: the one demonstrated transmission, running Buddhism→Christianity, with the loanword still visible in the saint's name. That is the standard the §10 claims must meet.

### Potential sources

- Conze, Edward, "Buddhism and Gnosis," *Numen* 14 @conze-1967
  `#d/mahayana #r/analogy #e/secondary #s/contested` · subj 1–4c CE · src 1967 · H3 · access: library
- Bianchi, Ugo (ed.), *The Origins of Gnosticism* (Messina, 1966) — where Conze's paper appears, and where the field tried and failed to define "Gnosticism." @bianchi-1967
  `#d/gnostic #r/analogy #e/secondary #s/contested` · subj 1–4c CE · src 1967 · H3 · access: library
- **Barlaam and Josaphat** — Manichaean → Arabic → Georgian → Latin; *bodhisattva* → *Bodisav* → *Iodasaph* → *Josaphat*. See W. C. Smith, *Towards a World Theology*, and the philology on the Georgian *Balavariani*. **The gold standard** (`methods.md` §5). @barlaam
  `#c/contact-route #r/genealogy #e/secondary` · subj 8–11c · src 1981– · H3 Q7 · access: library · [unverified]
- Clement of Alexandria, *Stromata* I.15 — mentions "Boutta." Thin but genuine. @clement
  `#d/hellenistic #r/vector #e/primary` · subj c. 200 CE · H3 · access: open · [unverified]
- ! Lindtner, Christian, *Geheimnisse um Jesus Christus* — Gospels derived from Mahāyāna sūtras. Rejected by specialists; a specimen of method failure. @lindtner
  `#d/mahayana #r/genealogy #e/secondary #s/fringe` · src 1998– · access: library · [unverified]
- ! 19th–20th c. Essene/Therapeutae-Buddhist theories; "Jesus in India" literature. @jesus-india
  `#c/historical-jesus #r/genealogy #e/secondary #s/fringe` · src 1894– · access: open

---

## 10. Diffusion: contact zones and vectors

The Tarim–Gansu corridor, 7th–10th c., held simultaneously: Tibetan administration at Dunhuang (c. 786–848); Manichaeism as Uyghur state religion (763–840) with the Turfan manuscript find; Church of the East monasticism at Bulayïq with Christian Sogdian manuscripts in Syriac script; Sogdian merchant networks; Chinese Buddhism and Chan. **Manichaeism, not Christianity, has the elaborated light-body metaphysics demonstrably present in the right place at the right time** — which makes Christianity an indirect ancestor at best, and may make H5 subsume H2, since Manichaeism is itself downstream of the Iranian glory complex.

### 10.0a What "elaborated light-body metaphysics" means, and why it matters

Added 2026-09-14. **Much of this subsection is prior knowledge, not read from the sources below,
and is marked `[unverified]` accordingly.** It is recorded because §10's central claim rests on it
and the claim was being carried by a phrase.

**The distinction the phrase is doing work for.** Christianity has light *imagery* — the robe of
glory, the transfiguration, uncreated light. Manichaeism has a light *mechanism*: light is a
substance, and the system specifies where it is, how it got there, how it is extracted, by whom,
and where it goes. That difference is what "elaborated" means here, and it is why §10 puts
Manichaeism rather than Christianity in the causal slot.

Its components, as I understand them:

- **Co-eternal Light and Darkness**, and a primordial defeat in which the Light-elements are
  devoured and mixed into matter. The cosmos is machinery built to extract them.
- **The Living Self** — light trapped in matter, including in the human body and in plants.
- **The Column of Glory**, identified with the Milky Way: a visible channel of ascending liberated
  light.
- **The Form of Light** — a luminous figure meeting the soul at death. Structurally close to the
  Zoroastrian *daēnā* at the Chinvat bridge, which is one reason H5's Iranian substrate is the
  better explanation than borrowing.
- **The body as an instrument of release.** The elect's diet, and the three seals of mouth, hands
  and breast, are a technology for liberating light particles rather than a moral code alone.
- **The Last Statue** — the final aggregation of redeemed light at the end of the cosmic process.

**Why this bears on Dzogchen.** `'od lus` is likewise mechanistic: a body is *processed* into
light by a specified practice, not merely described as radiant. The structural match is with the
Manichaean mechanism, not with Christian imagery — which is what makes "Christianity as donor"
the weaker hypothesis even where Christian presence in the corridor is attested.

  `#d/manichaean #c/light-body #e/secondary` · Q6, H2, H5 · [unverified]

? **Is the mechanism/imagery distinction defensible, or is it an artefact of which sources are
elaborated in the surviving record?** Manichaean cosmology survives insystematic doctrinal
compendia; Syriac light-theology survives largely in hymns. Genre may be producing the contrast.
This is `methods.md` §6 deflator 2 — genre convergence — pointed at our own comparison.

### 10.0b The corridor, and what is physically attested on it

**The route.** Ctesiphon and later Baghdad → Merv → Samarkand and Sogdia → Kashgar → the Tarim
oases (Kucha, Turfan, Khotan) → Dunhuang → Chang'an. `geography.md` carries the Q-ids and
coordinates for each.

**Who carried things along it.** Sogdian merchants, whose language was the corridor's lingua
franca; the Manichaean church; the Church of the East. These are not inferred from similarity —
they are attested by their own manuscripts, recovered in situ.

**What is physically attested, and where.** This is rung 4 evidence, and it is why co-presence is
not in doubt:

| Find | Where | What it shows |
|---|---|---|
| Berlin Turfan collection | Turfan / Kocho | Manichaean texts in Middle Persian, Parthian, Sogdian, Uyghur |
| Christian Sogdian manuscripts | Bulayïq | Church of the East monasticism, Syriac script, Sogdian language |
| Xi'an stele, 781 CE | Chang'an | Church of the East established under Tang patronage |
| Chinese Manichaean texts | Dunhuang | Manichaeism presenting itself in Buddhist vocabulary |
| Tibetan administrative and Buddhist documents | Dunhuang | Tibetan presence c. 786–848 |

**The dates line up.** Manichaeism was the Uyghur state religion 763–840; Tibet administered
Dunhuang c. 786–848; the Xi'an stele is 781. The overlap is roughly a century, in one corridor,
with all parties leaving manuscripts.

**The detail that matters most.** In its Chinese texts Manichaeism presents Mani as a **Buddha of
Light**, using Buddhist vocabulary throughout. Buddhist–Manichaean translation at the corridor's
eastern end is therefore not a hypothesis — it is documented, in that direction. `[unverified]`:
I have not read these texts and the titles and 731 date are from memory.

**And §14.8 shows the corridor working westbound.** The Barlaam material moved Sanskrit → Middle
Persian → Arabic → Georgian → Greek → Latin, with a Manichaean recension in the chain. Same
corridor, same actors, opposite direction, and a demonstrated result at rung 1.

  `#d/central-asia #c/contact-route #r/vector #e/secondary`

? **The eastbound mirror has not been worked.** We have a demonstrated westbound transmission and
an attested eastbound channel with the same carriers. What, if anything, came east?

### 10.0 Direction of flow, and which relation is being claimed

Recorded 2026-09-14, from xian's question: are there *any* homologies between Dzogchen and
Christian traditions, and does the flow run Christian → Dzogchen?

**First, the terms, because the project's vocabulary separates what the question joins.** §1.2 and
the `#r/` facet distinguish three claims. *Genealogy* is directional — one derives from the other.
*Homology* is not — both descend from a shared third source. So "is there a homology?" and "does
the flow run Christian → Dzogchen?" are different questions, and the register's current answers
differ: **probably yes to the first, probably no to the second.**

**The standing answer is H5, and it is a homology with no Christian donor.** The
Iranian–Hellenistic glory complex (*khvarenah*, radiate nimbus) is proposed as common ancestor to
Buddhist, Christian, Manichaean and Syriac light-imagery. On that account Dzogchen and Syriac
Christianity are genuinely related — cousins, not parent and child — and neither is the source.

**And §10's own finding narrows it further.** Manichaeism, not Christianity, has the elaborated
light-body metaphysics demonstrably present in the right place at the right time. The Church of the
East *is* attested in the corridor — Bulayïq, Christian Sogdian manuscripts in Syriac script, the
781 Xi'an stele, the Dunhuang Jingjiao documents — so the channel is real. But the tradition
carrying matching metaphysics through it is Manichaean, which makes Christianity an indirect
ancestor at best.

**If a Christian → Dzogchen genealogy is to be tested, chronology dictates its shape.** The most
cited phenomenological parallel — Palamite uncreated light — **cannot be the donor**: Palamas is
14th c., and Dzogchen's earliest datable stratum is c. 10th (`chronology.md`, `nubchen`). The only
chronologically available Christian donors are the **Syriac and East Syrian ascetic-mystical strata
of the 4th–7th c.** — Ephrem's robe of glory, the Macarian and Evagrian material — and those are
precisely the branch present in Central Asia. A hypothesis of this shape is coherent and testable;
one resting on Hesychasm is not, and the direction argument that makes Christian → Dzogchen the
only plausible flow does not rescue it.

**On the reverse direction, the register contains a counterexample.** §14.8 is a *demonstrated*
transmission from Buddhism into Christianity, at rung 1 — the Buddha's life-legend entering
Christian hagiography and the Roman Martyrology by a loanword chain. So "no direct transmission
from Buddhism into Christianity" does not hold as stated. What it does support is a sharper claim,
and a more useful one:

> In the single case where the whole chain is visible, what crossed was a **narrative**, not a
> doctrine; it crossed in the 8th–11th centuries, long after Christian doctrine was fixed; and the
> Christianising process stripped the Buddhist content while preserving only the name.

**The channel was open and doctrine did not cross it.** Any Buddhism → Christianity *doctrinal*
hypothesis now carries a burden it did not before: to explain why doctrine failed to cross in the
one case we can watch end to end.

? **Did the corridor that carried Barlaam west also carry Christian material east?** §14.8 shows it
working westbound, in Manichaean, Arabic and Georgian hands. The eastbound mirror — the same
actors, the same routes, toward Tibet — has not been asked in that form, and it is the form in
which a Christian → Dzogchen hypothesis would have to be evidenced.
? **Does H5 subsume H2?** §10 already suspects it. If the glory complex is the common ancestor and
Manichaeism the proximate carrier, then a direct Christian → Dzogchen claim is doing no work that
H5 does not do better.

### Primary references

- Berlin Turfan Collection; Chotscho finds; Christian Sogdian manuscripts from Bulayïq. @turfan
  `#d/central-asia #c/contact-route #e/primary` · subj 8–11c · Q6 H2 · access: open
- Xi'an ("Nestorian") Stele, 781 CE; Dunhuang Jingjiao documents. @xian-stele
  `#d/syriac #c/contact-route #e/primary` · subj 781 CE · Q6 · access: open

### Potential sources

- BeDuhn, Jason David, *The Manichaean Body: In Discipline and Ritual* — standard study of Manichaean body-theory and practice. @beduhn-2000
  `#d/manichaean #c/light-body #e/secondary` · subj 3–8c · src 2000 · H2 H5 · access: open (PDF)
- Gardner, Iain, & Samuel N. C. Lieu (eds.), *Manichaean Texts from the Roman Empire* @gardner-lieu
  `#d/manichaean #f/translation #e/primary` · subj 3–6c · src 2004 · H2 · access: purchase · [unverified]
- van Schaik, Sam, & Imre Galambos, *Manuscripts and Travellers* — one manuscript reconstructed into a picture of who actually moved along the road. **Model for well-done contact evidence.** @vanschaik-galambos
  `#d/central-asia #r/vector #e/secondary` · subj 10c · src 2012 · Q6 · access: library · [unverified]
- Moffett, Samuel Hugh, *A History of Christianity in Asia*, vol. 1 @moffett
  `#d/syriac #c/contact-route #e/secondary` · subj 1–15c · src 1992 · Q6 · access: purchase · [unverified]
- Dalton, Jacob, *The Taming of the Demons* — Dunhuang, ritual, and the imperial-to-postimperial transition. @dalton-2011
  `#d/tibetan #c/contact-route #e/secondary` · subj 8–11c · src 2011 · Q6 · access: purchase · [unverified]
- ! Palmer, Martin, *The Jesus Sutras* — popular treatment of the Jingjiao material; unreliable interpretive frame. Use the underlying documents. @palmer
  `#d/syriac #r/genealogy #e/secondary #s/fringe` · subj 7–10c · src 2001 · access: purchase · [unverified]

- van Oort, Johannes, "Manichaeism: Its sources and influences on Western Christianity," *Verbum et Ecclesia* 30 (2009) — van Oort is a Manichaeism and Augustine specialist. Bears on H2, though its frame is Manichaeism→West rather than →East. @vanoort-2009
  `#d/manichaean #r/genealogy #e/secondary` · subj 3–6c · src 2009 · H2 · access: held · license: cc-by
- ——, "Augustine and Manichaeism: new discoveries, new perspectives," *Verbum et Ecclesia* 27 (2006). @vanoort-2006
  `#d/manichaean #c/light-body #e/secondary` · subj 4–5c · src 2006 · H2 · access: held · license: cc-by

? **The decisive empirical question of the project:** what documented Tibetan–Manichaean or Tibetan–Christian *textual* contact exists at Dunhuang, as opposed to co-presence in one oasis? Co-presence is rung 5 on the §5 ladder — opportunity only.

---

## 11. Nexus, contact zone, and syncretic innovation (Q8)

### 11.1 Narrative summary

Serves Q8: what makes a contact zone generative rather than merely busy. Two literatures have to be
brought together, and neither cites the other. On one side, the ancient historians and archaeologists
of the caravan cities and Silk Road entrepôts — Rostovtzeff's *Caravan Cities* (1932) is the founding
comparative attempt and is still the closest thing to a precedent for the comparison-class method
`background.md` §5.3 requires. On the other, the modern literature on creative clusters and urban
innovation, which has the causal question but no premodern cases.

**A retrieval finding first, because it governs how this section can be built.** A dedicated
OpenAlex pass (queries `40-`–`51-`, see `lit/openalex/QUERIES.md`) returned almost nothing usable:
four hits for Kushan trade, one for Begram, zero for Greco-Buddhist art, zero for "contact zone"
in any relevant sense. The literature that matters here is **monographs**, and they are not indexed
with full text. Most entries below are therefore `access: library` or `unlocated` and carry
`[unverified]` — named from prior knowledge as acquisition targets, not as consulted sources. That
is an honest state for a section opened one day ago; it should not be mistaken for coverage.

**The negative case is the priority.** Dunhuang is the matched comparison for Gandhāra
(`background.md` §5.3) and the only one already inside this project: exceptional co-presence that
produced a library rather than a synthesis. Rong Xinjiang's lecture on why the cave was sealed is
the single most targeted item in this section.

### 11.2 Primary references

- The **Begram** deposit — Roman glass, Chinese lacquerware, Indian ivories, Alexandrian bronzes in two sealed 1st–2nd c. storerooms (DAFA, 1936–40). The material core of the Q8 case. @begram
  `#d/central-asia #c/material-culture #e/primary` · subj 1–2c CE · Q8a · access: unlocated (publication)
- **Kushan coinage** — Iranian, Greek, Indian and Buddhist figures from one mint; Bactrian legends in Greek script. Evidence of a state operating four religious vocabularies simultaneously, i.e. of precondition (2). @kushan-coins
  `#d/iranian #c/iconography #e/primary` · subj 1–3c CE · Q8a H7 · access: open (museum catalogues)
- **Rabatak inscription** (found 1993) — Bactrian; Kaniṣka's genealogy and royal titulary. @rabatak
  `#d/central-asia #c/loanword #e/primary` · subj c. 127 CE · Q8a · access: library · [unverified]
- **The Ancient Sogdian Letters** (c. 313 CE, Dunhuang) — merchant correspondence; the Sogdian network in its own voice. @sogdian-letters
  `#d/central-asia #c/contact-route #e/primary` · subj c. 313 CE · Q8a · access: library
- **The Dunhuang library cave** (Mogao Cave 17), sealed c. 1000 — the negative case's central object. @dunhuang-cave
  `#d/central-asia #c/material-culture #e/primary` · subj 5–11c · Q8a · access: open (IDP)

### 11.3 Potential sources

- Rostovtzeff, M. I., *Caravan Cities* (1932) — Petra, Jerash, Palmyra, Dura-Europos compared as a class. **The precedent for the comparison-class method**; dated, and its assumptions are of its period, but nothing has replaced its comparative ambition. @rostovtzeff-1932
  `#c/nexus #r/analogy #e/secondary #s/contested` · subj 1–3c CE · src 1932 · Q8a · access: library · [unverified]
- **Rong Xinjiang, "The Nature of the Dunhuang Library Cave and the Reasons for its Sealing,"** and *Eighteen Lectures on Dunhuang* (Brill) — **the highest-value item in this section.** Directly addresses why Dunhuang's co-presence produced preservation rather than synthesis. @rong-dunhuang
  `#d/central-asia #c/material-culture #e/secondary` · subj 5–11c · src 2013 · Q8a · access: library · [unverified]
- Galambos, Imre, *Dunhuang Manuscript Culture: End of the First Millennium* — manuscript practice at the negative case. @galambos-2020
  `#d/central-asia #f/manuscript #e/secondary` · subj 9–11c · src 2020 · Q8a · access: library · [unverified]
- de la Vaissière, Étienne, *Sogdian Traders: A History* (Brill) — the standard work on the network that **transmitted without innovating**, which is the distinction Q8 turns on. @delavaissiere
  `#d/central-asia #c/contact-route #e/secondary` · subj 3–10c · src 2005 · Q8a H7 · access: library · [unverified]
- Mairs, Rachel (ed.), *The Graeco-Bactrian and Indo-Greek World* (Routledge, 2020) — includes a chapter on Roman objects in the Begram hoard and the memory of Greek rule. The 450-year Hellenistic time-depth behind H8 is this volume's subject. @mairs-2020
  `#d/hellenistic #c/material-culture #e/secondary` · subj 300 BCE–200 CE · src 2020 · Q8a H8 · access: library
- Smith, Andrew M., *Roman Palmyra: Identity, Community, and State Formation* (2014) — the fullest treatment of the clearest negative case outside Asia. @smith-palmyra
  `#d/hellenistic #c/material-culture #e/secondary` · subj 1–3c CE · src 2014 · Q8a · access: library · [unverified]
- Kodama, Shinjiro, "The Palmyrene commercial settlement in Vologesia" (1965) — a Palmyrene trading colony on Parthian territory; small-scale evidence of how a caravan city projected itself outward. @kodama-1965
  `#d/hellenistic #c/contact-route #e/secondary` · subj 1–3c CE · src 1965 · Q8a · access: held · license: unspecified
- Denisenko, V. L., "Kushan Settlement Complexes in the Kashmir Valley," *Vestnik NSU* (2024) — settlement archaeology at the Kushan periphery. @denisenko-2024
  `#d/central-asia #c/material-culture #e/secondary` · subj 1–4c CE · src 2024 · Q8a · access: held · license: unspecified
- Jia, Ben, "Reading Hierarchy on the Silk Road — The Ancient Sogdian Letters," *Communications in Humanities Research* (2025) — social structure inside the Sogdian network. @jia-2025
  `#d/central-asia #c/contact-route #e/inferred` · subj c. 313 CE · src 2025 · Q8a · access: held · license: unspecified
- Hall, Peter, *Cities in Civilization* (1998) — the modern comparative treatment of urban creative episodes; explicitly asks Q8a, entirely for post-classical cases. Its hazard is the one `background.md` §5.3 names: it samples on the dependent variable throughout. @hall-1998
  `#c/nexus #r/analogy #e/secondary #s/contested` · subj 400 BCE–1990s · src 1998 · Q8a · access: library · [unverified]
- Jacobs, Jane, *The Economy of Cities* (1969) — the argument that cities generate novelty through recombination of existing work. Theoretical, unfalsifiable as stated, but the source of the intuition. @jacobs-1969
  `#c/nexus #r/analogy #e/secondary #s/speculative` · src 1969 · Q8a · access: purchase · [unverified]

### 11.3a Dunhuang — Q8a's negative case, and what the harvest turned up

Added 2026-08-27 from the Wikipedia citation harvest (`lit/wikipedia/`). Both entries are
**unread**; they are recorded so the acquisition state is legible, not because they have been used.

- Rong, Xinjiang. "The Nature of the Dunhuang Library Cave and the Reasons for its Sealing."
  *Cahiers d'Extrême-Asie* 11 (1999). DOI [10.3406/asie.1999.1155](https://doi.org/10.3406/asie.1999.1155).
  **The named target for Q8a.** Why Cave 17 was sealed governs what its contents are evidence *of*:
  a deliberate deposit and an abandoned store license different inferences from the same documents,
  and §14.7's survivorship problem turns on which it was. @rong-1999
  `#c/nexus #d/central-asia #e/secondary` · subj c. 1000 · src 1999 · Q8a · access: **wanted** — Persée refused · [unverified]
- Ponampon, Phra Kiattisak. *Dunhuang Manuscript S.2585: A Textual and Interdisciplinary Study on
  Early Medieval Chinese Buddhist Meditative Techniques and Visionary Experiences.* PhD thesis,
  Univ. of Cambridge, 2019. DOI [10.17863/CAM.31982](https://doi.org/10.17863/CAM.31982).
  Sits on the intersection of Q8a and `#c/thodgal` — visionary practice attested in a Dunhuang
  manuscript, supervised by a Dunhuang specialist. Retrieved in full. @ponampon-2019
  `#c/thodgal #d/central-asia #e/secondary` · subj C6–C8 · src 2019 · Q8a, Q4 · access: **held** · [unverified]

? **Does S.2585 bear on `thod rgal` or only on Chinese Buddhist visualisation?** The distinction is
the whole question. A shared vocabulary of visionary experience at Dunhuang is rung 5 (co-presence)
at best until someone shows the practices are related rather than merely adjacent — precisely the
error `methods.md` §5 exists to prevent, and precisely the inference the material invites.

### 11.3b Preconditions for a nexus — xian's, 2026-08-25, recorded 2026-09-15

**Recorded late**: given in August, and not carried into the register until an audit found them
missing. They bear directly on Q8, and one of them is an objection rather than a contribution.

**The proposal.** A **small-world / preferential-attachment network** — of trade, communication,
finance, artisans — is a *prerequisite* for a nexus to have widespread impact. Connectivity, and
cultural hegemony with it, is what drives the **diffusion** that leaves measurable evidence behind.

Consistent with **Geoffrey West's metabolic-scaling work on cities**, offered with its own caveat:
the work has structural problems, but it states mechanistic, refutable null hypotheses, which is
more than the qualitative nexus literature manages. That is the reason to keep it in view — a bad
model that can be refuted is worth more here than a good description that cannot.

**The objection, which is the sharper half.** *Rome, Washington and Beijing are highly connected
and are not workshops of innovation.* They are **administrative cities**, where bureaucracy,
orthodoxy, tradition and convention push against innovation despite high diversity. So:

> **Connectivity is necessary but not sufficient.** Any account of Q8 that predicts generativity
> from connection alone is refuted by the administrative capitals.

This is a live constraint on H7 and H12, and the project had been proceeding without it.

**The ecological framing offered with it**: administrative capitals have **low alpha diversity and
high beta diversity** — many distinct groups, little mixing within any one setting. The proposed
additional condition is **persistent alpha diversity across culturally relevant timescales**:
long-standing cross-cultural contact that makes familiarity ordinary, so that a New Yorker is
comfortable in Little Italy and Chinatown alike. Slave caregiving (§11.4) is then *one* pathway
that supplies both mixing and the persistence needed for re-transmission — one example, not the
mechanism.

  `#c/nexus #d/method #e/inferred` · H7, H12, Q8 · access: n/a · [unverified]

? **Does the alpha/beta framing survive contact with the cases?** It predicts that a nexus needs
sustained mixing *within* settings rather than mere co-presence of groups — which is exactly the
rung-5 problem (`methods.md` §5) restated for populations rather than texts. Gandhāra and Dunhuang
should be scored on it.
? **Is "administrative city" the right category, or is it a proxy?** Rome was generative earlier in
its history, and Baghdad was both administrative and a translation centre (§14.8). The variable may
be the *age* of the bureaucracy rather than its presence.
? **Geoffrey West's scaling work is unread and uncited here.** Named in August, never retrieved.

### 11.4 Transmission channels: how fusion actually happens

Serves H8 and H9. The linguistic literature supplies both the mechanism and a measurement.

- **Thomason, Sarah G., & Terrence Kaufman, *Language Contact, Creolization, and Genetic Linguistics* (1988)** — the borrowing scale: lexical borrowing indicates casual contact, structural borrowing indicates sustained intimate contact. **The operational instrument for H8**, converting "how deep was the contact" into a question about grammar rather than impression. @thomason-kaufman-1988
  `#c/loanword #d/method #e/secondary` · subj n/a · src 1988 · Q8a H8 · access: library · [unverified]
- Spinney, Laura, *Proto* — the source of the household/market observation as it entered this project: conservative kinship and nature vocabulary against volatile technological vocabulary. @spinney-2025
  `#d/indo-european #c/loanword #e/secondary` · subj 4500 BCE– · src 2025 · Q8a H8 · access: held
- Metal names and the Indo-European dispersal — `*h₂éyos` (copper/bronze) is reconstructible, while iron, tin and lead terms commonly derive from non-IE sources, and "metal" is a wanderwort shared across IE, Uralic, Turkic and sometimes Old Chinese. **The evidence that the split is real and not merely intuitive.** @metal-names
  `#d/indo-european #c/loanword #e/secondary` · subj 4000–1000 BCE · Q8a · access: open (academia.edu) · [unverified]
- Creolization and the Atlantic world; Gullah as a creole; jazz and foodways as non-linguistic fusion products. **The type specimen for household-channel fusion, and a warning that it can occur under coercion.** @creolization
  `#c/loanword #r/homology #e/secondary` · subj 17–20c · Q8a H8 · access: unlocated · [unverified]
- **Origo, Iris, "The Domestic Enemy: The Eastern Slaves in Tuscany in the Fourteenth and Fifteenth Centuries," *Speculum* 30 (1955), 321–66** — enslaved Tatars, Russians, Circassians, Greeks, Moors and Ethiopians in Florentine households, predominantly women, raising the children. **The only household channel Florence has**, and its cultural consequences appear unstudied. @origo-1955
  `#c/nexus #d/method #e/secondary` · subj 14–15c · src 1955 · Q8a H9 · access: library · [unverified]
- **Jones-Rogers, Stephanie E., *They Were Her Property: White Women as Slave Owners in the American South* (Yale UP, 2019)** — documents a market in enslaved wet nurses created by slaveholding white women and advertised in newspapers, a sector she describes as largely invisible. **The clearest evidence that the household channel was operated by the enslaved**, at scale, at the exact moment of children's language acquisition. @jonesrogers-2019
  `#c/nexus #d/method #e/secondary` · subj 1800–65 · src 2019 · Q8a H8 · access: purchase · [unverified]
- Harris, Joel Chandler, *Uncle Remus* (1880), and the West African Anansi/hare cycles behind it — a documented instance of the household channel: trickster tales carried by enslaved caregivers to white children. Harris's framing device *is* a description of the mechanism; his distortions are a separate problem. @uncle-remus
  `#c/lineage-narrative #r/genealogy #e/secondary #s/contested` · subj 18–19c · src 1880 · Q8a H8 · access: open · [unverified]
- Carney, Judith, *Black Rice: The African Origins of Rice Cultivation in the Americas* (2001) — a **technical** transfer via enslaved knowledge, i.e. the market/workshop channel rather than the household one. Useful precisely because it lets the two channels be distinguished in one society. @carney-2001
  `#c/material-culture #r/genealogy #e/secondary #s/contested` · subj 17–18c · src 2001 · Q8a H8 · access: library · [unverified]
- The AAVE-origins debate — creolist versus Anglicist accounts (Mufwene, Rickford, Poplack); and the question of African substrate features in white Southern speech. **The direct linguistic test of household-channel transmission**, and still contested. @aave-origins
  `#c/loanword #r/genealogy #e/secondary #s/contested` · subj 17–20c · Q8a H8 · access: library · [unverified]
- Lowe, Kate, & T. F. Earle (eds.), *Black Africans in Renaissance Europe* (CUP, 2005); and the "Rethinking 'Domestic Enemies': Slavery and Race Formation in Late Medieval Florence" literature. The Florentine end of the same question. @lowe-earle-2005
  `#c/nexus #d/hellenistic #e/secondary` · subj 14–16c · src 2005 · Q8a H9 · access: library · [unverified]
- ! Alessandro de' Medici's maternity — **contested**. Spini traces Simonetta da Collevecchio to the Roman peasantry; Nestor (1560s) reports the African-servile origin as a rumour circulated by Alessandro's exiled enemies; Hibbert and Brackett accept it. Catalogued as a case of ancestry claims generated as political weapons, **not** as evidence for the household channel. @alessandro
  `#c/nexus #r/deflation #e/secondary #s/contested` · subj 1510–37 · Q8a · access: open · [unverified]
- Florentine banking diaspora (Bardi, Peruzzi, Medici branches at London, Bruges, Avignon, Lyon) and the Council of Ferrara-Florence 1438–39 → Gemistos Plethon → Ficino. **Florence's contact runs outward and arrives late and elite** — the evidence behind H9's *diaspora-return* type. @florence-contact
  `#c/nexus #r/analogy #e/inferred` · subj 13–15c · Q8a H9 · access: library · [unverified]

- **Schafer, Edward H., *The Golden Peaches of Samarkand: A Study of T'ang Exotics* (1963)** — a catalogue of what actually moved into Tang China: goods, plants, animals, drugs, textiles, people. **The market-channel evidence base for the best-documented East Asian nexus**, and directly comparable to Begram in kind. Reached via the *Under Heaven* lead (§14.4). @schafer-1963
  `#d/central-asia #c/material-culture #e/secondary` · subj 7–9c · src 1963 · Q8a H8 · access: library · [unverified]
- **Tang Chang'an** as a comparison case — Buddhism, Nestorian Christianity, Manichaeism and Zoroastrianism all institutionally present; Chan emerges as a genuine synthesis; and the **Huichang persecution of 845 closes it**. A positive case with a datable termination, which few of the others have. @changan
  `#c/nexus #d/chan #e/secondary` · subj 7–9c · Q8a Q6 · access: library · [unverified]
- **al-Andalus** as a comparison case — the three-faith society, and the Greek→Arabic→Latin translation movement that carried philosophy across a religious boundary. A test for H7: doctrine *and* method crossed here, which the institutional-freeze reading has to accommodate. @al-andalus
  `#c/nexus #r/genealogy #e/secondary #s/contested` · subj 8–13c · Q8a H7 · access: library · [unverified]
- Nirenberg, David, *Communities of Violence* (1996) — argues that coexistence and systematic violence in medieval Iberia were **one system, not alternatives**. The corrective to any harmonised reading of *convivencia*, and a warning that "generative contact zone" may describe places that were also extremely violent. @nirenberg-1996
  `#c/nexus #r/deflation #e/secondary` · subj 13–14c · src 1996 · Q8a · access: library · [unverified]

- **Van Valen, Leigh, "A New Evolutionary Law," *Evolutionary Theory* 1 (1973)** — log-linear taxonomic survivorship curves implying extinction probability essentially independent of age. The origin of the memorylessness claim; contested, with age-dependence counterexamples in later paleobiology. @vanvalen-1973
  `#c/nexus #d/method #e/secondary #s/contested` · subj n/a · src 1973 · Q8a H10 · access: open · [unverified]
- **Arbesman, Samuel, "The Life-Spans of Empires," *Historical Methods* 44:3 (2011)** — tests the claim directly on polities: N = 41 empires over three millennia, lifespans fitting a **memoryless exponential distribution**, collapse rate independent of age. **The load-bearing citation for H10**, and the reason "they all ended" cannot be treated as informative. Small N. @arbesman-2011
  `#c/nexus #d/method #e/secondary` · subj 3000 BCE–2000 CE · src 2011 · Q8a H10 · access: open (PDF)
- **Norse–English contact and the Danelaw** — borrowing of the third-person plural pronouns (*they, them, their*) alongside core vocabulary and place-name elements. Pronoun borrowing sits near the top of the Thomason–Kaufman intensity scale: **the clearest available signature of household-level fusion**, and the comparison class's only *non-terminated* case. @norse-english
  `#c/loanword #r/genealogy #e/secondary` · subj 865–1100 · Q8a H8 · access: library · [unverified]
- Kay, Guy Gavriel, *The Last Light of the Sun* (2004) — Norse, Anglo-Saxon and Celtic Britain. The lead that surfaced the Danelaw as Q8a's missing case. @kay-lastlight
  `#c/nexus #d/method #e/heuristic` · subj 9–10c · src 2004 · Q8a · access: purchase

? **What did Dunhuang's co-presence actually produce?** The project needs this answer twice over —
for Q8a as the negative case, and for §10, where the contact argument depends on it. If Dunhuang
held Manichaeans, Church-of-the-East monks, Tibetan administrators and Chan translators in one oasis
for sixty years and produced no doctrinal synthesis, that is strong evidence for H7 and a serious
problem for H2.

### 11.5 Eco-evolutionary analogies (heuristic only)

Everything here is tagged `#e/heuristic`: real scholarship, used analogically, establishing **nothing
about culture**. The `#e/` facet records *use*, not quality. Importing population-biology models into
cultural history has a poor record — social Darwinism, crude memetics — and the specific disanalogies
are severe: cultural transmission is Lamarckian (acquired traits inherit), heavily horizontal, and
intentional. Treated as sources of questions, they are nonetheless unusually well matched to Q8.

**Mapped to the right hypotheses**, which are not all the same one:

- **Gould, Stephen Jay, *Wonderful Life* (1989)** — maximal *disparity* early, decimation after, and survival as substantially **contingent**. **The contingency claim must be split**: it governs *how* a radiation resolved — which lineages won, when — far more than *whether* one occurred. So it maps onto **Q8b** (which of many syntheses propagated is contingent) and **not** onto whether a zone is generative at all, which is structural. My earlier mapping onto H10 conflated the two. @gould-1989
  `#c/nexus #d/method #e/heuristic` · subj 505 Ma · src 1989 · H10 Q8b · access: purchase · [unverified]
- **Conway Morris, Simon, *Life's Solution: Inevitable Humans in a Lonely Universe* (2003)** — the direct rebuttal: **convergence, not contingency**, is the hallmark of evolutionary history; replay the tape and you get similar outcomes because the adaptive space is constrained. @conwaymorris-2003
  `#c/nexus #r/deflation #e/heuristic` · subj 505 Ma– · src 2003 · Q8a · access: purchase · against: @gould-1989 · [unverified]
- **May, Robert M., "Will a Large Complex System Be Stable?" *Nature* 238 (1972)** — in *random*-interaction models, increasing diversity and connectance destabilises. **Best used here as a null model, not an analogue.** Its value in ecology was never that real systems behave this way — the diversity–stability paradox is that they often do not — but that it forces you to say what structure real systems have that random ones lack. Transposed, the useful question is not "does plurality destabilise polities" but **"what structure does a persistent plural polity have that a random one would not?"** @may-1972
  `#c/nexus #d/method #e/heuristic` · subj n/a · src 1972 · Q8a · access: open · [unverified]
- **Intermediate disturbance hypothesis** (Connell 1978 and successors) — diversity peaks at *intermediate* disturbance: too little and competitive exclusion sets in, too much and only pioneers persist. The analogue behind **H11**. @connell-1978
  `#c/nexus #d/method #e/heuristic` · subj n/a · src 1978 · Q8a H12 · access: library · [unverified]
- Van Valen (1973) and the Red Queen — already entered at §11.4 for H10; the constant-hazard result belongs to this family. @vanvalen-1973
  `#c/nexus #r/analogy #e/heuristic` · src 1973 · H10 · access: open

- **Cambrian drivers — the ecological question, not the contingency one.** Current accounts combine (i) **unoccupied ecospace**, where limited species interaction let poorly-optimised body plans briefly persist; (ii) **predation and escalation**, the origin of durophagy and motile predators driving biomineralisation and defence; and (iii) **developmental innovation** in gene regulatory networks. The consolidation afterwards is the part that matters most here: **conservation of lineage-specific GRN kernels** is the standard explanation for why body plans froze and disparity never recurred. @cambrian-drivers
  `#c/nexus #d/method #e/heuristic` · subj 540–485 Ma · Q8a H12 H13 · access: open · [unverified]
- **Sperber, Dan, *Explaining Culture* (1996); Claidière & Sperber, "What are cultural attractors?"** — cultural attraction theory: transmission is **transformation rather than replication**, and distributions are shaped by attractors — variants that reconstruction reliably converges on. **Explicitly criticises the faithful-transmission assumption memetics requires.** The developed scholarly form of the analog-channel position (`methods.md` §1.2a). @sperber-attractors
  `#c/loanword #r/deflation #e/secondary` · src 1996, 2017 · Q7 H8 · access: open · [unverified]
- **Vedic *vikṛti pāṭha*** — *krama*, *jaṭā*, *ghana* and the other permutation recitations: **literal error-detecting codes**, redundancy purchased at high training cost by a tradition needing centuries of fidelity without writing. The extreme confirming case for `methods.md` §1.2b. @vedic-patha
  `#d/nikaya #c/translation-layer #e/secondary` · subj 1000 BCE– · Q7 H7 · access: library · [unverified]

- **Virulence–transmission tradeoff** — who bears the cost of a parasite's reproduction is frequency-dependent; high virulence damages the host population and feeds back as a cost to the parasite. **Transposed to culture it does not work, and H14 has been reformulated without it.** Two failures: (i) parasite virulence is a *byproduct* of within-host replication, whereas a doctrine's demands may be its content rather than a side-effect of spreading; (ii) the sign is wrong — see @iannaccone-1994. Retained as a worked example of an analogy that looked apt and was not. @virulence-tradeoff
  `#c/nexus #r/deflation #e/heuristic` · subj n/a · Q2 H14 · access: library · [unverified]
- **Iannaccone, Laurence R., "Why Strict Churches Are Strong," *American Journal of Sociology* 99:5 (1994), 1180–1211**; and "Sacrifice and Stigma," *JPE* 100:2 (1992) — costly demands **screen out free-riders and raise participation among those who remain**, so strictness makes groups stronger. Directly contradicts the naive reading in which demand caps spread. @iannaccone-1994
  `#c/nexus #r/deflation #e/secondary` · subj 20c · src 1992, 1994 · H14 · access: open · [unverified]
- **The Shakers** — mandatory celibacy left growth dependent entirely on conversion and adoption; peak membership around 6,000 in the 1840s, now effectively extinct. **The extinction branch of H14**, and a case where demands were *not* moderated. Also xian's correction that the cap can be biological, not merely social. @shakers
  `#c/nexus #d/christian #e/secondary` · subj 1770–present · H14 · access: library · [unverified]
- **Network effects and scale economies** — the right frame for "a common doctrine has infrastructure that amortises cost," which is economics rather than epidemiology. Demand-side network effects (a shared vocabulary is worth more the more people hold it) and supply-side scale economies (schools, copied texts) are distinct mechanisms and should not be merged. @network-effects
  `#c/nexus #d/method #e/heuristic` · subj n/a · H14 · access: library · [unverified]

**The debate is a pre-run of this project's own.** Gould's contingency and Conway Morris's
convergence are, structurally, H10 versus the Q8a preconditions programme: is generativity a lucky
draw, or does it follow reliably from conditions? That argument has run in paleobiology for
thirty-five years without resolution, on a far better evidentiary base than Q8a will ever have —
which is a sobering estimate of how tractable Q8a is, and an argument for prioritising Q8b.

→ **A cross-link back to the main inquiry.** Conway Morris's convergence is the biological form of
this project's deflator 4: similar conditions independently producing similar outcomes, no contact
required. The nexus programme and the Dzogchen inquiry turn out to share an opponent.

---

### 11.6 Diaspora as a mechanism

Promoted from "marked for inspection" to a first-class mechanism 2026-08-27 (`background.md` §11).
Treated as a **mechanism in H9's typology**, not as a condition on the others.

**The decision, and what it forecloses.** This was settled by decision rather than by finding. If
the material shows diaspora behaving as a cross-cutting condition on the other channels instead of
a channel in its own right, that is a result about the typology and must be recorded as one — not
absorbed silently into the section that assumes otherwise. Stated here so the assumption stays
visible.

**The discriminator: transmitter versus innovator.** H11 asserts that diasporas incite *observable
diffusion of innovation*. A network that carries three religions across a continent without altering
any of them is doing something real, but it is not that.

**Mount Athos is the newest specimen and the cleanest.** §14.8's chain passes through a Georgian
monastic community inside a Greek institution: Euthymius of Athos, a Georgian, translating into
Greek a text that reached him through Arabic from Middle Persian from Sanskrit. A diasporic
institution is the transmission node, and — unlike the Sogdian case — we can see exactly what it
altered, because the before and after both survive. It is the section's worked example precisely
because the alteration is legible. **§11.6b reclassifies what kind of example it is**: a
converter rather than a carrier, which is why it innovates in content without its origin link
having been cut.

**Why the household case is the type specimen.** §11.4 argues that the household channel transmits
what commerce cannot, because it operates across a generational boundary rather than a
transactional one. The African diaspora in the American Southeast is the case where this is least
deniable and best documented, and where the asymmetry of power makes "network" an inadequate
description. It anchors the section; the mercantile cases are read against it, not the reverse.

**Answered 2026-09-14, in the negative** — endogamy is a proxy for a maintained origin link, not
the cause. See §11.6a. Kept here because the question shaped the table that produced the answer.

### 11.6a The sort, done 2026-09-14

**The axis does not sort diasporas. It sorts diaspora × domain.** Every specimen below both
transmits and innovates — but in different registers, and the pattern in which register is the
finding.

| Specimen | Innovated in | Transmitted faithfully in | Link to origin | Tag |
|---|---|---|---|---|
| Maghribi traders | **institutions** — a multilateral reputation mechanism enforcing contracts without a sovereign | goods, and the law they carried from home | maintained | `#c/diaspora #d/method #e/secondary` |
| Armenians of New Julfa | **institutions** — commercial law, courts, a commenda-type contract, standardised correspondence | liturgy, language, confession | maintained | `#c/diaspora #e/secondary` |
| Sogdian network | **script** — the Sogdian alphabet, ancestor of Uyghur and so of Mongolian and Manchu | doctrine: Buddhist, Manichaean, Christian and Zoroastrian texts were translated and carried, not reworked | maintained | `#c/diaspora #d/central-asia #e/secondary` |
| Georgian monks at Athos | **content** — the Barlaam narrative was Christianised in transit (§14.8) | the narrative's structure and the name | maintained | `#c/diaspora #r/genealogy #e/secondary` |
| African diaspora, US Southeast | **content, decisively** — new languages, musics, religious forms | fragments only | **severed** | `#c/household-channel #e/secondary` |

**The pattern, and the mechanism proposed for it.** Four of five innovated in the *infrastructure of
exchange* — script, contract, court, reputation — while carrying content faithfully. Only the fifth
rebuilt content itself, and it is the only one whose link to origin was cut.

The proposed mechanism, **which is my inference and not something read in the sources below**: a
maintained link to origin is an error-correction channel in `background.md` §5.6's sense. You can
check your version against the source, and the check is cheap because the source still exists and
you can reach it. Under that regime, fidelity in content is also an *asset* — a trade diaspora's
value is partly that it is authentically from elsewhere, so altering the goods destroys the margin.
Sever the link and both conditions vanish at once: no check is available, and there is no origin
left for authenticity to refer to. Reconstitution from fragments is then not drift but the only
option, and it necessarily produces something new.

The exchange infrastructure is the mirror image. There the diaspora faces a problem **no home
institution has solved for it** — enforcing agreements at distance, across jurisdictions, with no
sovereign in common. Nothing can be transmitted because nothing exists to transmit, so it must be
invented. Greif's Maghribi coalition is the worked case.

? **This predicts a natural experiment that has not been looked for**: a single diaspora that loses
its origin link mid-history should switch from content-transmitter to content-innovator. Post-1453
Greeks, post-1492 Sephardim and the Parsis are candidates.
? **Endogamy is a proxy, not a cause.** The table's old endogamy column tracked the pattern because
high endogamy accompanies a maintained origin link — but the African diaspora was endogamous by
coercion while severed, and it innovated most. Link-to-origin explains both columns; endogamy
explains neither on its own. This supersedes the question asked when the section opened.

**What this does to H11.** The hypothesis holds for *diffusion* and needs narrowing for
*origination*: diasporas reliably diffuse innovation, but originate it in exchange infrastructure
rather than in content — except where the origin link is severed, which inverts the result. → see
the restatement in `background.md`.

### 11.6b What counts as a diaspora, and what Athos actually shows

**Working definition, xian's, adopted 2026-09-14: a diaspora is a dispersed community *embedded in
another culture*.** Embedding does the work that "dispersion" alone does not. It excludes a settler
population that displaces its host rather than living inside it, and a nomadic group passing
through without becoming resident — neither of which faces the problem that makes diasporas
interesting here, which is maintaining an identity while dependent on a host that does not share it.

**Applied to the Athos anomaly, the definition does not exclude the case — it reclassifies it.**
The Georgian monks were embedded, so they qualify. What distinguishes them is *which dimension*
they were embedded across relative to the material they moved. They were other than their hosts in
**language** and the same in **confession**. The Barlaam material was religious. So at the receiving
end it faced no confessional boundary at all — only a translation.

That makes Athos a different **role**, not a counterexample:

| Role | Material moves | Example |
|---|---|---|
| **carrier** | home content → host setting, boundary crossed at delivery | Sogdians carrying four religions into Tang China |
| **converter** | foreign content → the frame the diaspora *shares with its host* | Georgian monks turning an Arabic-derived tale into Orthodox hagiography |

A converter must remake content by construction: its whole function is to move material into a frame
it already occupies. So content innovation at Athos is not the mechanism failing but a different
operation, and §11.6a's prediction applies to carriers.

? **Is the carrier/converter distinction general, or an artefact of this one case?** It predicts
that any diaspora acting as a translation bureau — Baghdad's Syriac translators, the Toledo school
— will innovate in content regardless of its origin link.

### 11.6c Two specimens that test the mechanism — xian's, 2026-09-14

**Ashkenazi Jewry, before and after 1945 — the natural experiment, supplied.** §11.6a asked for a
diaspora that loses its origin link mid-history. This is a better instance than the candidates
listed there, on three counts: the severance is **sharp and datable** rather than gradual; it
severs by *annihilation of the source community* rather than by distance, so the break is total;
and both sides are documented in extraordinary depth.

The mechanism predicts a switch of register at the break, and the prediction appears to hold:

| | Before | After |
|---|---|---|
| Content | transmitted — Yiddish letters, rabbinic continuity, liturgy | **reconstituted** — Yiddish largely displaced; American Judaism re-forms into new denominations; Israeli Hebrew culture a deliberate construction; Hasidic courts rebuilt from remnant |
| Institutions | innovated — kehillah, later the Bund, Zionism, Hasidic courts | continues |

**Because the population is the same on both sides, most of the confounds that make the
cross-sectional comparison in §11.6a weak are held constant.** That is what the comparison of five
unlike diasporas cannot do.

  `#c/diaspora #d/method #e/inferred` · subj 19–20c · H11 · access: n/a · [unverified]

**The Roma — severance so complete the community lost its own origin.** Dispersed from northern
India, in Europe from roughly the 14th century. The Indic origin was not retained by the Roma
themselves; it was **recovered by philologists in the 18th century from the language**. There is no
sharper case of a severed link in the register.

The mechanism predicts content innovation, and Romani culture is heavily reconstituted with deep
borrowing from host cultures. But the case adds something the mechanism did not anticipate:

> **The core of the language transmitted faithfully anyway** — Indic grammar and basic lexicon
> survived the severance intact, which is precisely how the origin was recoverable at all.

**This is a third register, not a counterexample.** Core grammar and basic vocabulary are acquired
below the level of deliberate maintenance. No institution curates them, so severing the institution
does not touch them. They are the linguistic equivalent of §14a.2's **technical** ceramic
attributes — learned by immersion, invisible in the finished product, and conservative for exactly
that reason — while visible culture behaves like decoration and turns over.

So the transmitter/innovator axis has three registers, not two: **institutions** (invented under
dispersion), **curated content** (faithful while the origin link holds, reconstituted when it
breaks), and **below-conscious structure** (faithful regardless).

  `#c/diaspora #d/indo-european #e/inferred` · subj 14–20c · H11, H15 · access: n/a · [unverified]

**Yes — and the institutions are well documented.** §11.6c treated the Roma only as a severance
case. On the institutional register the mechanism also predicts innovation, and it is there:

- **The *kris romani*** — a tribunal adjudicating disputes within the community, strongest among
  Vlax Roma.
- ***Marime*** — a pollution and exclusion code that supplies the sanction the tribunal needs.

Together these are a private-order legal order: dispute resolution and enforcement with no recourse
to a state. That is the same *category* of institution as the Maghribi coalition's reputation
mechanism and the Armenian merchant courts, and the comparison is not mine — **Peter Leeson, who
works in the same institutional-economics tradition as Greif, has written on it directly.**

**But the problem being solved is different, and the difference sharpens the mechanism.** The
Maghribi and Armenian institutions enforce *commercial agency at distance*. The Romani institutions
maintain a *boundary* and settle *internal disputes*. §11.6a proposed that diasporas innovate
institutionally because no home institution has solved the distance problem for them. The Romani
case shows the driver is more general:

> Institutional innovation follows from **host institutions being unavailable** — and
> unavailability has two distinct causes. **Absence**: no sovereign spans the trade route, so no
> court can hear the case. **Hostility**: a sovereign exists and persecutes, so its courts are a
> threat rather than a fallback. Both force private order; they produce differently shaped
> institutions, because absence leaves a gap to fill while hostility requires a boundary to defend.

That is testable, and it predicts the shape from the cause rather than only predicting that
something will appear.

**A source-base caution, and the project's own new machinery flags it.** Much of the historical
record on Roma was produced by hostile authorities — expulsion edicts, police registers,
anti-"Gypsy" legislation. This is the condition `tags.md` §3 describes for `#v/polemical`: the
hostile witness is often the only witness, so such sources cannot be discarded and must instead be
marked and corrected for. Here it applies to a living population, which raises the stakes beyond
the Gnostic case that prompted the tag. Note also that "Gypsy law" in several of these titles is an
exonym; Ronald Lee, writing as a Romani author, is the `#v/emic` counterweight in this list.

- Weyrauch, Walter O., ed. *Gypsy Law: Romani Legal Traditions and Culture* (2003); and Weyrauch,
  "Gypsy Law" (2001). The standard collection. @weyrauch-2003
  `#c/diaspora #d/method #e/secondary` · src 2001–03 · H11 · access: library · [unverified]
- Leeson, Peter T. "Gypsy law" (2012). Private-order institutions in the Greif tradition, applied
  to the Roma — the bridge between this section and §11.6d. @leeson-2012
  `#c/diaspora #r/analogy #e/secondary` · src 2012 · H11, §5.6 · access: library · [unverified]
- Lee, Ronald. "The Rom-Vlach Gypsies and the Kris-Romani" (1997). @lee-1997
  `#c/diaspora #e/primary #v/emic` · src 1997 · H11 · access: library · [unverified]
- Caffrey, Susan, & Gary Mundy. "Informal Systems of Justice: The Formation of Law within Gypsy
  Communities" (1997). @caffrey-mundy-1997
  `#c/diaspora #d/method #e/secondary` · src 1997 · H11 · access: library · [unverified]

? **Does the absence/hostility split predict institutional shape elsewhere?** The Maghribi and
Armenians had host courts available and used them when convenient; the Roma did not. If the split
is real, a diaspora that moves from tolerated to persecuted should add boundary-defending
institutions without losing its commercial ones.

? **Does the three-register pattern hold outside language?** H15 predicts the same split for
ceramics, where technique is the conservative layer and decoration the volatile one. If both hold,
the register is a property of *how a thing is learned*, not of what kind of thing it is — which
would be a result about transmission in general rather than about diasporas.
? **Both specimens are reasoned from general knowledge and are unread.** The Ashkenazi before/after
table especially needs a historian's check before it carries any weight.

### 11.6d Sources for the sort

All identified 2026-09-14 by OpenAlex title search; **none has been read**.

- Greif, Avner. "Contract Enforceability and Economic Institutions in Early Trade: The Maghribi
  Traders' Coalition." *AER* 83 (1993); and "Reputation and Coalitions in Medieval Trade" (1989).
  The institutional-innovation case, and heavily cited in economics rather than history — which is
  why the project had not met it. @greif-1993
  `#c/diaspora #d/method #e/secondary` · src 1989–93 · H11, §5.6 · access: library · [unverified]
- Aslanian, Sebouh David. *From the Indian Ocean to the Mediterranean: The Global Trade Networks of
  Armenian Merchants from New Julfa* (2011). @aslanian-2011
  `#c/diaspora #r/vector #e/secondary` · subj 17–18c · src 2011 · H11 · access: library · [unverified]
- Grenet, Frantz. "Religious Diversity among Sogdian Merchants in Sixth-Century China" (2007).
  Bears directly on whether the Sogdians altered what they carried. @grenet-2007
  `#d/central-asia #c/diaspora #e/secondary` · subj 6c · src 2007 · H11, Q6 · access: library · [unverified]
- Rong, Xinjiang. "Sogdian Merchants and Sogdian Culture on the Silk Road" (2018). **Same author as
  the Dunhuang library-cave paper wanted for Q8a** (`lit/WANTED.md` W9). @rong-2018
  `#d/central-asia #c/diaspora #e/secondary` · subj 4–10c · src 2018 · H11, Q8a · access: library · [unverified]

## 12. Founder figures: milieu, lineage, and the singularity construction

### 12.1 Narrative summary

Both traditions present their founder as a discontinuity — a teaching without antecedents. In both
cases the historical record shows a crowded field, and in both cases the singularity is a later
construction. That the *same* construction appears twice, independently, is the section's point: it
is direct evidence for H6 (origin narratives converge because the genre converges), and it is a
`#r/analogy` of the safest kind, since no contact is required to explain it.

**The Buddha's lineage is better documented, because his tradition preserved it.** The canon names
his teachers — Āḷāra Kālāma and Uddaka Rāmaputta, from whom he learned the formless attainments and
whom he then surpassed — and names six rival contemporaries in the *Sāmaññaphala Sutta*. He is one
śramaṇa among many in a competitive religious market. The material conditions are equally legible:
the second urbanization from c. 500 BCE brought iron, agricultural surplus, new cities, coinage, new
polities, and a population able to support full-time renunciants.

**Jesus's lineage has exactly one solid datum, and it is a strong one: John the Baptist.** Multiply
attested, corroborated independently by Josephus, and *embarrassing* — accepting baptism implies
subordination, so the tradition would not have invented it. Jesus began inside someone else's
movement. Around that, the context is a plural Second Temple Judaism and a more Hellenized Galilee
than the popular picture allows: Sepphoris lies about 6 km from Nazareth and was rebuilt by Antipas
during Jesus's youth.

**What is not supportable**: travel to India or Tibet. Notovitch's 1894 *Life of Saint Issa* was
exposed as fabrication by Max Müller and the Hemis manuscript was never produced. Essene membership
is popular and unevidenced; Jesus's practice — eating with outsiders, no purity separatism — argues
against it.

→ The methodological observation is Smith's again at one remove: **the "singular creature" framing
is itself the object of study.** Isolating a founder from his context is what *Drudgery Divine*
diagnoses in Protestant scholarship on primitive Christianity, and the Buddhist case shows the same
move made by a different tradition for different reasons.

### 12.2 The Buddha's milieu

- *Sāmaññaphala Sutta* (DN 2) — names the six rival teachers: Pūraṇa Kassapa, Makkhali Gosāla (Ājīvika), Ajita Kesakambalī (materialist), Pakudha Kaccāyana, Sañjaya Belaṭṭhiputta, Nigaṇṭha Nātaputta (Mahāvīra). **The tradition's own record of a crowded market.** @samannaphala
  `#d/nikaya #c/lineage-narrative #e/primary` · subj 5–4c BCE · Q4 · access: open
- *Ariyapariyesanā Sutta* (MN 26) — the Buddha's named teachers, Āḷāra Kālāma and Uddaka Rāmaputta, and his departure from them. An explicit lineage claim, and an explicit repudiation. @ariyapariyesana
  `#d/nikaya #c/lineage-narrative #e/primary` · subj 5–4c BCE · Q4 · access: open
- Bronkhorst, Johannes, *Greater Magadha: Studies in the Culture of Early India* (Brill, 2007) — a non-Vedic cultural sphere in the lower Gangetic plain with its own karma/rebirth ideas, stūpa burial, distinct medicine and cyclical time; the cradle of Buddhism, Jainism and Ājīvikism, **not** an offshoot of Brahmanism. Contested: critics dispute how sharp the east/west division was. @bronkhorst-2007
  `#d/nikaya #r/deflation #e/secondary #s/contested` · subj 800–300 BCE · src 2007 · Q2 Q4 · access: library · [unverified]
- ——, *Buddhism in the Shadow of Brahmanism* (Brill, 2011). @bronkhorst-2011
  `#d/nikaya #c/emic-etic #e/secondary #s/contested` · subj 300 BCE–500 CE · src 2011 · Q2 · access: open (PDF) · [unverified]
- The second urbanization — iron, surplus, coinage, Magadha and Kosala. The material precondition for a renunciant class. @second-urbanization
  `#d/nikaya #c/material-culture #e/secondary` · subj 700–300 BCE · Q2 Q4 · access: library · [unverified]

### 12.3 Jesus's milieu

- Mark 1:9–11 // Matt 3:13–17 // Luke 3:21–22; Josephus, *Ant.* 18.5.2 — the baptism by John, and Josephus's independent notice of John. **The one solid lineage datum**, and the standard illustration of the criterion of embarrassment. @baptism
  `#d/christian #c/lineage-narrative #e/primary` · subj c. 28 CE · Q4 · access: open
- Sanders, E. P., *Jesus and Judaism* (1985); *The Historical Figure of Jesus* (1993) — the apocalyptic reconstruction, and the standard against which others argue. @sanders
  `#d/christian #c/historical-jesus #e/secondary` · subj 1c CE · src 1985, 1993 · Q4 · access: purchase · [unverified]
- Allison, Dale C., *Constructing Jesus* (2010) — on memory, and on how much of the reconstruction the sources can actually bear. @allison-2010
  `#d/christian #c/historical-jesus #e/secondary` · subj 1c CE · src 2010 · Q4 · access: purchase · [unverified]
- **Realized versus consistent eschatology** — C. H. Dodd argued the kingdom is *already present* in Jesus's proclamation; Schweitzer that it is imminent and future. The current majority position resolves them as inaugurated eschatology, holding both in tension. **This is the axis on which the "primacy of the present moment" question turns** (Q3): the parallel to Buddhist framings of awakening is available on the realized reading and largely disappears on the consistent one. @eschatology-debate
  `#d/christian #c/historical-jesus #e/secondary #s/contested` · subj 1c CE · src 1935– · Q3 · access: library · [unverified]
- Crossan, J. D., *The Historical Jesus* (1991); Mack, Burton, *A Myth of Innocence* (1988) — the Cynic-sage reconstruction: itinerant, propertyless, aphoristic. **Contested**, and its premise of a thoroughly Hellenized Galilee is disputed by Meyers and others. Included as the live alternative to the apocalyptic reading. @crossan-mack
  `#d/christian #c/historical-jesus #e/secondary #s/contested` · subj 1c CE · src 1988, 1991 · Q4 · access: purchase · against: @sanders · [unverified]
- Sepphoris and Tiberias — the archaeology of Hellenized Galilee. Material rather than textual evidence for the milieu. @galilee-archaeology
  `#d/hellenistic #c/material-culture #e/secondary` · subj 1c CE · Q4 · access: library · [unverified]
- ! Notovitch, Nicolas, *The Unknown Life of Jesus Christ* (1894) — the "Life of Saint Issa"; Jesus in India. **Exposed as fabrication by Max Müller**; the Hemis manuscript was never produced. Catalogued as the origin of a persistent claim, not as evidence. @notovitch-1894
  `#c/historical-jesus #r/genealogy #e/secondary #s/fringe` · src 1894 · access: open · [unverified]

### 12.4 The death of Jesus, and the traditions in which he does not die

Q3 asks whether any Christian scenario has a *living* Jesus entering the tomb and then undergoing
something like a great transfer. Several early traditions do deny the death — and **their fate is
the finding**. Orthodoxy defined itself partly by insisting on a real death, which is precisely
where the rainbow body's structure diverges. This strengthens H1 more than anything else located so
far, because it shows the two traditions actively diverging rather than merely differing.

- John 19:34 — the spear, blood and water. An **anti-docetic** detail: the text is arguing that he really died. @john1934
  `#d/christian #c/resurrection #e/primary` · subj 1c CE · Q3 H1 · access: open
- *Second Treatise of the Great Seth* (NHC VII,2); Coptic *Apocalypse of Peter* (NHC VII,3) — substitution and the laughing Jesus: someone else dies on the cross. @nhc-substitution
  `#d/gnostic #c/resurrection #e/primary` · subj 2–3c CE · Q3 · access: open
- Irenaeus, *Adversus Haereses* I.24 — reports Basilides's claim that Simon of Cyrene was crucified in Jesus's place. A hostile witness, and therefore evidence that the position was held. @irenaeus-basilides
  `#d/christian #c/canon-formation #e/primary` · subj 2c CE · Q3 · access: open
- Tacitus, *Annals* 15.44 — independent, hostile notice of the execution under Pilate. With the criterion of embarrassment, the basis for treating the crucifixion as among the best-attested facts about Jesus. @tacitus
  `#d/hellenistic #c/historical-jesus #e/primary` · subj c. 116 CE · Q3 · access: open
- ! Schonfield, Hugh, *The Passover Plot* (1965); and the Ahmadiyya tradition of survival and death at Srinagar. The apparent-death hypothesis. Not held in mainstream scholarship. @swoon
  `#c/historical-jesus #r/genealogy #e/secondary #s/fringe` · src 1965 · Q3 · access: purchase · [unverified]

? There is no forensic proof of death and there cannot be. What exists is unanimous early testimony
including from hostile and independent sources, and **no early tradition of survival** — the denials
that do exist (docetic, substitutionist) deny the *body* or the *identity of the victim*, not the
fact of a death on the cross. That distinction matters for Q3 and should not be blurred.

---

## 13. Method and theory

Full treatment in `methods.md`. Sources only here.

- Smith, Jonathan Z., *Drudgery Divine* @smith-1990
  `#d/method #r/deflation #e/secondary` · subj 1600–1990 · src 1990 · Q7 · access: purchase
- ——, *Map Is Not Territory*; *Imagining Religion* @smith-map
  `#d/method #r/analogy #e/secondary` · src 1978, 1982 · Q7 · access: purchase · [unverified]
- Lincoln, Bruce, "Theses on Method," *MTSR* 8 — two pages; the sharpest statement on scholarship versus its object. **Bears on the adherent-veto decision.** @lincoln-1996
  `#d/method #r/none #e/secondary` · src 1996 · Q5 · access: open · against: @wcsmith
- Smith, Wilfred Cantwell, *Towards a World Theology* — the adherent-acceptability principle. @wcsmith
  `#d/method #c/emic-etic #e/secondary #s/contested` · src 1981 · Q5 · access: library · against: @lincoln-1996 · [unverified]
- Headland, Pike & Harris (eds.), *Emics and Etics: The Insider/Outsider Debate* — **where Pike and Harris argue it out directly.** @headland-1990
  `#d/method #c/emic-etic #e/secondary` · src 1990 · Q5 · access: library
- McCutcheon, Russell T. (ed.), *The Insider/Outsider Problem in the Study of Religion* @mccutcheon-1999
  `#d/method #c/emic-etic #e/secondary` · src 1999 · Q5 · access: library · [unverified]
- Asad, Talal, *Genealogies of Religion*; Masuzawa, Tomoko, *The Invention of World Religions* — **"religion" and its cognates as historically constructed categories**; the reflexivity problem (`methods.md` §2.7). @asad-masuzawa
  `#d/method #c/emic-etic #e/secondary` · src 1993, 2005 · Q5 · access: purchase · [unverified]
- Taves, Ann, *Religious Experience Reconsidered* — the convergence explanation; deflator 4. @taves-2009
  `#d/method #r/deflation #e/inferred` · src 2009 · Q7 · access: purchase · [unverified]
- Spinney, Laura, *Proto* — the project's methodological prompt. @spinney-2025
  `#d/indo-european #c/loanword #e/secondary` · subj 4500 BCE– · src 2025 · Q7 · access: held
- Anthony, David W., *The Horse, the Wheel, and Language* @anthony-2007
  `#d/indo-european #c/material-culture #e/secondary` · subj 4500–1500 BCE · src 2007 · Q7 · access: purchase · [unverified]
- Reich, David, *Who We Are and How We Got Here* @reich-2018
  `#d/indo-european #c/genetics #e/secondary` · subj 50000 BCE– · src 2018 · Q7 · access: purchase · [unverified]
- **Zhang F. et al. (34 authors), "The genomic origins of the Bronze Age Tarim Basin mummies," *Nature* 599 (2021)** — genetically isolated local population, culturally cosmopolitan. **Culture moved; people did not. The project's calibration case for how genetics deflates a diffusion story.** @tarim-2021
  `#d/central-asia #c/genetics #e/secondary` · subj 2100–1700 BCE · src 2021 · Q7 · access: held · license: cc-by · doi 10.1038/s41586-021-04052-7
- Huerta-Sánchez E. et al., "Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA," *Nature* 512 (2014) — Tibetan highland adaptation. Included to **mark a boundary**: genetics answers questions about people; doctrines are not carried in genomes. @epas1-2014
  `#d/tibetan #c/genetics #e/secondary` · subj 40000 BCE– · src 2014 · Q7 · access: WANTED (W2) · doi 10.1038/nature13408
- Li C. et al., "Evidence that a West-East admixed population lived in the Tarim Basin as early as the early Bronze Age," *BMC Biology* 8 (2010); and "Analysis of ancient human mitochondrial DNA from the Xiaohe cemetery," *BMC Genetics* 16 (2015) — **the pre-2021 consensus that @tarim-2021 overturned**, by the group that established it. Holding the before *and* the after is what makes the calibration case arguable rather than asserted. @li-xiaohe
  `#d/central-asia #c/genetics #e/secondary #s/contested` · subj 2100–1700 BCE · src 2010, 2015 · Q7 · access: held · license: cc-by · against: @tarim-2021
- Dai S.-S. et al., "The Genetic Echo of the Tarim Mummies in Modern Central Asians," *Mol. Biol. Evol.* 39 (2022). @dai-2022
  `#d/central-asia #c/genetics #e/secondary` · subj 2100 BCE–present · src 2022 · Q7 · access: held · license: cc-by-nc
- Zhao X. et al., "Tracing bronze to iron age population dynamics in Northwest Xinjiang using ancient genomes," *Genome Biology* (2026). @zhao-2026
  `#d/central-asia #c/genetics #e/secondary` · subj 2000–500 BCE · src 2026 · Q6 Q7 · access: held · license: cc-by-nc-nd
- Wang T. et al., "Tianshanbeilu and the Isotopic Millet Road: reviewing the late Neolithic/Bronze Age radiation of human millet consumption from north China to Europe," *National Science Review* 6 (2019) — **subsistence and isotopes rather than genomes**: material evidence for the corridor, and a rare case where the thing demonstrably transmitted is a crop. @wang-2019
  `#d/central-asia #c/material-culture #e/secondary` · subj 3000–1000 BCE · src 2019 · Q6 Q7 · access: held · license: cc-by
- Hu H. et al., "Evolutionary history of Tibetans inferred from whole-genome sequencing," *PLoS Genetics* 13 (2017). @hu-2017
  `#d/tibetan #c/genetics #e/secondary` · subj 40000 BCE– · src 2017 · Q7 · access: held · license: cc-by
- **Haber M. et al., "Ancient DNA and the rewriting of human history: be sparing with Occam's razor," *Genome Biology* 17 (2016)** — a caution paper from inside the field about over-reading aDNA into simple migration stories. **Reads as a genetics-native statement of `methods.md` §6's deflators.** @haber-2016
  `#c/genetics #r/deflation #e/secondary` · subj n/a · src 2016 · Q7 · access: held · license: cc-by
- Hendy J., "Ancient protein analysis in archaeology," *Science Advances* 7 (2021) — paleoproteomics; what the newer molecular toolkit can and cannot establish. @hendy-2021
  `#c/material-culture #d/method #e/secondary` · subj n/a · src 2021 · Q7 · access: held · license: cc-by-nc
- Nelson S. et al., "Tracing population movements in ancient East Asia through the linguistics and archaeology of textile production," *Evolutionary Human Sciences* 2 (2020) — **converging linguistic and material evidence on one technology**, which is the Spinney/`Proto` method applied to East Asia. @nelson-2020
  `#d/central-asia #c/loanword #e/secondary` · subj 5000–1000 BCE · src 2020 · Q7 · access: held · license: cc-by
- Tocharian, Gāndhārī, Sogdian, Bactrian — the corridor's languages and their loanword evidence. @corridor-languages
  `#d/central-asia #c/loanword #e/secondary` · subj 1–10c CE · Q6 Q7 · access: library
- Witzel, E. J. Michael, *The Origins of the World's Mythologies* — ambitious deep-time diffusion; useful because contested. @witzel-2012
  `#d/indo-european #r/homology #e/secondary #s/contested` · subj 65000 BCE– · src 2012 · Q7 · access: purchase · [unverified]

---

## 14. Transmission distortion

Protocol in `methods.md` §3. Sources only here.

- Cross-translator study: Simmons / Reynolds / Clemente / Shane / Lukianowicz on shared Norbu terminology. → **The practicable H4 instrument.** @cross-translator
  `#c/translation-layer #d/dzogchen #e/inferred` · subj 1980s · H4 · access: partial
- Lopez, Donald S., Jr., *Prisoners of Shangri-La* — how Tibetan Buddhism was reshaped in Western reception. @lopez-1998
  `#d/tibetan #c/translation-layer #e/secondary` · subj 1900–1998 · src 1998 · H4 · access: purchase · [unverified]
- McMahan, David L., *The Making of Buddhist Modernism* — the idiom in which 20th-c. Buddhist teaching addressed Western audiences. @mcmahan-2008
  `#d/mahayana #c/translation-layer #e/secondary` · subj 1850–2008 · src 2008 · H4 · access: purchase · [unverified]
- Said, Edward, *Orientalism*, read alongside its Tibetology-specific critics — contested in application to Buddhist studies, which is itself informative. @said-1978
  `#d/method #c/translation-layer #e/secondary #s/contested` · subj 1800–1978 · src 1978 · H4 · access: purchase · [unverified]
- Tucci, Giuseppe, and the IsMEO milieu in Naples — Norbu's institutional context, and a case where scholarship and its political setting are hard to separate. @tucci
  `#d/tibetan #c/emic-etic #e/inferred` · subj 1930–80 · Q5 · access: library · [unverified]

### 14.4 Fiction as heuristic, and framing capture

Fiction is not evidence about the past and is tagged `#e/heuristic` — generative, never citable. It
belongs in §14 rather than a topical section because its relevance here is as a **transmission vector
into the researcher**: it shapes the questions before the sources do.

**Guy Gavriel Kay** writes historical fantasy by a consistent method: deep research into a period,
then displacement into a secondary world with names changed and, in his phrase, a quarter turn to the
fantastic. The method is more interesting than the genre label suggests, because **the displacement
is itself an epistemic marker.** By declining to name Justinian, Kay signals that what follows is
interpretation and not reconstruction — the same job the `#e/` facet performs in this register. A
useful model of *disciplined imagination*: imagination that flags itself as such.

- Kay, Guy Gavriel, *The Sarantine Mosaic* (*Sailing to Sarantium*, 1998; *Lord of Emperors*, 2000) — Justinianic Byzantium. **Its protagonist is a mosaicist**, and the books are substantially about craft, patronage, and an artisan's-eye view of empire. Closest of his works to this project: the market/workshop channel of H8, seen from inside. @kay-sarantine
  `#c/iconography #d/method #e/heuristic` · subj 6c CE · src 1998–2000 · H8 Q8 · access: purchase
- ——, *Under Heaven* (2010) — Tang China around the An Shi rebellion. **Produced a real lead**: the Huichang persecution of 845, now the fourth leg of `background.md` §7's 840s convergence. @kay-underheaven
  `#d/chan #c/contact-route #e/heuristic` · subj 8c CE · src 2010 · Q6 Q8 · access: purchase
- ——, *The Lions of Al-Rassan* (1995) — al-Andalus in the era of El Cid. Points at *convivencia* as a Q8 comparison case, and at the fact that its harmonious reading is contested. @kay-alrassan
  `#c/nexus #d/method #e/heuristic` · subj 11c · src 1995 · Q8a · access: purchase
- ——, *Tigana* (1990) — Renaissance Italy, and centrally about the **deliberate erasure of a conquered people's name from memory**. A dramatisation of transmission *failure*: §14's subject from the other side, and adjacent to the suppression question in Q4. @kay-tigana
  `#c/translation-layer #d/method #e/heuristic` · subj 15–16c · src 1990 · Q4 · access: purchase
- ——, *Children of Earth and Sky* (2016), *A Brightness Long Ago* (2019), *All the Seas of the World* (2022) — the Renaissance Adriatic and Mediterranean; Venice, Dubrovnik, the Ottoman frontier. A further Q8 comparison zone. @kay-adriatic
  `#c/nexus #d/method #e/heuristic` · subj 15–16c · src 2016–22 · Q8a · access: purchase

**Assessment.** Three risks; the third is the live one.

1. *Invented interiority.* Kay's rendering of how people experienced these worlds is fiction. The
   temptation is to let emotional plausibility substitute for evidence about experience — exactly the
   substitution the emic/etic discipline exists to block.
2. *Harmonisation.* His contact societies tend to be more convivial than the scholarship supports.
   The *convivencia* of al-Andalus is contested; Nirenberg's *Communities of Violence* argues that
   coexistence and systematic violence were not alternatives but one system.
3. *A positive-only sample.* Not a belief that fusion is normal — the working expectation is the
   opposite, that it is exceptional, which is precisely what makes Q8a worth asking. The real hazard
   is narrower and structural: **Kay writes only about cases where something happened.** He will
   never set a novel in a busy entrepôt where nothing came of it. So his corpus is a non-random
   sample containing positives and no negatives — the same fault as sampling on the dependent
   variable (`methods.md` §6, deflator 7), arriving by a different route. The influence is stated and
   predates the project, so the correction is not "read him later" but to treat the corpus as what it
   is: **a list of nominations, not of conclusions.**

**The productive use follows from that.** Kay's selection criterion is narrower and better than
"moments where cultures met interestingly": he picks **inflection points that left observable
long-range impacts on multiple subsequent cultural lineages**. Several of his locales recur in
Spinney's *Proto*, which is a weak independent check that the selection tracks something real. That
criterion is much closer to **Q8b** — downstream traceability — than to Q8a, which makes his corpus a
nomination list for the *tractable* half of Q8. So: **take his settings as candidate exceptional cases, then ask of each what
the exception consisted in, and test against the negative class.** Nominations to be checked, which
is exactly what `#e/heuristic` licenses.

**And his selection has a pattern worth naming.** Justinian's Byzantium amid plague and imperial
overreach; Tang at the An Shi rebellion; al-Rassan in the taifa period on the eve of the Reconquista;
Arbonne before the Albigensian Crusade; *Tigana* after conquest, about erasure; the Adriatic after
1453. **He does not write about fusion happening — he writes about fusion at the moment it is about
to be destroyed.** That is a novelist's choice of register, but it has an analytic consequence for
Q8a, developed in `background.md` §5.3: our case list may over-represent fusions that *ended*.

→ Kay's value is real and lies in question-generation, not evidence. The *Under Heaven* → Huichang
845 chain is the argument for the category: a novel pointed at a persecution edict that tightened a
dating argument. That is what `#e/heuristic` is for.

### 14.4a Cross-domain analogy: eco-evolutionary imports

Tagged `#e/heuristic` for the same reason fiction is. **Importing evolutionary logic into cultural
history has a poor track record** — social Darwinism, and memetics' thin yield — because the two
domains differ where it matters: cultural transmission is Lamarckian, horizontal at will, blending,
and intentional. These are analogies for generating questions, and are fenced accordingly.

**One distinction the register must keep sharp.** @arbesman-2011 is *not* an analogy: he measured
polity lifespans directly and found them memoryless. @vanvalen-1973 is its biological origin, and the
Cambrian material below is analogy only. Same intellectual neighbourhood, three different epistemic
statuses — which is the `#e/` facet doing exactly the work it exists for.

- **Gould, Stephen Jay, *Wonderful Life: The Burgess Shale and the Nature of History* (1989)** — Cambrian disparity and the contingency thesis: replay the tape and you get a different world. @gould-1989
  `#c/nexus #d/method #e/heuristic` · subj 538–515 Ma · src 1989 · Q7 Q8a · access: purchase · [unverified]
- Conway Morris, Simon — the standing reply: convergence is pervasive, and similar solutions recur independently under similar constraints. @conwaymorris
  `#d/method #r/deflation #e/heuristic` · src 1998– · Q7 · access: library · [unverified]
- Carroll, Sean B., *Endless Forms Most Beautiful* (2005) — evo-devo and Cambrian body plans; the other candidate referent for the flagged citation. @carroll-2005
  `#d/method #c/material-culture #e/heuristic` · src 2005 · Q8a · access: purchase · [unverified]

? **Bibliographic**: the source was given as Dawkins, *A Beautiful Life*. No such Dawkins title was
found. Gould's *Wonderful Life* is the likely referent given the Cambrian context; Carroll is the
alternative. → Confirm which.

**Three imports, in ascending order of usefulness.**

1. *Weak incumbency permits innovation.* Cambrian disparity arose while ecospace was largely
   unoccupied and incumbents few; as ecosystems filled, body-plan innovation was constrained. A
   structural analogue to H7 — innovation where boundary-maintenance is weak — and to explanation
   (c) in §5.3, since low incumbency is also low defence.
2. **Gould versus Conway Morris is Q7 in another domain.** Contingency (history matters; outcomes
   are path-dependent) against convergence (similar constraints produce similar solutions
   independently) **is the genealogy/analogy distinction**, argued for forty years with a developed
   sense of what counts as evidence on each side. The project should mine that debate for its
   *criteria*, not its conclusions.
3. *Innovation follows incumbency collapse, with a lag* — developed as **H13**, and it bears
   directly on the Dzogchen dating obstacle. See `background.md` §7.

### 14.5 Oral transmission regimes — who pays for error correction

Serves H7 via `methods.md` §1.2b. Vedic and Homeric epic solve the same analog-channel problem by
**opposite strategies**, and their diffusion histories differ accordingly.

- **Parry, Milman**, *The Making of Homeric Verse* (1971); **Lord, Albert B., *The Singer of Tales* (1960)** — oral-formulaic composition: metrically-fitted formulae, type-scenes and story-patterns as a *generator* rather than a stored text; the South Slavic *guslari* fieldwork showing the song stable while the text varied between performances. **Contested** — hard vs soft Parryists, revived neoanalysis, Kullmann arguing for literate composition. @parry-lord
  `#c/lineage-narrative #d/hellenistic #e/secondary #s/contested` · subj 8c BCE / 1930s · src 1960, 1971 · H7 · access: library · [unverified]
- **Alexandrian textual scholarship** — Zenodotus (first librarian, c. 284–260 BCE) marking suspect lines with the *obelos*; Aristarchus of Samothrace (head librarian 216–144 BCE) developing the fuller sign system with *hypomnemata* justifying each judgement, preserved in Venetus A. **The first genuine error-correction apparatus for Homer, and it is philological rather than priestly.** Built at the nexus (§11). @alexandrian-editors
  `#d/hellenistic #c/canon-formation #e/secondary` · subj 3–2c BCE · Q8b H7 · access: open · [unverified]
- Nagy, Gregory — the evolutionary model of Homeric textual fixation: progressive stabilisation through performance over centuries rather than a single dictation event. @nagy
  `#d/hellenistic #c/canon-formation #e/secondary #s/contested` · subj 8–2c BCE · Q8b · access: library · [unverified]

**The finding.** Error-correction regimes are **historically contingent, and the same material can
pass between them** — for Homer: singer → polis → library, with *correct* meaning successively "scans
and satisfies," "fits the agreed sequence," and "matches the best manuscripts." So which side of the
technique/doctrine line a tradition falls on is not a fact about the material. It is a question about
**which regime is currently paying**, and that changes.

### 14.5a Terma as a gated channel — and why the reading depends on where you stand

I called terma "a sanctioned form of the counterfeiting failure." **xian's correction — that the
pathway is gated by prior social standing, and so is honest signalling rather than an open
vulnerability — is better supported.** The apparatus:

- **Tertöns are prophesied and are held to be rebirths of Padmasambhava's disciples.** The channel is
  not open to all comers; it requires a prior recognition obtained through the ordinary route.
  **The exception is credentialled by the rule.**
- **Community authentication is central, not incidental.** Doctor's study is precisely about "the
  crucial role of religious communities in the construction and authentication of revelation," and
  about the polemics that surrounded it.
- **The signal has an unusual structure.** The yellow scroll (`shog ser`) in ḍākinī script is held to
  be decipherable *only* by the tertön it belongs to. So the object cannot be independently checked —
  it is a **non-transferable, third-party-unverifiable** token. That is the exact inverse of the Vedic
  case, where verification is public and any competent listener can perform it. When the signal itself
  cannot be checked, the burden falls back onto costly prior investment — years of training and
  recognition — which is the standard honest-signalling solution.

**Two things complicate it, and both are worth keeping.**

1. **Causality runs both ways.** Successful revelation *confers* standing as well as requiring it —
   Nyala Pema Dündul's stature was built partly on his treasures (§3.3). So the gate is softer than a
   pure prior-credential model: standing → revelation → more standing is a feedback loop, and a
   self-reinforcing one.
2. **The gate held inside Nyingma and not across schools.** Sakya Paṇḍita attacked Nyingma revelation
   as fabricated tantra in *A Clear Differentiation of the Three Codes*. So the authentication was
   **school-relative**.

→ **Which dissolves the disagreement between the two readings.** *Within* the school, terma is honest
signalling gated by credentials. *From outside*, it reads exactly as the counterfeiting failure mode,
because the outsider cannot verify the token and does not accept the credential that substitutes for
it. Both readings are correct from their respective positions — and **that an error-correction
regime's authority stops at the school boundary is H7 appearing precisely where H7 predicts it.**

- **Doctor, Andreas, *Tibetan Treasure Literature: Revelation, Tradition, and Accomplishment in Visionary Buddhism* (Snow Lion, 2005)** — the authentication question head-on: how a community decides whether a revealed text is Buddha Word. **The single best source for testing xian's gating hypothesis.** @doctor-2005
  `#c/terma #d/nyingma #e/secondary` · subj 11–19c · src 2005 · Q5 H7 · access: purchase · [unverified]
- **Gyatso, Janet, "The Logic of Legitimation in the Tibetan Treasure Tradition," *History of Religions* (1993)**; and *Apparitions of the Self* (1998) on Jigme Lingpa. The foundational analysis of legitimation strategy. @gyatso-1993
  `#c/lineage-narrative #d/nyingma #e/secondary` · subj 14–18c · src 1993, 1998 · Q4 Q5 · access: library · [unverified]
- **Sakya Paṇḍita, *sDom gsum rab dbye* (A Clear Differentiation of the Three Codes)**, 13th c. — attacks Nyingma revelation as fabricated. **A hostile witness, and therefore evidence that the authentication was contested at the time** rather than uniformly accepted. @sakya-pandita
  `#d/tibetan #r/deflation #e/primary` · subj 13c · Q5 H7 · access: library · [unverified]
- Mayer, Robert, & Cathy Cantwell — work on the Nyingma treasure tradition and its textual practices. @mayer-cantwell
  `#c/terma #d/nyingma #e/secondary` · subj 8–19c · access: library · [unverified]

? **Does the terma mechanism appear only in traditions with strong chain-of-transmission
requirements?** If revelation-bypass is a response to expensive lineage-based error-correction, it
should not appear where transmission is cheap. **Bön having its own treasure tradition is the first
check** — Bön also uses lineage transmission, so it is a confirming case rather than a test. A real
test needs a tradition with *weak* chain requirements and no revelation-bypass, or a strong-chain
tradition that never developed one. Chan is the obvious candidate: transmission is explicitly
person-to-person, so does anything play terma's role there?

**Two biological analogies offered for the gated channel** — xian's, 2026-08-25, recorded
2026-09-15. Both address the same design problem terma solves:
how a closed tradition admits novelty without losing the ability to tell itself from everything else.

- **The vertebrate adaptive immune system.** It must distinguish self from non-self while
  *generating* novel recognition capacity it did not inherit — and it does so in a **bounded
  region**, the hypervariable segments of the receptor genes. Variation is licensed in one place and
  forbidden everywhere else. That is structurally what terma does: revelation is permitted, but only
  through a gate with credentials attached.
- **CRISPR.** A bacterial system that imports foreign sequence into its own genome *deliberately*,
  as a record of what it has encountered, and uses it to recognise that material later. Contained
  importation of novelty, with the import becoming part of the self.

Per `methods.md` §1.2a these are analogies for generating questions, never evidence. The question
they generate is sharp: **where is the variation licensed, and what marks the boundary of the
licensed region?** For terma the answers are the tertön's standing and the yellow scroll; the
analogies suggest looking for the equivalent boundary marker in any tradition that admits revelation.

  `#c/terma #r/analogy #e/heuristic` · H7 · access: n/a

### 14.5b The Latter-day Saint parallel — a well-lit instance of the same mechanism

xian's observation, and **it is an established scholarly comparison**: "The Production of the Book of
Mormon in Light of a Tibetan Buddhist Parallel," *Dialogue* (2022). It surfaced in this project's own
`13-terma` query and was not followed up at the time.

**The structural correspondence is close.**

| Feature | Terma | Book of Mormon |
|---|---|---|
| Concealment narrative | Padmasambhava conceals for a prophesied revealer | Moroni buries the plates for a prophesied translator |
| Token | yellow scroll (`shog ser`) | golden plates |
| Decoding capacity | ḍākinī script, legible only to the destined tertön | "reformed Egyptian," via seer stone / Urim and Thummim |
| Token afterwards | often reconcealed or consumed | returned to the angel |
| Substitute verification | certification by established masters | the Three and Eight Witnesses' statements, printed in the book |
| External verdict | rejected by Sakya Paṇḍita as fabricated tantra | rejected by mainstream Christianity |

**The disanalogy is the informative part.** In the Tibetan case the credential *precedes* the
revelation — the tertön is prophesied and recognised, so the bypass is licensed by an existing
institution. Joseph Smith had **no prior standing to be gated by**: the credential *follows* the
revelation, which constitutes the institution rather than drawing on it.

→ **So the LDS case is a natural experiment on the gating hypothesis.** If gating by prior standing
were *necessary*, Smith should have failed. He did not. Gating is therefore a **sufficient** solution
to the unverifiable-token problem, not a necessary one — and the alternative is visible in what Smith
actually did: **substitute witness testimony and rapid community formation for prior credentials.**
The Witnesses' statements are a manufactured signal built to replace an absent one, which is the
Akerlof remedy — certification — improvised on the spot.

Both cases then confirm Doctor's central claim: **the community does the authenticating.** Terma
routes that through prior individual credentials; Smith routed it through witnesses and fast group
formation. Two paths to one function.

**Why this is worth more to the project than a curiosity.** The Tibetan case is visible only through
hagiography written long afterwards. The LDS case is **documented to a standard the project almost
never gets**: contemporary newspapers, court records, affidavits, hostile witnesses, competing
accounts by participants. For an inquiry that keeps running into archival silence (`methods.md` §7.1),
a well-lit instance of a mechanism otherwise seen only through devotional sources is a genuine
instrument — the modern case can be used to ask what the ancient sources would have looked like had
anyone been taking notes.

- **"The Production of the Book of Mormon in Light of a Tibetan Buddhist Parallel," *Dialogue: A Journal of Mormon Thought* 55:4 (2022)** — the comparison already made in print. @bom-terma-2022
  `#c/terma #r/analogy #e/secondary #s/contested` · subj 8–19c · src 2022 · Q5 H7 · access: WANTED — closed · doi 10.5406/15549399.55.4.02
- The Testimony of the Three Witnesses and of the Eight Witnesses, printed in the *Book of Mormon* (1830) — **a manufactured certification signal**, and a primary document of the substitute-verification strategy. @bom-witnesses
  `#d/christian #c/canon-formation #e/primary` · subj 1829–30 · H7 · access: open
- Bushman, Richard, *Joseph Smith: Rough Stone Rolling* (2005) — the standard scholarly biography; a believing historian writing critically, which makes it also a case study for `methods.md` §2.3 on insider/outsider versus emic/etic. @bushman-2005
  `#d/christian #c/emic-etic #e/secondary` · subj 1805–44 · src 2005 · Q5 · access: purchase · [unverified]
- "Political Rivalry and Doctrinal Debates: A Modern Tibetan Response to the Controversy of Buddhist Revelation" (2017) — terma controversy in a modern setting. @tibetan-revelation-2017
  `#c/terma #r/deflation #e/secondary #s/contested` · subj 20c · src 2017 · Q5 · access: WANTED — closed

### 14.6 The Christian sequence — canon, scriptorium, pecia, press

The same "who pays" question run through a second tradition, and it separates **two layers that
§14.5 ran together**: *canon* decides which replicators are admitted; *copying* decides fidelity per
replicator. They have different payers, different failure modes, and different histories.

**Layer 1 — canon as admission control.** Marcion's canon (c. 144) as provocation; Irenaeus arguing
for exactly four gospels; Eusebius sorting *homologoumena*, *antilegomena*, *notha*; Athanasius's
39th Festal Letter (367) listing the 27; Hippo (393) and Carthage (397).

**The stated criteria are apostolicity, catholicity and orthodoxy** — that is, provenance, spread,
*and content*. An earlier version of this entry claimed the Gospel of Mary "failed a provenance test
rather than a content test." **That claim is withdrawn as unsupported**, on two grounds:

1. **Causal order is not recoverable.** Provenance judgements may well have been *reached because of*
   content — a text read as Valentinian is then found to lack apostolic pedigree. The Fathers report
   provenance as their criterion, but they are not disinterested witnesses to their own reasoning.
   Taking their account of their criteria as the historical explanation is **emic capture**, the
   failure mode `methods.md` §2.5 names. I committed it.
2. **There may have been no adjudication at all.** The Gospel of Mary does not appear in the disputed
   lists; Eusebius does not discuss it. Absence from a canon list is not evidence of exclusion — it
   is compatible with simply not circulating widely enough to require a ruling.

What survives is narrower and still worth having: **apostolicity is structurally a chain-of-custody
criterion**, formally like the `lung` requirement (§1.3) and arrived at independently. Whether it did
the deciding is a separate question this section cannot settle.

**Layer 2 — copying fidelity.** Monastic scriptoria: a designated *corrector* checking against the
exemplar; colophons cursing anyone who alters the text; the Carolingian reform under Alcuin producing
a standardised Vulgate and Caroline minuscule — **a legibility standard is an error-reduction
technology**. Cost: parchment measured in herds, and monk-years. The payer is a landed monastery.

**The pecia system** is the sharpest instance. Medieval universities, facing demand-driven
multiplication of bad copies, authenticated a master *exemplar*, divided it into numbered quires
(*peciae*), and rented them one at a time. Copies therefore derive from the master rather than from
each other: **an explicit anti-drift mechanism operating at the institutional level**, and a shift of
the payer from monastery to stationer-and-university.

**Print, and where the digitisation actually happens.** Eisenstein argues print supplied *fixity*,
enabling comparison and correction instead of cumulative error. Johns contests it: fixity was an
achievement, not an inherent property, and *"must be recognized in order to exist"* — typographical
standardisation was far from settled by 1700.

**Movable type resolves part of this, and the resolution is xian's.** A sort is either an M or an N;
the typecase is a finite inventory of discrete physical objects. A scribe's hand is continuous —
letterforms vary by degree and can be misread through gradual deformation. So **movable type
genuinely digitises the channel, but only at the character level.** That is a real change of kind,
not merely a lower price for the same analog problem, which is what an earlier version of this entry
suggested.

But digitisation at the character level buys no fidelity at the text level. Compositors misread copy,
transpose and substitute; type gets pied; each new edition is a fresh resetting with fresh errors. So
print delivers **a discrete alphabet with a still-noisy selection process.**

**I first wrote "a digital code with no checksum." That was wrong, and the correction is xian's: the
checksum moved to the market.** Print shops competed, and accuracy was a differentiator a buyer could
pay for. Aldus Manutius built the Aldine reputation on exactly this — humanist collaborators editing
the texts, Aldus reportedly going through copies by hand to catch errors — and the model was taken up
by Froben at Basel, where Erasmus worked. **The corrector became a paid trade role inside a
commercial enterprise**, rather than a monk under a rule or a librarian under a king.

So the payer sequence completes, and the last step is a change of *kind*:

| Regime | Payer | Correctness certified by |
|---|---|---|
| Scriptorium | landed monastery | the rule, and the exemplar |
| *Pecia* | university and stationer | an authenticated master copy |
| **Print** | **buyers, via the publisher** | **reputation — selection by purchasers, not certification by authority** |

**Gresham's law states the limit precisely, and inverts the mechanism.** Bad money drives out good —
but only under a specific condition: **legal compulsion to accept both at par.** Where that
compulsion is absent, good money does not vanish; it circulates at a premium (Rolnick & Weber found
historical cases where bad money failed to displace good). The modern reading makes it a prisoner's
dilemma *created by* legal tender laws. The observation predates Gresham — Oresme and Copernicus
state it earlier.

Generalised: **selection tracks quality only if quality is priced at the point of exchange. Forced
parity does not merely blunt the selection, it reverses it** — when a copy is a copy regardless of
fidelity, the cheap copy wins.

**Three distinct ways the signal layer fails.** An earlier version of this entry called Gresham "the
forced-parity special case" of Akerlof. That is wrong: they are different failure modes reaching the
same outcome by opposite routes, and the distinction is the useful part.

| Failure | Condition | Mechanism | Remedy |
|---|---|---|---|
| **Blocked** — Gresham | quality *is* legible (you can weigh a coin) but law forces exchange at par | no gain from spending the good one, so it is hoarded | permit premium pricing; remove forced parity |
| **Absent** — Akerlof | quality is *not* legible | buyers pay only the average, so good sellers exit; the market can unravel to lemons only | certification, brands, warranties, licensing |
| **Counterfeited** — Johns | signal legible but forgeable | pirates copy the printer's device along with the text | enforcement: guild regulation, privileges, later copyright |

**This reframes a whole class of apparatus as anti-Gresham technology.** Alexandrian critical signs,
the *pecia* authentication mark, the printer's device and colophon, the imprimatur — each makes an
*invisible* property (textual accuracy) *visible at exchange*, so that it can be priced. Without such
a signal, an error-correction regime can pay for fidelity and still lose, because no buyer can tell.

→ **The regime schema therefore needs a fourth column.** Not just payer / mechanism / referent but
**signal**: how the check is made legible to whoever is choosing. See `background.md` §5.6.

**Johns's piracy evidence is the third mode.** Early modern print carried unauthorised reprints,
false imprints and misattribution: a book bearing a reputable printer's name might be a cheap pirated
reset with fresh errors. Readers could not take a printed book to be what it claimed. That is why he
holds fixity had to be *manufactured* — by guild regulation, personal vouching and reputation
networks — rather than being delivered by the technology. **The printer's device was the quality
signal, and pirates copied the device.**

- **Gresham's law** — bad money drives out good *under forced parity*; contested in its strong form (Rolnick & Weber). **The sharpest available statement of when selection stops tracking quality**, and xian's addition. @greshams-law
  `#c/nexus #d/method #e/secondary #s/contested` · subj 14c– · H7 · access: open · [unverified]
- **Akerlof, George A., "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism," *Quarterly Journal of Economics* 84:3 (1970)** — where buyers cannot observe quality they pay only the average, so good sellers withdraw, average quality falls, and the market can unravel until only bad goods remain. **Not the general case of Gresham but a distinct failure mode** — unobservability rather than forced parity. Remedies are warranties, brands and certification, which is why signalling is a necessary component of any market-based correction regime. Connects to the costly-signalling literature at @iannaccone-1994. @akerlof-1970
  `#c/nexus #d/method #e/secondary` · src 1970 · H7 H14 · access: open · [unverified]

**A convergence worth flagging.** About half the scribes, philologists, correctors and typesetters
working on Aldine editions came from the **Greek diaspora in Venice** — largely post-1453. So a
refugee population supplied the error-correction labour for a new medium, and that labour was the
press's competitive advantage. **H11 operating inside the print case**, and a concrete instance of a
diaspora diffusing innovation it did not originate.

*(What I earlier compressed to "the Alexandrian move on a new substrate," unpacked: the Alexandrian
librarians manufactured fixity for Homer by collation and editorial apparatus — comparing manuscripts,
marking suspect lines, justifying each judgement. Print-era editors did the same thing with the same
tools. But the print case is only **partly** that old move, because market reputation is a
selection mechanism with no ancient analogue.)*

- Athanasius, 39th Festal Letter (367); Eusebius, *Hist. Eccl.* III.25; Muratorian fragment. @canon-sources
  `#d/christian #c/canon-formation #e/primary` · subj 2–4c · Q4 H7 · access: open
- The pecia system; Carolingian scriptorium reform; Caroline minuscule. @pecia
  `#d/catholic #c/translation-layer #e/secondary` · subj 8–14c · H7 · access: library · [unverified]
- **Economic selection as an error-correction regime** — xian's argument, and it generalises past print: where a market exists, buyers select among producers, and accuracy is one dimension they select on. Weaker than natural selection in force and leakier in operation, but not absent, and plausibly **the dominant selective mechanism in the modern period**. Connects to H9's *institutional-capital* nexus type, whose mechanism this is. @economic-selection
  `#c/nexus #d/method #e/inferred` · subj 15c– · H7 H9 · access: n/a
- **Graeber, David, *Debt: The First 5,000 Years* (2011)** — credit and debt relations as prior to and constitutive of markets, and economic relations as moral and social ones. **The relevant use here is deflationary**: it blocks treating "economic selection" as a natural force. Markets are institutional arrangements, so a market is one more error-correction *regime* with a payer structure, not the absence of one. Contested on historical specifics; the anti-barter argument is the best-received part. @graeber-2011
  `#c/nexus #d/method #e/secondary #s/contested` · subj 3000 BCE–2011 · src 2011 · H7 H14 · access: purchase · [unverified]
- Aldus Manutius and the Aldine press; Froben at Basel; the corrector as a paid trade role; the Greek diaspora in Venice supplying much of the Aldine correction labour. @aldine
  `#d/hellenistic #c/contact-route #e/secondary` · subj 1490–1520 · H7 H11 · access: library · [unverified]
- Eisenstein, Elizabeth, *The Printing Press as an Agent of Change* (1979) vs **Johns, Adrian, *The Nature of the Book* (1998)** — fixity as inherent property vs as transitive achievement. @eisenstein-johns
  `#c/translation-layer #d/method #e/secondary #s/contested` · subj 15–18c · src 1979, 1998 · H7 · access: library · [unverified]

### 14.7 Survivorship — and the formal machinery a sister field already has

The project's recurring bias problems — archival silence, termination bias, positive-only samples —
share one structure: **inference conditioned on survival.** If it was not preserved, it is not
observed. That is not a humanities peculiarity; it is the organising problem of phylogenetics, which
reconstructs history almost entirely from survivors.

**And the transfer is literal, not metaphorical.** Manuscript stemmatics and phylogenetic inference
are formally the same problem: reconstruct a copying tree from extant witnesses. Barbrook, Howe,
Blake and Robinson, "The phylogeny of *The Canterbury Tales*," *Nature* 394 (1998), applied split
decomposition to 58 fifteenth-century manuscripts of the *Wife of Bath's Prologue* and found good
agreement with the conventionally-derived stemma. The field has a name — **phylomemetics**.

#### 14.7a Exactly how formal the correspondence is — and where it stops

Recorded 2026-09-15. §14.7 asserts the transfer is literal; this states the mapping, because
borrowing machinery without knowing which assumptions travel is how a method gets misapplied.

| Stemmatics | Phylogenetics |
|---|---|
| witness — a surviving manuscript | extant taxon |
| archetype | most recent common ancestor, the root |
| **shared error** (conjunctive) | **shared derived character**, a synapomorphy |
| shared *correct* reading | shared *ancestral* state — uninformative for grouping |
| separative error | character excluding a descent relationship |
| stemma | cladogram |
| contamination — a scribe using two exemplars | horizontal transfer, hybridisation, introgression |
| lost intermediate copies | extinct or unsampled lineages |

**The identity, not the analogy.** Both reconstruct an unobserved branching history from character
states in surviving terminals, and both hold that **only shared *derived* states group things**.
A shared correct reading is uninformative for the same reason a shared ancestral trait is: it can be
inherited from anywhere, or arrived at independently. Lachmann's principle and Hennig's are one
principle in two vocabularies. **"Error" and "derived character state" name the same logical role.**

**Four places the assumptions do not travel.** These are the cost of the borrowing:

1. **Polarity has no outgroup.** Phylogenetics roots a tree with an outgroup. Stemmatics usually
   cannot, and determines direction by judging which reading a copyist would more plausibly have
   produced — *lectio difficilior potior*, prefer the harder reading, because scribes simplify. That
   is a **content judgement with no phylogenetic counterpart**, and cladistics was built partly to
   escape such judgements.
2. **Contamination is normal rather than exceptional.** Scribes routinely consulted more than one
   exemplar, and scholarly copyists collated deliberately. The tree model is therefore violated as a
   matter of course, not occasionally.
3. **Ancestors survive.** A surviving manuscript can be the actual exemplar of another surviving
   manuscript — a terminal that is literally an internal node. Phylogenetic software assumes
   terminals are tips and handles this badly; stemmatics has a dedicated step for removing such
   witnesses.
4. **Variation is structured, not stochastic.** Scribal error follows psychology and orthography —
   eye-skip between similar line endings, doubled or dropped syllables. Errors are predictable in
   kind, which helps a human editor recognise them and violates the substitution models the software
   assumes.

**Two things worth borrowing, beyond the tree-building.**

- ***Lectio difficilior* is a directionality rule for transmission chains, and this project has a
  transmission chain.** It says deformation has a preferred direction: transmission simplifies. That
  is the analog-channel argument (`background.md` §5.5) stated as an editorial rule two centuries
  earlier, and it is directly applicable to H4 — across the Tibetan → Italian → English → print
  chain, the *simpler* reading is the likelier corruption, not the likelier original.
- **Bédier's objection, as a deflator.** Joseph Bédier observed that published stemmata were
  suspiciously often bipartite — split into exactly two branches — far more often than chance should
  allow, and argued that editors were producing the shape their method made available rather than
  the shape the evidence supported. Generalised: **a suspiciously regular result is evidence about
  the method, not about the world.** `methods.md` §6 has no deflator of this form, and the project
  builds typologies constantly. *(Bédier is prior knowledge, not retrieved; the 1928 critique is in
  French and did not surface in the index.)*

- Howe, Christopher J., & Ruth Connolly. "Responding to Criticisms of Phylogenetic Methods in
  Stemmatology" (2012). [10.1353/sel.2012.0008](https://doi.org/10.1353/sel.2012.0008). The
  methodological debate itself, which is what the project needs rather than another application.
  @howe-connolly-2012
  `#d/method #r/analogy #e/secondary` · src 2012 · §14.7, H4 · access: library · [unverified]

? **Should §6 gain a deflator for method-shaped results?** Bédier's form of objection — the answer
has the shape the instrument prefers — applies to every typology in this register, including the
diaspora sort and the rainbow-body typology.

Paleobiology has also named the specific biases and built corrections: the **Signor–Lipps effect**
(the last fossil occurrence precedes true extinction, so extinctions look gradual), **ghost
lineages** (branches inferred to exist with no direct record), the **pull of the recent**. Each has a
textual analogue: lost manuscripts, lost recensions, whole traditions inferable only from citation in
their opponents.

**The useful caveat is where the analogy was already tested and had to be modified.** Manuscripts
*contaminate* — a scribe consulting two exemplars produces reticulation, not a tree. Which is exactly
horizontal gene transfer, and it is why the 1998 study used a **network** method rather than a strict
tree. The disanalogy was found and handled rather than waved away.

- Barbrook, A. C., Howe, C. J., Blake, N., & Robinson, P., "The phylogeny of *The Canterbury Tales*," *Nature* 394 (1998), 839. @barbrook-1998
  `#c/lineage-narrative #d/method #e/secondary` · subj 15c · src 1998 · Q7 · access: open
- Phylomemetics — the general programme of phylogenetic analysis beyond the gene (*PLOS Biology*, 2011). @phylomemetics
  `#d/method #r/analogy #e/secondary` · src 2011 · Q7 · access: open · [unverified]
- Signor–Lipps effect; ghost lineages; pull of the recent — the named survivorship biases and their corrections. **The argument that this project's bias problems are tractable rather than sui generis.** @survivorship-biases
  `#d/method #r/deflation #e/heuristic` · src 1982– · Q7 · access: library · [unverified]

→ **The recommendation.** Where the project records a negative result (`methods.md` §7.1), the
question "would this archive have registered it?" can sometimes be replaced by an *estimate* rather
than a shrug. Birth–death and sampling-corrected models exist. Whether they are worth importing
depends on whether the corpus is ever large enough to fit one — probably not for Dzogchen, plausibly
for the manuscript traditions.

---

### 14.8 Barlaam and Josaphat — the project's positive control

Entered 2026-08-27 from a word-of-mouth source (see below). **Not yet worked; recorded for later
analysis.** Cross-checked against `en:Barlaam and Josaphat`, rev 1362809573 —
<https://en.wikipedia.org/w/index.php?title=Barlaam_and_Josaphat&oldid=1362809573>

**Why it matters here.** The Buddha's life-legend reached the Roman Martyrology as the life of a
Christian saint. That transmission is not hypothesised — it is **demonstrated, and demonstrated by
the evidence type this project ranks highest**. The chain is a loanword series, §5 rung 1:

`bodhisattva` (Sanskrit) → `Bodisav` (Middle Persian, 6th–7thc.) → `Būdhasaf`/`Yūdhasaf`
(Arabic, 8thc. — initial ﺑ *b* read as ﻳ *y* by a duplicated dot) → `Iodasaph` (Georgian, 10thc.)
→ `Ioasaph` Ἰωάσαφ (Greek, 11thc.) → `Iosaphat`/`Josaphat` (Latin)

with an independently attested translation chain beside it (rung 2): Sanskrit Mahāyāna text
(2nd–4thc.) → **a Manichaean version** → Arabic *Kitāb Bilawhar wa-Būd̠āsaf*, current in Baghdad
in the 8thc. → Georgian *Balavariani* (10thc.) → Greek, by **Euthymius of Athos** (d. 1028) →
Latin, 1048.

This is the project's **positive control**, and its value is calibrational: it shows what a real
Buddhist–Christian transmission leaves behind. Any rainbow-body/resurrection claim can be asked
directly — *does it have anything like this?* At present it does not.

**Three findings visible without further work.**

1. **The arbitrary detail outlived the structure.** The narrative was progressively Christianised
   until its Buddhist content was invisible for roughly a millennium — while the *name*, carrying
   no meaning to any receiving audience, preserved the genealogy intact through six languages.
   That is §5's ladder demonstrated rather than asserted: the shared arbitrary detail survives
   remodelling that erases every structural similarity. Worth promoting into §5 as the worked
   example if it holds up.
2. **The route runs through the Iranian and Manichaean corridor** — Middle Persian, a Manichaean
   recension, Baghdad. That is the same corridor H5 proposes on material grounds and the same
   religious traffic §10 tracks at Dunhuang. A transmission of this shape is attested; the question
   for H5 is whether a *second* one ran further east.
3. **An error-correction failure, ~1000 years long.** No mechanism in the Latin Church could detect
   a Buddhist provenance across a language boundary, because none was checking provenance at all —
   the martyrology's check was on sanctity, not on origin. In `background.md` §5.6's terms: a regime
   whose checked-against does not include the question that would have caught this. Compare the
   philological check that eventually did catch it (Conybeare, Peeters), which is a different
   regime entirely.

**Second source, better provenance.** David Bentley Hart, "Saint Śākyamuni,"
<https://davidbentleyhart.substack.com/p/saint-sakyamuni> — an Orthodox theologian and translator
writing without apparatus, but corroborating the record at every point the anonymous note departed
from it: the Persian step is present (6thc.), the Manichaean preference for the Persian version is
named, Barlaam is not described as invented, and **no 1960 removal is claimed**. Two additions:

  - **A candidate source text: the *Lalitavistara Sūtra*.** Specific enough to be checked, and it
    would pin the Sanskrit end of the chain that §5 rung 1 currently carries by name-evidence alone.
  - **A relic.** In 1571 the Venetian doge presented Portuguese King Sebastian with relics said to
  include Josaphat's spine. A physical object, datable and provenanced, generated by a transmission
    error — rung 4 material culture produced *by* a rung-1 chain. It also lands directly on
    @schopen-1997 (*Bones, Stones, and Buddhist Monks*): a bodhisattva's relic, venerated as a
    Christian saint's, in a Catholic reliquary. Worth pursuing on its own.

**Hart sharpens the error-correction question.** His framing is not that the Church *could not*
detect the import but that it absorbed it **without scandal** — nothing prompted a check. That is a
different failure from the one recorded above, and the better one: not absent capacity but absent
trigger. In `background.md` §5.6's terms the regime's checked-against was never invoked, because
no dissonance arose to invoke it. Hart's own question — what does frictionless absorption say about
medieval Christianity's temperament — is a `methods.md` §2 question in disguise, and the project
should not adopt his answer ("irony of providence") as an analytic category.

**The two sources are a tagging illustration.** Same story, same week, two retellings: one anonymous
and uncited that deformed the chain in four places, one by a named scholar that did not. The
register's evidential facet is doing exactly the work it exists for, and this pair is a cheap worked
example for `tags.md` if §9.1's facet question is ever taken up.

**A caution on the sainthood claim.** The popular form — "the Church canonised the Buddha" — is
looser than the record. They appear in **earlier editions of the Roman Martyrology** with a joint
feast on 27 November, and **not in the Roman Missal**. Eastern churches still commemorate them:
Greek Orthodox 26 August Julian, Slavic 19 November Julian. Formal canonisation is a different act
from martyrology inclusion, and the distinction should be preserved in anything the project writes.
Hart states flatly that no formal canonisation process was ever applied to Josaphat, which settles
this independently.

**The source is itself a specimen.** The item arrived as a Substack note (Nick Kistler,
`substack.com/@beardyspiritualman/note/c-314898489`, no citations, self-presented as personal
historical knowledge). Checked against the article above, the retelling had **dropped two links and
added one invention** — a live §3.1 distortion event with its source chain still visible:

| Note's claim | Record | Kind of error |
|---|---|---|
| Sanskrit → Arabic directly | Middle Persian `Bodisav` sits between | **dropped link** |
| — | a **Manichaean** recension carried it | **dropped link** — and the one that matters most here |
| Barlaam was "invented" as a Christian hermit | `Barlaam` ← Arabic `Bilawhar` ← Georgian `Balahvar`; possibly Sanskrit *bhagavan* (unproven) or *purohita* (Degener) | **invention** — the opposite of the truth: the name is further evidence of the chain |
| "removed from the liturgical calendar in 1960" | 1960 is when a *different* saint, Josaphat Kuntsevych, was set at 16 November. No removal in that year is recorded, and Orthodox commemoration continues | **conflation** |
| "the four marks of existence" | the legend turns on the **four sights** | doctrinal term substituted for narrative one |

  The compression is directional: every dropped link shortens the chain and makes the transmission
  look *more* direct and more surprising than it was. That is a testable prediction about how
  transmission stories deform in retelling, and this project has the register to test it on.
  → open question, `background.md` §11.

**Open questions on this case.**

? Is the *Lalitavistara Sūtra* the source text, as Hart suggests? Would pin the Sanskrit end of a
chain currently carried by name-evidence alone.
? The 1571 Josaphat relic given to King Sebastian — does it survive, and is it documented? A
physical object generated by a transmission error, and the point where this case touches
@schopen-1997.
? Was Barlaam's name derived from *bhagavan* (long assumed, unproven) or *purohita* (Degener)?
The answer changes how many rung-1 items the chain carries.
? Did the Latin Church have *any* provenance check that could in principle have caught this, or
only a sanctity check? Determines whether §5.6 records absent capacity or absent trigger.

**Sources.**

- Hart, David Bentley. "Saint Śākyamuni." Substack. Secondary, no apparatus, credentialed author;
  corroborates the record. `#d/christian #r/genealogy #e/secondary`
- Kistler, Nick. Substack note `c-314898489`. Uncited word-of-mouth retelling; retained **because**
  it is defective — it is the §3.1 specimen, not evidence for the history.
  `#d/mahayana #r/genealogy #e/secondary`
- `en:Barlaam and Josaphat`, rev 1362809573. Tertiary; used to adjudicate between the two above,
  not cited for any claim. `#d/method #f/reference #e/secondary`

## 14a. Durable artefacts as a transmission corpus — ceramics and basketry

Opened 2026-09-14 on xian's proposal. **A direction, not yet a programme**: the sources below were
identified by a retrieval probe on the same day and none has been read.

### 14a.1 Why this corpus, for this project

The project's question is general — what evidence distinguishes inheritance and homology from
analogy and convergence. The **specimens worked so far are all text-borne**: the rainbow body and
the resurrection, the Barlaam chain (§14.8), the terma material. That is a fact about which
examples were picked up first, not about the inquiry, and it has a cost — every transmission
question in those cases must clear §3's distortion problem before it reaches evidence.

Ceramics is a different **evidence class**, not a different subject. It is the densest rung-4
corpus that exists (`methods.md` §5, datable material culture), and if specimens are chosen for how
well they discriminate homology from analogy — which is the criterion the general question
implies — it is a strong specimen on its own account rather than a supplement to the Tibetan
material. Four properties the text-borne specimens lack:

- **Survivorship runs the right way.** Fired ceramic is effectively indestructible as sherd,
  ubiquitous, and low-value — so it is neither looted nor recycled, unlike metal. §14.7's
  survivorship problem is not absent but is *unusually mild*, and mild in a direction that can be
  characterised. Basketry is the control that shows what is normally lost: organic, and preserved
  only in deserts, bogs and dry caves.
- **The homology/analogy fight already happened here, with an independent referee.** Childe's
  culture-history read ceramic style as ethnicity; processualism demolished the inference; ancient
  DNA has partly rehabilitated it for some cases and refuted it for others. That is precisely
  `methods.md` §1.2's question — descent or convergence — argued for a century in a domain where
  an **independent, non-stylistic signal now exists to check the answer against**. No text-borne
  specimen offers that at any price.
- **The attribute classes separate along the project's own axis.** See §14a.2.
- **The literature is quantitative and indexed.** Unlike the nexus material (§17.1), it is
  reachable with the instruments already in this repository.

### 14a.2 The decomposition that makes it testable

Ceramic attributes split into two classes that transmit differently, and the split maps onto the
§5 ladder rather than cutting across it.

| Class | Examples | Learned how | Visible in the finished pot? | Ladder analogue |
|---|---|---|---|---|
| **Technical** (chaîne opératoire) | clay selection, temper, forming technique, firing regime | apprenticeship — requires access to the maker | largely not | rung 3, shared arbitrary detail |
| **Decorative** | motif, layout, surface treatment | copyable from the object alone | yes | rung 6, structural similarity |

This is the project's analog-channel argument in material form. A decorative motif can cross a
boundary carried by a traded pot, with no contact between potters; a firing regime cannot. So
**technical continuity is evidence of transmitted practice; decorative continuity is evidence of
contact with objects.** Where the two dissociate, the dissociation is the finding — and it is the
same shape as §14.8's result, where the arbitrary detail (a name) outlived every structural
feature of the story.

### 14a.3 Sources identified

Retrieved by OpenAlex title search, 2026-09-14. Query records in `lit/openalex/queries/`.

- Jordan, Peter, & Stephen Shennan. "Cultural transmission, language, and basketry traditions
  amongst the California Indians." *Journal of Anthropological Archaeology* 22 (2003).
  [10.1016/s0278-4165(03)00004-7](https://doi.org/10.1016/s0278-4165(03)00004-7).
  **Directly on xian's second example**, and it asks the project's question: do basketry traditions
  branch like a phylogeny or blend across neighbours? @jordan-shennan-2003
  `#c/material-culture #r/homology #e/secondary` · src 2003 · Q8b, H11 · access: closed · [unverified]
- Tehrani, Jamshid J., & Mark Collard. "Investigating cultural evolution through biological
  phylogenetic analyses of Turkmen textiles." *Journal of Anthropological Archaeology* 21 (2002).
  [10.1016/s0278-4165(02)00002-8](https://doi.org/10.1016/s0278-4165(02)00002-8).
  The companion method paper; cladistics applied to craft tradition. @tehrani-collard-2002
  `#c/material-culture #r/homology #e/secondary` · src 2002 · H11 · access: closed · [unverified]
- Olalde, I., et al. "The Beaker phenomenon and the genomic transformation of northwest Europe."
  (2018). The aDNA anchor for the pots-and-people question, and heavily cited. @olalde-2018
  `#c/genetics #r/genealogy #e/secondary` · src 2018 · Q6, Q8b · access: **check OA** · [unverified]

> Both craft-phylogenetics papers are in the *Journal of Anthropological Archaeology*. That is a
> journal-level target, and a cheaper route than topic search — see §17.1.

### 14a.4 What could go wrong

- **"Pots are not people."** The standing caution, and the reason the aDNA check matters. Style
  moves by trade, gift, exogamy and emulation without population movement.
- **Functional convergence is rampant.** A vessel that must hold liquid over a fire converges on a
  narrow set of forms everywhere, independently. This is `methods.md` §6 deflator 4 in material
  form, and it is *stronger* here than in the textual cases because the constraint is physical
  rather than cognitive.
- **The typology is the archaeologist's, not the potter's.** "Wares" and "types" are etic
  categories, and the Ford–Spaulding argument over whether types are discovered or imposed is
  §2's emic/etic problem in another field. Note the asymmetry worth exploiting: here the emic
  categories are **unavailable in principle**, where in the Tibetan material they are abundant.
  Two opposite failure conditions for one method.
- **Sampling on the dependent variable** (deflator 7): ceramic sequences are densest where
  excavation has been densest, which tracks modern institutions and not ancient activity.

? **Does the technical/decorative dissociation actually appear in a case where aDNA settles the
population question independently?** That is the whole proposal in one question, and Bell Beaker
is the obvious place to ask it.
? **Do ceramic tradition lifespans fit a constant-extinction (exponential) distribution?** See
`background.md` H15.

## 15. Reference tools and databases

- International Dunhuang Project (idp.bl.uk) — digitised manuscripts, searchable. @idp
  `#d/central-asia #f/dataset #e/secondary` · access: open
- BDRC / TBRC (tbrc.org) — Tibetan text digitisation archive. @bdrc
  `#d/tibetan #f/dataset #e/secondary` · access: open
- *Treasury of Lives* — peer-reviewed Tibetan biographical encyclopedia. @tol
  `#d/tibetan #f/reference #e/secondary` · access: open
- *Encyclopaedia Iranica* (iranicaonline.org) — the standard reference for the H5 material. @iranica
  `#d/iranian #f/reference #e/secondary` · access: open
- Gandhāran Buddhist Texts project (Univ. of Washington) — the birchbark manuscript editions. @gbt
  `#d/mahayana #f/dataset #e/secondary` · access: open
- *Bibliographia Iranica* — Turfan and Central Asian bibliography. @biblio-iranica
  `#d/central-asia #f/reference #e/secondary` · access: open

---

## 16. Controversy register

Live disagreements, recorded as pairs per `methods.md` §7 rather than resolved silently. **Current standing is our reading, not a verdict.**

| # | Dispute | Positions | Bears on | Standing |
|---|---|---|---|---|
| C1 | Origins of Mahāyāna | @hirakawa-1963 (lay-devotional) vs. @harrison-2018 / @nattier-2003 / @boucher-2008 (forest ascetic) vs. @schopen-1997 (cult of the book) | Q2 | Hirakawa displaced; forest vs. book unresolved |
| C2 | Dzogchen's relation to Chan | @demieville-1952 (derivation) vs. @vanschaik-influence + @nubchen (distinct) | Q4 | Settled against derivation |
| C3 | Where the rainbow body comes from | @tiso-2016 (Central Asian contact) vs. @germano-1994 (Tibetan mortuary substrate) | H2 | Germano favoured on dating; Tiso's fieldwork stands regardless |
| C4 | Is "Gnosticism" a usable category | @williams-1996 / @king-2003b (no) vs. inherited usage | H3 | Decided: scare quotes retained |
| C5 | Bön origins and the Tazig identification | @norbu-kailash (deep antiquity, western origin) vs. @bon-scholarship | H5 | Open; **circularity check pending** |
| C6 | The adherent veto | @wcsmith (adherent acceptability) vs. @lincoln-1996 (scholarly independence) | Q5 | **Decided 2026-08-27 for Lincoln/McCutcheon** — schism leaves the veto no determinate holder, and collective acceptability is unobservable (reportable only by authorities, hence a claim about standing). Emic testimony retained as evidence differing in type, not degree. `methods.md` §2.8 |
| C7 | Khenpo A Chö's death date | 1998 (literature) vs. 1999 (publisher copy) | Q1 | Trivial but diagnostic; unresolved |

---

## 17. Gaps and negative results

Recorded per `methods.md` §7. Absence of evidence, noted as such, is a finding. Search
provenance for everything below is in `lit/openalex/QUERIES.md` and `lit/epmc/QUERIES.md`.

### 17.1 Database coverage — a standing constraint

Two retrieval passes on 2026-08-23 established what these tools can and cannot reach. This
governs how much weight any future "not found" deserves.

- **OpenAlex verifies citations; it does not deliver this project's core literature.** Humanities
  monographs are metadata-only. Worse, for two central books what is indexed is a **review of the
  book, not the book** — Tiso's *Rainbow Body and Resurrection* appears only as a 2020 review in
  *Buddhist-Christian Studies*, Schopen's *Bones, Stones* only as a 2000 review in *Philosophy East
  and West*. Easy to mistake one for the other. See `lit/WANTED.md` §2.
- **Its full-text search is unusable for this field.** "rainbow body dzogchen tibetan buddhism"
  returned *A Brief History of Spiral Dynamics* as top hit. `title_and_abstract.search` is precise
  but low-recall. Use the latter, and treat a zero result as weak evidence.
- **The query idiom matters more than the query.** Established 2026-09-14 while looking for the
  craft-phylogenetics literature, and it generalises:
  - `title_and_abstract.search` with several words gives healthy **counts** and unusable
    **ranking** — "phylogenetic analysis basketry" returned a paper on manganese superoxide
    dismutase as its top hit.
  - `title.search` with several words returns **nothing at all**; it appears to require every term.
  - `title.search` with **one distinctive term** works, and found Jordan & Shennan, Tehrani &
    Collard, and the Beaker genomics paper immediately.

  So a zero from a multi-word title search means nothing whatever, and a bad ranking from a
  multi-word topic search is not evidence that the literature is thin. **Probe with single
  distinctive terms first**, then use `cites:` to walk outward from whatever that finds — which is
  how §17.2a's citation-overlap test was run.
- **Europe PMC covers only the etic half of the project** — ancient DNA, bioarchaeology,
  contemplative science. Tibetology, art history, textual studies are simply not indexed.
- **The nexus and comparative-urbanism literature is almost entirely unreachable.** A dedicated pass
  (queries `40-`–`51-`) returned four hits for Kushan trade, one for Begram, and zero for
  Greco-Buddhist art. See §11.1 — Q8's sources are monographs, and §11 is correspondingly thin.
- **Neither reaches Tibetan-language sources at all.** For §1.3 and the `terms.md` work, these
  tools are irrelevant; BDRC and the Dunhuang archives are the instruments.

**Route decided 2026-08-27 — Wikipedia citation harvesting.** §17.1 records a coverage gap; this is
the instrument chosen against it. The `/wikipedia` skill parses `{{cite …}}` templates out of article
wikitext, so it returns the **ISBN-bearing monographs that carry no URL** — precisely the class no
index this project can search will surface, and precisely what §11 is short of. On `en:Gandhara` it
found 150 citations, 7 of them with a durable identifier and no link.

Scope and cautions, recorded before the pass rather than after:
  - **This is a bibliography instrument, not a source.** Wikipedia is tertiary; nothing harvested
  enters the register on Wikipedia's authority. Harvested items are candidates, marked
    `[unverified]` until traced to the work itself.
  - **Targets:** the nexus articles §11 is thin on — Gandhara, Kushan Empire, Dunhuang, Silk Road,
  Begram, Greco-Buddhist art, Palmyra, Sogdia — plus the comparison-class sites the duration table
    will need.
  - **Known limit:** the harvester matches English citation templates. The `fr` and `de` editions use
  `{{Ouvrage}}` and `{{Literatur}}`, which it will silently miss — relevant because the Gandhāran
  and Iranian literature is disproportionately French and German. Extending the alias table is a
    precondition for treating a non-English pass as complete.
  - **Provenance:** every harvest carries a revision-pinned permalink. Record it, since the
    bibliography of a Wikipedia article is itself a moving target.
  - **Ran 2026-08-27.** 10 articles, 821 citations, **730 distinct works**, 32 cited by more
    than one article, and **257 carrying a durable identifier with no URL** — the class the
    earlier passes could not see. Output and cautions: `lit/wikipedia/README.md`; ranked list at
    `lit/wikipedia/ranked.md`.
  - **Two results worth naming.** Rong Xinjiang's 1999 paper on the sealing of the Dunhuang
    library cave — §17.3's named target for Q8a — was found with a DOI, though Persée refused the
    file. And Ponampon's 2019 Cambridge thesis on **visionary experience in a Dunhuang manuscript**
    was retrieved in full: not on any list, and sitting on the Q8a/`#c/thodgal` intersection.
  - **The instrument's limit, measured.** Dunhuang returned 27 citations against Palmyra's 243.
    On the question where Dunhuang is the negative case, that asymmetry bounds what the harvest
    can say — it is a fact about encyclopedia coverage, not about the field.

### 17.2 Searched, nothing found

Zero-hit queries. Given 15.1, these are suggestive, not conclusive — for the humanities items,
absence from the index is closer to "not indexed" than to "does not exist".

| Sought | Query | Weight |
|---|---|---|
| `thod rgal` / visionary practice literature | OpenAlex `12-thodgal` | low — indexing artefact likely |
| Origin of the nimbus/halo in Buddhist art | OpenAlex `16-nimbus-origin` | low — but @pons-2025 was found by other means |
| Robe of glory / Ephrem / Syriac clothing metaphor | OpenAlex `17-robe-glory` | low |
| Thukdam (OpenAlex) | OpenAlex `18-thukdam`; Europe PMC `27-thukdam2` | **none** — the literature exists and was found by other queries; a term-indexing failure, and a caution against trusting any single query |
| Self-mummification / sokushinbutsu | Europe PMC `25-mummify` | moderate — a plausible bioarchaeology topic, absent |
| Radiocarbon authentication of relics | Europe PMC `26-relics` | moderate — same |
| Buddhist mummification | Europe PMC `30-mummy` | moderate |
| **Manichaean–Dzogchen connection of any kind** | OpenAlex `62-mani-dzogchen` | **high — see below** |
| Manichaean light-body ↔ Tibetan Buddhism | OpenAlex `62-mani-dzogchen` | high |

#### 17.2a The strongest negative result the project has

Probe of 2026-09-14. Unlike most zero-results here, this one is **not** plausibly an indexing
artefact, because the same instrument in the same session returned healthy counts for each field
separately:

| Query | Hits |
|---|---|
| `Dzogchen` | 390 |
| `Tibetan Dunhuang manuscripts` | 197 |
| `Manichaeism Central Asia` | 115 |
| `Manichaean Tibetan` | 12 |
| `Manichaeism Tibet` | 8 |
| **`Manichaean Dzogchen`** | **0** |
| **`light body Tibetan Buddhism Manichaean`** | **0** |

Both literatures are substantial and separately well indexed. **Their intersection is
essentially unstudied, and the specific comparison §10 proposes has no hits at all.**

Why this zero carries more weight than the others in §17.2. A zero result normally tells you
little, because two very different things produce it: the literature may not exist, or the index
may simply not cover that area. You usually cannot tell which.

Here you can. The same search tool, run the same day, returned 390 results for Dzogchen and 115
for Manichaeism in Central Asia. So the index covers both fields well, which rules out "the tool
cannot see this material" as the explanation for the zero. What remains is that the work has not
been done.

Two readings, and the project should not choose between them yet:

1. **A real gap.** The philology required spans Middle Persian, Parthian, Sogdian, Uyghur, Coptic,
   Chinese, Syriac and Tibetan, and nobody holds all of it. Field boundaries, not evidence, may be
   what keeps the question unasked.
2. **A question already answered by silence.** Specialists in both fields may have considered and
   dismissed it without publishing a negative. `methods.md` §7.1's archival silence applies to
   modern scholarship as much as to ancient records.

**Done, 2026-09-14.** The test named here — do the two fields cite each other — was run against
the two standard Manichaean works, Klimkeit's *Gnosis on the Silk Road* and BeDuhn's *The
Manichaean Body*, using OpenAlex's `cites:` filter.

| Of the 149 works citing Klimkeit or BeDuhn | Count |
|---|---|
| mentioning **Tibet** in title or abstract | **0** |
| mentioning Dunhuang | 1 |
| mentioning India or Indian | 2 |
| mentioning Buddhism | 2 |

**This favours reading 1 over reading 2.** Had the field considered a Tibetan connection and
rejected it, some trace would be expected in 149 papers. Instead the field does look eastward —
there is work on Indic influence on Mani, and on Buddhism — and Tibet simply never appears. The
question looks to be outside the field's frame rather than settled within it.

Stated against itself: the control counts are small (2 and 2), so this is suggestive and not
decisive. But zero out of 149, in a literature that demonstrably asks adjacent questions, is a
different kind of silence from a bare zero-hit search.

### 17.3 Still open from earlier passes

- **No Wylie recovered** for the Pema Dündul terma title "Dzogchen Kazhag Rangdrol." → `terms.md`.
- **No documented Tibetan–Christian or Tibetan–Manichaean *textual* contact at Dunhuang** located —
  only co-presence, which is rung 5 on the `methods.md` §5 ladder. The project's decisive question.
  **Update 2026-08-27:** Rong Xinjiang's "The Nature of the Dunhuang Library Cave and the Reasons
  for its Sealing," *Cahiers d'Extrême-Asie* 11 (1999), is now identified with a DOI
  ([10.3406/asie.1999.1155](https://doi.org/10.3406/asie.1999.1155)) rather than a name — found by
  the Wikipedia harvest. Persée refused the file; see `lit/WANTED.md`. Still not read, so the gap
  above stands unchanged.
- **Norbu's Italian originals not located**; H4's direct test unavailable, hence the cross-translator
  workaround (§14).
- **No Tibetan-side iconographic study of the rainbow body located** connecting it to the
  Gandhāran/Iranian nimbus complex. Still possibly a real opening — @pons-2025 is the nearest
  approach found, and it does not cross into Tibet.
- **Tiso's pre-2016 articles not located.** Needed to date his hypothesis against his evidence.
- **Steindl-Rast prompt unverified.** Repeated in secondary accounts; no primary confirmation found.

## 18. Acquisition priority

Ranked by movement per unit effort. **29 items are now held locally** (`access: held`); this table
covers what is still wanted. Items verified to exist but not held are in `lit/WANTED.md`.

**Acquisition policy [decided 2026-08-27].** Fetch whatever can be fetched now and mark it for
later processing — retrieval and reading are separate passes, and conflating them has been letting
free items sit unfetched (W1 has been priority 1 across two passes without being pulled). **Books are
low priority to obtain**, on three grounds: length makes them expensive to process, format makes them
hard to excerpt mechanically, and copyright constrains what can be held or quoted. The consequence
worth stating plainly: this project's core literature is monographs, so a policy that deprioritises
books is a decision to work from reviews, articles and bibliographies for now — and any conclusion
resting on a book not read must say so.

| # | Item | Why | Access |
|---|---|---|---|
| 1 | @pons-2025 | Closest located treatment of H5, by a Gandhāra specialist | **held** — read first |
| 2 | *The Rainbow Body's Inner Cinema* (2025) | Directly on the founding question. **Preprint by a pharmacologist, not a Tibetologist — two independent reasons for `#s/speculative`** | **held** (`lit/direct/`, `.docx`) |
| 2a | Ponampon, *Dunhuang Manuscript S.2585* (Cambridge PhD, 2019) | Meditative technique and **visionary experience** in a Dunhuang manuscript — the Q8a/`#c/thodgal` intersection, supervised by Galambos. Unsought, open access, retrieved | **held** (`lit/direct/`) |
| 2b | Rong Xinjiang, "The Nature of the Dunhuang Library Cave…" (1999) | §17.3's named target for Q8a, now with a DOI | `WANTED.md` — Persée refused |
| 3 | @drewes-2010 | Cheapest correction of the largest misconception (Q2) | library |
| 4 | @lott-2020 + @tidwell-2025 | The nearest thing to a test of a rainbow-body-class claim | **held** |
| 5 | @tiso-2016 | The founding comparative question, with fieldwork | purchase — **book not in OpenAlex**, see `WANTED.md` W5 |
| 6 | Review of Tiso, *Buddhist-Christian Studies* (2020) | Cheap proxy for the reception question while the book is on order | `WANTED.md` W5 |
| 7 | @smith-1990 | Short; best read *before* the comparison hardens | purchase |
| 8 | @schopen-1997 | Converts the emic/etic commitment into a technique | library — **book not in OpenAlex**, see `WANTED.md` W6 |
| 9 | @hatchell-2014 | Puts `thod rgal` on the table first-hand | purchase |
| 10 | @bynum-1995 | Makes the Christian half specific instead of assumed | purchase |
| 11 | @headland-1990 | Settles the emic/etic vocabulary at the source | library |
