class Logger {
	private static Logger instance;

	private Logger() {
		// private constructor to prevent instantiation
	}

	public static Logger getInstance() {
		if (instance == null) {
			instance = new Logger();
		}
		return instance;
	}
}