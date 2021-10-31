
class AnyTemp:

    temperature = 0
    humidity = 0
    pressure = 0

    # instance attribute
    def __init__(self, i2c, model):
        self.model = model
        if model == "bme280":
            import BME280
            self.temp_obj = BME280.BME280(i2c=i2c)
        elif model == "aht10":
            import ahtx0
            self.temp_obj = ahtx0.AHT10(i2c)
        
    def read(self):
        if self.model == "bme280":
            self.temperature = (self.temp_obj.read_temperature()/100) * (9/5) + 32
            self.humidity = self.temp_obj.read_humidity()/1000
            self.pressure = self.temp_obj.pressure
        elif self.model == "aht10":
            self.temperature = self.temp_obj.temperature * (9/5) + 32
            self.humidity = self.temp_obj.relative_humidity

