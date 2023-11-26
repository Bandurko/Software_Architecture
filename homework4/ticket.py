from datetime import date


class Ticket:
    def __init__(self, price: int, departure_date: date, start_zone: int, finish_zone: int, is_luggage: bool,
                 place: int, road_number: int):
        self.price = price
        self.departure_date = departure_date
        self.start_zone = start_zone
        self.finish_zone = finish_zone
        self.is_luggage = is_luggage
        self.place = place
        self.road_number = road_number