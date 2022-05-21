/*
instantiate=create
 Constructure : a constructure is simply a function that used to create an object
 By convention, constructors in JavaScript begin with a
 capital letter to distinguish them from nonconstructor functions.
 */

var object1 = new Object();
var object2 = object1;
// var object = {};
// console.log(typeof object);

object1.myCustomProperty = "awesome!!";
console.log(object2.myCustomProperty);
console.log(object2["myCustomProperty"]);
