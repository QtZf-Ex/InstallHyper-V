### git clone https://github.com/ZaDr0t-sys/InstallHyper-V


print ('''
You need to chose Your OS

[+] (1) CentOS 7
[+] (2) CentOS 8
[+] (3) Debian 8
[+] (4) Debian 9
[+] (5) Debian 10

''')
ChooseOS = input()

if ChooseOS == "1":
    print ('''
    You selected CentOS 7
    Please write what you need to install
    Write only number. Example: 
    $1 2 3      ### Install Apache + PHP + Zabbix
    $1 3        ### Install Apache + Zabbix
    $3 2        ### Install Zabbix + PHP 

    [+] (1) Apache      # Install Apache version 2
    [+] (2) PHP         # Install PHP version 7
    [+] (3) Zabbix      # Install Zabbix last version

    ''')
    CentOS_7_Mass_Install = input()
    

if ChooseOS == "2":
    
    print ('''
    You selected CentOS 8
    Please write what you need to install

    [+] Apache      # Install Apache version 2
    [+] PHP         # Install PHP version 7
    [+] Zabbix      # Install Zabbix last version

    ''')
    
    CentOS_8_Mass_Install = input()

if ChooseOS == 3:
    
    print ('''
    You selected CentOS 8
    Please write what you need to install

    [+] Apache      # Install Apache version 2
    [+] PHP         # Install PHP version 7
    [+] Zabbix      # Install Zabbix last version

    ''')
    
    Debian_8_Mass_Install = input()

if ChooseOS == 4:
    
    print ('''
    You selected Debian 9
    Please write what you need to install

    [+] Apache      # Install Apache version 2
    [+] PHP         # Install PHP version 7
    [+] Zabbix      # Install Zabbix last version

    ''')
    
    Debian_9_Mass_Install = input()

if ChooseOS == 5:
    
    print ('''
    You selected Debian 10
    Please write what you need to install

    [+] Apache      # Install Apache version 2
    [+] PHP         # Install PHP version 7
    [+] Zabbix      # Install Zabbix last version

    ''')
    
    Debian_10_Mass_Install = input()