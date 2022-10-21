// User     : ltcastelnuovo
// Challenge: https://ringzer0ctf.com/challenges/58

function curry(orig_func) {
  var ap = Array.prototype,
    args = arguments;

  function fn() {
    ap.push.apply(fn.args, arguments);

    if (fn.args.length < orig_func.length) {
      return fn;
    } else {
      return orig_func.apply(this, fn.args);
    }
  }

  return function () {
    fn.args = ap.slice.call(args, 1);

    return fn.apply(this, arguments);
  };
}

function callback(x, y, i, a) {
  return !y.call(x, a[a["length"] - 1 - i].toString().slice(19, 21)) ? x : {};
}

function equal(o, o1) {
  var keys = Object.keys(o);
  var keys1 = Object.keys(o1);

  if (keys1.length != keys.length) {
    return false;
  }

  for (var i = 0; i < keys.length; i++) {
    if (keys[i] != keys1[i] || o[keys[i]] != o1[keys1[i]]) {
      return false;
    }
  }

  return true;
}

function hook(f1, f2, f3) {
  return function (x) {
    return f2(f1(x), f3(x));
  };
}

var h = curry(hook);

var fn = h(function (x) {
  return x >= 48;
}, new Function("a", "b", "return a && b;"));

function genFunc(_part) {
  if (!_part || !_part.length || _part.length !== 4) {
    return function () {};
  }

  const b1 = (y) => y <= 57;
  let b2 = null;

  if (fn(b1)(_part.charCodeAt(0))) {
    b2 = _part[0];
  } else {
    b2 = "'" + _part[0] + "'";
  }

  const key1_3 = _part.substring(1, 3); // key1 -> ey
  const func = "this." + _part[3] + "=" + _part.slice(1, 3) + "+"; // this.1=ey+
  const func_complete = func + b2; // this.1=ey+'k'

  console.log(func_complete);
  return;

  return new Function(key1_3, func_complete);
}

function validatekey() {
  let correct = true;

  const key = "abc1-def2-ghi3-jkl4-mno5";
  const keySplit = key.split("-");

  // Check done
  if (keySplit.length !== 5) {
    console.log("Invalid 1", keySplit.length);
    correct = false;
  }

  try {
    var o = keySplit.map(genFunc);
    // .reduceRight(callback, new (genFunc(keySplit[4]))(Function));

    // if (!equal(o, { T: "BG8", J: "jep", j: "M2L", K: "L23", H: "r1A" })) {
    //   console.log("Invalid 2", o);
    //   correct = false;
    // }
  } catch (e) {
    console.log("Invalid 3", e);
    correct = false;
  }

  if (correct) {
    console.log("--- Correct ---");
  } else {
    console.log("--- Wrong ---");
  }
}

validatekey();
