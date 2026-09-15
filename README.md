# culture.nexus

An inquiry into evidence for cultural transmission: how to tell **inheritance and homology** from
**analogy and convergence** when two traditions resemble each other, and what kinds of evidence —
trade, artistic and architectural motif, technology, language — can carry that distinction.

The Dzogchen material is the founding case, not the origin of the question. An apparent parallel
between the **rainbow body** and the Christian **resurrection**, met in Chögyal Namkhai Norbu's
*Talks in California, USA 1982*, was taken up as a specific instance of the general problem. The
general problem was there first.

What has changed is not the scope but the machinery: the general question now has questions,
hypotheses and methods of its own rather than being carried implicitly by the particular case.

## The general question and its founding case

| | Founding case | General question |
|---|---|---|
| Question | Are the rainbow body and the resurrection the same *kind* of claim? Is there any chain of contact? | What makes a contact zone generative? What conditions let ideas cross cultural boundaries? |
| Questions | Q1–Q7 | Q8 (a: preconditions, b: downstream traces) |
| Hypotheses | H1–H6 | H7–H14 |
| Status | Provisional answer favouring **structural difference** (H1), with the Central Asian contact window (§7) as the obstacle to any borrowing account | Actively expanding; the error-correction spine (§5.6) is the current organising idea |

They are not separable in practice, and were never meant to be: the transmission machinery keeps rewriting answers on the Dzogchen side, most recently the reading of `gter ma` as a credentialled bypass of an
expensive error-correction regime.

## Documents

| File | What it holds |
|---|---|
| `background.md` | The charter. Questions Q1–Q8, hypotheses H1–H16, findings, cross-checks, open questions. |
| `methods.md` | How the work is done. Comparison, the emic/etic distinction, transmission distortion, the evidence ladder, the seven deflators, tooling. |
| `resources.md` | The source register — topical sections of tagged entries with provenance fields. |
| `terms.md` | Technical glossary. Tibetan (Wylie), Greek, Syriac, Coptic, Avestan, plus method vocabulary. |
| `tags.md` | The faceted markup scheme and its controlled vocabulary — five facets plus two field markers. |
| `chronology.md` | Dated claims, and the date notation that binds this file and `geography.md`. |
| `geography.md` | Sites, regions and polities, keyed on Wikidata Q-ids. |
| `scripts/` | `build_tables.py` — derives the machine forms from the two index files. |
| `results/` | Generated tables, `.csv.gz`. Regenerate; do not hand-edit. |
| `lit/` | Retrieved sources, per-database manifests, query logs, and `WANTED.md`. See `lit/README.md`. |
| `validate.sh` | Structural checks over the register. Run it after editing. |

## Conventions

- **Every register entry carries an `#e/` tag** recording what it can be used to establish, not how
  good it is. `#e/devotional` marks a tradition's self-description; `#e/heuristic` marks fiction and
  cross-domain analogy, which generate questions and never support claims. `#e/attested` is the
  unmarked default — the information is in the other values.
- **`#r/` declares the kind of comparative claim**: genealogy, analogy, or homology. Collapsing these
  is the failure the project is built to avoid.
- **Negative results are recorded**, including zero-hit database queries. An absence is only evidence
  if the archive would have registered the thing had it happened (`methods.md` §7.1).
- **`[unverified]`** means compiled from prior knowledge, not checked against the source. About half
  the register carries it; that is the honest state, not a backlog to hide.

## Current state

Run `./validate.sh` for current counts and structural checks. They are not repeated here:
the figures went stale three times in a single session, and a stale count misinforms where
an absent one merely refers you to the instrument.

What the script counts: an **entry** is a `- ` item whose continuation carries an `#e/` tag, so
prose bullets in discursive sections are excluded. **Open questions** are inline `?` markers against
specific entries; the project-level decisions are separate, in `background.md` §11 and
`methods.md` §9.

**Decided 2026-08-27 — the adherent veto.** The project's longest-standing open item is settled:
a description need *not* be acceptable to adherents. Two grounds. Schism leaves the veto with no
determinate holder, since a tradition in schism contains parties whose accounts of it are mutually
unacceptable. And collective acceptability is not an observable quantity at all — it is reportable
only by authorities, so a report of it is a claim about **standing**, not about acceptance.

The same asymmetry that disqualifies the veto qualifies emic testimony, so the two commitments are
one position rather than two: a report with a determinate bearer (*"I feel sad"*, *"I witnessed the
body shrink"*) carries its own warrant and is interpretable through that bearer's context; a
predicate with no bearer does not. Emic testimony is therefore retained as evidence differing in
**type**, not degree — admitted, and read for what it is evidence of, which is frequently not the
proposition it asserts. → `methods.md` §2.8.

**Built 2026-08-27.** `chronology.md` and `geography.md`, on one schema across two axes —
entity, period, evidential tag — with the date notation specified once and binding both.
`scripts/build_tables.py` derives the machine forms into `results/*.csv.gz`, so the arithmetic has
a single home; the duration table for `background.md` §5.3's comparison class is the first output.
A Wikipedia citation harvest (`lit/wikipedia/`) reached 730 works, 257 of them carrying a durable
identifier and no URL — the monograph class no index this project can search will return.

**Changed 2026-09-14.** The evidential facet was split three ways. `#e/` now says what kind of
thing an entry is; `#v/` says whose frame it speaks from when that is not the analyst's; `#s/` says
how the literature regards it when that is not unremarkable. A census had found that no entry
carried both a kind and a standing value, because the single facet forbade it — so the register had
been discarding one answer per entry. See `tags.md` §5.1.

**The most consequential open items**, all in `background.md` §11 and `methods.md` §9:

1. **What Dunhuang's co-presence actually produced** — needed twice over, as Q8's negative case and as
   the hinge of the contact argument.
2. **Whether "universal replicator theory" is the right frame**, given that fidelity is manufactured
   rather than given.
