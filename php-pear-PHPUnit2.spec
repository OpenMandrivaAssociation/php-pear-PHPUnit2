%define		_class		PHPUnit2
%define		_status		stable
%define		_pearname	%{_class}

%define		_requires_exceptions pear(%s.php)

Summary:	%{_pearname} - regression testing framework for unit tests
Name:		php-pear-%{_pearname}
Version:	2.2.1
Release:	%mkrel 5
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/PHPUnit2/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
%define		_noautoreq	'pear(%s.php)'

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/ .

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{Extensions/{Log,CodeCoverage,TestDox},Framework,Runner,Tests/{Extensions/TestDox,Framework,Runner},TextUI,Util}

install %{_pearname}-%{version}/Extensions/*.php %{buildroot}%{_datadir}/pear/%{_class}/Extensions
install %{_pearname}-%{version}/Extensions/Log/*.php %{buildroot}%{_datadir}/pear/%{_class}/Extensions/Log
install %{_pearname}-%{version}/Extensions/CodeCoverage/*.php %{buildroot}%{_datadir}/pear/%{_class}/Extensions/CodeCoverage
install %{_pearname}-%{version}/Extensions/TestDox/*.php %{buildroot}%{_datadir}/pear/%{_class}/Extensions/TestDox
install %{_pearname}-%{version}/Framework/*.php %{buildroot}%{_datadir}/pear/%{_class}/Framework
install %{_pearname}-%{version}/Runner/*.php %{buildroot}%{_datadir}/pear/%{_class}/Runner
install %{_pearname}-%{version}/Tests/*.php %{buildroot}%{_datadir}/pear/%{_class}/Tests
install %{_pearname}-%{version}/Tests/Extensions/*.php %{buildroot}%{_datadir}/pear/%{_class}/Tests/Extensions/
install %{_pearname}-%{version}/Tests/Extensions/TestDox/*.php %{buildroot}%{_datadir}/pear/%{_class}/Tests/Extensions/TestDox/
install %{_pearname}-%{version}/Tests/Framework/*.php %{buildroot}%{_datadir}/pear/%{_class}/Tests/Framework
install %{_pearname}-%{version}/Tests/Runner/*.php %{buildroot}%{_datadir}/pear/%{_class}/Tests/Runner
install %{_pearname}-%{version}/TextUI/*.php %{buildroot}%{_datadir}/pear/%{_class}/TextUI
install %{_pearname}-%{version}/Util/*.php %{buildroot}%{_datadir}/pear/%{_class}/Util

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{_pearname}.xml


