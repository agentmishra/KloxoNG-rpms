%define repohost repos.kloxong.org
%define mirrorhost raw.githubusercontent.com/KloxoNGCommunity/KloxoNG-rpms/dev/kloxong/mirror
Summary: KloxoNG release file and package configuration
Name: kloxong-release
Version: 0.1.0
Release: 1
License: AGPLV3
Group: System Environment/Base
URL: http://kloxong.org/

BuildArch: noarch
Packager: John Parnell Pierce <john@luckytanuki.com>
Vendor: Kloxo Next Generation Repository, http://%{repohost}/
#BuildRequires: redhat-rpm-config
Obsoletes: mratwork-release
Conflicts: mratwork-testing

%description
Kloxo Next Generation rpm release. This package contains yum configuration for the Kloxo Next Generation RPM Repository.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/yum.repos.d/

cat > %{buildroot}/%{_sysconfdir}/yum.repos.d/kloxong.repo << _EOF_
[kloxong-release-neutral-noarch]
name=KloxoNG - release-neutral-noarch
baseurl=http://%{repohost}/repo/kloxong/release/neutral/noarch/
mirrorlist=https://%{mirrorhost}/kloxong-release-neutral-noarch-mirrors.txt
enabled=1
gpgcheck=0

[kloxong-release-neutral-arch]
name=KloxoNG - release-neutral-arch
baseurl=http://%{repohost}/repo/kloxong/release/neutral/\$basearch/
mirrorlist=https://%{mirrorhost}/kloxong-release-neutral-\$basearch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-release-version-noarch]
name=KloxoNG - release-version-noarch
baseurl=http://%{repohost}/repo/kloxong/release/centos\$releasever/noarch/
mirrorlist=https://%{mirrorhost}/kloxong-release-centos\$releasever-noarch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-release-version-arch]
name=KloxoNG - release-version-arch
baseurl=http://%{repohost}/repo/kloxong/release/centos\$releasever/\$basearch/
mirrorlist=https://%{mirrorhost}/kloxong-release-centos\$releasever-\$basearch-mirrors.txt
enabled=1
gpgcheck=0

[kloxong-testing-neutral-noarch]
name=KloxoNG - testing-neutral-noarch
baseurl=http://%{repohost}/repo/kloxong/testing/neutral/noarch/
mirrorlist=https://%{mirrorhost}/mratwork-testing-neutral-noarch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-testing-neutral-arch]
name=KloxoNG - testing-neutral-arch
baseurl=http://%{repohost}/repo/kloxong/testing/neutral/\$basearch/
mirrorlist=https://%{mirrorhost}/mratwork-testing-neutral-\$basearch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-testing-version-noarch]
name=KloxoNG - testing-version-noarch
baseurl=http://%{repohost}/repo/kloxong/testing/centos\$releasever/noarch/
mirrorlist=https://%{mirrorhost}/mratwork-testing-centos\$releasever-noarch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-testing-version-arch]
name=KloxoNG - testing-version-arch
baseurl=http://%{repohost}/repo/kloxong/testing/centos\$releasever/\$basearch/
mirrorlist=https://%{mirrorhost}/mratwork-testing-centos\$releasever-\$basearch-mirrors.txt
enabled=0
gpgcheck=0

[kloxong-srpms]
name=KloxoNG - srpms
baseurl=http://%{repohost}/repo/kloxong/SRPMS/
mirrorlist=https://%{mirrorhost}/mratwork-SRPMS-mirrors.txt
enabled=0
gpgcheck=0

# ==================================

[kloxong-ius-stable]
name=KloxoNG - IUS Community Packages for EL \$releasever (stable) - arch
baseurl=http://dl.iuscommunity.org/pub/ius/stable/CentOS/\$releasever/\$basearch
mirrorlist=http://mirrors.iuscommunity.org/mirrorlist/?repo=ius-centos\$releasever&arch=\$basearch&protocol=http
enabled=1
gpgcheck=0
exclude=mysql51* mysql56*

[kloxong-ius-archive]
name=KloxoNG - IUS Community Packages for EL \$releasever (archive) - arch
baseurl=http://dl.iuscommunity.org/pub/ius/archive/CentOS/\$releasever/\$basearch
mirrorlist=http://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos\$releasever-archive&arch=\$basearch&protocol=http
enabled=1
gpgcheck=0
exclude=mysql51* mysql56*

