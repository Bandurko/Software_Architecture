from bus_stop import BusStop


class BusRoute:
    def __init__(self, id: int, remark: str, capacity: int, bus_stops: list[BusStop]):
        self.id = id
        self.remark = remark
        self.capacity = capacity
        self.bus_stops = bus_stops