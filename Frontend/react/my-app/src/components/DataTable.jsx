import { useEffect, useState } from "react";
import { fetchUsers, getLength } from "./data/users.js";



export default function DataTable() {
	const [message, setMessage] = useState("Data Table");
	const [page, setPage] = useState(0)
	const [perPage, setPerPage] = useState(5)
	const [data, setData] = useState([])
	const [maxPage, setMaxPage] = useState(Math.ceil(getLength() / perPage))
	// console.log('data,', data)


	// console.log('max page', Math.ceil(getLength() / perPage))

	const handlePrev = () => {
		if (page === 0) return
		setPage(page - 1)
	}

	const handleNext = () => {
		if (page === maxPage - 1) return
		setPage(page + 1)
	}

	useEffect(() => {
		// console.log(page, perPage)
		const newData = fetchUsers(page, perPage)
		setMaxPage(Math.ceil(getLength() / perPage))
		setData(newData)
	}, [page, perPage])

	return (
		<div>
			<h1>{message}</h1>
			<table>
				<thead>
					<tr>
						{[
							{ label: "ID", key: "id" },
							{ label: "Name", key: "name" },
							{ label: "Age", key: "age" },
							{ label: "Occupation", key: "occupation" },
						].map(({ label, key }) => (
							<th key={key}>{label}</th>
						))}
					</tr>
				</thead>
				<tbody>
					{data.map(({ id, name, age, occupation }) => (
						<tr key={id}>
							<td>{id}</td>
							<td>{name}</td>
							<td>{age}</td>
							<td>{occupation}</td>
						</tr>
					))}
				</tbody>
			</table>
			<button onClick={handlePrev}>Prev</button>	<button onClick={handleNext}>Next</button>
			<div>Page {page + 1} of {maxPage}</div>
			<select onChange={(e) => {
				setPerPage(Number(e.target.value))
			}}>
				<option value="5">Show 5</option>
				<option value="10">Show 10</option>
				<option value="20">Show 20</option>
			</select>
		</div>
	);
}
