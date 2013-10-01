%define		status		stable
%define		pearname	PHP_Depend
%include	/usr/lib/rpm/macros.php
Summary:	PHP_Depend design quality metrics for PHP packages
Name:		php-pdepend-PHP_Depend
Version:	1.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.pdepend.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	a639153c9d24316ffadd8fff6df0123b
URL:		http://pear.pdepend.org/package/PHP_Depend/
BuildRequires:	php-channel(pear.pdepend.org)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-channel(pear.pdepend.org)
Requires:	php-pear
Suggests:	php-pecl-imagick
Obsoletes:	php-pdepend-PHP-Depend
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Depend is an adaption of the Java design quality metrics software
JDepend and the NDepend metric tool.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup
mv docs/PHP_Depend/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/pdepend
%{php_pear_dir}/PHP/Depend.php
%{php_pear_dir}/PHP/Depend
