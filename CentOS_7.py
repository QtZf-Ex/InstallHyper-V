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
    

def Install_PHP():
    os.system("sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
    os.system("sudo rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm")
    os.system("vi /etc/yum.repos.d/remi-php71.repo")
    f = open('/etc/yum.repos.d/remi-php71.repo', 'w')
    
    
    
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")
    os.system("")

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