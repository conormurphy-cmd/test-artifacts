// Reads the version from the extension manifest and displays it in the popup
const manifest = chrome.runtime.getManifest();
document.getElementById('version').textContent = `v${manifest.version}`;
