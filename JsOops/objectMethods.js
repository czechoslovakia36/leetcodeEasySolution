var person = {
  name: "Nick",
  sayName: function () {
    console.log(this.name);
  },
};

person.sayName();

function sayNameForAll() {
  console.log(this.name);
}

var person2 = new Object();
person2.name = "Pick";
person2.sayName = sayNameForAll;

person2.sayName();
