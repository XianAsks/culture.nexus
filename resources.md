# Resource Register

*Topical catalogue of sources. Reasoning: `methods.md`. Questions and findings: `background.md`. Markup: `tags.md`.*

Status: rev. 3, 2026-08-23. Validate with `./validate.sh`.

---

## 0. How to read an entry

```
- Author, *Title* — one line on what it establishes. @citekey
  `#tags` · subj <period it is about> · src <year written> · <Q/H it bears on>
  · access: <status> · chain: <transmission> · against: @citekey · [unverified]
```

**Fields.** `subj` and `src` are separate because a 1990 book about the first century must never be dated by its publication (`methods.md` §4). `bears-on` names the question or hypothesis the source can actually settle, so the register stays actionable rather than decorative. `chain` records the transmission path for anything translated — the §14 problem made visible per item. `against` points to the entry it contradicts; both then appear in the controversy register (§16).

**Access.** `open` (free online) · `library` · `purchase` · `unlocated` (exists, not yet found) · `held` (we have it).

**Strength of evidence** is carried by the `#e/` tag and governed by the ladder in `methods.md` §5. Summary: `#e/primary` a source text · `#e/attested` documentary or material backing · `#e/inferred` reasonable inference beyond direct evidence · `#e/contested` live disagreement · `#e/speculative` thin · `#e/fringe` outside consensus · `#e/devotional` self-description, i.e. emic · `#e/unverified` not yet checked.

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
  `#d/dzogchen #c/rainbow-body #e/devotional` · subj 1982 · src 1988 (© 1982) · Q1 Q3 · access: held · chain: Tib→It (oral)→En (Barry Simmons)
- ——, *Talks in Conway, USA, July 1982 & January 1983* — same translator and period, different audience. Control for audience-driven vocabulary shift. @norbu-conway
  `#d/dzogchen #c/translation-layer #e/devotional` · subj 1982–83 · src n.d. · H4 · access: purchase · chain: Tib→It→En (Simmons)
- ——, *The Cycle of Day and Night* — carries the lineage-origin narrative behind H6. @norbu-cycle
  `#d/dzogchen #c/lineage-narrative #e/devotional` · subj mythic/8c · src 1984 · Q4 H6 · access: purchase · chain: Tib→En (J. M. Reynolds) · [unverified]
- ——, *The Crystal and the Way of Light* — general introduction; also where Norbu writes on Changchub Dorje. @norbu-crystal
  `#d/dzogchen #c/primordial-basis #e/devotional` · subj 20c · src 1986 · Q1 · access: purchase · chain: →En (ed. John Shane)
- ——, with Adriano Clemente, *The Supreme Source: … Kunjed Gyalpo* — the root Mind Series tantra in English. @norbu-supreme
  `#d/dzogchen #c/primordial-basis #e/primary` · subj 9–10c · src 1999 · Q1 · access: purchase · chain: Tib→It→En (Clemente/Lukianowicz) · [unverified]
- ——, *Drung, Deu and Bön* — Norbu as historian of pre-Buddhist Tibet. @norbu-drung
  `#d/bon #c/lineage-narrative #e/contested` · subj pre-7c · src 1995 · Q4 · access: purchase · [unverified]
- ——, *The Light of Kailash*, 3 vols — Norbu's major historical work; strong Zhang Zhung antiquity claims. **The clearest case of a lineage holder doing etic work.** @norbu-kailash
  `#d/bon #c/emic-etic #e/contested` · subj pre-7c–17c · src 2009–15 · Q4 · access: purchase · chain: Tib→En (Rossi, N. Simmons) · against: @bon-scholarship
- `Kun byed rgyal po` and the Eighteen Texts of the Mind Series. @kunjed
  `#d/dzogchen #c/primordial-basis #e/primary` · subj 9–10c · Q1 · access: purchase · [unverified]
- *Seventeen Tantras* of the Seminal Heart (`snying thig`) — where `thod rgal` and the light-body material concentrate. @seventeen-tantras
  `#d/dzogchen #c/thodgal #e/primary` · subj 11c+ · Q1 Q3 · access: unlocated · [unverified]
- *Zhang Zhung Nyen Gyud* — Bön aural transmission; its rainbow-body lineage incl. Tapihritsa. @zznyengyud
  `#d/bon #c/rainbow-body #e/primary` · subj claimed pre-7c · Q1 · access: unlocated · [unverified]
- Dunhuang Tibetan manuscripts (IOL Tib J; Pelliot tibétain) — **the only genuinely 8th–10th c. Tibetan witnesses; the evidentiary floor under every dating claim here.** @dunhuang-tib
  `#d/central-asia #c/contact-route #e/primary` · subj 8–10c · Q6 · access: open (IDP)
- `gter ma` literature generally — revealed texts attributed to earlier concealment. The sharpest emic/etic problem in Tibetan studies. @terma
  `#c/emic-etic #d/nyingma #e/contested` · subj 11c+ (claimed 8c) · Q4 · access: n/a

? Does the ebook carry a series number, and is it the Sept. 1988 first printing? — **resolved: © 1982, 1st ed. 1st printing Sept 1988.**
→ Cross-translator comparison (Simmons / Reynolds / Clemente / Shane / Lukianowicz) is the practicable H4 instrument absent Italian. `methods.md` §3.2 step 4.

---

## 2. Dzogchen studies

The field has moved from Karmay's founding survey toward the Dunhuang manuscripts and the Seminal Heart's visionary and funerary material. Central finding for us: the earliest layer (Mind Series, 9th–10th c.) differs markedly from the later one (Seminal Heart, 11th c.+), and **the rainbow body belongs to the later layer** — the load-bearing objection to H2.

### Potential sources

- Karmay, Samten G., *The Great Perfection (rDzogs chen)* — the founding philological survey; still baseline. @karmay-1988
  `#d/dzogchen #r/none #e/attested` · subj 8–14c · src 1988 · Q1 · access: library · [unverified]
- van Schaik, Sam, *Approaching the Great Perfection* @vanschaik-2004
  `#d/dzogchen #r/none #e/attested` · subj 14c · src 2004 · Q1 · access: purchase · [unverified]
- ——, "The Early Days of the Great Perfection," *JIABS* 27.1 — dates the earliest stratum from Dunhuang. **Governs the §4 dating obstacle.** @vanschaik-2004b
  `#d/dzogchen #c/contact-route #e/attested` · subj 9–10c · src 2004 · Q6 H2 · access: open · [unverified]
- ——, *earlytibet.com* — research blog citing manuscripts directly. @earlytibet
  `#d/dzogchen #f/web #e/attested` · subj 8–11c · src 2007– · Q1 Q6 · access: open
- Germano, David, "Architecture and Absence in the Secret Tantric History of rDzogs Chen," *JIABS* 17.2 — locates the Seminal Heart in a **Tibetan mortuary substrate**, not an imported one. @germano-1994
  `#d/dzogchen #c/death-process #e/attested` · subj 11–14c · src 1994 · H2 · access: open · against: @tiso-2016 · [unverified]
- Hatchell, Christopher, *Naked Seeing* — `thod rgal` across Dzogchen, Kālacakra and Bön. Best entry to the practice side. @hatchell-2014
  `#d/dzogchen #c/thodgal #e/attested` · subj 11–15c · src 2014 · Q1 · access: purchase
- Achard, Jean-Luc, *L'Essence perlée du secret* — Bön Dzogchen and light-body doctrine. @achard-1999
  `#d/bon #c/light-body #e/attested` · subj 11–14c · src 1999 · Q1 · access: library · [unverified]
