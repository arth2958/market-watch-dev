# Local loss-review preview

No private holdings, account identifiers, portfolio-derived symbol lists, file samples or raw historical price dumps belong in this directory or repository.

The only upload processor is `../loss-monitor.html`, in an opaque-origin sandbox (`allow-scripts allow-downloads`, no allow-same-origin). Its CSP denies network connections, forms, objects, images and scripts other than the exact hashed code. File rows exist only in page memory, render through textContent and clear on reload/Clear. Parent receives numerical height only. No portfolio persistence or analytics.

The fixed public universe uses the third-party S&P constituent dataset and a static ETF list. Yahoo/yfinance adjusted closes produce historical correlations; the published child contains derived top-three matches plus public closing snapshots only, not raw daily history. Coverage and dates are displayed. Highest means highest positive 1-year Pearson correlation in that fixed universe, excluding identical ticker and known same-issuer share classes. It is not a tax or suitability finding.

Build tools are research utilities, not a scheduled workflow. In a private working directory: copy source files and universe.json, install pandas/yfinance, run build_public_data.py, then compose.py (which expects the dev checkout under ./dev). compose.py creates the standalone child and adds the navigation once. Do not commit generated public-market-data.json (raw history). Rebuild requires price/method and content review, sandbox/network/storage tests and mobile/desktop pixel review.

The preview is snapshot-only. No broker feed, wash-sale history ingestion, background notification or daily update schedule is active. New lot template supports long/short stock and ETF lots; options use aggregate broker P/L snapshot only. Publication to production requires a fresh user Go for the reviewed dev revision.
