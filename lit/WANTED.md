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
| ~~W1~~ | ~~*The Rainbow Body's Inner Cinema*~~ | — | **HELD as of 2026-08-27** — `lit/direct/pdf/W1-rainbow-body-inner-cinema.docx`. It is a **`.docx`**; the earlier failure was a PDF mime-type check rejecting a file that had downloaded correctly | Q1, Q3 | done |
| W2 | Huerta-Sánchez E. et al., **"Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA"**, *Nature* 2014 | `PMC4134395` · PMID 25043035 · [10.1038/nature13408](https://doi.org/10.1038/nature13408) | Europe PMC reports `isOpenAccess=Y, hasPDF=Y`, but `download_pdf` hangs and times out (twice) | Q7 (boundary case) | PMC web UI or publisher |
| W3 | Wang C.-C. et al., **"Genomic insights into the formation of human populations in East Asia"**, *Nature* 2021 | `PMC7993749` · PMID 33618348 · [10.1038/s41586-021-03336-2](https://doi.org/10.1038/s41586-021-03336-2) | same — metadata says a PDF exists; the download hangs | Q6, Q7 | PMC web UI or publisher |
| W4 | McCutcheon, R. T. (ed.), ***The Insider/Outsider Problem in the Study of Religion: A Reader*** (1999) | `W1491539038` · closed · no DOI | monograph; closed access | Q5, adherent-veto decision | library / purchase |

| W7 | **"The Production of the Book of Mormon in Light of a Tibetan Buddhist Parallel,"** *Dialogue* 55:4 (2022) | `W4321511807` · [10.5406/15549399.55.4.02](https://doi.org/10.5406/15549399.55.4.02) | closed access | Q5, H7 — the terma/LDS comparison already in print | library / *Dialogue* archive |
| W8 | "Political Rivalry and Doctrinal Debates: A Modern Tibetan Response to the Controversy of Buddhist Revelation" (2017) | `W2601818785` | closed access, no DOI recorded | Q5 — terma authentication contested in a modern setting | library |
| W9 | Rong Xinjiang, **"The Nature of the Dunhuang Library Cave and the Reasons for its Sealing,"** *Cahiers d'Extrême-Asie* 11 (1999) | DOI [10.3406/asie.1999.1155](https://doi.org/10.3406/asie.1999.1155), resolving to <https://www.persee.fr/doc/asie_0766-1177_1999_num_11_1_1155> | Persée refused the file: `docAsPDF` 403, `renderPdf` 404 | **Q8a — the named target** | Persée web UI, or ILL |

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

1. ~~**W1**~~ — **held** 2026-08-27. Two independent reasons for `#e/speculative`: it is an
   unreviewed preprint, *and* its author is an independent pharmacology researcher rather than a
   scholar of the field. Do not collapse the second into the first.
1b. **W9 (Rong Xinjiang)** — the highest-value item on this list. Q8a's decisive question has been
   waiting on it, and it is now identified precisely rather than by name.
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
