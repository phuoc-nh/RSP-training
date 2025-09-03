
class PercentageDiscount {

	constructor(discountVal) {
		this.discountVal = discountVal
	}

	discount(value) { // 10%
		return value - value * this.discountVal
	}

}

class FlatRateDiscount {

	constructor(discountVal) {
		this.discountVal = discountVal
	}

	discount(value) {
		return value - this.discountVal
	}

}

class DiscountContext {
	constructor() {
		this.discounts = []
	}

	add(discount) {
		this.discounts.push(discount)
	}

	discount(price) {
		for (const discount of this.discounts) {
			price = discount.discount(price)
		}

		return price
	}
}

const discountContext = new DiscountContext()


const tenPercentDiscount1 = new PercentageDiscount(0.1)
const fivePercentDiscount = new PercentageDiscount(0.05)
const twentyDollarsDiscount = new FlatRateDiscount(20)

discountContext.add(tenPercentDiscount1)
discountContext.add(twentyDollarsDiscount)

let price = 100


price = discountContext.discount(price)
console.log(price)