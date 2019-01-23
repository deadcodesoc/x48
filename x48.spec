%define x11_prefix      /usr/X11R6
Name:      	x48
Summary:   	x48 is an HP 48 GX emulator
Version:   	0.4.3
Release:  	1
Copyright: 	GPL
Group:     	Applications/Math
URL:            https://sourceforge.net/projects/x48/
Source:    	x48-%{version}.tar.gz
#Patch:    	x48.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires:  	readline

%description
 This is an emulator of the HP 48 SX and GX calculator.
 Romdumps are available from http://x48.berlios.de/

%prep
%setup -q

%build
xmkmf
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

mkdir ${RPM_BUILD_ROOT}/usr/share/doc/x48-${VERSION}

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%doc	README
	%{x11_prefix}/bin/x48
	%{x11_prefix}/bin/dump2rom
	%{x11_prefix}/bin/checkrom
	%{x11_prefix}/bin/mkcard
	%{x11_prefix}/man/*
	/etc/X11/app-defaults/X48


