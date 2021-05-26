from math import trunc


class animal:
    """Class that both bears and fish will extend"""

    def __init__(self, category):
        """Super class for bear and fish"""
        self._category = category

    def __add__(self, other):
        if other._category == self._category:
            return animal(category=self._category)  # How does python create new items of a type
        elif other._category != self._category:
            return None

    def __str__(self):
        "String representation of the class"
        return self._category


class bears(animal):
    """Class to model an asexual bear"""

    def __init__(self, family="brown"):
        """Initialize an bear animal
        family    the bears type i.e., brown, polar e.t.c
        """
        super().__init__(category="bear")
        self._family = family


class fish(animal):
    """Class to model an asexual fish"""

    def __init__(self, family="mackarel"):
        """Initialize a fish animal
        family    the fishe's type i.e., tilapia, mackerel e.t.c
        """
        super().__init__(category="fish")
        self._family = family


if __name__ == '__main__':
    import random

    def find_none(item):
        itemcontainsnone = False
        for x in range(len(item)):
            if item[x] == None:
                itemcontainsnone = True
                break
            if itemcontainsnone == True:
                break

        if isinstance(item, (list)) and  itemcontainsnone == True:
            none_found = False
            while not none_found:
                x = random.randint(0, len(item) - 1)
                if item[x] == None:
                    none_found == True
                    return x
                else:
                    pass

    ocean = list()  # The ocean, the habitat
    ocean_specie_type = [bears(), fish(), None]
    for x in range(20):
        x = random.randint(0, 2)
        ocean.append(ocean_specie_type[x])

    print("Initial Ocean")  # Display ocean
    ocen = ""
    for x in range(len(ocean)):
        ocen += str(ocean[x]) + " "
    print(ocen)

    # random sequence of movements
    for x in range(len(ocean) + 1):

        motion_decider = random.randint(0, 2)
        if motion_decider == 0 and x < len(ocean):
            if ocean[x] != None:
                print(str(ocean[x]), "at positon ",[x], " is immobile")
            else:
                print("None")

        elif motion_decider == 1:  # forward motion
            if x == len(ocean):
                break
            if x == len(ocean) - 1:
                print(str(ocean[x]), "at positon ",
                      [x], "can't move anymore further")
                break  # end of loop

            if ocean[x] == None:
                print("nothing to move at position ",[x])
                continue

            else:

                if ocean[x + 1] == None:
                    print(str(ocean[x]), " moves from ", [x], "to ",[x+1])
                    temp = ocean[x]  # temp storage for animal at positon x
                    ocean[x] = None
                    ocean[x+1] = temp

                elif isinstance(ocean[x], (bears)) and isinstance(ocean[x + 1], (fish)):
                    print("fish at position ", [
                        x+1], "dies, blood goes brrr, bear tummy full")
                    ocean[x + 1] = None
                elif isinstance(ocean[x], (fish)) and isinstance(ocean[x + 1], (bears)):
                    print("fish at position ", [
                        x], "dies, blood goes brrr, bear tummy full")
                    ocean[x] = None
                elif isinstance(ocean[x], (fish)) and isinstance(ocean[x + 1], (fish)):
                    try:
                        print("Mating ensues between fishes at positions",
                              [x], "and",[x+1])
                        t = find_none(ocean)
                        ocean[t] = ocean[x] + ocean[x + 1]
                        print("fish offspring has moved to position", [t])
                    except TypeError:
                        print("No free space for offspring")
                    
                    # put a new instance of fish in a random location that is unoccupied
                elif isinstance(ocean[x], (bears)) and isinstance(ocean[x + 1], (bears)):
                    # put a new instance of bears in a  random location that is unoccupied
                    try:
                        print("Mating ensues between bears at positions",
                              [x], "and",[x+1])
                        t = find_none(ocean)
                        ocean[t] = ocean[x] + ocean[x + 1]
                        print("bear offspring has moved to position", [t])
                    except TypeError:
                        continue

        elif motion_decider == 2:
            # same as above except move backward
            if x == 0:
                print("No space to move back to for",
                      str(ocean[x]), "at positon",[x])
                pass

            elif x < len(ocean) and x != 0:
                if ocean[x] == None:
                    print("nothing to move at positon ",[x])
                    continue
                elif ocean[x - 1] == None and ocean[x] != None:
                    print(str(ocean[x]),[x], " moved 1 step backward to position ",[x-1] )
                    temp = ocean[x]  # temp storage for animal at positon x
                    ocean[x] = None
                    ocean[x-1] = temp

                elif isinstance(ocean[x], (bears)) and isinstance(ocean[x - 1], (fish)):
                    print("fish at position ", [
                          x-1], "dies, blood goes brrr, bear tummy full")
                    ocean[x - 1] = None
                elif isinstance(ocean[x], (fish)) and isinstance(ocean[x - 1], (bears)):
                    print("fish at position ", [
                          x], "dies, blood goes brrr, bear tummy full")
                    ocean[x] = None

                elif isinstance(ocean[x], (fish)) and isinstance(ocean[x - 1], (fish)):
                    try:
                        freespace = find_none(ocean)
                        print("Mating ensues between fishes at positions",
                              [x], "and", x-1)
                        ocean[freespace] = ocean[x] + ocean[x - 1]
                        print("New fish child at positon ", [freespace])
                    except TypeError:
                        continue
                    # put a new instance of fish in a random location that is unoccupied
                elif isinstance(ocean[x], (bears)) and isinstance(ocean[x - 1], (bears)):
                    # put a new instance of bears in a  random location that is unoccupied
                    try:
                        freespace = find_none(ocean)
                        print("Mating ensues between bears at positions",
                              [x], "and", x-1)
                        ocean[freespace] = ocean[x] + ocean[x - 1]
                        print("New bear child at positon ", [freespace])
                    except TypeError:
                        print("type")

        else:
            print("end")
            break

    print("Final ocean")
    ocen = ""
    for x in range(len(ocean)):
        ocen += str(ocean[x]) + " "
    print(ocen)
