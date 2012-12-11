Name:		trickle
Version:	1.07
Release:	%mkrel 7
URL:		http://monkey.org/~marius/pages/?page=trickle
Source:		http://monkey.org/~marius/trickle/trickle-%{version}.tar.gz
Source1:	trickled.conf
Summary:	Lightweight userspace bandwidth shaper
Group:		Networking/File transfer
License:	BSD
BuildRequires:	libevent-devel
# patch from debian, overloads fread() and fwrite()
Patch0:		trickle-1.07-deb-fread_fwrite_overload.patch
Patch1:		trickle-1.07-format-strings.patch
Patch2:		trickle-1.07-libdir.patch
Patch3:		trickle-1.07-CVE-2009-0415.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
trickle is a portable lightweight userspace bandwidth shaper. It can
run in collaborative mode (together with trickled) or in stand alone mode.

trickle works by taking advantage of the unix loader preloading.
Essentially it provides, to the application, a new version of the
functionality that is required to send and receive data through sockets.
It then limits traffic based on delaying the sending and receiving of
data over a socket. trickle runs entirely in userspace and does not
require root privileges.

%prep
%setup -q
%apply_patches
touch -r configure aclocal.m4 Makefile.in stamp-h.in

%build
%configure2_5x
# it mistakenly assumes in_addr_t is not defined in <netinet/in.h>
sed -i.in_addr_t -e '/in_addr_t/d' config.h
#gw parallel make considered unsafe
make

%install
rm -rf %{buildroot}

%makeinstall
install -D -m 644 -p %SOURCE1 %buildroot%_sysconfdir/trickled.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE TODO README
%config(noreplace) %_sysconfdir/trickled.conf
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}d
%{_libdir}/%{name}/%{name}-overload.so
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}d.conf.5.*
%{_mandir}/man8/%{name}d.8.*


%changelog
* Tue Feb 01 2011 Götz Waschk <waschk@mandriva.org> 1.07-7mdv2011.0
+ Revision: 634812
- fix library dir to make it work on x86_64 (bug #62362)
- add security patch from Fedora
- add sample config file for trickled

* Wed Dec 22 2010 Oden Eriksson <oeriksson@mandriva.com> 1.07-6mdv2011.0
+ Revision: 623882
- rebuilt against libevent 2.x

* Sun Aug 09 2009 Götz Waschk <waschk@mandriva.org> 1.07-5mdv2010.0
+ Revision: 412353
- fix format string
- spec fixes

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.07-4mdv2009.0
+ Revision: 269438
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Gustavo De Nardin <gustavodn@mandriva.com> 1.07-3mdv2009.0
+ Revision: 218299
- avoid parallel build, it is broken
- removed huge Debian patch, fixing build in a simpler way now, just
  deleting redefinition of in_addr_t in config.h
- P0: fread_fwrite_overload patch, taken from previous Debian patch, seemed
  the only really interesting piece

* Wed May 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.07-2mdv2009.0
+ Revision: 207051
- rebuilt against libevent-1.4.4

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Aug 07 2007 Nicolas Vigier <nvigier@mandriva.com> 1.07-1mdv2008.0
+ Revision: 59939
- Import trickle

