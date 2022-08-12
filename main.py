import log_sign, item_add, os, time
from getpass import getpass
from rich import print


def repit(password):

        ## Printing 

        os.system("clear")
        i = ""
        num1 = 0
        while num1 < os.get_terminal_size()[0]:
            i = str(i) + " "
            num1 += 1
        x = ""
        num2 = 0

        if (int(os.get_terminal_size()[0]-4)/2)%2 != 0:
            size = (int(os.get_terminal_size()[0]-4)/2)-0.5
        else:
            size = (int(os.get_terminal_size()[0]-4)/2)
            
        while num2 < size:
            x = str(x) + " "
            num2 += 1

        up  = "[underline][#12FFA4]" + str(i) + "[/#12FFA4][/underline]"
        med = "[#12FFA4]" + str(x) + "[/#12FFA4]"
        print(str(up) + "\n" + str(med) +"[underline][#14BDFF]Menu[/#14BDFF][/underline]"+ str(med)+"\n[#0E7C83]1)[/#0E7C83][#14BDFF]New item[/#14BDFF] \n[#0E7C83]2)[/#0E7C83][#14BDFF]View items[/#14BDFF] \n[#0E7C83]3)[/#0E7C83][#14BDFF]Delete item[/#14BDFF] \n[#0E7C83]4)[/#0E7C83][#14BDFF]Reset[/#14BDFF] \n[#0E7C83]5)[/#0E7C83][#14BDFF]Safe note[/#14BDFF] \n[#0E7C83]6)[/#0E7C83][#14BDFF]View safe note[/#14BDFF] \n[#0E7C83]7)[/#0E7C83][#14BDFF]Delete note[/#14BDFF] \n[#0E7C83]8)[/#0E7C83][#14BDFF]Exit[/#14BDFF] \n"+ up)
        item_quest = input(": ")

        ## Mechanics
        
        if int(item_quest) == 1:
            os.system("clear")
            try:
                item_add.Dencrypt(password)
                item_add.new_item()
                item_add.Encrypt()
                time.sleep(0.5)            
                repit(password)
            except:
                item_add.Encrypt()
                print("[#12FFA4]You wrote something wrong. Try again![/#12FFA4]")
                time.sleep(1)
                repit(password)

        elif int(item_quest) == 2:
            try:
                os.system("clear")
                item_add.Dencrypt(password)
                print("[#14BDFF]What is the name of the item[/#14BDFF] (type all to see all)[#14BDFF];[/#14BDFF]")
                item_add.item_search(str(input(": ")))
                item_add.Encrypt()
                print("[#FF1420]Press any key to continue[/#FF1420]")
                input()
                repit(password)
            except:
                item_add.Encrypt()
                print("[#14BDFF]You wrote something wrong. Try again![/#14BDFF]")
                time.sleep(1)
                repit(password)         

        elif int(item_quest) == 3:
            try:
                os.system("clear")
                item_add.Dencrypt(password)
                item_add.delete_item()
                item_add.Encrypt()
                time.sleep(0.5)
                repit(password)
            except:
                item_add.Encrypt()
                print("[#14BDFF]You wrote something wrong. Try again![/#14BDFF]")
                time.sleep(1)
                repit(password)
        elif int(item_quest) == 4:
            print("[#14BDFF]Are you sure (type yes to continue);[/#14BDFF]")
            sec = input(": ")
            if sec == "yes":
                os.remove("database.db") 
                time.sleep(0.5)
                main()
            else:
                time.sleep(0.5)
                repit(password)
        elif int(item_quest) == 5:
            os.system("clear")
            try:
                item_add.Dencrypt(password)
                item_add.safe_note()
                item_add.Encrypt()
                time.sleep(0.5)            
                repit(password)
            except:
                item_add.Encrypt()
                print("[#12FFA4]You wrote something wrong. Try again![/#12FFA4]")
                time.sleep(1)
                repit(password)
        
        elif int(item_quest) == 6:
            try:
                os.system("clear")
                item_add.Dencrypt(password)
                print("[#14BDFF]What is the name of the note[/#14BDFF] (type all to see all)[#14BDFF];[/#14BDFF]")
                item_add.safe_note_search(str(input(": ")))
                item_add.Encrypt()
                print("[#FF1420]Press any key to continue[/#FF1420]")
                input()
                repit(password)
            except:
                item_add.Encrypt()
                print("[#14BDFF]You wrote something wrong. Try again![/#14BDFF]")
                time.sleep(1)
                repit(password)

        elif int(item_quest) == 7:
            try:
                os.system("clear")
                item_add.Dencrypt(password)
                item_add.delete_note()
                item_add.Encrypt()
                time.sleep(0.5)
                repit(password)
            except:
                item_add.Encrypt()
                print("[#14BDFF]You wrote something wrong. Try again![/#14BDFF]")
                time.sleep(1)
                repit(password)   

        else:
            pass

def main():
    os.system("clear")
    print("[#0E7C83]1)[/#0E7C83][#14BDFF] Login[/#14BDFF] \n[#0E7C83]2)[/#0E7C83] [#14BDFF]Sign in[/#14BDFF]")
    log_r_sign = input(": ")
    
       
    if int(log_r_sign) == 2:
        name = input("Username: ")
        password = getpass("Password: ")
        log_sign.new_acc(name, password)

        ## Printing

        os.system("clear")
        i = ""
        num1 = 0
        while num1 < os.get_terminal_size()[0]:
            i = str(i) + " "
            num1 += 1
        x = ""
        num2 = 0

        if (int(os.get_terminal_size()[0]-4)/2)%2 != 0:
            size = (int(os.get_terminal_size()[0]-4)/2)-0.5
        else:
            size = (int(os.get_terminal_size()[0]-4)/2)
            
        while num2 < size:
            x = str(x) + " "
            num2 += 1

        up  = "[underline][#12FFA4]" + str(i) + "[/#12FFA4][/underline]"
        med = "[#12FFA4]" + str(x) + "[/#12FFA4]"
        print(str(up) + "\n" + str(med) +"[underline][#14BDFF]Menu[/#14BDFF][/underline]"+ str(med)+"\n[#0E7C83]1)[/#0E7C83][#14BDFF]New item[/#14BDFF] \n[#0E7C83]2)[/#0E7C83][#14BDFF]Exit[/#14BDFF] \n"+ up)
        item_quest = input(": ")

        ## Mechanics

        if int(item_quest) == 1:
            try:
                os.system("clear")
                item_add.new_item()
                item_add.Encrypt()
                time.sleep(0.5)
                repit(password)
            except:
                item_add.Encrypt()
                print("[#14BDFF]You wrote something wrong. Try again![/#14BDFF]")
                time.sleep(1)
                repit(password)
        else:
            item_add.Encrypt()



    elif int(log_r_sign) == 1:
        name = input("Username: ")
        password = getpass("Password: ")
        item_add.Dencrypt(password)

        log_sign.login(name, password)
        item_add.Encrypt()
        repit(password)
            
if __name__ == '__main__':
    main()
