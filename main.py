def main():
    
    ##################################################
    # Comlete your code here
    #Use the same variables: celsius fahrenheit 
    ##################################################
    celsius = 0
    fahrenheit = 0

    print("This program will convert Celsius to Fahrenheit:\n \n")
    celsius = input('Enter a temperature in Celsius?\n')

    celsius = int(celsius)
    fahrenheit = (9 / 5 * celsius) + 32
    print(f'You entered {celsius: .2f} Celsius and that is: {fahrenheit:.2f} in Fahrenheit')
    ########################################
    # Do not delete the return statement
    ########################################

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
