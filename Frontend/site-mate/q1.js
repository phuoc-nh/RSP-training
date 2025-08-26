// // type Task = {
// //   id: number;
// //   title: string;
// //   status: "todo" | "in-progress" | "done";
// // };

// function groupTasksByStatus(tasks) {
// 	// implement
// 	const statusMap = {}

// 	for (let i = 0; i < tasks.length; i++) {
// 		const task = tasks[i];
// 		if (!(task.status in statusMap)) {
// 			statusMap[task.status] = []
// 		}

// 		statusMap[task.status].push(task)

// 	}

// 	console.log(statusMap)
// }


// let tasks = [
// 	{ id: 1, title: "Design UI", status: "todo" },
// 	{ id: 2, title: "Fix bug", status: "in-progress" },
// 	{ id: 3, title: "Write tests", status: "done" },
// 	{ id: 4, title: "Refactor API", status: "in-progress" }
// ]

// groupTasksByStatus(tasks)

// async function fetchWithRetry(url, retries = 3) {
// 	// implement
// 	let count = 0
// 	for (let i = 1; i < 3; i++) {
// 		try {
// 			const res = await fetch(url)
// 			return res
// 		} catch (error) {
// 			if (count == retries) {
// 				throw error
// 			}

// 		}
// 	}
// }

