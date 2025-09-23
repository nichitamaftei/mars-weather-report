def day_with_suffix(day): # this function gets a day (e.g 3) and returns a string with its suffix
    if not isinstance(day, int):
        raise ValueError("Day must be an integer")
    if day <= 0:
        raise ValueError("Day must be a positive integer and above 0")
    if day >= 31:
        raise ValueError("Day must be less than or equal to 31")
    
    if 11 <= day <= 13:
        return f"{day}th"
    last_digit = day % 10
    if last_digit == 1:
        return f"{day}st"
    elif last_digit == 2:
        return f"{day}nd"
    elif last_digit == 3:
        return f"{day}rd"
    else:
        return f"{day}th"
    

def detailedSol(data, solInput): # this function gives you specific details on the selected Sol (mars day)
    
    print(f"SOL {solInput} was chosen.")
    
    avgTemp = data[solInput]["AT"]["av"]
    print(f"Average temperature: {avgTemp}°C")
    
    lowestTemp = data[solInput]["AT"]["mn"]
    print(f"Lowest temperature recorded: {lowestTemp}°C")
    
    highestTemp = data[solInput]["AT"]["mx"]
    print(f"Highest temperature recorded: {highestTemp}°C")