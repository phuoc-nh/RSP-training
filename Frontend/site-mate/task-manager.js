const Status = {
	TODO: 'todo',
	IN_PROGRESS: 'in-progress',
	DONE: 'done'
}

const Priority = {
	HIGH: 'high',
	MEDIUM: 'medium',
	LOW: 'low'
}

// task
class Task {
	constructor(id, title, status = Status.TODO, priority) {
		this._id = id
		this._title = title
		this._status = status
		this._priority = priority
	}

	getId() {
		return this._id
	}

	getStatus() {
		return this._status
	}

	getPriority() {
		return this._priority
	}


	updateStatus(status) {
		this._status = status
	}
}

// repository for saving purpose, dependency inversion 
class Repository {
	constructor() {
		this.tasks = []
	}

	addTask(task) {
		this.tasks.push(task)
	}

	getTasks() {
		return this.tasks
	}
}

// task manager
class TaskManager {
	constructor(repository) {
		this.repository = repository
		this.id = 0
	}

	addTask(title, status, priority) {
		const task = new Task(this.id, title, status, priority)
		this.id += 1
		this.repository.addTask(task)
	}

	getTasks(filters = []) {
		if (filters.length === 0) return this.repository.getTasks()

		// apply filters here

		let tasks = this.repository.getTasks()
		filters.forEach(filter => {
			tasks = filter.filter(tasks)
		})

		return tasks
	}


}

class IFilter {
	filter(tasks) {
		throw new Error('Not implemented')
	}
}

// filter strategy follows open/closed principle
class FilterByStatus extends IFilter {

	constructor(statusList) {
		super()
		this.statusList = statusList
	}

	filter(tasks) {
		console.log(this.statusList)
		return tasks.filter(task => this.statusList.includes(task.getStatus()))
	}
}

class FilterByPriority extends IFilter {
	constructor(priority) {
		super()
		this.priority = priority
	}

	filter(tasks) {
		return tasks.filter(task => task.getPriority() === this.priority)
	}
}

// Create repository and task manager
const repo = new Repository();
const manager = new TaskManager(repo);

// Sample data
const titles = [
	"Design UI", "Fix bug", "Write tests", "Refactor API", "Deploy app",
	"Update docs", "Review PR", "Setup CI", "Optimize DB", "Plan sprint"
];
const statuses = [Status.TODO, Status.IN_PROGRESS, Status.DONE];
const priorities = [Priority.HIGH, Priority.MEDIUM, Priority.LOW];

// Add 10 sample tasks
for (let i = 0; i < 10; i++) {
	const title = titles[i];
	const status = statuses[i % statuses.length];
	const priority = priorities[i % priorities.length];
	manager.addTask(title, status, priority);
}

const filterByStatus = new FilterByStatus([Status.DONE, Status.TODO])
const filterByPriority = new FilterByPriority(Priority.HIGH)

const filters = [filterByStatus]

console.log(manager.getTasks(filters));