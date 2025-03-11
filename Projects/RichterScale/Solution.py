#Print Values
print(
    """+-----------+-------------------------+--------------------------+
| Richter   | Energy (Joules)         | TNT Equivalent (tons)    |
+-----------+-------------------------+--------------------------+
| 1.0       | 2.0 x 10^6              | 4.8 x 10^-4              |
| 5.0       | 2.0 x 10^12             | 4.8 x 10^2               |
| 9.1       | 2.8 x 10^18             | 6.7 x 10^8               |
| 9.2       | 4.0 x 10^18             | 9.5 x 10^8               |
| 9.5       | 1.1 x 10^19             | 2.7 x 10^9               |
+-----------+-------------------------+--------------------------+
    """
)

def conversion(ricther):
    Ricther_to_Energy =10**(1.5*ricther+4.8)
    ENergy_to_TNT = Ricther_to_Energy/(4.184 * (10**9))
    
    print(f"Richter scale value = {ricther}",
      f"Energy in joules =  {Ricther_to_Energy}",
      f"TNT in tons = {ENergy_to_TNT}" , sep="\n")

def main():
    while True:
        ricther = input("Enter a positive float: ")
        try:
            value = float(ricther)
            if value > 0:
                conversion(value)
                break
            else:
                print("The number must be greater than zero. Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid positive float.")


main()