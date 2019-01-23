Name:      	x48
Summary:   	x48 is an HP 48 GX emulator
Version:   	0.4.2
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

%files
/etc/X11/app-defaults/X48
/usr/X11R6/bin/x48
/usr/X11R6/bin/dump2rom
/usr/X11R6/bin/checkrom
/usr/X11R6/bin/mkcard

