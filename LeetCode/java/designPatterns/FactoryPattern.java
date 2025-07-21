interface Vehicle {
	String getType();
}

class Car implements Vehicle {
	@Override
	public String getType() {
		return "Car";
	}
}

class Truck implements Vehicle {
	@Override
	public String getType() {
		return "Truck";
	}
}

interface VehicleFactory {
	Vehicle createVehicle();
}

class CarFactory implements VehicleFactory {
	@Override
	public Vehicle createVehicle() {
		return new Car();
	}
}

class TruckFactory implements VehicleFactory {
	@Override
	public Vehicle createVehicle() {
		return new Truck();
	}
}
