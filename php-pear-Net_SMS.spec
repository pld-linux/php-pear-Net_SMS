# TODO:
# - fix pl description (it's ugly)
%define		status		beta
%define		pearname	Net_SMS
Summary:	%{pearname} - SMS functionality
Summary(pl.UTF-8):	%{pearname} - obsługa SMS
Name:		php-pear-%{pearname}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	348ede2d6bbfe9cc7bd0ddf9c817d03e
URL:		http://pear.php.net/package/Net_SMS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 4.2.0
Requires:	php(gettext)
Requires:	php-pear
Suggests:	php-pear-HTTP_Request2
Suggests:	php-pear-Mail
Suggests:	php-pear-Net_SMPP_Client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear HTTP/Request2.*

%description
This package provides SMS functionality and access to SMS gateways.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarcza obsługę SMS jak i bramek do wysyłania wiadomości.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_SMS/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc README install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/SMS.php
%{php_pear_dir}/Net/SMS
