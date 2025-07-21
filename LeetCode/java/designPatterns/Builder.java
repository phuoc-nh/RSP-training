class Burger {
	private String bread;
	private String meat;
	private Boolean cheese;

	public Burger(String bread, String meat, Boolean cheese) {
		this.bread = bread;
		this.meat = meat;
		this.cheese = cheese;
	}
	
	public String getBread() {
		return bread;
	}

	public String getMeat() {
		return meat;
	}

	public Boolean hasCheese() {
		return cheese;
	}
	
	public void setBread(String bread) {
		this.bread = bread;
	}

	public void setMeat(String meat) {
		this.meat = meat;
	}
	public void setCheese(Boolean cheese) {
		this.cheese = cheese;
	}
}

class BurgerBuilder {
	private String bread;
	private String meat;
	private Boolean cheese;

	public BurgerBuilder setBread(String bread) {
		this.bread = bread;
		return this;
	}
	
	public BurgerBuilder setMeat(String meat) {
		this.meat = meat;
		return this;
	}

	public BurgerBuilder setCheese(Boolean cheese) {
		this.cheese = cheese;
		return this;
	}
	
	public Burger build() {
		return new Burger(bread, meat, cheese);
	}
}