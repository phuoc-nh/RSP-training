const root = 'https://hacker-news.firebaseio.com/v0'

const PER_PAGE = 6
let curPage = 0
let jobs = null
// let reachEnd = false

const initialLoading = document.getElementById('initial-load')
const moreButton = document.getElementById('more')

async function fetchJobsIds() {

	if (!jobs) {

		const res = await fetch(root + '/jobstories.json')
		const data = await res.json()



		jobs = data

	}



	const start = curPage * PER_PAGE
	const end = start + PER_PAGE

	// if (end >= jobs.length) {
	// 	console.log('reach end')
	// 	reachEnd = true
	// }


	return jobs.slice(start, end)

	// call everything at once rather than sequent call
	// let jobDetails = await Promise.all(
	// 	data.map(jobid =>
	// 		fetch(URL + `/item/${jobid}.json`).then(res => res.json())
	// 	)
	// )
	// console.log(jobDetails)
}

async function fetJobsDetail() {


	// set loading here button 

	moreButton.innerText = 'Loading'
	moreButton.disabled = true

	const data = await fetchJobsIds()
	// call everything at once rather than sequent call
	let jobDetails = await Promise.all(
		data.map(jobid =>
			fetch(root + `/item/${jobid}.json`).then(res => res.json())
		)
	)
	console.log(jobDetails)
	curPage += 1

	renderJobs(jobDetails)
	console.log('initial-load', initialLoading)

	initialLoading.hidden = true
	moreButton.hidden = false
	moreButton.innerText = 'More'
	moreButton.disabled = false
}


function renderJobs(jobs) {
	const container = document.getElementById('container')

	jobs.forEach(job => {

		const div = document.createElement('div')
		// div.className
		const title = document.createElement('div')
		title.innerText = job.title
		const by = document.createElement('div')
		by.innerText = `Posted by: ${job.by}`

		div.appendChild(title)
		div.appendChild(by)

		container.appendChild(div)

	})

}

fetJobsDetail()