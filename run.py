# importing the necessary libraries used for this script
from marsWeatherReport import getWeatherFromMars, day_with_suffix, plottingTemps, detailedSol
from datetime import datetime 
        
def main(): # this function is the first to run
    print("Welcome to the Mars Weather Tracking application! \nBelow is a list of available Sol's containing data")
    
    data = getWeatherFromMars()
    availableSols = data["sol_keys"]

    for sol in availableSols: # spits out a list of all the available Sols
        dt = datetime.strptime(data[sol]['First_UTC'], "%Y-%m-%dT%H:%M:%SZ")
        formattedDate = f"{day_with_suffix(dt.day)} {dt.strftime('%B %Y')}"
        print(f"SOL {sol} ({formattedDate})")
    
    # asks the user what they want to do
    solInput = str(input("Please pick a Sol number from the list below to see the detailed weather stats OR type 'graph' to have a visualisation of these stats for all 7 Sols: "))
    
    if solInput == "graph": # if the user types "graph" then execute the plottingTemps() function with args
        plottingTemps(data, availableSols)
    else: # otherwise execute the detailedSol() function with args
        detailedSol(data, availableSols, solInput)
    
if __name__ == "__main__":
    main() # executes the main() function