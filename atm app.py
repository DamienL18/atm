



def pin():
   
    tries = 3
    while tries >=0:
        pin = int(input('Sorry but we couldnt find your face in the database, attempt inputting your pin: '))
        if pin==(5000):
            print("Correct... One moment please, we are fetching your inquired amount of cash")
            return True
        else:
            print("Incorrect Password, please try again")
            tries += 1
    print("Incorrect Password, you have no remaining attempts to input your pin")
    return False

def start_menu():
    balance=1000000
   
    print('Thank You For choosing the ATM-O-TRONIC 5000 available only on python.')
    print("Java, HTML, C++ as well as many more programming languages soon to come. c:")
    print("PSSSSSTTTTT... For future references; your pin is hidden in the machines name") 
    print('Please wait for the facial recognition to process your image...')

    if pin():
            print('1  for Balance\n')
            print('2 for Withdrawal\n')
            print('3 for Deposit\n')
            print('4 To Exit\n')

            transaction = int(input('Choose which transaction best fits your needs today:'))
            if transaction == 1:
                print('Your Balance is $',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('NO','no'):
                    print('Thank you enjoy the remainder of your day  type start_menu()')
                 
            elif transaction == 2:
                
                withdrawl = float(input('How Much Would you like to  withdraw? \n$10 $20 $40 $60 $80 $100 :'))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now $',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('NO','no'):
                        print('Thank you enjoy the remainder of your day  type start_menu() ')
                    
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('yes')
                
            elif transaction == 3:
                deposit = float(input('How much money would you want our trustworthy money elves to protect?  '))
                balance = balance + deposit
                print('Your Balance is $',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('NO','no'):
                    print('Thank You, enjoy the remainder of your day type start_menu() ')
               
            elif transaction == 4:
                
                print('Thank you for choosing ATM-O-TRONIC 5000\n')
              
        

    print("Exiting Program, type start_menu() ")

start_menu()

