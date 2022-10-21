// User     : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/31

var _commands = [
  "val", //0
  "cpass", // 1
  "alk3", // 2
  "02l1", // 3
  "?p=", // 4
  "indexOf",
  "href",
  "location",
  "<div class='error'>Wrong password sorry.</div>",
  "html",
  "#cresponse",
  "click",
  ".c_submit", // 12
];

$(".c_submit")[click](function () {
  var input = $("#cpass")[val]();

  if (input == "02l1" + "alk3") {
    if (
      document[_commands[7]][_commands[6]][_commands[5]](_commands[4]) == -1
    ) {
      document[_commands[7]] =
        document[_commands[7]][_commands[6]] + _commands[4] + input;
    }
  } else {
    $(_commands[10])[_commands[9]](_commands[8]);
  }
});
