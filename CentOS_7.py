from main import *
from PHP_Config_V71 import *
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
    # Подключение репозитория + его установка
    os.system("sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
    os.system("sudo rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm")
    
    # Использование функции Config_reni_php71_repo из PHP_Config_V71
    os.system(Config_reni_php71_repo)
    
    
    os.system("sudo yum update -y")
    os.system("sudo yum install php php-fpm php-gd php-mysql -y")
    os.system("sudo systemctl restart php-fpm -y")
    os.system("sudo systemctl status php")
    print(''' \n\nend of install PHP\n\n''')
### definitions of what needs to be installed

if ('1' in CentOS_7_Mass_Install[0]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[0]):
    Install_PHP()

elif ('3' in CentOS_7_Mass_Install[0]):
    print ("go to install Zabbix")



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
