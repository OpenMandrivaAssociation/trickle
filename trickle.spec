Summary:	Lightweight userspace bandwidth shaper
Name:		trickle
Version:	1.07
Release:	8
Group:		Networking/File transfer
License:	BSD
Url:		http://monkey.org/~marius/pages/?page=trickle
Source0:	http://monkey.org/~marius/trickle/%{name}-%{version}.tar.gz
Source1:	trickled.conf
# patch from debian, overloads fread() and fwrite()
Patch0:		trickle-1.07-deb-fread_fwrite_overload.patch
Patch1:		trickle-1.07-format-strings.patch
Patch2:		trickle-1.07-libdir.patch
Patch3:		trickle-1.07-CVE-2009-0415.patch
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(libtirpc)

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
export LDFLAGS="$LDFLAGS -ltirpc"
%configure2_5x
# it mistakenly assumes in_addr_t is not defined in <netinet/in.h>
sed -i.in_addr_t -e '/in_addr_t/d' config.h

make

%install
%makeinstall
install -D -m 644 -p %SOURCE1 %{buildroot}%{_sysconfdir}/trickled.conf

%files
%doc LICENSE TODO README
%config(noreplace) %{_sysconfdir}/trickled.conf
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}d
%{_libdir}/%{name}/%{name}-overload.so
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}d.conf.5.*
%{_mandir}/man8/%{name}d.8.*

