import os

def Config_reni_php71_repo():

    TXT_config_reni_php71_repo ='''# This repository only provides PHP 7.1 and its extensions
# NOTICE: common dependencies are in "remi-safe"

[remi-php71]
name=Remi's PHP 7.1 RPM repository for Enterprise Linux 7 - $basearch
#baseurl=http://rpms.remirepo.net/enterprise/7/php71/$basearch/
#mirrorlist=https://rpms.remirepo.net/enterprise/7/php71/httpsmirror
mirrorlist=http://cdn.remirepo.net/enterprise/7/php71/mirror
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-remi

[remi-php71-debuginfo]
name=Remi's PHP 7.1 RPM repository for Enterprise Linux 7 - $basearch - debuginfo
baseurl=http://rpms.remirepo.net/enterprise/7/debug-php71/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-remi

[remi-php71-test]
name=Remi's PHP 7.1 test RPM repository for Enterprise Linux 7 - $basearch
#baseurl=http://rpms.remirepo.net/enterprise/7/test71/$basearch/
#mirrorlist=https://rpms.remirepo.net/enterprise/7/test71/httpsmirror
mirrorlist=http://cdn.remirepo.net/enterprise/7/test71/mirror
enabled=0
gpgcheck=1 '''
    os.system("echo TXT_config_reni_php71_repo > /etc/yum.repos.d/remi-php71.repo/etc/yum.repos.d/remi-php71.repo")
