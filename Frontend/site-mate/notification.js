class Service {
	processNotification() { }
}

class EmailService extends Service {
	processNotification(message) {
		console.log('EmailService processing ', message)
	}
}

class SMSService extends Service {
	processNotification(message) {
		console.log('SMSService processing ', message)
	}
}
class AnalyticsService extends Service {
	processNotification(message) {
		console.log('AnalyticsService processing ', message)
	}
}

class Notification {
	constructor() {
		this.subscribers = {}
	}

	subscribe(key, service) {
		this.subscribers[key] = service
	}

	unsubscribe(key) {
		if (!(key in this.subscribers)) return false

		delete this.subscribers[key]
		return true
	}

	notify(message) {
		for (const key in this.subscribers) {
			const service = this.subscribers[key]
			service.processNotification(message)
		}
	}
}

const email = new EmailService()
const sms = new SMSService()
const analytics = new AnalyticsService()

const notificationSystem = new Notification()
notificationSystem.subscribe('email', email)
notificationSystem.subscribe('sms', sms)
notificationSystem.subscribe('analytics', analytics)



notificationSystem.notify('Hello world')

console.log('Unsubscribe email service')
notificationSystem.unsubscribe('email')

notificationSystem.notify('Hello world again')
