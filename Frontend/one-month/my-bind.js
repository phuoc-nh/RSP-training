const john = {
	age: 42,
	getAge: function () {
		return this.age;
	},
};

console.log(john.getAge()); // 42

// getAge runs in global context which age is undefined
const getAge = john.getAge;
console.log(getAge()); // undefined

// apply call function with specific this and arguments
// call is similar to apply, but it takes arguments as a list

// Bind returns a new function with a specific this context

Function.prototype.myBind = function (thisArg, ...argArray) {
	// throw 'Not implemented!';
	// bind return the function with binding object values in the context
	// since bind return a new function and it could capture args
	const func = this;
	return function (...args) {
		// when execute the bind function
		// it execute the original with custom this context
		// original args
		// and new args when calling the function
		return func.apply(thisArg, [...argArray, ...args]) // it also needs to return data back from called function so I put return here

	}
};