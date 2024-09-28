#TODO: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME=40


def bake_time_remaining(elapsed_bake_time):

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.

def preparation_time_in_minutes(number_of_layers): 
   
    preparation_by_layers=2 
    number_of_layers= number_of_layers * preparation_by_layers
    return number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    total_preparation_time = preparation_time_in_minutes(number_of_layers)
    return total_preparation_time + elapsed_bake_time

