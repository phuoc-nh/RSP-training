class ATM {
	#pin; // private
	constructor(pin) { this.#pin = pin; }

	withdraw(amount, enteredPin) {
		if (enteredPin === this.#pin) {
			console.log(`Withdrew $${amount}`);
		} else {
			console.log("Invalid PIN");
		}
	}
}

const atm = new ATM(1234);
atm.withdraw(100, 1234); // ✅ Withdrew $100
atm.withdraw(50, 1111);  // ❌ Invalid PIN
// console