class ConfigManager {
	// receive config path
	// initilaise it
	// static instance
	static #instance;
	#config

	constructor(configObject) {
		if (ConfigManager.#instance) {
			return ConfigManager.#instance
		}

		this.#config = configObject
		ConfigManager.#instance = this
	}

	static getInstance(configObject) {
		if (!ConfigManager.#instance) {
			ConfigManager.#instance = new ConfigManager(configObject)
		}

		return ConfigManager.#instance
	}

	get(key) {
		return this.#config[key]
	}

}