%define name amigadepacker
%define version 0.04
%define release 4

Summary: Uncompressor for various AmigaOS formats
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: File tools
Url: https://zakalwe.fi/~shd/foss/amigadepacker/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Amigadepacker uncompresses various compression formats used on
AmigaOS. The supported formats are PowerPacker, XPK SQSH, and
MMCMP. It can also decrypt PowerPacker encrypted data files.

%prep
%setup -q
chmod 644 README ChangeLog COPYING*

%build
./configure
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


%changelog
* Sun Aug 28 2011 Götz Waschk <waschk@mandriva.org> 0.04-3mdv2012.0
+ Revision: 697266
- rebuild

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 0.04-2mdv2011.0
+ Revision: 421402
- fix build

* Mon Aug 25 2008 Götz Waschk <waschk@mandriva.org> 0.04-1mdv2009.0
+ Revision: 275670
- new version
- update license

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 226152
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Götz Waschk <waschk@mandriva.org>
    - fix URL

* Sat Oct 20 2007 Götz Waschk <waschk@mandriva.org> 0.03-1mdv2008.1
+ Revision: 100597
- new version

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0.02-2mdv2008.0
+ Revision: 55216
- Import amigadepacker

