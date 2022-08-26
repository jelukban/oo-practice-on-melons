############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing = pairing

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    crenshaw = MelonType(code="cren",first_harvest=1996, color="green", \
        is_seedless=True, is_bestseller=False, name="Crenshaw")
    crenshaw.add_paring("mint")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(code="yw", code=2013, color="yellow", \
        is_seedless=False, is_bestseller=True, name="Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    musk = MelonType(code="musk", first_harvest=1998, color="green", \
        is_seedless=True, is_bestseller=True, name="musk")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType(code="cas", first_harvest=2003, color="orange", \
        is_seedless=False, is_bestseller=False, name="casaba")
    casaba.add_pairing("strawberries and mint")
    all_melon_types.append(casaba)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
