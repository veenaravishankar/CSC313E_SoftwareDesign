#expected output:
#[3, 5, 3, 6, 3, 9]
#[14, 5, 3, 6, 14, 9]
def main():
    list = [14, 5, 3, 6, 14, 9]
    new_list = new_value_int_list(list, 14, 3)
    print(new_list)
    print(list)

def new_value_int_list(list, val_search, val_replace):
    new_list = list
    for i in range(len(new_list) - 1):
        if(new_list[i] = val_search):
            new_list[i] = val_replace
    
    return new_list

main()