# definition of the class card and is heritance

class card():
    """event card class"""
    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class fire(card):
    """fire card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "fire"
        self._description = "Some forests are burned down randomly"


class rain(card):
    """rain card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "rain"
        self._description = "Some swamps are flooded randomly"


class rescue(card):
    """rescue card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "rescue"
        self._description = "Game time shortens"


class betrayal(card):
    """betrayal card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "betrayal"
        self._description = "Game time expands"


class adrenalin(card):
    """adrenalin card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "adrenalin"
        self._description = "Players speed and damage multiplied by 2"


class expansion(card):
    """expansion card class"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self._name = "expansion"
        self._description = "Some inacessible hexagons become accessible"
