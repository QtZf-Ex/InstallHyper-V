from ast import In
from asyncio.windows_events import NULL
from re import S
from main import *
import os

CentOS_7_Mass_Install = CentOS_7_Mass_Install.split()

# Просмотр выбранных пунктов 
print("You have chosen: ", CentOS_7_Mass_Install)


# Настройка Firewalld 
# Настройка Iptables https://github.com/ZaDr0t-sys/InstallHyper-V

### def func to install Apache v2, PHP v7, Zabbix 


def Install_Apache():
    print(''' \n\nInstall Apache\n\n''')
    os.system("sudo yum update && sudo yum upgrade -y")
    os.system("sudo yum update httpd -y")
    os.system("sudo yum install httpd -y")

    # Открыть порт 90 и 443 http https + reload firewalld 
    os.system("sudo firewall-cmd --permanent --add-service=http")
    os.system("sudo firewall-cmd --permanent --add-service=https")
    os.system("sudo firewall-cmd --reload")

    # Запуск + проверить статус httpd
    os.system("sudo systemctl start httpd")
    os.system("sudo systemctl status httpd")

    # автозапуск 
    os.system("sudo systemctl enable httpd")

    # Получить информацию о apache
    os.system("Apache Info: >> Info")
    os.system("""ip a | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1 >> Info""")
    os.system("hostname -I >> Info\n\n\n")

    # End
    print(''' \n\nend of install Apache\n\n''')

def Install_PHP():
    print(''' \n\nInstall PHP\n\n''')

    Standart_User_Is_Whoami = input("Standart User for owner of Apache is: " + os.system("whoami") + "OK?\n")
    if Standart_User_Is_Whoami == "y" or Standart_User_Is_Whoami == "Y":
        Standart_User = Standart_User_Is_Whoami
        print("OK, Apache owner is" + Standart_User + "\n\n\n")
    
    elif Standart_User_Is_Whoami == "n" or Standart_User_Is_Whoami == "N":
        Standart_User_whoami = os.system("whoami")
        Standart_User = input("\n\nStandart User is" + os.system("whoami") + "?\n\n")
        print("Apache owner is "+ Standart_User) 
    
    else:
        print("You entered an unspecified value. You need to use Y or N. Start again...")
        Standart_User = NULL

    if Standart_User_Is_Whoami == "y" or Standart_User_Is_Whoami == "Y" or Standart_User != NULL:
        
        # Установка PHP
        os.system("sudo yum install php php-mysql")
        os.system("sudo systemctl restart httpd.service")

        # Установка владельца Apache
        os.system("sudo chown -R " + Standart_User + "/var/www/html/")

        #Создание файлика info.php
        os.system("cp info.php /var/www/html/info.php")
        
        # Получить информацию о php
        os.system("Apache Info: >> Info")
        os.system("""ip a | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1 >> Info""")
        os.system("hostname -I >> Info\n\n\n")

        # http://your_server_IP_address/info.php



        print(''' \n\nend of install PHP\n\n''')
        ### definitions of what needs to be installed

if ('1' in CentOS_7_Mass_Install[0]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[0]):
    Install_PHP()

elif ('3' in CentOS_7_Mass_Install[0]):
    print('Zabbix')



if ('1' in CentOS_7_Mass_Install[1]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[1]):
    Install_PHP()

elif ('3' in CentOS_7_Mass_Install[1]):
    print("go to install Zabbix_2")    



if ('1' in CentOS_7_Mass_Install[2]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[2]):
    Install_PHP()

elif ('3' in CentOS_7_Mass_Install[2]):
    print("go to install Zabbix_3")  

# Создай try, чтобы выводилось красиво, а не фигня в конце. Там выводится line 80 в ауте range
