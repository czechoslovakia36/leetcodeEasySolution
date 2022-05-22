/*a = [1, 3, 4, 5, 6];

if (1 in a) {
  console.log("Yes!!");
}
*/
// IN OPERATOR LOOKS FOR A PROPERTY WITH A GIVEN NAME IN A SPECIFIC OBJECT
//  in operator check for both own properties and prototype properties
// hasOwnProperty only check if given property exists and is an own property
var person = {
  name: "Nick",
  sayName: function () {
    console.log(this.name);
  },
  age: 25,
};

console.log("sayName" in person);
console.log("toString" in person);
console.log(person.hasOwnProperty("toString"));

// REMOVING PROPERTIES
delete person.age;
console.log(person);

// ENUMERATION(MEANS WE CAN ITERATE USING FOR LOOP)

for (property in person) {
  console.log("Name:   " + property);
  console.log("Value:   " + person[property]);
}

//  KEY FUNCTION RETURN ARRAY OF ALL THE KEYS OF OBJECT
console.log(Object.keys(person));



