# ToDo:
# - fix pl description (it's ugly)
%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SMS
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - SMS functionality
Summary(pl):	%{_pearname} - obs³uga SMS
Name:		php-pear-%{_pearname}
Version:	0.0.2
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9d1c20d30a2dee07e7c2d0fe380650cd
URL:		http://pear.php.net/package/Net_SMS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-gettext
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTTP/Request.*)' 'pear(Mail.*)'

%description
This package provides SMS functionality and access to SMS gateways.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza obs³ugê SMS jak i bramek do wysy³ania wiadomo¶ci.

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
