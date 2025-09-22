function displayLight(id, className, duration) {
	return new Promise(resolve => {
		const light = document.getElementById(id);
		light.classList.add(className);
		setTimeout(() => {
			light.classList.remove(className);
			resolve();
		}, duration);
	});
}

async function display() {
	await displayLight('red', 'red-light', 4000);
	await displayLight('yellow', 'yellow-light', 1000);
	await displayLight('green', 'green-light', 3000);
	display();
}

display();