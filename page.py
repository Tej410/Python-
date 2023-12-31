# name = input("enter your name")

# if(len(name)<3):
#     print("name must be atleast three characters")
# elif(len(name)>50):
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")    



# weight = int(input("enter your weight"))
# unit = input("(L)bs or (K)g:").lower()
# if(unit == 'k'):
#     print(f'you are {weight*2.2}pounds')
# elif unit == 'l':
#     print(f'you are {weight*0.45}kilograms')  
# else:
#     print('wrong unit entered!') 



# secret_number = 8
# no_of_guesses = 3

# while no_of_guesses:
#     entered_number = int(input('Guess:'))
#     if secret_number == entered_number:
#         print("You are correct!")
#         break
#     no_of_guesses-=1

# if not no_of_guesses:
#     print('Sorry you failed!')


prev = ""
while True:
    i = input('>')
    if i == 'help':
        print('start - to start the car\nstop  - to stop the car\nquit  - to quit ')
    elif i=='start' :
        if prev!='start':
            print('Car started')
            prev = 'start'
        else:
            print('Car is already started')    
    elif i=='stop' :
        if prev!='stop':
            print('Car stopped')
            prev = 'stop'
        else:
            print("Car at stop already")    
    elif i=='quit':
        print("Quitting...")
        break
    else:
        print("I dont understand. Enter again- ")    

    
