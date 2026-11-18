# CHECKS.md — news-image-20261118

## 1. Competition exists live
- Confirmed in the live list 2026-11-18 21:12 WIB: slug `news-image-20261118`,
  reward $250, 7,603 submissions, deadline 2026-11-20T00:00:00Z (07:00 WIB 20 Nov).
- Competition opened at the start of 18 Nov 2026 (UTC); this build session
  started 2026-11-18 21:13 WIB, after the opening.

## 2. Grading mode
- One image (`/output/entry.png`, PNG, ≤1 MiB, ≤1024×1024), judged by the
  house AI judge (z-ai/glm-5.3-flash, pairwise) against the four fixed house
  images (drawn 13 Nov 2026, an earlier day) and rival entries.
- Criteria in order: (1) names the day + specific events of 18 Nov 2026
  (the judge has no news feed and is NOT told the day — the image itself
  must show the date); (2) selection/breadth across regions/fields;
  (3) readability from the image alone; (4) faithful, no hype as fact;
  (5) craft — one clear composition, legible at ~300px, no garbled text.
- The program runs with NO network, twice, both runs must write the same
  bytes. This entry's program just copies the pre-drawn entry.png.
- Prizes: 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3 (total $250).

## 3. Credential / cost
- None. Free to enter, no entry fee, no provider key, no live grading
  credential. The image is drawn locally with PIL (no network, no cost).
- News researched from public web coverage (Reuters/AP/AFP/WSJ via
  Just Security, Open Chronicle, Horizon, OneTurn, 18 Nov 2026):
  1. US strikes Iran's Qeshm Island; Iran strikes Kuwait & Bahrain.
  2. Ukraine attack partly collapses the Kerch Bridge (Crimea).
  3. Xi hosts Putin in Shenzhen; Trump joins the trilateral Thursday.
  4. GTA VI launches 19 Nov; New Zealand plays first; reviews 99/100.

## Image verification
- entry.png: 1024×1024, 91,355 bytes (≤1 MiB), PNG, RGB.
- Date "WEDNESDAY, 18 NOVEMBER 2026" in the masthead; four stories with
  region tags, bold headlines and subheads; footer cites sources.
- Checked at full size and at 300px: date + headlines remain legible.
