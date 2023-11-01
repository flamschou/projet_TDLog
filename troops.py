class troops():
    """troops class"""
    def __init__(self, index):
        self._name = None
        self._description = None
        self._speed = None
        self._health = None
        self._damage = None
        self._index = index
        self._color = None
        self._range = None
        self._side = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def speed(self):
        return self._speed

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    @property
    def index(self):
        return self._index

    @property
    def color(self):
        return self._color

    @property
    def range(self):
        return self._range

    @property
    def side(self):
        return self._side


class assassin(troops):
    """assassin class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "assassin"
        self._description = "Fast and light"
        self._speed = 3
        self._health = 4
        self._damage = 3
        self._color = "red"
        self._range = 1
        self._side = "offense"


class magician(troops):
    """magician class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "magician"
        self._description = "Average speed and health, but secret powers"
        self._speed = 1
        self._health = 6
        self._damage = 2
        self._color = "red"
        self._range = 2
        self._side = "offense"


class turret(troops):
    """turret class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "turret"
        self._description = "Slow but powerful"
        self._speed = 1
        self._health = 8
        self._damage = 6
        self._color = "red"
        self._range = 3
        self._side = "offense"


class archer(troops):
    """archer class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "archer"
        self._description = "Light and long range"
        self._speed = 2
        self._health = 3
        self._damage = 3
        self._color = "blue"
        self._range = 3
        self._side = "defense"


class engineer(troops):
    """engineer class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "engineer"
        self._description = "Average speed and health, but secret powers"
        self._speed = 1
        self._health = 6
        self._damage = 2
        self._color = "blue"
        self._range = 2
        self._side = "defense"


class shield(troops):
    """shield class"""
    def __init__(self, index):
        super().__init__(index)
        self._name = "shield"
        self._description = "Slow but powerful"
        self._speed = 1
        self._health = 12
        self._damage = 3
        self._color = "blue"
        self._range = 1
        self._side = "defense"
