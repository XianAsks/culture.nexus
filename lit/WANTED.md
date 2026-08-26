# Wanted — verified but not accessible

Items whose **existence and citation details are confirmed** by a database lookup, but
whose full text we do not have. Distinct from `../resources.md` §17, which lists things
we have looked for and *not* confirmed to exist at all.

Maintained by hand. Verified means: an OpenAlex work ID or a PMCID/PMID was retrieved,
with a DOI where one exists. It does **not** mean the item has been read.

---

## 1. Confirmed, no full text

| # | Item | Verified as | Why not held | Bears on | Route |
|---|---|---|---|---|---|
| W1 | **"The Rainbow Body's Inner Cinema: Phosphenes, Ultrasubjective Hyperspace, and a Neurophenomenological Framework for Tibetan Mystical Experience"** (2025) | `W4410982367` · gold OA · [10.31234/osf.io/89tms_v1](https://doi.org/10.31234/osf.io/89tms_v1) | download via the skill failed; it is an **OSF preprint**, freely readable at the DOI | Q1, Q3 | fetch direct from OSF |
| W2 | Huerta-Sánchez E. et al., **"Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA"**, *Nature* 2014 | `PMC4134395` · PMID 25043035 · [10.1038/nature13408](https://doi.org/10.1038/nature13408) | Europe PMC reports `isOpenAccess=Y, hasPDF=Y`, but `download_pdf` hangs and times out (twice) | Q7 (boundary case) | PMC web UI or publisher |
| W3 | Wang C.-C. et al., **"Genomic insights into the formation of human populations in East Asia"**, *Nature* 2021 | `PMC7993749` · PMID 33618348 · [10.1038/s41586-021-03336-2](https://doi.org/10.1038/s41586-021-03336-2) | same — metadata says a PDF exists; the download hangs | Q6, Q7 | PMC web UI or publisher |
| W4 | McCutcheon, R. T. (ed.), ***The Insider/Outsider Problem in the Study of Religion: A Reader*** (1999) | `W1491539038` · closed · no DOI | monograph; closed access | Q5, adherent-veto decision | library / purchase |

| W7 | **"The Production of the Book of Mormon in Light of a Tibetan Buddhist Parallel,"** *Dialogue* 55:4 (2022) | `W4321511807` · [10.5406/15549399.55.4.02](https://doi.org/10.5406/15549399.55.4.02) | closed access | Q5, H7 — the terma/LDS comparison already in print | library / *Dialogue* archive |
| W8 | "Political Rivalry and Doctrinal Debates: A Modern Tibetan Response to the Controversy of Buddhist Revelation" (2017) | `W2601818785` | closed access, no DOI recorded | Q5 — terma authentication contested in a modern setting | library |

## 2. Book confirmed only through its reviews

A distinction worth keeping, because it is easy to mistake one for the other. For these
two, **OpenAlex does not index the book** — it indexes a journal review of the book. The
review is a real, citable source in its own right (and useful: reviews summarise and
criticise), but it is not the work itself.

| # | Book wanted | What is actually indexed | Bears on |
|---|---|---|---|
| W5 | Tiso, F. V., ***Rainbow Body and Resurrection*** (North Atlantic Books, 2016) | a 2020 review in *Buddhist-Christian Studies* — `W3114936353`, [10.1353/bcs.2020.0026](https://doi.org/10.1353/bcs.2020.0026), closed | Q3, Q6, H2 |
| W6 | Schopen, G., ***Bones, Stones, and Buddhist Monks*** (1997) | a 2000 review in *Philosophy East and West* — `W2061561327`, [10.1353/pew.2000.0001](https://doi.org/10.1353/pew.2000.0001), closed | Q2, Q5 |

→ Both reviews are worth acquiring on their own account: a review of Tiso by the
Buddhist-Christian studies community is direct evidence of how that field received the
contact hypothesis, which is a `methods.md` §1.1 question.

## 3. Priority

1. **W1** — free at the DOI, directly on the project's founding question, and the only
   item here obtainable in under a minute. Caveat: it is a **preprint**, not peer
   reviewed; tag `#e/speculative` until that changes.
2. **W5 review** — cheap proxy for the reception question while the book itself is on order.
3. **W2** — the citation is already usable in the register without the full text, since it
   is cited there only to mark a boundary (genetics answers questions about people, not
   doctrines).
4. **W4**, **W6**, **W3** — library or purchase; none blocking.

## 4. Not listed here

- Items sought and **not confirmed to exist**: `../resources.md` §17 (Tiso's pre-2016
  articles; a Tibetan-side iconographic study of the rainbow body; documented
  Tibetan–Manichaean textual contact at Dunhuang).
- Items never searched for because no database reaches them — Tibetan-language sources,
  most of the Tibetology and religious-studies monograph literature. See `README.md`.
