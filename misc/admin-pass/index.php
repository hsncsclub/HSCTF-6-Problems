<?php
	if ($_POST['password']) {
		if (md5($_POST['password']) === '6df4c2a41091d8c737db7a44e3d07fb3') {
			echo 'congrats the flag is hsctf{' . $_POST['password'] . '}';
		} else {
			echo 'l0000000l thats the wrong password lmfao!';
		}
		echo '<hr>oh hi you entered a password</hr>';
	}
?>

<!DOCTYPE html>

<html>
	<head>
		<!-- IMPORTANT NOTE: THE FLAG IS NOT hsctf{literally_not_the_flag} -->
		<title>admin password checker</title>
		<meta charset='utf-8'>
		<meta author='Weastie'>
		<style>
			body {
				background-color: purple;
				color: white;
			}
			a {
				color: white !important
			}
			a:hover {
				margin-top: 80px;
			}
		</style>
	</head>
	<body>
		<h1> password checker </h1>
		<form method='POST'>
			<h1> pls enter password here </h1>
			<input type='text' name='password' placeholder='password' />
			<input type='submit' />
		</form>
		<hr>
		<h1> as my tribute to richard michael stallman </h1>
		<h1> here is a link to the open source github </h1>
		<marquee scrolldelay='1'>
			<a href='https://gitlab.com/WeastieWeastie/admin-password/'>https://gitlab.com/WeastieWeastie/admin-password/</a>
		</marquee>
	</body>
</html>