- Klein, Anne C., & Tenzin Wangyal, *Unbounded Wholeness* @klein-2006
  `#d/bon #c/primordial-basis #e/attested` · subj 11c+ · src 2006 · Q1 · access: purchase · [unverified]
- Rossi, Donatella, *The Philosophical View of the Great Perfection in the Tibetan Bon Religion* — Rossi also translated Norbu; note how often scholarly and community roles overlap here. @rossi-1999
  `#d/bon #c/emic-etic #e/attested` · subj 11c+ · src 1999 · Q1 · access: purchase · [unverified]

- Baker, Ian, "Embodying Enlightenment: Physical Culture in Dzogchen as revealed in Tibet's Lukhang Murals," *Asian Medicine* 7 (2012) — `thod rgal` and the body in a datable visual source. Bridges §2 and §6: Dzogchen practice *as depicted*, i.e. iconographic evidence rather than doctrinal assertion. @baker-2012
  `#d/dzogchen #c/iconography #e/attested` · subj 17c · src 2012 · Q1 H5 · access: held · license: unspecified
- Chaoul, M. Alejandro, "Magical Movement (`'phrul 'khor`): Ancient Tibetan Yogic Practices from the Bön Religion," *Asian Medicine* 3 (2007). Chaoul has worked closely with Bön lineage holders — read with §14 in view. @chaoul-2007
  `#d/bon #c/thodgal #e/attested` · subj 11c+ · src 2007 · Q1 · access: held · license: unspecified
- Roberti di Sarsina, Paolo, "Chögyal Namkhai Norbu Rinpoche: Dzogchen and Tibetan Tradition. From Shang Shung into the Modern World," *Religions* 3 (2012) — the only peer-reviewed treatment of the project's primary author located so far. **The author is a physician writing on integrative medicine, not a Tibetologist**; sympathetic presentation, not independent scholarship. @robertidisarsina-2012
  `#d/dzogchen #c/emic-etic #e/devotional` · subj 20c · src 2012 · Q1 · access: held · license: cc-by

### Bön as the double test case

- **As control**: an independent rainbow-body lineage in a tradition Christianity had no route to. If the doctrine appears there too, Christian influence loses its explanatory advantage. @bon-control
  `#d/bon #r/deflation #e/inferred` · subj 11c+ · H1 H2 · access: n/a
- **As emic westward claim**: Bön's origin account places its source in **Tazig** (`sTag gzig`) and Olmo Lungring, conventionally identified with Iranian lands. @bon-tazig
  `#c/emic-etic #r/genealogy #e/devotional` · subj claimed pre-7c · H5 · access: n/a
- Martin, Dan; Kvaerne, Per; Karmay — standard scholarship on Bön origins and the Tazig identification. @bon-scholarship
  `#d/bon #r/genealogy #e/contested` · subj pre-7c–11c · src 1985–2010 · H5 · access: library · against: @norbu-kailash · [unverified]

? **Circularity check required** (`methods.md` §2.6): is the Tazig↔Iran identification the tradition's own, or a scholarly gloss the tradition later absorbed? H5 cannot lean on the Bön convergence until this is settled.

---

## 3. The rainbow body

Not one claim but a graded family; typology in `background.md` §4. Only type (a) leaves physical evidence; only type (c), the great transfer, resembles the Christian assumption family — and it does so by *skipping* death. The modern evidentiary centre is Khenpo A Chö, investigated by Tiso, who is simultaneously the best resource and a specimen of the §1.1 problem.

### Primary references

- Nyala Pema Dündul (`Nyag bla Padma bdud 'dul`), 1816–1872 — tertön of Nyarong; founded Kalzang Monastery 1860; teacher of Tertön Sogyal; rainbow body in Saga Dawa 1872 with the standard apparatus (rainbows, three earth-tremors, music, spheres of light, fragrance). **Type (b).** Norbu's "master of my master"; the intermediate is Changchub Dorje (d. 1978). @pema-dundul
  `#c/rainbow-body #d/nyingma #e/devotional` · subj 1816–72 · Q1 Q3 · access: n/a
- Pema Dündul's terma: Guru Amitāyus long-life practice, "Union of Primordial Essences"; plus the cycle Norbu transcribes as **"Dzogchen Kazhag Rangdrol."** @pema-dundul-terma
  `#c/terma #f/manuscript #e/unverified` · subj 19c · Q1 · access: unlocated · chain: Tib→spoken It→En transcription
- Khenpo A Chö, d. **1998 or 1999**, Kham — the best-documented modern case. @khenpo-acho
  `#c/rainbow-body #f/object #e/contested` · subj 1998/99 · Q1 · access: n/a

### Potential sources

- Tiso, Francis V., *Rainbow Body and Resurrection* — field interviews, textual history, and an explicit Central Asian contact hypothesis. **Read evidence chapters and hypothesis chapters as separate documents.** @tiso-2016
  `#c/rainbow-body #r/genealogy #e/contested` · subj 8c–1999 · src 2016 · Q3 Q6 H2 · access: purchase · against: @germano-1994
- ——, pre-2016 articles on the rainbow body in early Dzogchen texts; doctoral work on Milarepa. → Show whether the contact hypothesis grew from the evidence or preceded it. @tiso-articles
  `#c/rainbow-body #r/genealogy #e/unverified` · src pre-2016 · Q6 · access: unlocated
- *Treasury of Lives*, "Nyakla Pema Dudul" — peer-reviewed biography; the etic counterpart to the hagiography. @tol-pemadudul
  `#d/tibetan #f/reference #e/attested` · subj 1816–72 · Q1 · access: open
- Rigpa Wiki / Rangjung Yeshe Wiki entries — useful for Tibetan orthography, unreliable for citation. @rywiki
  `#d/tibetan #f/reference #e/devotional` · access: open
- "Investigating the Rainbow Body," *Lion's Roar* — reportage on the Tiso investigation. @lionsroar-rainbow
  `#c/rainbow-body #f/popular #e/devotional` · src c. 2017 · access: open
- Pistono, Matteo, *In the Shadow of the Buddha* — biographical material on Tertön Sogyal and the Nyarong lineage. Leads, not citations. @pistono
  `#d/tibetan #f/popular #e/devotional` · subj 19–20c · src 2011 · access: purchase · [unverified]
- Steindl-Rast, Br. David — reportedly the origin of Tiso's inquiry. → Verify; if so the comparison was framed emically before evidence was gathered. @steindlrast
  `#d/catholic #r/analogy #e/unverified` · Q6 · access: unlocated

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
  `#c/death-process #r/deflation #e/attested` · subj 2015–19 · src 2020 · Q1 Q3 Q5 · access: held · license: cc-by · doi 10.3389/fpsyg.2020.599190
- Tidwell, Tawni L., "Life in Suspension with Death: Biocultural Ontologies, Perceptual Cues, and Biomarkers for the Tibetan Tukdam Postmortem Meditative State," *Culture, Medicine and Psychiatry* (2025) — Tidwell is trained in both Tibetan medicine and anthropology, so this sits *on* the emic/etic seam rather than on one side of it. @tidwell-2025
  `#c/emic-etic #d/tibetan #e/attested` · subj 2015–24 · src 2025 · Q5 · access: held · license: cc-by
