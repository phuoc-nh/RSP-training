// class Flight {
// 	constructor(flightId, from, to, takeOffTime, seatBookings) {
// 		this.flightId = flightId
// 		this.from = from
// 		this.to = to
// 		this.takeOffTime = takeOffTime
// 		// this.seatBookings = seatBookings // list of seats
// 		// this.bookedSeats = new Set()
// 	}

// 	// book(seatId) {
// 	// 	if (seatId in this.bookedSeats) {
// 	// 		throw new Error('The seat is not available')
// 	// 	}

// 	// 	this.bookedSeats.add(seatId)

// 	// 	return true
// 	// }

// 	// cancel(seatId) {
// 	// 	this.bookedSeats.delete(seatId)
// 	// }

// }

// const BookingStatus = {
// 	AVAILABLE: 'available',
// 	RESERVED: 'reserved',
// }

// class SeatBooking {
// 	constructor(seatId, flightId) {
// 		this.seatId = seatId
// 		this.customerId = undefined
// 		this.flightId = flightId
// 		this.status = BookingStatus.AVAILABLE
// 	}

// 	book(customerId) {
// 		this.customerId = customerId
// 		this.status = BookingStatus.RESERVED
// 	}

// 	cancel() {
// 		this.customerId = undefined
// 		this.status = BookingStatus.AVAILABLE
// 	}

// }



// class Customer {
// 	constructor(customerId, email, passport) {
// 		this.customerId = customerId
// 		this.email = email
// 		this.passport = passport
// 	}
// }

// class Manager {
// 	constructor() {
// 		this.flights = []
// 		this.seats = []
// 	}

// 	seed() {
// 		const sampleFlights = [
// 			{ flightId: 'F1', from: 'SGN', to: 'HAN' },
// 			{ flightId: 'F2', from: 'HCM', to: 'DAD' },
// 			{ flightId: 'F3', from: 'SGN', to: 'KUL' },
// 		]

// 		for (const f of sampleFlights) {
// 			const takeOff = new Date().toISOString()
// 			const flight = new Flight(f.flightId, f.from, f.to, takeOff, [])

// 			// create 10 seats per flight
// 			for (let i = 1; i <= 10; i++) {
// 				const seatId = `S${i}` // simple seat ids S1..S10
// 				const seat = new SeatBooking(seatId, flight.flightId)

// 				this.seats.push(seat)
// 			}

// 			this.flights.push(flight)
// 		}
// 		return this.flights

// 	}

// 	book(seatId, customerId) {
// 		const seat = this.seats.find(s => s.seatId === seatId)
// 		if (!seat) {
// 			throw Error('Invalid seat')
// 		}
// 		console.log('seat', seat)
// 		seat.book(customerId)
// 	}

// 	listFlights() {
// 		return this.flights
// 	}

// 	listSeats(flightId) {
// 		return this.seats.filter(s => s.flightId === flightId)
// 	}

// }


// const manager = new Manager()
// manager.seed()


// // console.log(manager.listSeats('F1'))

// const customer = new Customer(1, 'abc', 'zxc')

// manager.book('S1', customer.customerId)

// console.log(manager.listSeats('F1'))

class Flight {
	constructor(flightId, from, to, takeOffTime, capacity = 10) {
		this.flightId = flightId;
		this.from = from;
		this.to = to;
		this.takeOffTime = takeOffTime;
		this.seats = [];

		// Initialize seats for this flight
		for (let i = 1; i <= capacity; i++) {
			const seatId = `${flightId}-S${i}`; // unique per flight
			this.seats.push(new Seat(seatId, flightId));
		}
	}

	listSeats() {
		return this.seats;
	}

	findSeat(seatId) {
		return this.seats.find(s => s.seatId === seatId);
	}

	availableSeats() {
		return this.seats.filter(s => s.isAvailable());
	}
}

const SeatStatus = {
	AVAILABLE: "available",
	RESERVED: "reserved",
};

class Seat {
	constructor(seatId, flightId) {
		this.seatId = seatId;
		this.flightId = flightId;
		this.status = SeatStatus.AVAILABLE;
	}

	reserve() {
		if (this.status !== SeatStatus.AVAILABLE) {
			throw new Error("Seat is not available");
		}
		this.status = SeatStatus.RESERVED;
	}

	release() {
		this.status = SeatStatus.AVAILABLE;
	}

	isAvailable() {
		return this.status === SeatStatus.AVAILABLE;
	}
}


const BookingStatus = {
	CONFIRMED: "confirmed",
	CANCELLED: "cancelled",
};

class Booking {
	constructor(bookingId, customer, flightId, seatId) {
		this.bookingId = bookingId;
		this.customer = customer; // reference to Customer object
		this.flightId = flightId;
		this.seatId = seatId;
		this.status = BookingStatus.CONFIRMED;
	}

	cancel() {
		this.status = BookingStatus.CANCELLED;
	}
}


class Manager {
	constructor() {
		this.flights = [];
		this.seats = [];
		this.bookings = []; // NEW
		this.nextBookingId = 1;
	}

	seed() {
		const sampleFlights = [
			{ flightId: "F1", from: "SGN", to: "HAN" },
			{ flightId: "F2", from: "HCM", to: "DAD" },
			{ flightId: "F3", from: "SGN", to: "KUL" },
		];

		for (const f of sampleFlights) {
			const takeOff = new Date().toISOString();
			const flight = new Flight(f.flightId, f.from, f.to, takeOff);

			// create 10 seats per flight
			for (let i = 1; i <= 10; i++) {
				const seatId = `${f.flightId}-S${i}`; // unique seat ids per flight
				const seat = new SeatBooking(seatId, flight.flightId);
				this.seats.push(seat);
			}

			this.flights.push(flight);
		}
		return this.flights;
	}

	book(flightId, seatId, customer) {
		const seat = this.seats.find(s => s.seatId === seatId && s.flightId === flightId);
		if (!seat) throw Error("Invalid seat");
		if (seat.status !== "available") throw Error("Seat already taken");

		seat.book(customer.customerId);

		const booking = new Booking(
			this.nextBookingId++,
			customer,
			flightId,
			seatId
		);
		this.bookings.push(booking);

		return booking;
	}

	cancelBooking(bookingId) {
		const booking = this.bookings.find(b => b.bookingId === bookingId);
		if (!booking) throw Error("Booking not found");

		booking.cancel();

		const seat = this.seats.find(
			s => s.seatId === booking.seatId && s.flightId === booking.flightId
		);
		if (seat) seat.cancel();

		return booking;
	}

	listBookings() {
		return this.bookings;
	}
}


const manager = new Manager();
manager.seed();

const customer = new Customer(1, "alice@example.com", "P12345");

// Book a seat
const booking1 = manager.book("F1", "F1-S1", customer);
console.log("Booking created:", booking1);

// Cancel booking
manager.cancelBooking(booking1.bookingId);
console.log("After cancellation:", manager.listBookings());

