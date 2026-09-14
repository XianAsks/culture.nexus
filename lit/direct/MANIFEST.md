# lit/direct — items fetched directly, outside the database skills

For open-access items retrieved from a publisher, repository or preprint server
by URL, where neither the OpenAlex nor the Europe PMC skill could deliver the
file. Provenance is recorded per item because there is no query log to fall back
on.

PDFs and other full texts live in `pdf/` and are **gitignored** (`lit/.gitignore`,
`*/pdf/`). This manifest is committed; the files are not.

Retrieved 2026-08-27.

## Held

| # | Item | File | Format | Bytes | Source | Verified |
|---|---|---|---|---|---|---|
| D1 | Keppel Hesselink, Jan M. "The Rainbow Body's Inner Cinema: Phosphenes, Ultrasubjective Hyperspace, and a Neurophenomenological Framework for Tibetan Mystical Experience" (2025) | `W1-rainbow-body-inner-cinema.docx` | **docx** | 1,025,410 | <https://osf.io/download/89tms/> · DOI [10.31234/osf.io/89tms_v1](https://doi.org/10.31234/osf.io/89tms_v1) | title and abstract read from `word/document.xml` |
| D2 | Ponampon, Phra Kiattisak. *Dunhuang Manuscript S.2585: A Textual and Interdisciplinary Study on Early Medieval Chinese Buddhist Meditative Techniques and Visionary Experiences.* PhD thesis, University of Cambridge, 2019 | `ponampon-2019-dunhuang-S2585.pdf` | PDF 1.3 | 12,361,645 | <https://www.repository.cam.ac.uk/handle/1810/284608> · DOI [10.17863/CAM.31982](https://doi.org/10.17863/CAM.31982) | title page extracted |

### Notes on D1

Formerly `WANTED.md` W1, priority 1 across two passes. **It is a `.docx`, not a
PDF** — the earlier attempt recorded a failure because the download was checked
for PDF mime type. The download always worked; the check was wrong.

The author is **Jan M. Keppel Hesselink, MD/PhD, an independent researcher in
pharmacology**, writing from a meditation centre — not a Tibetologist, and the
piece is an unreviewed preprint. `#e/speculative` was already assigned on the
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
single item this session retrieved. **Unread.**

## Attempted and failed

| Item | Route | Result |
|---|---|---|
| Rong Xinjiang, "The Nature of the Dunhuang Library Cave and the Reasons for its Sealing," *Cahiers d'Extrême-Asie* 11 (1999) | DOI [10.3406/asie.1999.1155](https://doi.org/10.3406/asie.1999.1155) → Persée | DOI resolves to <https://www.persee.fr/doc/asie_0766-1177_1999_num_11_1_1155>; both `docAsPDF` (403) and `renderPdf` (404) refused. → `WANTED.md` |
| "The Provenance and Character of the Dunhuang Documents," Toyo Bunko | `toyo-bunko.or.jp` URL cited by two Wikipedia articles | **404 — the cited link is dead.** A citation can be live in the encyclopedia and dead on the web; this is why the harvest yields candidates, not sources. |
