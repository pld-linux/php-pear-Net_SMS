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
Version:	0.0.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3d9f94258a133b3855b00e0f3fec8c7f
URL:		http://pear.php.net/package/Net_SMS/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides SMS functionality and access to SMS gateways.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza obs³ugê SMS jak i bramek do wysy³ania wiadomo¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
