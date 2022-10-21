<?php

// User     : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/254

$output = "";

$password = true;
$hash = "0e463854177790028825434984462555"; // strlen = 32

// here password should be truthy
if ($hash == $password && $hash !== $password) {

    echo "strlen: " . strlen($password) . PHP_EOL;

    // here password should be a long string
    if (strlen($hash) == strlen($password)) {
        $output = "success";
    } else {
        $output = "error 1";
    }
} else {
    $output = "error 2";
}

echo $output . PHP_EOL;
