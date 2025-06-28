// Array.prototype.myFilter = function (callbackFn, thisArg) {
// 	console.log(thisArg)
// 	throw 'Not implemented!';
// };
Array.prototype.myFilter = function (callbackFn, thisArg) {
	const len = this.length;
	const results = [];

	console.log(this);

	for (let k = 0; k < len; k++) {
		const kValue = this[k];
		if (
			// Ignore index if value is not defined for index (e.g. in sparse arrays).
			// Determines whether an object has a property with the specified name.
			// useful for arrays with holes like [1, , 3]
			Object.hasOwn(this, k) &&
			callbackFn.call(thisArg, kValue, k, this)
		) {
			results.push(kValue);
		}
	}

	return results;
};

// ar = [1, 2, 3]
// console.log(ar.myFilter((item) => item > 1, {})); // [2, 3]

const arr = [10, 20, 30];

function isBigEnough(value, index, array) {
	console.log(this); // ← this will be { min: 15 }
	return value >= this.min;
}

// const result = arr.myFilter(isBigEnough, { min: 15 });
arr.filter((a, i, arr) => {
	console.log(a, i, arr);
	return a > 15;
})

// const o = { a: 2, b: 3 };
// console.log(Object.hasOwn(o, 'a')); // true
// console.log(Object.hasOwn(o, 'c')); // false