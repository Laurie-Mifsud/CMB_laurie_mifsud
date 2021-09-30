from numpy import random

MIN_NUMBER = 0
MAX_NUMBER = 1053

def game():
    ''' The game in itself    
    '''
    
    # The random number to guess
    r = random.randint(MIN_NUMBER,MAX_NUMBER)
    found = False
    
    # (Eternal) loop
    while not found:
        
        entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")
        while not entry.isdigit():
            print("please input a number")
            entry = input("\nEnter a number between "+str(MIN_NUMBER)+" and "+str(MAX_NUMBER)+": ")

        entry = int(entry)
        # Condition on what to do
        if entry == r:
            print("\n\nGood job, it was "+str(r)+"!!!")
            found=True
        elif entry>r:
            print("You are too high! Try: "+str(r-10)+"+10") 
        else:
            print("A bit more? or simply: "+str(r-10)+"+10")
    	 
# Start the game only if you wish
#playerwish = input("Hello, want to play a game? ")
#if playerwish in ["yes", "y"] :
game()
	


