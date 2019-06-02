<?php
include '../config.php';
$conn = mysqli_connect($servername, $username, $password, "keith_db");
$result = mysqli_query($conn, "SELECT * FROM users WHERE username='".$_POST["username"]."' AND password='".$_POST["password"]."';");
if (mysqli_num_rows($result) == 0) {
echo("<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">
  <title>ess-que-el</title>
  <link href=\"bootstrap.min.css\" rel=\"stylesheet\">
  <link href=\"signin.css\" rel=\"stylesheet\">
</head>
<body class=\"text-center\">
  <form method=\"post\" class=\"form-signin\">
    <h1 class=\"h3 mb-3 font-weight-normal\">Keith's Secret Site</h1>");
if ($_POST["username"]) {
echo("    <h1 class=\"h3 mb-3 font-weight-normal\">Incorrect!</h1>");
}
echo("<label for=\"usernameInput\" class=\"sr-only\">Username</label>
    <input id=\"usernameInput\" name=\"username\" class=\"form-control\" placeholder=\"Username\" required autofocus>
    <label for=\"inputPassword\" class=\"sr-only\">Password</label>
    <input type=\"password\" name=\"password\" id=\"passwordInput\" class=\"form-control\" placeholder=\"Password\" required>
    <button class=\"btn btn-lg btn-primary btn-block\" type=\"submit\">Sign in</button>  
  </form>
</body>
</html>");
} else {
echo("<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">
  <title>ess-que-el</title>
  <link href=\"bootstrap.min.css\" rel=\"stylesheet\">
  </style>
</head>
<body class=\"text-center\">
  <h1 class=\"h3 mb-3 font-weight-normal\">Hello Keith!</h1>
  <h1 h1 class=\"h3 mb-3 font-weight-normal\">The flag is hsctf{mysql_real_escape_string}</h1>
</body>
</html>");
}