import java.util.ArrayList;
import java.util.List;

interface Observer {
	void update(String message);
}

class ConcreteObserver implements Observer {
	private String name;

	public ConcreteObserver(String name) {
		this.name = name;
	}

	@Override
	public void update(String message) {
		System.out.println(name + " received message: " + message);
	}
}

class Publisher {
	private List<Observer> observers = new ArrayList<>();

	public void subscribe(Observer observer) {
		observers.add(observer);
	}

	public void unsubscribe(Observer observer) {
		observers.remove(observer);
	}

	public void notify(String message) {
		for (Observer observer : observers) {
			observer.update(message);
		}
	}
}