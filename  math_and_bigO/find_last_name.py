We need to be able to search our LockedIn user base more quickly! Our users are complaining that the search bar is painfully slow. You'll notice that if you run the code in its current state, it will take a very long time.

The find_last_name function takes

    names_dict: a dictionary of first_name -> last_name.
    first_name: a string.

If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None.

Write the function so that it runs quickly! It should be O(1).

def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)
