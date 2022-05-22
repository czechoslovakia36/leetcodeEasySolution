a = new Array(1, 2, 3);

// console.log(a);
// console.log(Array.isArray(a));

function reflect(value) {
  // arguments object is not array.
  console.log(arguments[0]);
  console.log(arguments[1]);
  return value;
}

// console.log(reflect(5));
console.log(reflect(2, 4));
// console.log(reflect.length);


// FUNCTION WHICH ACCEPTS DYNAMIC NUMBER OF ARRAY


function sum(){

    var result=0;
    i=0
    len=arguments.length

    while(i<len){
        result+=arguments[i];
        i++;
    }
 return result
}
console.log(sum(1,2,3,4,5))