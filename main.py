import log_sign, item_add, hashlib
from getpass import getpass

def repit(password):
    
        item_quest = input("1)New item \n2)View items \n3)Exit \n:")
        
        if int(item_quest) == 1:
            item_add.Dencrypt(password)
            item_add.new_item()
            item_add.Encrypt()
            repit(password)
        
        elif int(item_quest) == 2:
            item_add.Dencrypt(password)
            item_add.item_search(str(input("What is the name of the item; \n: ")))
            item_add.Encrypt()
            repit(password)
        else:
            pass

def main():
    log_r_sign = input("1) Login \n2) Sign in \n: ")
    
       
    if int(log_r_sign) == 2:
        name = input("Username: ")
        password = getpass("Password: ")
        log_sign.new_acc(name, password)


        item_quest = input("1)New item \n2)Exit \n:")
        
        if int(item_quest) == 1:
            item_add.new_item()
            item_add.Encrypt()
            
            quest_2 = input("1)New item \n2)View items \n3)Exit \n: ") 

            if int(quest_2) == 1:
                item_add.Dencrypt(password)
                item_add.new_item()
                item_add.Encrypt()
                repit(password)
            elif int(quest_2) == 2:
                item_add.Dencrypt(password)
                item_add.item_search(str(input("What is the name of the item; \n: ")))
                item_add.Encrypt()
                repit(password)
            else:
                pass

        else:
            pass


    elif int(log_r_sign) == 1:
        name = input("Username: ")
        password = getpass("Password: ")
        item_add.Dencrypt(password)

        log_sign.login(name, password)
        item_add.Encrypt()
        repit(password)
        
    else:
        pass
            
if __name__ == '__main__':
    main()
