<?php

// User     : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/254

$input = "00000000000000000000000000000000";
// $input = $_GET['pass'];

// Here I have deobfuscated the code from: https://ringzer0ctf.com/challenges/254/?code
function main()
{
    global $input;

    // match A-Z, a-z, 0-9
    if (!preg_match('/^[^\W_]+$/', $input)) {
        return "Error 1: RegEx";
    }

    // admin1674227342
    // only value checking, value must match
    if ("0e463854177790028825434984462555" != $input) {
        return "Error 2: 0e463854177790028825434984462555 != " . $input;
    }

    // value and type checking, type must not match
    if ("0e463854177790028825434984462555" === $input) {
        return "Error 3: 0e463854177790028825434984462555 ===" . $input;
    }

    // $_GET['input'] must be of length 32 (md5 hash output)
    if (strlen($input) != 32) {
        return "Error 4: 32 != " . strlen($input);
    }

    return "Correct password";
}

echo main() . PHP_EOL;
