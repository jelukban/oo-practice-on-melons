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
    crenshaw.add_pairing("mint")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(code="yw", first_harvest=2013, color="yellow", \
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

#print(make_melon_types())

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("\n")
        print(f"{melon.name} pairs with \n- {melon.pairing}")

#print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_by_code = {}

    for melon in melon_types:
        melon_type_by_code[melon.code]=melon.name

    return melon_type_by_code

print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from,\
        harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        self.is_sellable = self.shape_rating > 5 and self.color_rating > 5 and\
            self.harvested_from != "Field 3"

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    Melon_1 = Melon(melons_by_id["yw"], shape_rating=8, color_rating=7, \
         harvested_from="Field 2", harvested_by="Shiela")
    Melon_1.is_sellable()
    melons.append(Melon_1)
    Melon_2 = Melon(melons_by_id["yw"], shape_rating=3, color_rating=4,  \
        harvested_from="Field 2", harvested_by="Shiela")
    Melon_2.is_sellable()
    melons.append(Melon_2)
    Melon_3 = Melon(melons_by_id["yw"], shape_rating=9, color_rating=8,  \
        harvested_from="Field 3", harvested_by="Shiela")
    Melon_3.is_sellable()
    melons.append(Melon_3)
    Melon_4 = Melon(melons_by_id["cas"], shape_rating=10, color_rating=6,  \
        harvested_from="Field 35", harvested_by="Shiela")
    Melon_4.is_sellable()
    melons.append(Melon_4)



    Melon_5 = Melon(melons_by_id["cren"], shape_rating=8, color_rating=9, \
        harvested_from="Field 35", harvested_by="Michael")
    Melon_5.is_sellable()
    melons.append(Melon_5)

    Melon_6 = Melon(melons_by_id["cren"], shape_rating=8, color_rating=2, \
        harvested_from="Field 35", harvested_by="Michael")
    Melon_6.is_sellable()
    melons.append(Melon_6)

    Melon_7 = Melon(melons_by_id["cren"], shape_rating=2, color_rating=3, \
        harvested_from="Field 4", harvested_by="Michael")
    Melon_7.is_sellable()
    melons.append(Melon_7)

    Melon_8 = Melon(melons_by_id["musk"], shape_rating=6, color_rating=7, \
        harvested_from="Field 4", harvested_by="Michael")
    Melon_8.is_sellable()
    melons.append(Melon_8)

    Melon_9 = Melon(melons_by_id["yw"], shape_rating=7, color_rating=10, \
        harvested_from="Field 3", harvested_by="Sheila")
    Melon_9.is_sellable()
    melons.append(Melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print(f"Harvested by {melon.harvested_by} from {melon.harvested_from} {'CAN BE SOLD' if melon.is_sellable else 'NOT SELLABLE'}")

get_sellability_report(make_melons(make_melon_types()))