- Namdul, Tenzin, "Death and Happiness: Exploring the Temporalities of the Meditated Death and Everyday Life in Tibetan Buddhist Communities," *Culture, Medicine and Psychiatry* (2025). @namdul-2025
  `#c/death-process #d/tibetan #e/attested` · subj 2015–24 · src 2025 · Q5 · access: held · license: cc-by

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
  `#d/chan #r/vector #e/attested` · subj 8–10c · src 2015 · Q6 · access: purchase
- ——, "Dzogchen, Chan and the Question of Influence" — addresses the methodological question directly. @vanschaik-influence
  `#d/chan #r/deflation #e/attested` · subj 8–10c · src n.d. · Q4 Q7 · access: open · against: @demieville-1952
- Meinert, Carmen — Chan–Dzogchen Dunhuang manuscript studies. @meinert
  `#d/chan #r/genealogy #e/attested` · subj 8–10c · src 2002–07 · Q6 · access: library · [unverified]
- Demiéville, Paul, *Le concile de Lhasa* — the classic Samye study; source of the older derivation thesis and a specimen of its period's assumptions. @demieville-1952
  `#d/chan #r/genealogy #e/contested` · subj 792–94 · src 1952 · Q4 · access: library · against: @vanschaik-influence · [unverified]
- Broughton, Jeffrey — early Chan; the *bSam gtan mig sgron*'s doxography. @broughton
  `#d/chan #r/analogy #e/attested` · subj 8–10c · src 1983–2009 · Q4 · access: library · [unverified]

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
  `#d/mahayana #f/article #e/attested` · subj 1c BCE–5c CE · src 2010 · Q2 · access: library · [unverified]
- Harrison, Paul (ed.), *Setting Out on the Great Way* — incl. "The Forest Hypothesis." Current state of the question. @harrison-2018
  `#d/mahayana #c/asceticism #e/attested` · subj 1–3c CE · src 2018 · Q2 · access: purchase · against: @hirakawa-1963
- Nattier, Jan, *A Few Good Men* — close reading of the *Ugraparipṛcchā* against lay-origins. @nattier-2003
  `#d/mahayana #c/asceticism #e/attested` · subj 1–2c CE · src 2003 · Q2 · access: purchase · against: @hirakawa-1963 · [unverified]
- Boucher, Daniel, *Bodhisattvas of the Forest and the Formation of the Mahāyāna* @boucher-2008
  `#d/mahayana #c/asceticism #e/attested` · subj 1–3c CE · src 2008 · Q2 · access: purchase
- Schopen, Gregory, *Bones, Stones, and Buddhist Monks* — **the methodological model for this project**; inscriptions and archaeology against normative texts. @schopen-1997
  `#d/nikaya #c/emic-etic #e/attested` · subj 2c BCE–5c CE · src 1997 · Q2 Q5 · access: purchase
- ——, *Figments and Fragments of Mahāyāna Buddhism in India* @schopen-2005
  `#d/mahayana #c/emic-etic #e/attested` · subj 2–7c CE · src 2005 · Q2 · access: purchase · [unverified]
- ——, "Mahāyāna in Indian Inscriptions," *IIJ* — the epigraphic-invisibility finding. @schopen-1979
  `#d/mahayana #c/material-culture #e/attested` · subj 2–8c CE · src 1979 · Q2 · access: library · [unverified]
- ! Hirakawa, Akira, "The Rise of Mahāyāna Buddhism and Its Relationship to the Worship of Stūpas" — the lay-devotional origins thesis. **Displaced, and retained deliberately**: it is the source of the received popular picture, and its persistence is itself a transmission-distortion phenomenon. @hirakawa-1963
  `#d/mahayana #c/asceticism #e/contested` · subj 1–3c CE · src 1963 · Q2 · access: library · against: @harrison-2018
- "Origins of the Mahāyāna," *Indo-Iranian Journal* 63.4 — recent review. @iij-2020
  `#d/mahayana #f/article #e/attested` · subj 1c BCE–5c CE · src 2020 · Q2 · access: library
- Walser, Joseph, *Nāgārjuna in Context* — Mahāyāna's social and institutional setting. @walser-2005
  `#d/mahayana #c/material-culture #e/attested` · subj 2–3c CE · src 2005 · Q2 · access: purchase · [unverified]
- Salomon, Richard, *Ancient Buddhist Scrolls from Gandhāra*; *The Buddhist Literature of Ancient Gandhāra* @salomon
  `#d/mahayana #f/manuscript #e/attested` · subj 1–2c CE · src 1999, 2018 · Q2 · access: purchase · [unverified]

---

## 6. Iconography and the glory complex (H5)

The project's most tractable thread: physical, datable, geographically located. Gandhāran nimbus 1st c. CE; Christian halo only 4th c. CE. The better reading is not Buddhist→Christian transmission but a **shared Iranian–Hellenistic glory complex** feeding both — `#r/homology`, and with no dating obstacle. **Method caution** (`methods.md` §5): a shared visual convention shows contact between *workshops*, not that the doctrines the images illustrate travelled with them.

### Primary references

- Gandhāran Buddha with nimbus, Kushan schist — the object raised in the brief. @gandhara-nimbus
  `#c/iconography #r/homology #e/primary` · subj 1c CE · H5 · access: open (Wikimedia Commons)
- Kaniṣka coinage with haloed Buddha, Bactrian legend *BODDO* — datable, portable, state-issued. **The strongest single evidence class for the motif's currency along trade routes.** @kanishka-coins
  `#d/hellenistic #c/iconography #e/attested` · subj 2c CE · H5 · access: open (British Museum) · [unverified]
- Sasanian rock reliefs and silver: the ruler's circular nimbus — where *khvarenah* becomes a halo. @sasanian-nimbus
  `#d/iranian #c/iconography #e/attested` · subj 3–7c CE · H5 · access: open · [unverified]
- "Flaming shoulders" motif, Kushan royal and Buddhist imagery — an Iranian radiance convention entering Buddhist art. **A shared *arbitrary* detail**, which per the §5 ladder counts for more than a shared plausible one. @flaming-shoulders
  `#c/iconography #r/genealogy #e/inferred` · subj 1–3c CE · H5 Q7 · access: open · [unverified]
- Manichaean book illumination, Turfan — documented connection to Syriac and Armenian Gospel illumination. @manichaean-art
  `#d/manichaean #c/iconography #e/attested` · subj 8–11c · H5 Q6 · access: open (Iranica)

### Potential sources

- *Encyclopaedia Iranica*, "FARR(AH)"; Wikipedia, "Khvarenah" — the Iranian glory concept, Avestan through Middle Persian, and its Sasanian visual expression. @farrah
  `#d/iranian #c/glory #e/attested` · subj 1200 BCE–7c CE · H5 · access: open
- Wikipedia, "Halo (religious iconography)"; Britannica, "halo (art)" — orientation and starting chronology; follow to specialists before citing. @halo-ref
  `#c/iconography #f/reference #e/inferred` · subj 5c BCE–15c CE · H5 · access: open
- Greco-Buddhist art of Gandhāra; the first anthropomorphic Buddha images. **Calibration case: this is what demonstrable cultural contact leaves behind.** @greco-buddhist
  `#d/hellenistic #c/material-culture #e/attested` · subj 1–5c CE · Q5 Q7 · access: library

- **Pons, Jessie, "The Buddha and the Sun Disk: Some Reflections on the Dialectics of Light in Gandhāran Art," *Acta Asiatica Varsoviensia* 38 (2025)** — the closest thing yet located to a direct treatment of H5: light as a visual and conceptual problem in Gandhāran art, by a Gandhāra specialist. **Read first.** @pons-2025
  `#d/hellenistic #c/glory #e/attested` · subj 1–5c CE · src 2025 · H5 · access: held · license: cc-by-nc-sa · doi 10.60018/acasva.xbmi1252
