// static/app.js
let currentUser = '';

async function register() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const res = await fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await res.json();
  alert(data.message || data.error);
}

async function login() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const res = await fetch('/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  });
  const data = await res.json();
  if (data.encKey) {
    currentUser = username;
    document.getElementById('actions').style.display = 'block';
    alert('Login successful!');
  } else {
    alert(data.error);
  }
}

async function action(type) {
  const amount = parseInt(document.getElementById('amount').value) || 0;
  const res = await fetch('/action', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: currentUser, action: type, amount })
  });
  const data = await res.json();
  document.getElementById('result').innerText =
    data.balance !== undefined ? 'Balance: ' + data.balance : data.error;
}

function deposit() { action('deposit'); }
function withdraw() { action('withdraw'); }
function balance() { action('inquiry'); }
