%define		_class		PHPUnit2
%define		upstream_name	%{_class}

%define		_requires_exceptions pear(%s.php)

Name:		php-pear-%{upstream_name}
Version:	2.3.6
Release:	%mkrel 4
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHPUnit2 is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at http://www.junit.org/ .

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_bindir}/phpunit
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-4mdv2012.0
+ Revision: 742181
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-3
+ Revision: 679560
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.6-2mdv2011.0
+ Revision: 613753
- the mass rebuild of 2010.1 packages

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.6-1mdv2010.1
+ Revision: 478812
- update to new version 2.3.6

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-6mdv2010.1
+ Revision: 467959
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-5mdv2007.0
+ Revision: 82511
- Import php-pear-PHPUnit2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-1mdk
- 2.2.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdk
- initial Mandriva package (PLD import)

