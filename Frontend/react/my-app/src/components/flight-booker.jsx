import React, { useEffect, useState } from 'react'
// 2025-07-24 correct format to display in input date

const TODAY = new Date()
const DAY_IN_MILLISECONDS = 24 * 60 * 60 * 1000
function format(date) {
	// const date = new Date()
	const year = date.getFullYear().toString()
	const month = (date.getMonth() + 1).toString().padStart(2, '0')
	const day = date.getDate().toString().padStart(2, '0')
	console.log(year, month, day)

	return `${year}-${month}-${day}`
}



export default function Booker() {
	const [type, setType] = useState('one-way')
	const [departureDate, setDepartureDate] = useState(format(new Date(Date.now() + DAY_IN_MILLISECONDS))) // Tomorrow
	const [returnDate, setReturnDate] = useState(departureDate)
	
	console.log('format', format(new Date))

	// useEffect(() => {
	// 	console.log('departureDate', departureDate)
	// }, [departureDate])

	const submit = (e) => {	
		e.preventDefault()
		alert('Success')

	}

	return (
		<form onSubmit={submit} className='flight-booker'>
			<select name="start-date" defaultValue={type} onChange={(event) => setType(event.target.value)}>
				<option value="one-way">one-way flight</option>
				<option value="round-trip">round trip</option>
			</select>
			<input
				type="date"
				value={departureDate}
				onChange={event => setDepartureDate(event.target.value)}
				min={TODAY}
			/> 

			{type === 'round-trip' &&
				<input
					type="date"
					value={returnDate}
					onChange={event => setReturnDate(event.target.value)}
					min={departureDate}
				/>}

			<input type="submit" value="Book" />
		</form>
	)
}
