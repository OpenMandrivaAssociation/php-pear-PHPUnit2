%define		_class		PHPUnit2
%define		upstream_name	%{_class}
%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	2.3.6
Release:	6
Summary:	Regression testing framework for unit tests

License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHPUnit2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/ .

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_bindir}/phpunit
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


