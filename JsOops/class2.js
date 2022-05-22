// Consturtor is just a function

function Person() {}

var person1 = new Person();
var person2 = new Person();

console.log(typeof person1);

function Person(name) {
  this.name = name;
  this.sayName = function () {
    console.log(this.name);
  };
}

var person1 = new Person("Nick");
console.log(person1.name);