- Tanabe, Katsumi, "Gandhāran Smiling Buddhas Revisited — Farewell to the so-called Archaic Smile" (2023) — a specialist undoing a long-standing misreading of a Gandhāran convention. Method value beyond its subject: a worked case of iconographic over-interpretation being corrected. @tanabe-2023
  `#c/iconography #r/deflation #e/attested` · subj 1–4c CE · src 2023 · H5 Q7 · access: held · license: cc-by-nc-nd
- Faresin, Emanuela, & G. Salemi, "Buddhist Stele of Swat Valley: Point Cloud Analysis and Interpretation" (2019) — 3D documentation of a Gandhāran stele; method rather than argument. @faresin-2019
  `#c/material-culture #d/hellenistic #e/attested` · subj 1–5c CE · src 2019 · H5 · access: held · license: cc-by
- Hauser-Ulrich, Johann G., *Deconstructing the Sikri Fasting Buddha: Buddhist Aniconism and…* (MA thesis, Wisconsin–Milwaukee, 2026) — aniconism and its abandonment: when and why the Buddha became depictable. @hauserulrich-2026
  `#d/hellenistic #c/iconography #e/inferred` · subj 1–3c CE · src 2026 · H5 Q2 · access: held · license: unspecified
- Mackenthun, Tamara C., *Continuity in Iranian Leadership Legitimization: Farr-i Izadi, Shi'ism, and…* (Boise State thesis, 2009) — traces *farr* across a very long span. A thesis, and the continuity claim is ambitious; orientation, not authority. @mackenthun-2009
  `#d/iranian #c/glory #e/inferred` · subj 1200 BCE–20c · src 2009 · H5 · access: held · license: unspecified

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
  `#d/gnostic #c/canon-formation #e/attested` · subj 2c CE · src 2003 · Q1 · access: purchase · [unverified]
- Watterson, Meggan, *Mary Magdalene Revealed* — named in the brief for its account of Jesus's persistence. MTS (Harvard Div.), MDiv (Union); the book sits deliberately between theology and spiritual memoir, and reception splits on exactly that (thin referencing, limited engagement with the text itself, large memoir component). **Read as a contemporary theological reading and a reception document, not as the critical treatment.** Pair with @king-2003. @watterson-2019
  `#d/christian #c/historical-jesus #e/devotional` · subj 1c CE / 2019 · src 2019 · Q3 · access: purchase
- Pagels, Elaine, *The Gnostic Gospels*; *Beyond Belief* — where the popular framing originates; Pagels was more cautious about Buddhist parallels than her readers. @pagels-1979
  `#d/gnostic #r/analogy #e/attested` · subj 2–4c CE · src 1979, 2003 · H3 · access: purchase · [unverified]
- de Boer, Esther, *The Gospel of Mary: Beyond a Gnostic and a Biblical Mary Magdalene* @deboer
  `#d/gnostic #c/canon-formation #e/attested` · subj 2c CE · src 2004 · Q1 · access: library · [unverified]

- Kateusz, Ally, *Mary and Early Christian Women: Hidden Leadership* (Palgrave, 2019) — argues from **art and material evidence** as well as texts, which puts it methodologically closer to §6 than to §7. Open access via OAPEN. @kateusz-2019
  `#d/christian #c/iconography #e/attested` · subj 1–6c CE · src 2019 · Q1 Q3 · access: held · license: cc-by-nc-nd
- Smith, Daniel A., "Revisiting the Empty Tomb: The Early History of Easter" (2010) — the development of the empty-tomb tradition, i.e. precisely the strand Q3 argues has *no* Dzogchen analogue. @dasmith-2010
  `#d/christian #c/resurrection #e/attested` · subj 1–2c CE · src 2010 · Q3 H1 · access: held · license: cc-by-nc-nd

? Does the Gospel of Mary actually contain a doctrine of Jesus's continuing presence, or is that supplied by later reading? With pages 1–6 and 11–14 missing this may be undecidable — which would itself be a §14 finding.

---

## 8. Christian scholarship on body, light, and resurrection

Bynum's finding is the indispensable move: Christian resurrection doctrine was for over a millennium preoccupied with *material* continuity, and that preoccupation is what the doctrine is about. It cuts both ways — sharpening the contrast with a rainbow body that dissolves matter, and opening an unexpected convergence with relic culture, incorruptibility and `ring bsrel`. **The relic parallel is less glamorous than the resurrection parallel and probably more real.**

### Potential sources

- Bynum, Caroline Walker, *The Resurrection of the Body in Western Christianity, 200–1336* — **essential**; establishes what the doctrine claimed, the precondition for comparing it. @bynum-1995
  `#d/christian #c/resurrection #e/attested` · subj 200–1336 · src 1995 · Q1 Q3 H1 · access: purchase · [unverified]
- Martin, Dale B., *The Corinthian Body* — Pauline body-language against Greco-Roman physiology. @martin-1995
  `#d/christian #c/resurrection #e/attested` · subj 1c CE · src 1995 · Q1 · access: purchase · [unverified]
- Brock, Sebastian, *The Luminous Eye* — Syriac light-theology and the robe of glory; entry point to Syriac studies. @brock
  `#d/syriac #c/glory #e/attested` · subj 4c CE · src 1985 · H5 · access: purchase · [unverified]
- Williams, Michael A., *Rethinking "Gnosticism"* @williams-1996
  `#d/gnostic #r/deflation #e/attested` · subj 2–4c CE · src 1996 · H3 · access: purchase · [unverified]
- King, Karen L., *What Is Gnosticism?* — with Williams, the reason "Gnostic" keeps its scare quotes. Both are also case studies in category construction from heresiological polemic. @king-2003b
  `#d/gnostic #r/deflation #e/attested` · subj 2–4c CE · src 2003 · H3 · access: purchase · [unverified]
- Lossky, Vladimir; Meyendorff, John — Palamism and the uncreated light. @lossky-meyendorff
  `#d/orthodox #c/transfiguration #e/attested` · subj 14c · src 1944–74 · Q3 · access: library · [unverified]

---

## 9. The Buddhism–"Gnosticism" comparison literature

Conze is the respectable representative: his 1967 *Numen* paper grew from a 1960 Moscow lecture that met such hostility from Indian delegates it reached the front page of *Pravda*. His framing is more careful than his reputation — he compared Mahāyāna to **gnosis**, explicitly not to the Gnostics as a social group. Below him quality falls sharply. Against all of it stands **Barlaam and Josaphat**: the one demonstrated transmission, running Buddhism→Christianity, with the loanword still visible in the saint's name. That is the standard the §10 claims must meet.

### Potential sources

- Conze, Edward, "Buddhism and Gnosis," *Numen* 14 @conze-1967
  `#d/mahayana #r/analogy #e/contested` · subj 1–4c CE · src 1967 · H3 · access: library
- Bianchi, Ugo (ed.), *The Origins of Gnosticism* (Messina, 1966) — where Conze's paper appears, and where the field tried and failed to define "Gnosticism." @bianchi-1967
  `#d/gnostic #r/analogy #e/contested` · subj 1–4c CE · src 1967 · H3 · access: library
