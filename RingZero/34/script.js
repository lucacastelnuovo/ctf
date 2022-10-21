// User     : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/34

const u = "administrator";
const p = [];
const k = [176, 214, 205, 246, 264, 255, 227, 237, 242, 244, 265, 270, 283];

for (i = 0; i < u.length; i++) {
  p.push(k[i] - (i * 10 + u.charCodeAt(i)));
}

console.log("Password:", String.fromCharCode.apply(null, p));
