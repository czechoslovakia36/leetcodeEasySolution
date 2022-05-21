function add(a, b) {
  return a + b;
}

console.log(add(2, 3));

var sub = function (a, b) {
  return a - b;
};
console.log("sub-->", sub)
console.log(sub(5, 2));

// passing function as an argument

function sum(add, sub) {
  return add + sub;
}

console.log(sum(add,sub));
