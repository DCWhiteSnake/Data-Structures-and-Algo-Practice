class animal:
    """Class that both bears and fish will extend"""
    def __init__(self, category):
        """Super class for bear and fish"""
        self._category = category
        
    def __add__(self, other):
        if other._category == self._category:
            return animal(category = self._category)
        else:
            return None

    def __str__(self):
        "String representation of the class"
        return str(self._category)


class bears(animal):
    """Class to model an asexual bear"""
    def __init__(self, family = "brown"):
        """Initialize an bear animal
        family    the bears type i.e., brown, polar e.t.c
        """
        super().__init__(category = "bear")
        self._family = family
        

class fish(animal):
    """Class to model an asexual fish"""
    def __init__(self, family = "mackarel"):
        """Initialize a fish animal
        family    the fishe's type i.e., tilapia, mackerel e.t.c 
        """
        super().__init__(category = "fish")
        self._family = family

if __name__ == '__main__':
    import random
    ocean = list() # The ocean, the habitat
    ocean_specie_type = [bears(), fish(), None]  
    for x in range(100):
        x = random.randint(0,2)
        ocean.append(ocean_specie_type[x])

    # random sequence of movements
    for x in range(len(ocean)):   
        motion_decider = randint(0,2) 
            if motion_decider == 0:
                pass  # stand still
            elif motion_decider == 1:
                # Insert logic to move backward here, and also to procreate and place new item in a random positon
            elif motion_decider == 2:
                # same as above except move forward
        