- **Barlaam and Josaphat** — Manichaean → Arabic → Georgian → Latin; *bodhisattva* → *Bodisav* → *Iodasaph* → *Josaphat*. See W. C. Smith, *Towards a World Theology*, and the philology on the Georgian *Balavariani*. **The gold standard** (`methods.md` §5). @barlaam
  `#c/contact-route #r/genealogy #e/attested` · subj 8–11c · src 1981– · H3 Q7 · access: library · [unverified]
- Clement of Alexandria, *Stromata* I.15 — mentions "Boutta." Thin but genuine. @clement
  `#d/hellenistic #r/vector #e/primary` · subj c. 200 CE · H3 · access: open · [unverified]
- ! Lindtner, Christian, *Geheimnisse um Jesus Christus* — Gospels derived from Mahāyāna sūtras. Rejected by specialists; a specimen of method failure. @lindtner
  `#d/mahayana #r/genealogy #e/fringe` · src 1998– · access: library · [unverified]
- ! 19th–20th c. Essene/Therapeutae-Buddhist theories; "Jesus in India" literature. @jesus-india
  `#c/historical-jesus #r/genealogy #e/fringe` · src 1894– · access: open

---

## 10. Diffusion: contact zones and vectors

The Tarim–Gansu corridor, 7th–10th c., held simultaneously: Tibetan administration at Dunhuang (c. 786–848); Manichaeism as Uyghur state religion (763–840) with the Turfan manuscript find; Church of the East monasticism at Bulayïq with Christian Sogdian manuscripts in Syriac script; Sogdian merchant networks; Chinese Buddhism and Chan. **Manichaeism, not Christianity, has the elaborated light-body metaphysics demonstrably present in the right place at the right time** — which makes Christianity an indirect ancestor at best, and may make H5 subsume H2, since Manichaeism is itself downstream of the Iranian glory complex.

### Primary references

- Berlin Turfan Collection; Chotscho finds; Christian Sogdian manuscripts from Bulayïq. @turfan
  `#d/central-asia #c/contact-route #e/primary` · subj 8–11c · Q6 H2 · access: open
- Xi'an ("Nestorian") Stele, 781 CE; Dunhuang Jingjiao documents. @xian-stele
  `#d/syriac #c/contact-route #e/primary` · subj 781 CE · Q6 · access: open

### Potential sources

- BeDuhn, Jason David, *The Manichaean Body: In Discipline and Ritual* — standard study of Manichaean body-theory and practice. @beduhn-2000
  `#d/manichaean #c/light-body #e/attested` · subj 3–8c · src 2000 · H2 H5 · access: open (PDF)
- Gardner, Iain, & Samuel N. C. Lieu (eds.), *Manichaean Texts from the Roman Empire* @gardner-lieu
  `#d/manichaean #f/translation #e/primary` · subj 3–6c · src 2004 · H2 · access: purchase · [unverified]
- van Schaik, Sam, & Imre Galambos, *Manuscripts and Travellers* — one manuscript reconstructed into a picture of who actually moved along the road. **Model for well-done contact evidence.** @vanschaik-galambos
  `#d/central-asia #r/vector #e/attested` · subj 10c · src 2012 · Q6 · access: library · [unverified]
- Moffett, Samuel Hugh, *A History of Christianity in Asia*, vol. 1 @moffett
  `#d/syriac #c/contact-route #e/attested` · subj 1–15c · src 1992 · Q6 · access: purchase · [unverified]
- Dalton, Jacob, *The Taming of the Demons* — Dunhuang, ritual, and the imperial-to-postimperial transition. @dalton-2011
  `#d/tibetan #c/contact-route #e/attested` · subj 8–11c · src 2011 · Q6 · access: purchase · [unverified]
- ! Palmer, Martin, *The Jesus Sutras* — popular treatment of the Jingjiao material; unreliable interpretive frame. Use the underlying documents. @palmer
  `#d/syriac #r/genealogy #e/fringe` · subj 7–10c · src 2001 · access: purchase · [unverified]

- van Oort, Johannes, "Manichaeism: Its sources and influences on Western Christianity," *Verbum et Ecclesia* 30 (2009) — van Oort is a Manichaeism and Augustine specialist. Bears on H2, though its frame is Manichaeism→West rather than →East. @vanoort-2009
  `#d/manichaean #r/genealogy #e/attested` · subj 3–6c · src 2009 · H2 · access: held · license: cc-by
- ——, "Augustine and Manichaeism: new discoveries, new perspectives," *Verbum et Ecclesia* 27 (2006). @vanoort-2006
  `#d/manichaean #c/light-body #e/attested` · subj 4–5c · src 2006 · H2 · access: held · license: cc-by

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
  `#c/nexus #r/analogy #e/contested` · subj 1–3c CE · src 1932 · Q8a · access: library · [unverified]
- **Rong Xinjiang, "The Nature of the Dunhuang Library Cave and the Reasons for its Sealing,"** and *Eighteen Lectures on Dunhuang* (Brill) — **the highest-value item in this section.** Directly addresses why Dunhuang's co-presence produced preservation rather than synthesis. @rong-dunhuang
  `#d/central-asia #c/material-culture #e/attested` · subj 5–11c · src 2013 · Q8a · access: library · [unverified]
- Galambos, Imre, *Dunhuang Manuscript Culture: End of the First Millennium* — manuscript practice at the negative case. @galambos-2020
  `#d/central-asia #f/manuscript #e/attested` · subj 9–11c · src 2020 · Q8a · access: library · [unverified]
- de la Vaissière, Étienne, *Sogdian Traders: A History* (Brill) — the standard work on the network that **transmitted without innovating**, which is the distinction Q8 turns on. @delavaissiere
  `#d/central-asia #c/contact-route #e/attested` · subj 3–10c · src 2005 · Q8a H7 · access: library · [unverified]
- Mairs, Rachel (ed.), *The Graeco-Bactrian and Indo-Greek World* (Routledge, 2020) — includes a chapter on Roman objects in the Begram hoard and the memory of Greek rule. The 450-year Hellenistic time-depth behind H8 is this volume's subject. @mairs-2020
  `#d/hellenistic #c/material-culture #e/attested` · subj 300 BCE–200 CE · src 2020 · Q8a H8 · access: library
- Smith, Andrew M., *Roman Palmyra: Identity, Community, and State Formation* (2014) — the fullest treatment of the clearest negative case outside Asia. @smith-palmyra
  `#d/hellenistic #c/material-culture #e/attested` · subj 1–3c CE · src 2014 · Q8a · access: library · [unverified]
- Kodama, Shinjiro, "The Palmyrene commercial settlement in Vologesia" (1965) — a Palmyrene trading colony on Parthian territory; small-scale evidence of how a caravan city projected itself outward. @kodama-1965
  `#d/hellenistic #c/contact-route #e/attested` · subj 1–3c CE · src 1965 · Q8a · access: held · license: unspecified
- Denisenko, V. L., "Kushan Settlement Complexes in the Kashmir Valley," *Vestnik NSU* (2024) — settlement archaeology at the Kushan periphery. @denisenko-2024
  `#d/central-asia #c/material-culture #e/attested` · subj 1–4c CE · src 2024 · Q8a · access: held · license: unspecified
- Jia, Ben, "Reading Hierarchy on the Silk Road — The Ancient Sogdian Letters," *Communications in Humanities Research* (2025) — social structure inside the Sogdian network. @jia-2025
  `#d/central-asia #c/contact-route #e/inferred` · subj c. 313 CE · src 2025 · Q8a · access: held · license: unspecified
