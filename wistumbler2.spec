Summary:	Wireless network sniffer
Summary(pl):	Sniffer sieci bezprzewodowych
Name:		wistumbler2
Version:	00
Release:	0.pre3.1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.nopcode.org/prj/wistumbler2/%{name}.%{version}-pre3.tar.gz
# Source0-md5:	922da338af586c24d81cdd87b2020c0e
URL:		http://www.nopcode.org/?t=wistumbler2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}.%{version}-pre3

%build
env PREFIX=%{_prefix} USE_GTK=1 \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}}

%{__make} install \
	INSTGRP=$(id -g) \
	MANGRP=$(id -g) \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	ETC=$RPM_BUILD_ROOT%{_sysconfdir} \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	SHARE=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	MAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* CHANGELOG FAQ README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/%{name}*
