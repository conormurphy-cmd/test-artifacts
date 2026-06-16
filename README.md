# Chrome Extensions

Internal Chrome extensions for the trading team. Download links are updated automatically by the release pipeline when a new version is tagged.

## Extensions

<!-- EXTENSIONS_TABLE -->
| Extension | Latest Version | Download |
|-----------|---------------|----------|
| Hello World | — | — |
| Price Ticker | — | — |
<!-- /EXTENSIONS_TABLE -->

## Releasing a New Version

Extensions are versioned independently using tags in the format `<extension-name>/v<semver>`.

```bash
# Tag and push a new release
git tag hello-world/v1.0.0
git push origin hello-world/v1.0.0
```

The pipeline will automatically:
1. Stamp the version into `manifest.json`
2. Build a `.zip` artefact
3. Create a versioned GitHub Release (e.g. `hello-world/v1.0.3`) — permanent record
4. Create/update a stable `hello-world/latest` release — the download URL in this README never changes
5. Update the version number shown in this README

## Installing an Extension (Developer Mode)

1. Download the `.zip` from the link above and unzip it.
2. Open Chrome and go to `chrome://extensions`.
3. Enable **Developer mode** (toggle, top-right).
4. Click **Load unpacked** and select the unzipped folder.

## Adding a New Extension

1. Create a directory under `extensions/` with your extension's slug as the name (e.g. `extensions/my-tool`).
2. Add a valid `manifest.json` (Manifest V3) and your extension files.
3. Add a row to the table above with `—` placeholders:
   ```
   | My Tool | — | — |
   ```
4. Tag a release — the pipeline will populate the download link automatically.

## Workflows

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `ci-extensions.yml` | Push / PR to `main` affecting `extensions/**` | Detects which extension directories changed, validates and builds **only those** |
| `build-extension.yml` | Tag push `<extension>/v*.*.*` | Builds the tagged extension, creates a GitHub Release, updates this README |

The CI workflow uses a matrix job — if you change `hello-world` and `price-ticker` in the same commit, both are validated in parallel. If you only change `hello-world`, `price-ticker` is never touched.

## Repository Structure

```
.
├── extensions/
│   ├── hello-world/           # Example extension (green)
│   │   ├── manifest.json
│   │   ├── popup.html
│   │   ├── popup.js
│   │   └── icons/
│   └── price-ticker/          # Example extension (blue)
│       ├── manifest.json
│       ├── popup.html
│       ├── popup.js
│       └── icons/
├── scripts/
│   └── update_readme.py       # README updater (called by release pipeline)
└── .github/
    └── workflows/
        ├── ci-extensions.yml  # CI — validates changed extensions only
        └── build-extension.yml # CD — builds and releases a tagged extension
```
