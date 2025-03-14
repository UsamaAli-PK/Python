print(
    """+-----------+-------------------------+--------------------------+
| Richter   | Energy (Joules)         | TNT Equivalent (tons)    |
+-----------+-------------------------+--------------------------+
| 1.0       |    1995262.314968789    |   0.000476879137688307   |
| 5.0       |   1.9952623149688e+12   |   476.8791337688404      |
| 9.1       |   2.81838293126449e+18  |   673609687.204692       |
| 9.2       |   3.98107170553499e+18  |   951498773.5982201      |
| 9.5       |  1.1220184543019633e+19 |   2681608466.304882      |
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
