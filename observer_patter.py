# Pattern: Observer Pattern

# Description:
# The Observer pattern establishes a one-to-many relationship between objects, where changes in one object (called the subject or observable) are automatically notified to and updated in the dependent objects (called observers). This pattern enables loose coupling between the subject and observers, allowing for easy addition and removal of observers without affecting the subject's code.

# Real-time Situations:
# The Observer pattern is useful in scenarios where you need to maintain consistency between multiple objects based on changes in a particular object. Some real-time situations where the Observer pattern can be applied include:

# Event-driven systems: GUI frameworks often use the Observer pattern to handle user interactions and update the UI components accordingly. When an event occurs (e.g., a button click), the subject (e.g., the button) notifies all its observers (e.g., event handlers) to perform specific actions.
# Stock market updates: In a financial application, when the price of a stock changes, various components, such as charts, statistics panels, and notifications, need to be updated. The stock object acts as the subject, and the different components act as observers that receive the update when the stock price changes.
# Messaging systems: In a messaging application, when a new message is received, it needs to be displayed in multiple chat windows or notification panels. The message sender acts as the subject, and the chat windows or notification panels act as observers that are updated with the new message.
# Example Implementation:

# Let's consider an example of a weather monitoring system. In this system, there is a WeatherData subject that represents the current weather conditions. We'll have two observers: CurrentConditionsDisplay and StatisticsDisplay. These observers will be notified whenever the weather data changes and update their respective displays accordingly.

# Here's an implementation of the Observer pattern in Python:


class WeatherData:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay:
    def update(self, temperature, humidity, pressure):
        # Update current conditions display based on the new measurements
        print(f"Current conditions: {temperature}F degrees, {humidity}% humidity")


class StatisticsDisplay:
    def update(self, temperature, humidity, pressure):
        # Update statistics display based on the new measurements
        print("Updating statistics display...")


# Usage example
weather_data = WeatherData()
current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()

weather_data.register_observer(current_display)
weather_data.register_observer(statistics_display)

# Simulate weather data changes
weather_data.set_measurements(75, 60, 30.4)
