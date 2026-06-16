const manifest = chrome.runtime.getManifest();
document.getElementById('version').textContent = `v${manifest.version}`;

// Mock price data — in a real extension this would come from an API or background script
const prices = [
  { market: 'Man City vs Arsenal — 1X2', price: 1.85, change: +0.03 },
  { market: 'LeBron Points O/U 27.5',    price: 1.91, change: -0.05 },
  { market: 'Chiefs ML',                  price: 2.10, change:  0.00 },
  { market: 'Djokovic Set Handicap -1.5', price: 1.74, change: +0.12 },
];

const container = document.getElementById('prices');

prices.forEach(({ market, price, change }) => {
  const dir   = change > 0 ? 'up' : change < 0 ? 'down' : 'flat';
  const arrow = change > 0 ? '▲' : change < 0 ? '▼' : '—';
  const sign  = change > 0 ? '+' : '';

  const row = document.createElement('div');
  row.className = 'row';
  row.innerHTML = `
    <span class="market">${market}</span>
    <span>
      <span class="price ${dir}">${price.toFixed(2)}</span>
      <span class="change">${arrow} ${sign}${change.toFixed(2)}</span>
    </span>
  `;
  container.appendChild(row);
});
