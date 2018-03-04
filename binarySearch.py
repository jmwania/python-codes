#Our sample list
sampleList = [0,2,6,78,65,56,23,1,6]
search_list = sorted(sampleList)


#Get some input
search_for = int(input("What would you like to search for? "))

#############################################################
def search(search_for, sampleList):
    loop_counter = 0
    lowerbound = 0
    upperbound = len(search_list) - 1
    found = False

    while found == False and lowerbound <= upperbound:
        midpoint = (lowerbound + upperbound) // 2
        if search_list[midpoint] == search_for:
            found = True
            loop_counter +=1
            return found
        elif search_list[midpoint] < search_for:
            lowerbound = midpoint + 1
        else:
            upperbound = midpoint - 1
    return found

#############################################################

if search(search_for, search_list):
    print ("Item found.")
else:
    print ("Item doesn't exist.")

#############################################################


