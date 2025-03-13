# Lab1

def find_duplicate(list_of_numbers):
    #print(list_of_numbers)
    new = {x for x in list_of_numbers if list_of_numbers.count(x)>1}
    #print(new);
    
    if len(new)==0:
        return False;
    else:
        return True;
    
