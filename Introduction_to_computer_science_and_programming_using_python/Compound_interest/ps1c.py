##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input('Enter the initial deposit: '))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home = 800000.0
portion_down_payment = 0.25
required_down_payment = portion_down_payment * cost_of_dream_home
months = 36
epsilon = 100
steps = 0


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

#amount_saved(r) is a rising function

if initial_deposit >= required_down_payment - epsilon:   #amount_saved(r = 0) >= required_down_payment - epsilon
    r = 0.0
elif initial_deposit * (1 + 1 / 12)**months < required_down_payment - epsilon:   #amount_saved(r = 1) < required_down_payment - epsilon
    r = None
else:   #amount_saved(r = 0) < required_down_payment - epsilon AND amount_saved(r = 1) >= required_down_payment - epsilon => exists a search interval
    low = 0.0
    high = 1.0
    r = (low + high) / 2
    steps += 1
    
    while abs(initial_deposit * (1 + r / 12)**months - required_down_payment) > epsilon:
        if initial_deposit * (1 + r / 12)**months > required_down_payment:
            high = r
        else:
            low = r
        r = (low + high) / 2
        steps += 1

print('Best savings rate:', r, '[or very close to this number]')
print('Steps in bisection search:', steps, '[or very close to this number]')
