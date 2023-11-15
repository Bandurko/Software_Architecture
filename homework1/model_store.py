from service import Point3D, Angle3D, Color

class Camera:
    def __init__(self) -> None:
        self.location: Point3D = Point3D()
        self.angle: Angle3D = Angle3D()

    def rotate(self, angle: Angle3D) -> None:
        pass

    def move(self, point: Point3D) -> None:
        pass

class Flash:
    def __init__(self) -> None:
        self.location: Point3D = Point3D()
        self.angle: Angle3D = Angle3D()
        self.color: Color = Color()
        self.power: float = 0.0

    def rotate(self, angle: Angle3D) -> None:
        pass

    def move(self, point: Point3D) -> None:
        pass

class Texture:
    pass

class Poligon:
    def __init__(self) -> None:
        self.points: list[Point3D] = [Point3D()]

class PoligonalModel:
    def __init__(self, texture: list[Texture]) -> None:
        self.poligons: list[Poligon] = [Poligon()]
        self.texture: list[Texture] = texture

class Scene:
        def __init__(self, id: int, models: PoligonalModel, flashes: Flash) -> None:
            self.id = id
            self.models = models
            self.flashes = flashes

        def metod1(self, type1):
            return type(type1)

        def metod2(self, type2):
            return type(type2)