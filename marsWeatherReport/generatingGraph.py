import matplotlib.pyplot as plt

def plottingTemps(validatedData, availableSols): # this function generates the graph
    
    if validatedData == {} and availableSols == []:
        raise KeyError('There are no available sols and data to plot')
    if validatedData == {}:
        raise KeyError('There is no available data to plot with')
    if availableSols == []:
        raise KeyError('There are no available sols to plot')
    
    fig, ax = plt.subplots()
    
    yAvgTemps = []
    yMinTemps = []
    yMaxTemps = []
    
    for sol in availableSols: # for every sol (mars day) 
        yAvgTemps.append(validatedData[sol]["AT"]["av"]) # adds the average temp to a list 
        
    for sol in availableSols:
        yMinTemps.append(validatedData[sol]["AT"]["mn"]) # adds the lowest temp to a list
    
    for sol in availableSols:
        yMaxTemps.append(validatedData[sol]["AT"]["mx"]) # adds the highest temp to a list

    # plots each line on the graph  
    plt.plot(availableSols, yAvgTemps, marker='o', label="Average", color="green")
    plt.plot(availableSols, yMinTemps, marker='o', label="Min", color="blue")
    plt.plot(availableSols, yMaxTemps, marker='o', label="Max", color="red")
    
    ax.legend()
    ax.set_xlabel("Sol")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Mars Atmospheric Temperatures")
    
    plt.savefig("mars_weather_plot.png")
    print("The chart GUI should be shown, if you're running this script on a docker container the chart is saved in a file called 'mars_weather_plot.png'")
    plt.show()
    
    return fig