var person = {
  _name: "nick",

  get name() {
    console.log("Reading Name!!");
    return this._name;
  },

  set name(value) {
    console.log("Setting name to %s", value);
    this._name = value;
  },
};

console.log(person.name);
person.name = "John";

console.log(person.name);
console.log(person);
