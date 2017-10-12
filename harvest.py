############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless = False, is_bestseller = False):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    cas = MelonType('Casaba', 'cas', 2003, 'orange')
    cren = MelonType('Crenshaw', 'cren', 1996, 'green')
    yel = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow', False, True)

    musk.add_pairing(['mint'])
    cas.add_pairing(['strawberries', 'mint'])
    cren.add_pairing(['proscuitto'])
    yel.add_pairing(['ice cream'])

    all_melon_types.extend([musk, cas, cren, yel])

    return all_melon_types


def print_melon_pairings(melon_list):
    """ Print each melon's pairings."""

    for melon in melon_list:
        print "{} pairs with".format(melon.name)
        for pairing in melon.pairings:
            print "- {}".format(pairing)


def make_melon_type_lookup(melon_list):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_list:
        melon_dict[melon.code] = melon

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape, color, field, person):
        self.melon_type = melon_type
        self.shape = shape
        self.color = color
        self.field = field
        self.person = person

    def is_sellable(self):
        return ((self.shape > 5) and (self.color > 5) and (self.field != 3))



def make_melons(melon_dict):
    """Returns a list of Melon objects."""

    melon_1 = Melon(melon_dict['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_dict['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_dict['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_dict['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_dict['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_dict['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_dict['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_dict['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_dict['yw'], 7, 10, 3, 'Sheila')

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = melon.is_sellable()
        if sellable:
            print "Harvested by {} from Field # {} CAN BE SOLD".format(melon.person, melon.field)
        else:
            print "Harvested by {} from Field # {} NOT SELLABLE".format(melon.person, melon.field)
