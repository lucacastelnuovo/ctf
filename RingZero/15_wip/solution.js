#!/usr/bin/env node

const fs = require("fs");

let elf = fs.readFileSync("./elf.txt", "utf8");

while (/^[a-z\d+/=]+$/i.test(elf)) {
  elf = Buffer.from(elf, "base64").toString("binary");
}

elf = Buffer.from(elf, "binary").reverse();

fs.writeFileSync("./elf.bin", elf);
