function classNames(...args) {
	console.log('====', args)
	// args.forEach(a => {
	//   console.log('>>>>', a)
	// })
	let res = []
	function dfs(cur) {
		if (typeof cur === 'string' || typeof cur === 'number') {
			if (cur) {
				res.push(cur)
			}
			return
		}

		if (Array.isArray(cur)) {
			for (let i = 0; i < cur.length; i++) {
				dfs(cur[i])
			}
		}

		else if (typeof cur === 'object') {
			for (const key in cur) {
				console.log('jey', key)
				if (cur[key]) {
					dfs(key)
				}
			}
		}
	}

	dfs(args)

	console.log('res >>', res.join(' '))

	return res.join(' ')
}

// classNames('foo', 'bar'); // 'foo bar'
// classNames('foo', { bar: true }); // 'foo bar'
// classNames({ 'foo-bar': true }); // 'foo-bar'
// classNames({ 'foo-bar': false }); // ''
// classNames({ foo: true }, { bar: true }); // 'foo bar'
// classNames({ foo: true, bar: true }); // 'foo bar'
// classNames({ foo: true, bar: false, qux: true }); // 'foo qux'
// classNames(null, false, 'bar', undefined, 0, 1, { baz: null }, '')
// classNames('boo', true && 'loo', false && 'booz', {
// 	foo: true,
// 	bar: false,
// 	baz: 1,
// })
// classNames(null, false, 'bar', undefined, 0, 1, { baz: null }, '')
classNames(null, false, 'bar', undefined, 0, 1, { baz: null }, '')
// expect(
//       classNames(null, false, 'bar', undefined, 0, 1, { baz: null }, ''),
//     ).toEqual('bar 1');