[kloxong-ius-testing]
name=KloxoNG - IUS Community Packages for EL \$releasever (testing) - arch
baseurl=http://dl.iuscommunity.org/pub/ius/testing/CentOS/\$releasever/\$basearch
mirrorlist=http://mirrors.iuscommunity.org/mirrorlist?repo=ius-centos\$releasever-testing&arch=\$basearch&protocol=http
enabled=0
gpgcheck=0
exclude=mysql51* mysql56*

# ==================================

# for Webtatic
[kloxong-webtatic]
name=KloxoNG - Webtatic for CentOS \$releasever - \$basearch
baseurl=http://repo.webtatic.com/yum/el\$releasever/\$basearch
mirrorlist=http://mirror.webtatic.com/yum/el\$releasever/\$basearch/mirrorlist
enabled=1
gpgcheck=0
exclude=mysql* nginx*

[kloxong-webtatic-archive]
name=KloxoNG - Webtatic for CentOS \$releasever Archive - \$basearch
baseurl=http://repo.webtatic.com/yum/el\$releasever-archive/\$basearch
mirrorlist=http://mirror.webtatic.com/yum/el\$releasever-archive/\$basearch/mirrorlist
enabled=0
gpgcheck=0
exclude=mysql* nginx*

[kloxong-webtatic-testing]
name=KloxoNG - Webtatic for CentOS \$releasever Testing - \$basearch
baseurl=http://repo.webtatic.com/yum/el\$releasever/\$basearch
mirrorlist=http://mirror.webtatic.com/yum/el\$releasever-testing/\$basearch/mirrorlist
enabled=0
gpgcheck=0
exclude=mysql* nginx*


# ==================================

[kloxong-remi]
name=KloxoNG - Les RPM de remi pour Enterprise Linux \$releasever - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/remi/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/remi/mirror
enabled=0
gpgcheck=0
includepkgs=php-ffmpeg php-ioncube-loader

[kloxong-remi-php55]
name=KloxoNG - Les RPM de remi de PHP 5.5 pour Enterprise Linux \$releasever - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/php55/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/php55/mirror
enabled=0
gpgcheck=0
includepkgs=php-ffmpeg php-ioncube-loader

[kloxong-remi-php56]
name=KloxoNG - Les RPM de remi de PHP 5.6 pour Enterprise Linux 6 - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/php56/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/php56/mirror
enabled=0
gpgcheck=0
includepkgs=php-ffmpeg php-ioncube-loader

[kloxong-remi-php70]
name=KloxoNG - Les RPM de remi de PHP 7.0 pour Enterprise Linux 6 - arch
baseurl=http://rpms.famillecollet.com/enterprise/\$releasever/php70/\$basearch/
mirrorlist=http://rpms.famillecollet.com/enterprise/\$releasever/php70/mirror
enabled=0
gpgcheck=0
includepkgs=php-ffmpeg php-ioncube-loader

# ==================================

[kloxong-epel]
name=KloxoNG - Extra Packages for EL \$releasever - arch
baseurl=http://download.fedoraproject.org/pub/epel/\$releasever/\$basearch
mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=epel-\$releasever&arch=\$basearch
enabled=1
gpgcheck=0
exclude=postfix* exim* ssmtp* pdns*

# ==================================

# for varnish
[kloxong-varnish]
name=KloxoNG - Varnish for EL \$releasever - arch
baseurl=https://packagecloud.io/varnishcache/varnish51/el/\$releasever/\$basearch
enabled=1
gpgcheck=0

# ==================================

# for hiawatha
[kloxong-centosec]
name=KloxoNG - CentOS \$releasever Packages from CentOS.EC
baseurl=http://centos\$releasever.ecualinux.com/\$basearch
enabled=0
gpgcheck=0
exclude=cairo*

# ==================================

# for nginx
[kloxong-nginx]
name=Kloxo-MR - nginx repo
baseurl=http://nginx.org/packages/mainline/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0

# for nginx-stable
[kloxong-nginx-stable]
name=Kloxo-MR - nginx-stable repo
baseurl=http://nginx.org/packages/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0

# ==================================

# for mariadb
[kloxong-mariadb]
name=Kloxo-MR - mariadb 32bit repo
baseurl=http://yum.mariadb.org/10.0/centos/\$releasever/\$basearch/
enabled=1
gpgcheck=0

# ==================================

