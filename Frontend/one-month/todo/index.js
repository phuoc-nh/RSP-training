
function addTask() {
	const taskInput = document.getElementById('task')
	const task = taskInput.value

	console.log('task', task)
	const taskChild = document.createElement('span')
	taskChild.innerText = task

	const newEl = document.createElement('li')
	newEl.appendChild(taskChild)

	const deleteBtn = document.createElement('button')
	deleteBtn.innerText = 'Delete'
	deleteBtn.addEventListener('click', function () {
		console.log('delete')
		const todoContainer = document.getElementById('todo-container')
		todoContainer.removeChild(newEl)
	})
	newEl.appendChild(deleteBtn)

	const todoContainer = document.getElementById('todo-container')
	todoContainer.appendChild(newEl)

	taskInput.value = ''
}