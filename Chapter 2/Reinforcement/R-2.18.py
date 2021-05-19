from Progression import FibonacciProgression

two_two = FibonacciProgression(2,2)


progression_items=[next(two_two) for x in range(8)] # Use list Comprehension syntax
                                                    # to get up to eight item.

eight_item = progression_items[7]                   # Harvest the eight item.
