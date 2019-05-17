<?php
$flag = file_get_contents("/flag");

if (!isset($_GET["md4"]))
{
	highlight_file(__FILE__);
	die();
}

if ($_GET["md4"] == hash("md4", $_GET["md4"]))
{
	echo $flag;
}
else
{
	echo "bad";
}
?>
