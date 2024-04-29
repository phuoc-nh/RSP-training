
// timestamps = [1, 1, 1, 11]
// messages = ['message-2', 'message-2', 'message-3', 'message-2']
// k = 5

// let messageTime = {
// 	// task: last time process
// }
// let ret = []

// for (let i = 0; i < messages.length; i++) {
// 	let message = messages[i]
// 	let time = timestamps[i]

// 	if (message in messageTime) {
// 		let lastTime = messageTime[message]
// 		if (lastTime + k < time) {
// 			ret.push('true')
// 			messageTime[message] = time
// 		} else {
// 			ret.push('false')
// 		}
// 	} else {
// 		ret.push('true')
// 		messageTime[message] = time
// 	}
// }


// console.log(ret)

// ===========================

// const n = 5
// const task_memory = [4,2,3,4,1]
// const task_type = [1,1,1,1,1]
// const max_memory = 4

// const memoryType = []
// for (let i = 0; i < task_memory.length; i++) {
// 	const memory = task_memory[i];
// 	const type = task_type[i]

// 	memoryType.push([type, memory])
// }
// memoryType.sort((a, b) => {
//     if (b[0] === a[0]) {
//         return b[1] - a[1];
//     } else {
//         return b[0] - a[0];  
//     }
// });
// let time = 0

// while (memoryType.length > 0) {
// 	console.log(memoryType)
// 	let curMemoryType = memoryType.pop()
// 	let type = curMemoryType[0]
// 	let memory = curMemoryType[1]

// 	if (memoryType.length > 0) {
// 		let nextMemoryType = memoryType[memoryType.length - 1]
// 		let nextType = nextMemoryType[0]
// 		let nextMemory = nextMemoryType[1]

// 		if (type == nextType && memory + nextMemory <= max_memory) {
// 			memoryType.pop()
// 		}
// 	}
// 	time += 1
// }

// console.log(time)

// ===============================

products = [  [ '100', 'dcoupon1' ],
[ '50', 'dcoupon1' ],
[ '30', 'dcoupon1' ],
[ '100', 'dcoupon2' ],
[ '50', 'dcoupon2' ],
[ '30', 'dcoupon2' ]]

discounts = [  [ 'dcoupon1', '0', '60' ],
[ 'dcoupon1', '1', '30' ],
[ 'dcoupon1', '1', '20' ],
[ 'dcoupon2', '2', '20' ],
[ 'dcoupon2', '1', '85' ],
[ 'dcoupon2', '0', '15' ]]
// d0 fix price
// d1 %
// d2 deduct price 

discountMap = {}

for (let i = 0; i < discounts.length; i++) {
	const d = discounts[i];
	if (d[0] in discountMap) {
		discountMap[d[0]].push([d[1], d[2]])
	} else {
		discountMap[d[0]] = [[d[1], d[2]]]
	}

}

console.log(discountMap)
let total = 0
for (let i = 0; i < products.length; i++) {
	const product = products[i];

	// if (product.length >= 2) {
	let minPrice = parseInt(product[0])
	let price = product[0]
	for (let j = 1; j < product.length; j++) {
		if (product[j] in discountMap) {
			let discount = discountMap[product[j]]

			for (let l = 0; l < discount.length; l++) {
				const element = discount[l];

			if (element[0] == '0') {
				minPrice = Math.min(minPrice, parseInt(element[1]))
			} else if (element[0] == '1') {
				minPrice = Math.min(minPrice, Math.floor(price - price * parseInt(element[1]) / 100))
			} else if (element[0] == '2') {
				minPrice = Math.min(minPrice, price - element[1])
			}
		}

		}
	}
	// console.log(product)
	// console.log(minPrice)
	// console.log('===========')
	total += minPrice
}

console.log(total)