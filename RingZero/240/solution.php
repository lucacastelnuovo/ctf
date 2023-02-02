<?php
// User : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/240

ini_set('error_displays', 0);

$ip = htmlspecialchars($_GET['url'], ENT_QUOTES);

$f = fsockopen($ip, 80, $errno, $errstr, 5);

if ($f) {
    $result = shell_exec('ping -c 4 ' . $ip);

    echo '<div class="alert alert-success">' . nl2br($result) . '</div>';
    exit;
}

echo '<div class="alert alert-danger">' . $errstr . '</div>';
