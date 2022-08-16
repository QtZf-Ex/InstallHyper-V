from main import *
import os

CentOS_7_Mass_Install = CentOS_7_Mass_Install.split()

print(CentOS_7_Mass_Install[0])
print(len(CentOS_7_Mass_Install))
print(CentOS_7_Mass_Install)

# Настройка Firewalld 
# Настройка Iptables https://github.com/ZaDr0t-sys/InstallHyper-V

### def func to install Apache v2, PHP v7, Zabbix 


def Install_Apache():
    os.system("sudo yum update && sudo yum upgrade -y")
    os.system("sudo yum update httpd")
    os.system("sudo yum install httpd")

    # Открыть порт 90 и 443 http https + reload firewalld 
    os.system("sudo firewall-cmd --permanent --add-service=http")
    os.system("sudo firewall-cmd --permanent --add-service=https")
    os.system("sudo firewall-cmd --reload")

    # Запуск + проверить статус httpd
    os.system("sudo systemctl start httpd")
    os.system("sudo systemctl status httpd")
    
    # Получить имя хоста
    os.system("hostname -I")

    # curl -4 icanhazip.com Также в качестве альтернативы вы можете использовать curl для запроса IP-адреса icanhazip.com, который предоставит вам ваш публичный IPv4-адрес, видимый в другом месте в Интернете:
    
    # автозапуск 
    os.system("sudo systemctl enable httpd")

### definitions of what needs to be installed

if ('1' in CentOS_7_Mass_Install[0]):
    Install_Apache()

elif ('2' in CentOS_7_Mass_Install[0]):
    print ("go to install PHP")

elif ('3' in CentOS_7_Mass_Install[0]):
    print ("go to install Zabbix")


if ('1' in CentOS_7_Mass_Install[1]):
    print("go to install Apache_2")

elif ('2' in CentOS_7_Mass_Install[1]):
    print("go to install PHP_2")

elif ('3' in CentOS_7_Mass_Install[1]):
    print("go to install Zabbix_2")    


if ('1' in CentOS_7_Mass_Install[2]):
    print("go to install Apache_3")

elif ('2' in CentOS_7_Mass_Install[2]):
    print("go to install PHP_3")

elif ('3' in CentOS_7_Mass_Install[2]):
    print("go to install Zabbix_3")  