import log_sign, item_add, hashlib
from getpass import getpass

def repit():
    
        item_quest = input("1)New item \n2)View items \n3)Exit \n:")
        
        if int(item_quest) == 1:
            item_add.new_item()
            repit()
        
        elif int(item_quest) == 2:
            item_add.item_search(str(input("What is the name of the item; \n: ")))
            repit()
        else:
            pass

def main():
    log_r_sign = input("1) Login \n2) Sign in \n: ")
    
       
    if int(log_r_sign) == 2:
        log_sign.new_acc(input("Username: "), getpass("Password: "))

        item_quest = input("1)New item \n2) Exit \n:")
        
        if int(item_quest) == 1:
            item_add.new_item()
            
            quest_2 = input("1)New item \n2)View items \n3)Exit \n: ") 

            if int(quest_2) == 1:
                item_add.new_item()
                repit()
            elif int(quest_2) == 2:
                item_add.item_search(str(input("What is the name of the item; \n: ")))
                repit()
            else:
                pass

        else:
            pass


    elif int(log_r_sign) == 1:
        log_sign.login(input("Username: "), getpass("Password: "))
        
        repit()
        
    else:
        pass
            
if __name__ == '__main__':
    main()