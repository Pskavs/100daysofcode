import data_manager as dm
dm = dm.DataManager()
class FlightData:
    def __init__(self, data):
        self.flight_data = data

    def find_cheapest_flight(self,sheet_flight):
        for flight in self.flight_data:
            flight_price = float(flight['price']["grandTotal"])
            if flight_price < sheet_flight['lowestPrice']:
                sheet_flight['lowestPrice'] = flight_price
                cheapest_flight = flight
        dm.edit_data(sheet_flight)
        return cheapest_flight