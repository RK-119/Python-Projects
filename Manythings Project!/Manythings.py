# This below code will help to perform basic math probelems (+,-,*,/,%) & to check that given no: is prime number/not & string(concatenation,Reverse,length) 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check prime number or not!")
    print("7. String Concatenation")
    print("8. String Reverse")
    print("9. String Length")
    print("10. Exit")
    
    choice = int(input("Enter your choice: "))
    #for choice in range(1, 6):  # Loops from 0 to 5
      #print(choice)

    if choice == 1:     # Performing Addition 
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("1. Sum =", a + b)
        # break                                                        

    elif choice == 2:   # Performing Subtraction
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("2. Difference =", a - b)
        # break

    elif choice == 3:   # Peforming Multiplication
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("3. Product =", a * b)
        # break

    elif choice == 4:   # Performing Division
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("4. Quotient =", a / b)
        # break

    elif choice == 5:   # Performing Modulus
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("5. Modulus =", a % b)
        # break

    elif choice == 6:   # Performing to check wheather a number is prime or not!
        num = int(input("Enter a number: "))
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print("Not a prime number")
                    break
            else:
                print("Prime number")
                #break
        else:
            print("Not a prime number")
        #break

    elif choice == 7:   # Performing String Concatenation
      string_1 = input("Enter a first word: ") # Hello
      string_2 = input("Enter a second word: ") # World!
      concatenated_string = string_1 + string_2 # Hello + World!
      print("The Concatenated String is: ",concatenated_string) # Hello world!
      print("Thank you!")
     # break

    elif choice == 8:   # Performing String Reverse
      string = input("Enter a the word: ") # Hello 
      reversed_string = string[::-1] 
      print(reversed_string)  # Output: olleH
      #break

    elif choice == 9:   # Performing String Length
      string = input("Enter a the word: ") # Hello 
      print(len(string))  # Output: 5
      #break
      
    elif choice == 10:  # Exit the program
        print("Exiting the program. Thank you! & Goodbye!")
        break
    else:
        print("Invalid option! Try again.")


# End of the program
