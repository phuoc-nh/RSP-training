public interface PaymentStrategy {
	void pay(int amount);
}

class CreditCardPayment implements PaymentStrategy {
	@Override
	public void pay(int amount) {
		System.out.println("Paid " + amount + " using Credit Card.");
	}
}

class PayPalPayment implements PaymentStrategy {
	@Override
	public void pay(int amount) {
		System.out.println("Paid " + amount + " using PayPal.");
	}
}

class ShoppingCart {
	private PaymentStrategy paymentStrategy;

	public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
		this.paymentStrategy = paymentStrategy;
	}

	public void checkout(int amount) {
		if (paymentStrategy == null) {
			System.out.println("No payment method selected.");
			return;
		}
		paymentStrategy.pay(amount);
	}

	
}
