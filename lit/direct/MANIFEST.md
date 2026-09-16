# lit/direct — items fetched directly, outside the database skills

For open-access items retrieved from a publisher, repository or preprint server
by URL, where neither the OpenAlex nor the Europe PMC skill could deliver the
file. Provenance is recorded per item because there is no query log to fall back
on.

PDFs and other full texts live in `pdf/` and are **gitignored** (`lit/.gitignore`,
`*/pdf/`). This manifest is committed; the files are not.

Retrieved 2026-08-27 (D1, D2) and supplied 2026-09-16 (D3).

## Held

| # | Item | File | Format | Bytes | Source | Verified |
|---|---|---|---|---|---|---|
| D1 | Keppel Hesselink, Jan M. "The Rainbow Body's Inner Cinema: Phosphenes, Ultrasubjective Hyperspace, and a Neurophenomenological Framework for Tibetan Mystical Experience" (2025) | `W1-rainbow-body-inner-cinema.docx` | **docx** | 1,025,410 | <https://osf.io/download/89tms/> · DOI [10.31234/osf.io/89tms_v1](https://doi.org/10.31234/osf.io/89tms_v1) | title and abstract read from `word/document.xml` |
| D2 | Ponampon, Phra Kiattisak. *Dunhuang Manuscript S.2585: A Textual and Interdisciplinary Study on Early Medieval Chinese Buddhist Meditative Techniques and Visionary Experiences.* MPhil dissertation, University of Cambridge, submitted 10 Oct 2018, deposited 2019 | `ponampon-2018-dunhuang-S2585.pdf` | PDF 1.3 | 12,361,645 | <https://www.repository.cam.ac.uk/handle/1810/284608> · DOI [10.17863/CAM.31982](https://doi.org/10.17863/CAM.31982) | title page extracted |
| D3 | Derbac, Mihai. *The "Five Early" (sNga lnga) Texts of the Tibetan Buddhist Tradition rDzogs chen Sems sde: A Historical, Literary and Textual Study with Critical Edition and Translation of the Tibetan Texts.* PhD thesis, University of Calgary, August 2019 | `derbac-2019-five.pdf` | PDF 1.6 | 1,878,597 | supplied by xian · <http://hdl.handle.net/1880/110861> · PRISM, Univ. of Calgary · ProQuest 27544949 | title page, abstract and table of contents read |

### Notes on D1

Formerly `WANTED.md` W1, priority 1 across two passes. **It is a `.docx`, not a
PDF** — the earlier attempt recorded a failure because the download was checked
for PDF mime type. The download always worked; the check was wrong.

The author is **Jan M. Keppel Hesselink, MD/PhD, an independent researcher in
pharmacology**, writing from a meditation centre — not a Tibetologist, and the
piece is an unreviewed preprint. `#s/speculative` was already assigned on the
grounds of preprint status; the author's distance from the field is a second,
independent reason and should not be collapsed into the first.

### Notes on D2

Not on any acquisition list — surfaced by the Wikipedia citation harvest
(`lit/wikipedia/`). A Cambridge doctoral thesis supervised by **Imre Galambos**,
a Dunhuang specialist, on meditative technique and **visionary experience** in a
Dunhuang manuscript.

That intersection is the project's, and was not expected to exist: Q8a asks what
Dunhuang's co-presence produced, and `#c/thodgal` asks about visionary practice.
A full-text, open-access, supervised study sitting on both is the most valuable
single item this session retrieved.

**Read 2026-09-16**; the findings are `../../resources.md` §11.3c. Two corrections
to this record, both made on the document itself: it is an **MPhil dissertation**,
not a PhD thesis — the degree is named on the title page and the declaration form,
and the text is 23,041 words over 76 pages — and it was **submitted 10 October
2018**, the repository's 2019 being the deposit date. Both errors arrived with the
Wikipedia harvest's metadata and survived until the file was opened. The file was
renamed to match on 2026-09-16.

### Notes on D3

Supplied by xian on 2026-09-16, not sought by any query; the route by which it was
obtained is not recorded here because it is not known to this manifest. The
identifiers above are the ones printed in the document's own front matter.

**The file arrived named `mihai-2019-five.pdf`, which is the author's given name.**
The surname is **Derbac** — PRISM's own citation reads "Derbac, M. (2019)". Renamed
2026-09-16. Noted because it is the second name-or-degree error in this directory
inside one day, and the first one that originated with us rather than with a
metadata source: a filename is a citation too, and nothing validates it.

**Copyright.** Calgary graduate students retain copyright; the ProQuest microform
edition carries its own all-rights-reserved notice. Held for reading, as with the
rest of `pdf/` — which is why `pdf/` is gitignored.

**Read so far**, as of 2026-09-16: pp. 1–24 (front matter, abstract, ch. 1),
**ch. 4** (methods of textual criticism, pp. 69–96), **ch. 5** (the phylogenetic
analysis, pp. 97–120 — the collated apparatus at 5.6, pp. 121–35, skimmed as
apparatus), and **ch. 8's metrical argument** (pp. 186–201). Plus whole-document
term searches.

**Unread**: ch. 2 (lineage history), ch. 3 (oral and textual transmission), chs. 6–7
(the critical editions), the translations at 8.1–8.5, and ch. 9 (conclusion).

No register entry written yet.

## Attempted and failed

| Item | Route | Result |
|---|---|---|
| Rong Xinjiang, "The Nature of the Dunhuang Library Cave and the Reasons for its Sealing," *Cahiers d'Extrême-Asie* 11 (1999) | DOI [10.3406/asie.1999.1155](https://doi.org/10.3406/asie.1999.1155) → Persée | DOI resolves to <https://www.persee.fr/doc/asie_0766-1177_1999_num_11_1_1155>; both `docAsPDF` (403) and `renderPdf` (404) refused. → `WANTED.md` |
| "The Provenance and Character of the Dunhuang Documents," Toyo Bunko | `toyo-bunko.or.jp` URL cited by two Wikipedia articles | **404 — the cited link is dead.** A citation can be live in the encyclopedia and dead on the web; this is why the harvest yields candidates, not sources. |
