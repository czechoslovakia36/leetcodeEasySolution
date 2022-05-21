array = [1, 2, 3, 4];
array2 = new Array(1, 2, 3, 4, 5);

console.log(array, array2);

let method = "push";
let value = 5;

method = method.toLowerCase();

switch (method) {
  case "push":
    array[method](value);
    array2[method](value);
  case "pop":
    array[method]();
    array2[method]();

    console.log(array);
    console.log(array2);
}

// identifying REFERENCE TYPE

console.log(array instanceof Array);
