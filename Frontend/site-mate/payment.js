class PaymentMethod {
	pay() { }
}

class PayPal extends PaymentMethod {
	pay() {
		console.log('Pay by paypal')
	}
}

class Stripe extends PaymentMethod {
	pay() {
		console.log('Pay by Stripe')
	}
}

class CreditCard extends PaymentMethod {
	pay() {
		console.log('Pay by CreditCard')
	}
}

class PaymentFactory {


	constructor(method) {
		this.paymentRegistry = {}

		// if (method === 'paypal') {
		// 	return new PayPal()
		// }

		// if (method === 'stripe') {
		// 	return new Stripe()
		// }

		// if (method === 'creditCard') {
		// 	return new CreditCard()
		// }
	}

	register(payment, paymentClass) {
		this.paymentRegistry[payment] = paymentClass
	}

	create(payment) {
		if (!(payment in this.paymentRegistry)) {
			throw Error('Not supported')
		}

		const PaymentClass = this.paymentRegistry[payment]
		return new PaymentClass
	}

}

const paymentFactory = new PaymentFactory()
paymentFactory.register('paypal', PayPal)
paymentFactory.register('stripe', Stripe)
paymentFactory.register('creditCard', CreditCard)

const payByCredit = paymentFactory.create('creditCard')
payByCredit.pay()