

#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining based on the elapsed bake time.
    
    Parameters:
        elapsed_bake_time (int): The time in minutes elapsed since the start of the baking process.
    
    Returns:
        int: The total time needed to complete the baking session.

    This function takes an integer representing the time elapsed in minutes. It calculates the minutes left to finish.
    
    """
    return(EXPECTED_BAKE_TIME-elapsed_bake_time)


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time based on the number of layers.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    
    Returns:
        int: The total time needed to bake the number of layers.

    This function takes an integer representing the number of lasagna 
    layers. It calculates the minutes needed to cook the layers.
    
    """
    return(TIME_PER_LAYER*number_of_layers)


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    Layer_time=preparation_time_in_minutes(number_of_layers)
    return(Layer_time + elapsed_bake_time)
    


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
