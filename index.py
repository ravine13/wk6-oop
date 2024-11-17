# Smartphone and Smartwatch example
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.battery_life = battery_life

    def charge(self, amount):
        self.battery_life += amount
        print(f"{self.device_info()} charged to {self.battery_life}%")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()}.")

class Smartwatch(Device):
    def __init__(self, brand, model, step_count=0):
        super().__init__(brand, model)
        self.step_count = step_count

    def track_steps(self, steps):
        self.step_count += steps
        print(f"{self.device_info()} tracked {self.step_count} steps today.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()} - optimized for smartwatch display.")

# Polymorphism
class Vehicle:
    def move(self):
        pass  # Placeholder method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Create instances and test Smartphone, Smartwatch
phone = Smartphone("Apple", "iPhone 14", 50)
phone.charge(30)
phone.install_app("Spotify")

watch = Smartwatch("Samsung", "Galaxy Watch 5")
watch.track_steps(500)
watch.install_app("Fitness App")

# Create instances and test Polymorphism with vehicles
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
