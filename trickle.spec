Name:		trickle
Version:	1.07
Release:	%mkrel 6
URL:		http://monkey.org/~marius/pages/?page=trickle
Source:		http://monkey.org/~marius/trickle/trickle-%{version}.tar.gz
Summary:	Lightweight userspace bandwidth shaper
Group:		Networking/File transfer
License:	BSD
BuildRequires:	libevent-devel
# patch from debian, overloads fread() and fwrite()
Patch0:		trickle-1.07-deb-fread_fwrite_overload.patch
Patch1:		trickle-1.07-format-strings.patch
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
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
# it mistakenly assumes in_addr_t is not defined in <netinet/in.h>
sed -i.in_addr_t -e '/in_addr_t/d' config.h
%make

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE TODO README
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}d
%{_libdir}/%{name}/%{name}-overload.so
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}d.conf.5.*
%{_mandir}/man8/%{name}d.8.*
