import matplotlib.pyplot as plt

def plottingTemps(data, availableSols): # this function generates the graph
    yAvgTemps = []
    yMinTemps = []
    yMaxTemps = []
    
    for sol in availableSols: # for every sol (mars day) 
        yAvgTemps.append(data[sol]["AT"]["av"]) # adds the average temp to a list 
        
    for sol in availableSols:
        yMinTemps.append(data[sol]["AT"]["mn"]) # adds the lowest temp to a list
    
    for sol in availableSols:
        yMaxTemps.append(data[sol]["AT"]["mx"]) # adds the highest temp to a list

    # plots each line on the graph  
    plt.plot(availableSols, yAvgTemps, marker='o', label="Average", color="green")
    plt.plot(availableSols, yMinTemps, marker='o', label="Min", color="blue")
    plt.plot(availableSols, yMaxTemps, marker='o', label="Max", color="red")
    
    plt.legend()
    plt.xlabel("Sol")
    plt.ylabel("Temperature (°C)")
    plt.title("Mars Atmospheric Temperatures")
    plt.savefig("mars_weather_plot.png")
    print("The chart GUI should be shown, if you're running this script on a docker container the chart is saved in a file called 'mars_weather_plot.png'")
    plt.show()