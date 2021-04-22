u'\u20a6'
Balance = 0
from datetime import datetime
import random



database = {} #dictionary

def init():

    print('Welcome to Barclays Bank')

    ownAccount =int(input("Aleady have an account? 1 (Yes) 2 (No) \n"))
    
    if (ownAccount == 1):
        login()

    elif(ownAccount == 2):
        register() 

    else:
        print("You selected and invalid option")
        init()

def login():

    print("=========Login=========")
    accountNumberFromUser = int(input("Enter your account number \n"))
    password = input("Enter your password \n")

    
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:    
     
              print("Invalid account or Password")
    login()  
    
    

def register():

        print("*******Register*******")

        email = input("Please enter your email address \n")
        first_name = input("What is your first name? \n")
        last_name = input("What is your last name? \n")
        password= input("Please create a password \n")

        accountNumber = accountNumberGeneration()

        database[accountNumber] = [first_name, last_name, email, password]

        
        print("Your Account Has been created")
        print("== == == == == == == == == == == =")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print("== == == == == == == == == == == =")

        login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d:%m:%y")
    print("Current Time =", current_time)
    print("Current Date =", current_date)

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaints (4) Logout (5) Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        Complaints()
    elif(selectedOption == 4):
        
        logout()
    elif(selectedOption == 5):
        
        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print ("how much would you like to withdaw? \n")
    Amount = input('Enter the amount \n')
    print ("please take your " "\u20a6"+ Amount)
    selectedOptions = int(input ("Would you like to perform another transaction? 1 (yes) 2 (No) \n"))
    
    if (selectedOptions == 1):
        login()
    elif(selectedOptions == 2):
        exit()
    else:
        
     print ("Invalid option selected") 
         
      


def depositOperation():
   # print ('You selected %s' % selectedOption)
    depositAmount = input('How much would you like to deposit? \n')
    print ('Current Balance is ' "\u20a6"+ depositAmount)
    selectedOptions = int(input ("Would you like to perform another transaction? 1 (yes) 2 (No) \n"))
    
    if (selectedOptions == 1):
        login()
    elif(selectedOptions == 2):
        exit()
    else:
        
     print ("Invalid option selected")

def Complaints():
    _ = input("What issue would you like to report? \n")
    print ('Thank you for contacting us')
    selectedOptions = int(input ("Would you like to perform another transaction? 1 (yes) 2 (No) \n"))
    
    if (selectedOptions == 1):
        login()
    elif(selectedOptions == 2):
        exit()
    else:
        
     print ("Invalid option selected")

def accountNumberGeneration():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

###### ACTUAL BANKING SYSTEM ########

init()







# if (name in allowedUsers):
#     password = input("Enter your password \n")
#     userId = allowedUsers.index(name)
    
#     if (password == allowedPassword[userId]):
#         print ('welcome %s' % name)
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         current_date = now.strftime("%d:%m:%y")
#         print("Current Time =", current_time)
#         print("Current Date =", current_date)
#         print ('These are the options available')
#         print ('1. Withdrawal')
#         print ('2. Deposit')
#         print ('3. Complaints')

#         selectedOptions = int(input('Please select an option:'))

#         if (selectedOptions == 1):
#             print ('You selected %s' % selectedOptions)
#             print ('How much would you like to withdraw?')
#             Amount = input('Enter Amount:')
#             print ('Take your cash')

#         elif (selectedOptions == 2):
#             print ('You selected %s' % selectedOptions)
#             depositAmount = input('How much would you like to deposit? \n')
#             print ('Current Balance is' " " + depositAmount)
            

#         elif (selectedOptions == 3):
 #            print ('You selected %s' % selectedOptions)
 #            complaints = input('What issue would you like to report? \n')
  #           print ('Thank you for contacting us')

#         else:
#             print ('Invalid option selected')
        
#     else:
#         print('Password incorrect please try again')

    
# else: 
#     print('Name not found')    
