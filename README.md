# Market watch review

Dev preview: https://arth2958.github.io/market-watch-dev/

This is a public review copy, not the production release. Production requires the owner's explicit Go. Keep the review banner and noindex tag on this dev copy. Noindex is not access control: anyone can read the page and repository.

## What is in the page

- Earnings momentum: verified report snapshots, separate quarter and fixed-year weekly proxies, source evidence, and a temporary scratchpad.
- Tim Knight watch: a partial disclosed book, source dates, disclosure-day market prices, timestamped delayed quote snapshots, hypothetical price-only short comparisons, confirmed covers and source links.

The single `index.html` contains the layout, CSS, JavaScript, data and a compressed evidence image. It needs no build service, login, market API, downloaded font or secret. Clicking Refresh does not refresh quotes. Scratchpad changes are not saved or sent anywhere.

## How to update without changing the other tab

1. Open `index.html` in GitHub and choose Edit. Search for `id="earnings"` or `id="knight"` to locate the tab being updated. Preserve the other section.
2. Make source-grounded data changes, including dates and caveats. Do not merely change the checked date when a source failed.
3. Keep the visible text and the matching sortable `data-*` values together. These are two copies of the same fact, not separate estimates.
4. Commit to main. GitHub Pages publishes main's root folder. Wait for the Pages deployment to finish successfully.
5. Open the deployed page, verify the changed numbers and source links, then check both tabs on a phone and desktop. A commit alone is not a successful release.
6. Keep the approved companion dashboard in sync through its own publishing process. This repository does not automatically write to another dashboard or production repository.

### Knight rows

Search for `data-ticker="AAOI"` for an example. Each `price-row` is followed by its `price-detail` row. Keep them together when adding or removing a holding.

Sortable attributes are `data-ticker`, `data-date` (YYYY-MM-DD), `data-open`, `data-close`, `data-current`, and `data-pl`. Use plain numbers without dollar signs or commas in numeric attributes. Use an empty string for unavailable data, never zero. Visible cells also need the formatted values, quote session and exact source timestamp. Source links and stop caveats belong in the following detail row.

Short P/L percent = (disclosure-day close - delayed quote) / disclosure-day close * 100. A positive result means the stock fell. This is not Tim's actual trading return: disclosure closes are not his fills, and share sizes, fees, dividends and borrow costs are unknown. Leave it unavailable when the disclosure-day close is unavailable. Never substitute a weekday for a weekend disclosure date.

For covers, add the source-confirmed cover date and that session's market prices to the covers table. Absence from a later video is not proof of an exit. A new disclosure is not necessarily a new initiation. Do not turn chart resistance or a gap into an exact stop.

### Earnings data and scratchpad

The `verifiedHistory` object near the script contains verified weekly readings used by the scratchpad and weekly chart. Keep its values consistent with the displayed snapshot, checked date and source notes. Never mix forecast years to calculate a weekly revision. A comparison requires seven-day spacing. The easing-cuts proxy needs four same-year weekly readings and three negative changes that become progressively less negative. A gap or year change breaks that sequence.

Quarter revisions and weekly fixed-year EPS are different series. Preserve that distinction. Do not present a proprietary Earnings Scout signal or a trading entry recommendation. Update the archived evidence image only when its label, source report and visible endpoints also change.

## Review checklist

- Both tabs load directly using `#earnings` and `#knight`.
- Phone widths of 320 and 390 pixels have no sideways scrolling; desktop tables remain readable.
- Sort each Knight column both ways; unavailable numeric values stay last and details remain attached to their ticker.
- Expand a holding and cover row; check the linked sources.
- Switch quarter/weekly charts and inspect the chart data.
- Add a temporary reading; check validation and Reset.
- Confirm displayed dates, delayed quote timestamps and source limitations.
- Compare the actual published file with the intended commit, not just the editor preview.

## Production release

Do not turn this dev repository into production. Use a separate approved production repository. Remove or replace dev-only labels there, check the audience and all source permissions, and verify the final Pages URL and deployed contents. Never copy workflows or data destinations blindly. New design or logic changes return to dev for review before production.

This is a dated public-facts dashboard, not a complete live portfolio or trading advice. Subscriber-only source material must not be republished here as full posts or charts.