- Hall, Peter, *Cities in Civilization* (1998) — the modern comparative treatment of urban creative episodes; explicitly asks Q8a, entirely for post-classical cases. Its hazard is the one `background.md` §5.3 names: it samples on the dependent variable throughout. @hall-1998
  `#c/nexus #r/analogy #e/contested` · subj 400 BCE–1990s · src 1998 · Q8a · access: library · [unverified]
- Jacobs, Jane, *The Economy of Cities* (1969) — the argument that cities generate novelty through recombination of existing work. Theoretical, unfalsifiable as stated, but the source of the intuition. @jacobs-1969
  `#c/nexus #r/analogy #e/speculative` · src 1969 · Q8a · access: purchase · [unverified]

### 11.4 Transmission channels: how fusion actually happens

Serves H8 and H9. The linguistic literature supplies both the mechanism and a measurement.

- **Thomason, Sarah G., & Terrence Kaufman, *Language Contact, Creolization, and Genetic Linguistics* (1988)** — the borrowing scale: lexical borrowing indicates casual contact, structural borrowing indicates sustained intimate contact. **The operational instrument for H8**, converting "how deep was the contact" into a question about grammar rather than impression. @thomason-kaufman-1988
  `#c/loanword #d/method #e/attested` · subj n/a · src 1988 · Q8a H8 · access: library · [unverified]
- Spinney, Laura, *Proto* — the source of the household/market observation as it entered this project: conservative kinship and nature vocabulary against volatile technological vocabulary. @spinney-2025
  `#d/indo-european #c/loanword #e/attested` · subj 4500 BCE– · src 2025 · Q8a H8 · access: held
- Metal names and the Indo-European dispersal — `*h₂éyos` (copper/bronze) is reconstructible, while iron, tin and lead terms commonly derive from non-IE sources, and "metal" is a wanderwort shared across IE, Uralic, Turkic and sometimes Old Chinese. **The evidence that the split is real and not merely intuitive.** @metal-names
  `#d/indo-european #c/loanword #e/attested` · subj 4000–1000 BCE · Q8a · access: open (academia.edu) · [unverified]
- Creolization and the Atlantic world; Gullah as a creole; jazz and foodways as non-linguistic fusion products. **The type specimen for household-channel fusion, and a warning that it can occur under coercion.** @creolization
  `#c/loanword #r/homology #e/attested` · subj 17–20c · Q8a H8 · access: unlocated · [unverified]
- **Origo, Iris, "The Domestic Enemy: The Eastern Slaves in Tuscany in the Fourteenth and Fifteenth Centuries," *Speculum* 30 (1955), 321–66** — enslaved Tatars, Russians, Circassians, Greeks, Moors and Ethiopians in Florentine households, predominantly women, raising the children. **The only household channel Florence has**, and its cultural consequences appear unstudied. @origo-1955
  `#c/nexus #d/method #e/attested` · subj 14–15c · src 1955 · Q8a H9 · access: library · [unverified]
- **Jones-Rogers, Stephanie E., *They Were Her Property: White Women as Slave Owners in the American South* (Yale UP, 2019)** — documents a market in enslaved wet nurses created by slaveholding white women and advertised in newspapers, a sector she describes as largely invisible. **The clearest evidence that the household channel was operated by the enslaved**, at scale, at the exact moment of children's language acquisition. @jonesrogers-2019
  `#c/nexus #d/method #e/attested` · subj 1800–65 · src 2019 · Q8a H8 · access: purchase · [unverified]
- Harris, Joel Chandler, *Uncle Remus* (1880), and the West African Anansi/hare cycles behind it — a documented instance of the household channel: trickster tales carried by enslaved caregivers to white children. Harris's framing device *is* a description of the mechanism; his distortions are a separate problem. @uncle-remus
  `#c/lineage-narrative #r/genealogy #e/contested` · subj 18–19c · src 1880 · Q8a H8 · access: open · [unverified]
- Carney, Judith, *Black Rice: The African Origins of Rice Cultivation in the Americas* (2001) — a **technical** transfer via enslaved knowledge, i.e. the market/workshop channel rather than the household one. Useful precisely because it lets the two channels be distinguished in one society. @carney-2001
  `#c/material-culture #r/genealogy #e/contested` · subj 17–18c · src 2001 · Q8a H8 · access: library · [unverified]
- The AAVE-origins debate — creolist versus Anglicist accounts (Mufwene, Rickford, Poplack); and the question of African substrate features in white Southern speech. **The direct linguistic test of household-channel transmission**, and still contested. @aave-origins
  `#c/loanword #r/genealogy #e/contested` · subj 17–20c · Q8a H8 · access: library · [unverified]
- Lowe, Kate, & T. F. Earle (eds.), *Black Africans in Renaissance Europe* (CUP, 2005); and the "Rethinking 'Domestic Enemies': Slavery and Race Formation in Late Medieval Florence" literature. The Florentine end of the same question. @lowe-earle-2005
  `#c/nexus #d/hellenistic #e/attested` · subj 14–16c · src 2005 · Q8a H9 · access: library · [unverified]
- ! Alessandro de' Medici's maternity — **contested**. Spini traces Simonetta da Collevecchio to the Roman peasantry; Nestor (1560s) reports the African-servile origin as a rumour circulated by Alessandro's exiled enemies; Hibbert and Brackett accept it. Catalogued as a case of ancestry claims generated as political weapons, **not** as evidence for the household channel. @alessandro
  `#c/nexus #r/deflation #e/contested` · subj 1510–37 · Q8a · access: open · [unverified]
- Florentine banking diaspora (Bardi, Peruzzi, Medici branches at London, Bruges, Avignon, Lyon) and the Council of Ferrara-Florence 1438–39 → Gemistos Plethon → Ficino. **Florence's contact runs outward and arrives late and elite** — the evidence behind H9's *diaspora-return* type. @florence-contact
  `#c/nexus #r/analogy #e/inferred` · subj 13–15c · Q8a H9 · access: library · [unverified]

? **What did Dunhuang's co-presence actually produce?** The project needs this answer twice over —
for Q8a as the negative case, and for §10, where the contact argument depends on it. If Dunhuang
held Manichaeans, Church-of-the-East monks, Tibetan administrators and Chan translators in one oasis
for sixty years and produced no doctrinal synthesis, that is strong evidence for H7 and a serious
problem for H2.

---

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
  `#d/nikaya #r/deflation #e/contested` · subj 800–300 BCE · src 2007 · Q2 Q4 · access: library · [unverified]
- ——, *Buddhism in the Shadow of Brahmanism* (Brill, 2011). @bronkhorst-2011
  `#d/nikaya #c/emic-etic #e/contested` · subj 300 BCE–500 CE · src 2011 · Q2 · access: open (PDF) · [unverified]
- The second urbanization — iron, surplus, coinage, Magadha and Kosala. The material precondition for a renunciant class. @second-urbanization
  `#d/nikaya #c/material-culture #e/attested` · subj 700–300 BCE · Q2 Q4 · access: library · [unverified]

### 12.3 Jesus's milieu

- Mark 1:9–11 // Matt 3:13–17 // Luke 3:21–22; Josephus, *Ant.* 18.5.2 — the baptism by John, and Josephus's independent notice of John. **The one solid lineage datum**, and the standard illustration of the criterion of embarrassment. @baptism
  `#d/christian #c/lineage-narrative #e/primary` · subj c. 28 CE · Q4 · access: open
