%define		_class		Gtk2
%define		_subclass	ExceptionDump
%define		_status		stable
%define		_pearname	Gtk2_ExceptionDump
Summary:	%{_pearname} - Analyze exceptions, php and PEAR errors visually
Summary(pl.UTF-8):	%{_pearname} - wizualna analiza wyjątków oraz błędów php i PEAR-a
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6c20413bc86bfddada2c98bcf44103b0
URL:		http://pear.php.net/package/Gtk2_ExceptionDump/
BuildRequires:	php-pear-PEAR >= 1:1.4.8
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-15
Requires:	php-pear-Gtk2_VarDump >= 0.2.0
Requires:	php-pear-Gtk2_VarDump >= 1.0.0
Requires:	php-pear-PEAR-core >= 1:1.4.8
Requires:	php-gtk2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Displays Exceptions, PHP Errors and PEAR_Error objects in a nice and
clean way. It also allows to inspect parameters passed to methods and
to drag and drop the files causing the error to any editor. Copying a
string representation of the exception to clipboard is also supported.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa wyświetla wyjątki, błędy PHP i obiekty PEAR_Error w ładny i
przejrzysty sposób. Pozwala także obejrzeć parametry przekazane
metodom i przeciągać pliki powodujące błędy do dowolnego edytora.
Obsługiwane jest także kopiowanie do schowka reprezentacji znakowej
wyjątku.

Ta klasa ma w PEAR status: %{_status}.

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
