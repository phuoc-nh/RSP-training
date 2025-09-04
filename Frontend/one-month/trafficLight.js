// // Red light: 4000ms
// // Yellow light: 500ms
// // Green light: 3000ms
// // display red text 

// async function red(time = 4000) {
// 	// display red in 4000ms and remove it after 
// 	// console.log('red')
// 	// await setTimeout(() => {
// 	// }, time);
// 	return new Promise((res, rej) => {
// 		console.log('red')
// 		setTimeout(() => {
// 			res()
// 		}, time);
// 	})
// }

// async function yellow(time = 500) {
// 	// display red in 4000ms and remove it after 
// 	return new Promise((res, rej) => {
// 		console.log('yellow')
// 		setTimeout(() => {
// 			res()
// 		}, time);
// 	})
// }

// async function green(time = 3000) {
// 	return new Promise((res, rej) => {
// 		console.log('green')
// 		setTimeout(() => {
// 			res()
// 		}, time);
// 	})
// }

// async function trafficLift() {
// 	await red()
// 	await yellow()
// 	await green()
// 	await trafficLift
// }

// trafficLift()
// function colorText(text, color) {
// 	const colors = {
// 		red: '\x1b[31m',
// 		yellow: '\x1b[33m',
// 		green: '\x1b[32m',
// 		reset: '\x1b[0m'
// 	};
// 	return colors[color] + text + colors.reset;
// }
// async function showLight(name, color, seconds) {
// 	for (let i = seconds; i > 0; i--) {
// 		console.log(colorText(`${name.toUpperCase()} (${i}s)`, color));
// 		await new Promise(res => setTimeout(res, 1000));
// 	}
// }

// async function trafficLight() {
// 	while (true) {
// 		await showLight('red', 'red', 4);
// 		await showLight('yellow', 'yellow', 1);
// 		await showLight('green', 'green', 3);
// 	}
// }

// trafficLight();

async function trafficLight(color, time) {
	for (let i = time; i >= 0; i--) {
		console.log(color, i)
		await new Promise((res, rej) => setTimeout(() => { }, 1000))
	}
}

async function trafficLight(color, time) {
	for (let i = time; i >= 0; i--) {
		console.log(color, i)
		// need to resolve the promise by attaching it to settime out function callback
		// otherwise, the promise will never fulfill and stuck at the first promise
		await new Promise((res, rej) => setTimeout(res, 1000))
	}
}
async function run() {

	while (true) {

		await trafficLight('red', 5)
		await trafficLight('yellow', 1)
		await trafficLight('green', 5)
	}

}

run()