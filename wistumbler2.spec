Summary:	Wireless network sniffer
Summary(pl.UTF-8):	Sniffer sieci bezprzewodowych
Name:		wistumbler2
Version:	00
%define		_pre	pre3
Release:	0.%{_pre}.1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.nopcode.org/prj/wistumbler2/%{name}.%{version}-%{_pre}.tar.gz
# Source0-md5:	922da338af586c24d81cdd87b2020c0e
URL:		http://www.nopcode.org/?t=wistumbler2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wireless network sniffer.

%description -l pl.UTF-8
Sniffer sieci bezprzewodowych.

%prep
%setup -q -n %{name}.%{version}-%{_pre}

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}*
