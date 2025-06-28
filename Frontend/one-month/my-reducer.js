Array.prototype.myReduce = function (callbackFn, initialValue) {
	const noInit = initialValue === undefined

	const values = this
	let res = noInit ? values[0] : initialValue
	let start = noInit ? 1 : 0

	for (let i = start; i < values.length; i++) {
		res = callbackFn(res, values[i])
	}
	return res
};

[1, 2, 3].myReduce(multiplyByIndex, 0)