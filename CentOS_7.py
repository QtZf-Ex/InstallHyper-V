from ast import In
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

    # Получить имя хоста
    os.system("ip a | grep eth0 >> Info")
    os.system("#curl -4 hostname.com >> Info")
    os.system("hostname -I >> Info")
    print(''' \n\nend of install Apache\n\n''')

def Install_PHP():
    print(''' \n\nInstall PHP\n\n''')
    Standart_User = input('''\n\nStandart User is? (root)\n\n''')
    print(Standart_User) 
    print(Standart_User) 
    print(Standart_User) 
    print(Standart_User) 
    print(Standart_User) 
    print(Standart_User) 
    print(Standart_User) 
    



    # Установка PHP
    os.system("sudo yum install php php-mysql")
    os.system("sudo systemctl restart httpd.service")
    
    # Установка владельца Apache
    Info_PHP = "<?php phpinfo(); ?>"
    os.system("sudo chown -R " + Standart_User + "/var/www/html/")
    os.system("echo " + Info_PHP +" >> /var/www/html/info.php >>")

    os.system("""ip a | grep eth0 | grep inet | awk '{print $2}' | cut -d"/" -f1""")

#    http://your_server_IP_address/info.php

def Install_MariaDB():

    os.system("sudo yum install mariadb-server")
    os.system("sudo systemctl start mariadb")
    os.system("sudo systemctl enable mariadb.service")
    os.system("sudo mysql_secure_installation")
    os.system("")
    os.system("")
    os.system("")




    print(''' \n\nend of install PHP\n\n''')
### definitions of what needs to be installed

if ('1' in CentOS_7_Mass_Install[0]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[0]):
    Install_MariaDB()

elif ('3' in CentOS_7_Mass_Install[0]):
    Install_PHP()



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
