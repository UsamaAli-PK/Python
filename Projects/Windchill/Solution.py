def conversion(temp,speed):
    
    air_temp = temp
    air_speed = speed 
    
    if air_speed < 0:
        print("Error: Wind speed cannot be negative")
        return
    
    wct_index = 35.74 + (0.6215*air_temp) - (35.75 * air_speed**0.16) + (0.4275*air_temp*air_speed**0.16)
    print(
          f" Temperature (in F) = {air_temp}",
          f" Air speed (in MPH) = {air_speed}",
          f" Wind Chill Temperature Index = {wct_index}",
          sep="\n")
    print()


conversion(10,15)
conversion(0,25)
conversion(-10 , 35)

Temperature = float(input("Enter Temperature (in F) = "))

Speed = float(input("Enter Air speed (in MPH) = "))

conversion(Temperature,Speed)
