const apiBase = '/api';
const companySelect = document.getElementById('companySelect');
const devicesGrid = document.getElementById('devicesGrid');
const filterSelect = document.getElementById('filterSelect');
const notification = document.getElementById('notification');

let currentCompanyId = null;
let lastKnownStatuses = {};
const pollInterval = 10000;

async function fetchCompanies() {
  const res = await fetch(`${apiBase}/companies`);
  const data = await res.json();
  return data.companies;
}

async function fetchDevices(companyId) {
  const res = await fetch(`${apiBase}/companies/${companyId}/devices`);
  const data = await res.json();
  return data.devices;
}

// Render key details for each device
function renderDevices(devices) {
  const filter = filterSelect.value;
  const filtered = devices.filter(d => filter === 'all' || d.status === filter);
  devicesGrid.innerHTML = '';
  filtered.forEach(d => {
    const tile = document.createElement('div');
    tile.className = 'tile';

    const info = document.createElement('div');
    info.className = 'device-info';

    const name = document.createElement('div');
    name.className = 'device-name';
    name.textContent = `Name: ${d.device_name}`;
    info.appendChild(name);

    const id = document.createElement('div');
    id.className = 'device-id';
    id.textContent = `ID: ${d.device_id}`;
    info.appendChild(id);

    const last = document.createElement('div');
    last.className = 'device-last';
    last.textContent = d.latest_ts
      ? `Last Reading: ${new Date(d.latest_ts).toLocaleString()}`
      : `Last Reading: No readings`;
    info.appendChild(last);

    tile.appendChild(info);

    const status = document.createElement('div');
    status.className = `status ${d.status}`;
    status.textContent = d.status;
    tile.appendChild(status);

    devicesGrid.appendChild(tile);
  });
}

function showNotification(msg) {
  notification.textContent = msg;
  notification.classList.add('show');
  setTimeout(() => notification.classList.remove('show'), 4000);
}

async function loadDevices() {
  if (!currentCompanyId) return;
  const devices = await fetchDevices(currentCompanyId);
  devices.forEach(d => {
    const prev = lastKnownStatuses[d.device_id];
    if (prev && prev === 'offline' && d.status === 'online') {
      showNotification(`${d.device_name} (ID: ${d.device_id}) came ONLINE`);
    }
    lastKnownStatuses[d.device_id] = d.status;
  });
  renderDevices(devices);
}

async function init() {
  const companies = await fetchCompanies();
  renderCompanies(companies);
  companySelect.addEventListener('change', async e => {
    currentCompanyId = e.target.value;
    lastKnownStatuses = {};
    await loadDevices();
  });
  filterSelect.addEventListener('change', loadDevices);
  setInterval(loadDevices, pollInterval);
}
init();

function renderCompanies(companies) {
  companySelect.innerHTML = '<option value="">-- Select company --</option>';
  companies.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c.id;
    opt.textContent = c.name;
    companySelect.appendChild(opt);
  });
}
