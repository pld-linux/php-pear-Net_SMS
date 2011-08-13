# TODO:
# - fix pl description (it's ugly)
%define		status		beta
%define		pearname	Net_SMS
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - SMS functionality
Summary(pl.UTF-8):	%{pearname} - obsługa SMS
Name:		php-pear-%{pearname}
Version:	0.2.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	b5050c69a7967361e630d0483788e7c4
URL:		http://pear.php.net/package/Net_SMS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-common >= 3:4.2.0
Requires:	php-gettext
Requires:	php-pear
Suggests:	php-pear-HTTP_Request
Suggests:	php-pear-Mail
Suggests:	php-pear-Net_SMPP_Client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTTP/Request.*)' 'pear(Mail.*)' pear(Net/SMPP/Client.*)

%description
This package provides SMS functionality and access to SMS gateways.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ten pakiet dostarcza obsługę SMS jak i bramek do wysyłania wiadomości.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
%{php_pear_dir}/Net/SMS
