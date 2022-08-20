import log_sign, item_add, os
from getpass import getpass
from rich import print

def main():
    os.system("clear")
    print("[#0E7C83]1)[/#0E7C83][#14BDFF] Login[/#14BDFF] \n[#0E7C83]2)[/#0E7C83] [#14BDFF]Sign in[/#14BDFF]")
    log_r_sign = input(": ")
    
       
    if int(log_r_sign) == 2:
        name = input("Username: ")
        password = getpass("Password: ")
        log_sign.new_acc(name, password)
        item_add.Encrypt()
        item_add.repit(password)

    elif int(log_r_sign) == 1:
        name = input("Username: ")
        password = getpass("Password: ")
        item_add.Dencrypt(password)

        log_sign.login(name, password)
        item_add.Encrypt()
        item_add.repit(password)
            
if __name__ == '__main__':
    main()