# for atrpms
[kloxong-atrpms]
name=Kloxo-MR - Fedora Core \$releasever - $basearch - ATrpms
baseurl=http://dl.atrpms.net/el\$releasever-\$basearch/atrpms/stable
enabled=0
gpgcheck=0
exclude=clam*

# ==================================

# for litespeed
[kloxong-litespeed]
name=KloxoNG - LiteSpeed Tech Repository for CentOS \$releasever - \$basearch
baseurl=http://rpms.litespeedtech.com/centos/\$releasever/\$basearch/
#failovermethod=priority
enabled=0
gpgcheck=0

[kloxong-litespeed-update]
name=KloxoNG - LiteSpeed Tech Repository for CentOS \$releasever - \$basearch
baseurl=http://rpms.litespeedtech.com/centos/\$releasever/update/\$basearch/
#failovermethod=priority
enabled=0
gpgcheck=0

# ==================================

# for mod-pagespeed
[kloxong-google-mod-pagespeed]
name=KloxoNG - google-mod-pagespeed
baseurl=http://dl.google.com/linux/mod-pagespeed/rpm/stable/\$basearch
enabled=1
gpgcheck=0

# ==================================

# for mod_mono
[kloxong-mod-mono]
name=KloxoNG - mod_mono
baseurl=http://download.mono-project.com/repo/centos/
enabled=0
gpgcheck=0

# ==================================

# for CentOS kernel
[kloxong-centos-kernel]
name=KloxoNG - CentOS kernel
baseurl=http://elrepo.org/linux/kernel/el\$releasever/\$basearch
enabled=0
gpgcheck=0

# ==================================

# for RSysLog
[kloxong-rsyslog-v8-devel]
name=KloxoNG - Adiscon Rsyslog v8-devel for CentOS-\$releasever-\$basearch
baseurl=http://rpms.adiscon.com/v8-devel/epel-\$releasever/\$basearch
enabled=0
gpgcheck=0

[kloxong-rsyslog-v8-stable]
name=KloxoNG - Adiscon Rsyslog v8-stable for CentOS-\$releasever-\$basearch
baseurl=http://rpms.adiscon.com/v8-stable/epel-\$releasever/\$basearch
enabled=0
gpgcheck=0

# ==================================

[kloxong-zfs]
name=KloxoNG - ZFS on Linux for EL \$releasever
baseurl=http://archive.zfsonlinux.org/epel/\$releasever/\$basearch/
enabled=0
gpgcheck=0

# ==================================

[kloxong-gleez]
name=KloxoNG - Gleez repo for CentOS-\$releasever-\$basearch
baseurl=http://yum.gleez.com/\$releasever/\$basearch/
enabled=0
gpgcheck=0
includepkgs=hhvm*

# ==================================

[kloxong-ulyaoth]
name=KloxoNG - Ulyaoth Repository
baseurl=http://repos.ulyaoth.net/centos/\$releasever/\$basearch/os/
enabled=0
gpgcheck=0

# ==================================

[kloxong-rpmforge]
name=KloxoNG - RHEL \$releasever - RPMforge.net - dag
baseurl=http://apt.sw.be/redhat/el\$releasever/en/\$basearch/rpmforge
mirrorlist=http://apt.sw.be/redhat/el\$releasever/en/mirrors-rpmforge
enabled=0
gpgcheck=0

[kloxong-rpmforge-extras]
name=KloxoNG - RHEL \$releasever - RPMforge.net - extras
baseurl=http://apt.sw.be/redhat/el\$releasever/en/\$basearch/extras
mirrorlist=http://apt.sw.be/redhat/el\$releasever/en/mirrors-rpmforge-extras
enabled=0
gpgcheck=0

_EOF_

%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo-mr.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxomr.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/kloxo-custom.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/lxcenter.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/lxlabs.repo
%{__rm} -rf %{_sysconfdir}/yum.repos.d/mratwork.repo
%{__cp} -f %{buildroot}/%{_sysconfdir}/yum.repos.d/kloxong.repo %{_sysconfdir}/yum.repos.d/kloxong.repo.repo

%clean

%post

%files
%defattr(-, root, root, 0755)
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/mratwork.repo

%changelog
* Mon Jan 29 2018 John Parnell Pierce <john@luckytanuki.com> 
- rebrand to Kloxo Next Generation
- change product name to kloxong
- add obsolete for kloxomr 
- change MRatWork to kloxong

* Mon Dec 16 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 0.0.1-1
- first release
