from re import I
from tkinter import N, NE
from main import *
import os

CentOS_7_Mass_Install = CentOS_7_Mass_Install.split()

# Просмотр выбранных пунктов 
print("You have chosen: ", CentOS_7_Mass_Install)


# Настройка Firewalld 
# Настройка Iptables https://github.com/ZaDr0t-sys/InstallHyper-V

### def funcs to install Apache v2, PHP v7, Zabbix 


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

    Standart_User = os.system("whoami")

    # Установка PHP
    os.system("sudo yum install php php-mysql")
    os.system("sudo systemctl restart httpd.service")

    # Установка владельца Apache
    os.system("sudo chown -R " + str(Standart_User) + "/var/www/html/")

    #Создание файлика info.php
    os.system("cp info.php /var/www/html/info.php")
        
    # Получить информацию о php
    os.system("Apache Info: >> Info")
    os.system("""ip a | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1 >> Info""")
    os.system("hostname -I >> Info\n\n\n")

    # http://your_server_IP_address/info.php

    print(''' \n\nend of install PHP\n\n''')
    ### definitions of what needs to be installed

    def Install_Iptables():
        if os.system(" systemctl | grep firewalld | wc -l") >= 1:
            print("Iptables Установлен")
            Need_Install_Config = input("Настроить конфиг? y/n?")
            if Need_Install_Config == "y" or Need_Install_Config == "Y":
                print("Установка")
            elif Need_Install_Config == "n" or Need_Install_Config == "N":
                print("Завершение")
            else:
                print("Введите корректное значение y/n")
                return Install_Iptables()
        elif os.system(" systemctl | grep firewalld | wc -l") == 0:
            print("Iptables не установлен")
            os.system("sudo yum install iptables-services -y")
            os.system("sudo systemctl start iptables")
            os.system("sudo systemctl enable iptables")
            



try:

    if ('1' in CentOS_7_Mass_Install[0]):
        Install_Apache()

    elif ('2' in CentOS_7_Mass_Install[0]):
        Install_PHP()

    elif ('3' in CentOS_7_Mass_Install[0]):
        print('https://www.zabbix.com/ru/download?zabbix=6.2&os_distribution=centos&os_version=7&components=proxy&db=mysql&ws=')
    
    elif ('4' in CentOS_7_Mass_Install[0]):
        Install_Iptables()



    if ('1' in CentOS_7_Mass_Install[1]):
        Install_Apache()

    elif ('2' in CentOS_7_Mass_Install[1]):
        Install_PHP()

    elif ('3' in CentOS_7_Mass_Install[1]):
        print("https://www.zabbix.com/ru/download?zabbix=6.2&os_distribution=centos&os_version=7&components=proxy&db=mysql&ws=")    



    if ('1' in CentOS_7_Mass_Install[2]):
        Install_Apache()

    elif ('2' in CentOS_7_Mass_Install[2]):
        Install_PHP()

    elif ('3' in CentOS_7_Mass_Install[2]):
        print("https://www.zabbix.com/ru/download?zabbix=6.2&os_distribution=centos&os_version=7&components=proxy&db=mysql&ws=")  
except:
    print("End...")

# Создай try, чтобы выводилось красиво, а не фигня в конце. Там выводится line 80 в ауте range