- Sanders, E. P., *Jesus and Judaism* (1985); *The Historical Figure of Jesus* (1993) — the apocalyptic reconstruction, and the standard against which others argue. @sanders
  `#d/christian #c/historical-jesus #e/attested` · subj 1c CE · src 1985, 1993 · Q4 · access: purchase · [unverified]
- Allison, Dale C., *Constructing Jesus* (2010) — on memory, and on how much of the reconstruction the sources can actually bear. @allison-2010
  `#d/christian #c/historical-jesus #e/attested` · subj 1c CE · src 2010 · Q4 · access: purchase · [unverified]
- Crossan, J. D., *The Historical Jesus* (1991); Mack, Burton, *A Myth of Innocence* (1988) — the Cynic-sage reconstruction: itinerant, propertyless, aphoristic. **Contested**, and its premise of a thoroughly Hellenized Galilee is disputed by Meyers and others. Included as the live alternative to the apocalyptic reading. @crossan-mack
  `#d/christian #c/historical-jesus #e/contested` · subj 1c CE · src 1988, 1991 · Q4 · access: purchase · against: @sanders · [unverified]
- Sepphoris and Tiberias — the archaeology of Hellenized Galilee. Material rather than textual evidence for the milieu. @galilee-archaeology
  `#d/hellenistic #c/material-culture #e/attested` · subj 1c CE · Q4 · access: library · [unverified]
- ! Notovitch, Nicolas, *The Unknown Life of Jesus Christ* (1894) — the "Life of Saint Issa"; Jesus in India. **Exposed as fabrication by Max Müller**; the Hemis manuscript was never produced. Catalogued as the origin of a persistent claim, not as evidence. @notovitch-1894
  `#c/historical-jesus #r/genealogy #e/fringe` · src 1894 · access: open · [unverified]

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
  `#c/historical-jesus #r/genealogy #e/fringe` · src 1965 · Q3 · access: purchase · [unverified]

? There is no forensic proof of death and there cannot be. What exists is unanimous early testimony
including from hostile and independent sources, and **no early tradition of survival** — the denials
that do exist (docetic, substitutionist) deny the *body* or the *identity of the victim*, not the
fact of a death on the cross. That distinction matters for Q3 and should not be blurred.

---

## 13. Method and theory

Full treatment in `methods.md`. Sources only here.

- Smith, Jonathan Z., *Drudgery Divine* @smith-1990
  `#d/method #r/deflation #e/attested` · subj 1600–1990 · src 1990 · Q7 · access: purchase
- ——, *Map Is Not Territory*; *Imagining Religion* @smith-map
  `#d/method #r/analogy #e/attested` · src 1978, 1982 · Q7 · access: purchase · [unverified]
- Lincoln, Bruce, "Theses on Method," *MTSR* 8 — two pages; the sharpest statement on scholarship versus its object. **Bears on the adherent-veto decision.** @lincoln-1996
  `#d/method #r/none #e/attested` · src 1996 · Q5 · access: open · against: @wcsmith
- Smith, Wilfred Cantwell, *Towards a World Theology* — the adherent-acceptability principle. @wcsmith
  `#d/method #c/emic-etic #e/contested` · src 1981 · Q5 · access: library · against: @lincoln-1996 · [unverified]
- Headland, Pike & Harris (eds.), *Emics and Etics: The Insider/Outsider Debate* — **where Pike and Harris argue it out directly.** @headland-1990
  `#d/method #c/emic-etic #e/attested` · src 1990 · Q5 · access: library
- McCutcheon, Russell T. (ed.), *The Insider/Outsider Problem in the Study of Religion* @mccutcheon-1999
  `#d/method #c/emic-etic #e/attested` · src 1999 · Q5 · access: library · [unverified]
- Asad, Talal, *Genealogies of Religion*; Masuzawa, Tomoko, *The Invention of World Religions* — **"religion" and its cognates as historically constructed categories**; the reflexivity problem (`methods.md` §2.7). @asad-masuzawa
  `#d/method #c/emic-etic #e/attested` · src 1993, 2005 · Q5 · access: purchase · [unverified]
- Taves, Ann, *Religious Experience Reconsidered* — the convergence explanation; deflator 4. @taves-2009
  `#d/method #r/deflation #e/inferred` · src 2009 · Q7 · access: purchase · [unverified]
- Spinney, Laura, *Proto* — the project's methodological prompt. @spinney-2025
  `#d/indo-european #c/loanword #e/attested` · subj 4500 BCE– · src 2025 · Q7 · access: held
- Anthony, David W., *The Horse, the Wheel, and Language* @anthony-2007
  `#d/indo-european #c/material-culture #e/attested` · subj 4500–1500 BCE · src 2007 · Q7 · access: purchase · [unverified]
- Reich, David, *Who We Are and How We Got Here* @reich-2018
  `#d/indo-european #c/genetics #e/attested` · subj 50000 BCE– · src 2018 · Q7 · access: purchase · [unverified]
- **Zhang F. et al. (34 authors), "The genomic origins of the Bronze Age Tarim Basin mummies," *Nature* 599 (2021)** — genetically isolated local population, culturally cosmopolitan. **Culture moved; people did not. The project's calibration case for how genetics deflates a diffusion story.** @tarim-2021
  `#d/central-asia #c/genetics #e/attested` · subj 2100–1700 BCE · src 2021 · Q7 · access: held · license: cc-by · doi 10.1038/s41586-021-04052-7
- Huerta-Sánchez E. et al., "Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA," *Nature* 512 (2014) — Tibetan highland adaptation. Included to **mark a boundary**: genetics answers questions about people; doctrines are not carried in genomes. @epas1-2014
  `#d/tibetan #c/genetics #e/attested` · subj 40000 BCE– · src 2014 · Q7 · access: WANTED (W2) · doi 10.1038/nature13408
- Li C. et al., "Evidence that a West-East admixed population lived in the Tarim Basin as early as the early Bronze Age," *BMC Biology* 8 (2010); and "Analysis of ancient human mitochondrial DNA from the Xiaohe cemetery," *BMC Genetics* 16 (2015) — **the pre-2021 consensus that @tarim-2021 overturned**, by the group that established it. Holding the before *and* the after is what makes the calibration case arguable rather than asserted. @li-xiaohe
  `#d/central-asia #c/genetics #e/contested` · subj 2100–1700 BCE · src 2010, 2015 · Q7 · access: held · license: cc-by · against: @tarim-2021
- Dai S.-S. et al., "The Genetic Echo of the Tarim Mummies in Modern Central Asians," *Mol. Biol. Evol.* 39 (2022). @dai-2022
  `#d/central-asia #c/genetics #e/attested` · subj 2100 BCE–present · src 2022 · Q7 · access: held · license: cc-by-nc
- Zhao X. et al., "Tracing bronze to iron age population dynamics in Northwest Xinjiang using ancient genomes," *Genome Biology* (2026). @zhao-2026
  `#d/central-asia #c/genetics #e/attested` · subj 2000–500 BCE · src 2026 · Q6 Q7 · access: held · license: cc-by-nc-nd
- Wang T. et al., "Tianshanbeilu and the Isotopic Millet Road: reviewing the late Neolithic/Bronze Age radiation of human millet consumption from north China to Europe," *National Science Review* 6 (2019) — **subsistence and isotopes rather than genomes**: material evidence for the corridor, and a rare case where the thing demonstrably transmitted is a crop. @wang-2019
  `#d/central-asia #c/material-culture #e/attested` · subj 3000–1000 BCE · src 2019 · Q6 Q7 · access: held · license: cc-by
