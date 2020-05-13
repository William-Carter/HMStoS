def formattedtosecond(formatted, *args):
    """
    Takes a string that looks something like "00:33:24" and converts it to seconds.
    Returns false if input isn't not formatted correctly.
    Allows for just seconds as well. For example, 33:24 would be written as 2004
    Maximum of 23:59:59
    Add True as a second argument to see the reason for a string failing
    """
    debug = False
    if len(args) > 0:
        if args[0] == True:
            debug = True
    parsed = formatted.split(":")
    # Check if the amount is more than just seconds
    if not len(parsed) == 1:

        # Check that all parts of the list are numbers
        for item in parsed:
            try:
                int(item)
            except:
                if debug:
                    print("Not a number")
                return False

        # Reverse list to make it easier to work with
        parsed = parsed[::-1]

        # Check that there aren't more than three arguments (##:##:##:## doesn't make any sense)
        if len(parsed) > 3:
            if debug:
                print("Too many arguments")
            return False

        # Makes sure that the int value of each argument isn't over the max limit
        for i in range(len(parsed)):
            if i < 2:
                if int(parsed[i]) > 59:
                    if debug:
                        print("Minutes or seconds exceed max limit")
                    return False
            else:
                if int(parsed[i]) > 23:
                    if debug:
                        print("Hours exceed max limit")
                    return False

        # Stops something like 15:000000002 being read as 15:02
        for i in parsed:
            if len(i) > 2:
                if debug:
                    print("Too many leading 0s")
                return False

        # Unless it's the highest order, make sure it has two digits (So no 4:5:02, but 5:02 is still fine)
        for i in range(len(parsed)):
            if len(parsed)-1 > i:
                if len(parsed[i]) < 2:
                    if debug:
                        print("Missing leading 0")
                    return False

        # Finally getting the total amount of seconds.
        # Works by multipling the weight by 60 depending on what order it is. For example a minute is weighted *60 and an hour is weighting *60*60
        seconds = 0
        for i in range(len(parsed)):
            work = int(parsed[i])
            for j in range(i):
                work = work*60
            seconds += work
        return seconds
    else:
        try:
            return int(parsed[0])
        except:
            if debug:
                print("Not a number")
            return False


# Just some tests
if __name__ == "__main__":
    testList = ["300", "1:00", "15:30:34", "fifty",
                "05:00", "5:00", "005:00", "5:000", "5:99"]
    for test in testList:
        print(test)
        print(formattedtosecond(test))
