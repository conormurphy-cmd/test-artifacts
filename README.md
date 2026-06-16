# Chrome Extensions

Internal Chrome extensions for the trading team. Download links are updated automatically by the release pipeline when a new version is tagged.

## Extensions

<!-- EXTENSIONS_TABLE -->
| Extension | Latest Version | Download |
|-----------|---------------|----------|
| Hello World | `v1.0.2` | [⬇️ Download](https://github.com/conormurphy-cmd/test-artifacts/releases/download/hello-world/v1.0.2/hello-world-v1.0.2.zip) |
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
3. Create a GitHub Release with the zip attached
4. Update the download link in this README

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

## Repository Structure

```
.
├── extensions/
│   └── hello-world/          # Example extension
│       ├── manifest.json
│       ├── popup.html
│       ├── popup.js
│       └── icons/
├── scripts/
│   └── update_readme.py      # README updater (called by CI)
└── .github/
    └── workflows/
        └── build-extension.yml
```
