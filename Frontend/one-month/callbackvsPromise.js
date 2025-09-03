// function getFirstData(callback) {
// 	setTimeout(() => {
// 		callback({ id: 1, content: 'first' })
// 	}, 1000);
// }

// function getSecondData(data, callback) {
// 	setTimeout(() => {
// 		callback({ id: data.id, content: `${data.content} + seonc` })
// 	}, 1000);
// }

// getFirstData((data) => {
// 	getSecondData(data, (data) => {
// 		console.log(data)
// 	})
// })

function getFirstData() {
	return new Promise((res, rej) => {
		setTimeout(() => {
			res({ id: 1, content: 'first' })
		}, 1000);
	})
}

function getSecondData(data) {
	return new Promise((res, rej) => {
		setTimeout(() => {
			res({ id: data.id, content: `${data.content} + seonc` })
		}, 1000);
	})
}

getFirstData().then(data => {
	getSecondData(data).then(data => {
		console.log(data)
	})
})