%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	ExceptionDump
%define		_status		beta
%define		_pearname	Gtk2_ExceptionDump
Summary:	%{_pearname} - Analyze exceptions, php and PEAR errors visually
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	472d43e96c10ccacae3a306095711d61
URL:		http://pear.php.net/package/Gtk2_ExceptionDump/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-15
Requires:	php-pear-Gtk2_VarDump >= 0.2.0
Requires:	php-pear-PEAR >= 1:1.4.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays Exceptions, PHP Erros and PEAR_Error objects in a nice and
clean way. It also allows to inspect parameters passed to methods and
to drag and drop the files causing the error to any editor. Copying a
string representation of the exception to clipboard is also supported.

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Gtk2/ExceptionDump
%{php_pear_dir}/Gtk2/ExceptionDump/InfoBox.php
%{php_pear_dir}/Gtk2/ExceptionDump/Stack.php
%{php_pear_dir}/Gtk2/ExceptionDump/StackModel.php
%{php_pear_dir}/Gtk2/ExceptionDump.php
