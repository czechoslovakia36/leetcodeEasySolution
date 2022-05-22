function sayName(msg) {
  console.log(msg);
}

function sayName(msg) {
  console.log(`${msg} is latest`);
}

// IN JAVASCRIPT FUNCTION WHICH APPEARS AT LAST WINS

console.log(sayName("helllo"));
