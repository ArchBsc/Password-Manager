import log_sign, item_add, os, time
from getpass import getpass
from rich import print


def repit(password):
        os.system("clear")
        i = ""
        num1 = 0
        while num1 < os.get_terminal_size()[0]:
            i = str(i) + "_"
            num1 += 1
        x = ""
        num2 = 0

        if (int(os.get_terminal_size()[0]-4)/2)%2 != 0:
            size = (int(os.get_terminal_size()[0]-5)/2)
        else:
            size = (int(os.get_terminal_size()[0]-4)/2)
            
        while num2 < size:
            x = str(x) + "-"
            num2 += 1

        up  = "[#12FFA4]" + str(i) + "[/#12FFA4]"
        med = "[#12FFA4]" + str(x) + "[/#12FFA4]"
        print(str(up) + "\n" + str(med) +"[#14BDFF]Menu[/#14BDFF]"+ str(med)+"\n[#0E7C83]1)[/#0E7C83][#14BDFF]New item[/#14BDFF] \n[#0E7C83]2)[/#0E7C83][#14BDFF]View items[/#14BDFF] \n[#0E7C83]3)[/#0E7C83][#14BDFF]Delete item[/#14BDFF] \n[#0E7C83]4)[/#0E7C83][#14BDFF]Exit[/#14BDFF] \n"+ up)
        item_quest = input(": ")
        
        if int(item_quest) == 1:
            os.system("clear")
            item_add.Dencrypt(password)
            item_add.new_item()
            item_add.Encrypt()
            time.sleep(0.5)            
            repit(password)
        
        elif int(item_quest) == 2:
            os.system("clear")
            item_add.Dencrypt(password)
            print("[#14BDFF]What is the name of the item[/#14BDFF] (type all to see all)[#14BDFF];[/#14BDFF]")
            item_add.item_search(str(input(": ")))
            item_add.Encrypt()
            print("[#FF1420]Press any key to continue[/#FF1420]")
            input()
            repit(password)
        elif int(item_quest) == 3:
            os.system("clear")
            item_add.Dencrypt(password)
            item_add.delete()
            item_add.Encrypt()
            time.sleep(0.5)
            repit(password)
        else:
            pass

def main():
    log_r_sign = input("1) Login \n2) Sign in \n: ")
    
       
    if int(log_r_sign) == 2:
        name = input("Username: ")
        password = getpass("Password: ")
        log_sign.new_acc(name, password)
        os.system("clear")
        while num1 < os.get_terminal_size()[0]:
            i = str(i) + "-"
            num1 += 1
        x = ""
        num2 = 0

        if (int(os.get_terminal_size()[0]-4)/2)%2 != 0:
            size = (int(os.get_terminal_size()[0]-5)/2)
        else:
            size = (int(os.get_terminal_size()[0]-4)/2)
            
        while num2 < size:
            x = str(x) + "-"
            num2 += 1
        
        up  = "[#12FFA4]" + str(i) + "[/#12FFA4]"
        med = "[#12FFA4]" + str(x) + "[/#12FFA4]"
        print(up + "\n"+ med +"[#14BDFF]Menu[/#14BDFF]"+ med +"\n[#0E7C83]1)[/#0E7C83][#14BDFF]New item[/#14BDFF] \n[#0E7C83]2)[/#0E7C83][#14BDFF]Exit[/#14BDFF] \n"+ up)
        item_quest = input(": ")
 
        if int(item_quest) == 1:
            os.system("clear")
            item_add.new_item()
            item_add.Encrypt()
            time.sleep(0.5)
            repit(password)
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
