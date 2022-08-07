import log_sign, item_add, hashlib
from getpass import getpass

def main():
    log_r_sign = input("1) Login \n2) Sign in \n: ")
    
       
    if int(log_r_sign) == 2:
        log_sign.new_acc(input("Username: "), getpass("Password: "))

        item_quest = input("1)New item \n2) Exit \n:")
        
        if item_quest == 1:
            log_sign.new_item(str(input("Enter your username: ")), str(input("Enter your email: ")), str(getpass("Enter your password: ")), str(input("Enter the url of website: ")))
            
            quest_2 = input("1)New item \n2)View items \n3)Exit \n: ") 

            if int(quest_2) == 1:
                item_add.new_item(str(input("What is the name of the item; \n: ")))
                item_add.repit(log_sign, item_add)
            elif int(quest_2) == 2:
                item_add.item_search(str(input("What is the name of the item; \n: ")))
                item_add.repit(log_sign, item_add)
            else:
                pass

        else:
            pass


    elif int(log_r_sign) == 1:
        log_sign.login(input("Username: "), getpass("Password: "))
        
        item_add.repit(log_sign, item_add)
        
    else:
        pass
            
if __name__ == '__main__':
    main()