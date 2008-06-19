%define name amigadepacker
%define version 0.03
%define release %mkrel 2

Summary: Uncompressor for various AmigaOS formats
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: File tools
Url: http://zakalwe.fi/~shd/foss/amigadepacker/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Amigadepacker uncompresses various compression formats used on
AmigaOS. The supported formats are PowerPacker, XPK SQSH, and
MMCMP. It can also decrypt PowerPacker encrypted data files.

%prep
%setup -q
chmod 644 README ChangeLog COPYING*

%build
%configure
%make CFLAGS="%optflags"
%check
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
install -m 755 %name %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
install -m 644 %name.1 %buildroot%_mandir/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING*
%_bindir/%name
%_mandir/man1/%name.1*