- Hu H. et al., "Evolutionary history of Tibetans inferred from whole-genome sequencing," *PLoS Genetics* 13 (2017). @hu-2017
  `#d/tibetan #c/genetics #e/attested` · subj 40000 BCE– · src 2017 · Q7 · access: held · license: cc-by
- **Haber M. et al., "Ancient DNA and the rewriting of human history: be sparing with Occam's razor," *Genome Biology* 17 (2016)** — a caution paper from inside the field about over-reading aDNA into simple migration stories. **Reads as a genetics-native statement of `methods.md` §6's deflators.** @haber-2016
  `#c/genetics #r/deflation #e/attested` · subj n/a · src 2016 · Q7 · access: held · license: cc-by
- Hendy J., "Ancient protein analysis in archaeology," *Science Advances* 7 (2021) — paleoproteomics; what the newer molecular toolkit can and cannot establish. @hendy-2021
  `#c/material-culture #d/method #e/attested` · subj n/a · src 2021 · Q7 · access: held · license: cc-by-nc
- Nelson S. et al., "Tracing population movements in ancient East Asia through the linguistics and archaeology of textile production," *Evolutionary Human Sciences* 2 (2020) — **converging linguistic and material evidence on one technology**, which is the Spinney/`Proto` method applied to East Asia. @nelson-2020
  `#d/central-asia #c/loanword #e/attested` · subj 5000–1000 BCE · src 2020 · Q7 · access: held · license: cc-by
- Tocharian, Gāndhārī, Sogdian, Bactrian — the corridor's languages and their loanword evidence. @corridor-languages
  `#d/central-asia #c/loanword #e/attested` · subj 1–10c CE · Q6 Q7 · access: library
- Witzel, E. J. Michael, *The Origins of the World's Mythologies* — ambitious deep-time diffusion; useful because contested. @witzel-2012
  `#d/indo-european #r/homology #e/contested` · subj 65000 BCE– · src 2012 · Q7 · access: purchase · [unverified]

---

## 14. Transmission distortion

Protocol in `methods.md` §3. Sources only here.

- Cross-translator study: Simmons / Reynolds / Clemente / Shane / Lukianowicz on shared Norbu terminology. → **The practicable H4 instrument.** @cross-translator
  `#c/translation-layer #d/dzogchen #e/inferred` · subj 1980s · H4 · access: partial
- Lopez, Donald S., Jr., *Prisoners of Shangri-La* — how Tibetan Buddhism was reshaped in Western reception. @lopez-1998
  `#d/tibetan #c/translation-layer #e/attested` · subj 1900–1998 · src 1998 · H4 · access: purchase · [unverified]
- McMahan, David L., *The Making of Buddhist Modernism* — the idiom in which 20th-c. Buddhist teaching addressed Western audiences. @mcmahan-2008
  `#d/mahayana #c/translation-layer #e/attested` · subj 1850–2008 · src 2008 · H4 · access: purchase · [unverified]
- Said, Edward, *Orientalism*, read alongside its Tibetology-specific critics — contested in application to Buddhist studies, which is itself informative. @said-1978
  `#d/method #c/translation-layer #e/contested` · subj 1800–1978 · src 1978 · H4 · access: purchase · [unverified]
- Tucci, Giuseppe, and the IsMEO milieu in Naples — Norbu's institutional context, and a case where scholarship and its political setting are hard to separate. @tucci
  `#d/tibetan #c/emic-etic #e/inferred` · subj 1930–80 · Q5 · access: library · [unverified]

---

## 15. Reference tools and databases

- International Dunhuang Project (idp.bl.uk) — digitised manuscripts, searchable. @idp
  `#d/central-asia #f/dataset #e/attested` · access: open
- BDRC / TBRC (tbrc.org) — Tibetan text digitisation archive. @bdrc
  `#d/tibetan #f/dataset #e/attested` · access: open
- *Treasury of Lives* — peer-reviewed Tibetan biographical encyclopedia. @tol
  `#d/tibetan #f/reference #e/attested` · access: open
- *Encyclopaedia Iranica* (iranicaonline.org) — the standard reference for the H5 material. @iranica
  `#d/iranian #f/reference #e/attested` · access: open
- Gandhāran Buddhist Texts project (Univ. of Washington) — the birchbark manuscript editions. @gbt
  `#d/mahayana #f/dataset #e/attested` · access: open
- *Bibliographia Iranica* — Turfan and Central Asian bibliography. @biblio-iranica
  `#d/central-asia #f/reference #e/attested` · access: open

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
| C6 | The adherent veto | @wcsmith (adherent acceptability) vs. @lincoln-1996 (scholarly independence) | Q5 | **Undecided — `methods.md` §9.1** |
| C7 | Khenpo A Chö's death date | 1998 (literature) vs. 1999 (publisher copy) | Q1 | Trivial but diagnostic; unresolved |

---

## 17. Gaps and negative results

Recorded per `methods.md` §7. Absence of evidence, noted as such, is a finding. Search
provenance for everything below is in `lit/openalex/QUERIES.md` and `lit/epmc/QUERIES.md`.

### 15.1 Database coverage — a standing constraint

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
- **Europe PMC covers only the etic half of the project** — ancient DNA, bioarchaeology,
  contemplative science. Tibetology, art history, textual studies are simply not indexed.
- **The nexus and comparative-urbanism literature is almost entirely unreachable.** A dedicated pass
  (queries `40-`–`51-`) returned four hits for Kushan trade, one for Begram, and zero for
  Greco-Buddhist art. See §11.1 — Q8's sources are monographs, and §11 is correspondingly thin.
- **Neither reaches Tibetan-language sources at all.** For §1.3 and the `terms.md` work, these
  tools are irrelevant; BDRC and the Dunhuang archives are the instruments.

### 15.2 Searched, nothing found

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

### 15.3 Still open from earlier passes

- **No Wylie recovered** for the Pema Dündul terma title "Dzogchen Kazhag Rangdrol." → `terms.md`.
- **No documented Tibetan–Christian or Tibetan–Manichaean *textual* contact at Dunhuang** located —
  only co-presence, which is rung 5 on the `methods.md` §5 ladder. The project's decisive question.
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

| # | Item | Why | Access |
|---|---|---|---|
| 1 | @pons-2025 | Closest located treatment of H5, by a Gandhāra specialist | **held** — read first |
| 2 | *The Rainbow Body's Inner Cinema* (2025) | Free at OSF; directly on the founding question. **Preprint — tag `#e/speculative`** | `WANTED.md` W1 |
| 3 | @drewes-2010 | Cheapest correction of the largest misconception (Q2) | library |
| 4 | @lott-2020 + @tidwell-2025 | The nearest thing to a test of a rainbow-body-class claim | **held** |
| 5 | @tiso-2016 | The founding comparative question, with fieldwork | purchase — **book not in OpenAlex**, see `WANTED.md` W5 |
| 6 | Review of Tiso, *Buddhist-Christian Studies* (2020) | Cheap proxy for the reception question while the book is on order | `WANTED.md` W5 |
| 7 | @smith-1990 | Short; best read *before* the comparison hardens | purchase |
| 8 | @schopen-1997 | Converts the emic/etic commitment into a technique | library — **book not in OpenAlex**, see `WANTED.md` W6 |
| 9 | @hatchell-2014 | Puts `thod rgal` on the table first-hand | purchase |
| 10 | @bynum-1995 | Makes the Christian half specific instead of assumed | purchase |
| 11 | @headland-1990 | Settles the emic/etic vocabulary at the source | library |
