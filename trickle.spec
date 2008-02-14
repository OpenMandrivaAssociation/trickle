Name:		trickle
Version:	1.07
Release:	%mkrel 1
URL:		http://monkey.org/~marius/pages/?page=trickle
Source:		http://monkey.org/~marius/trickle/trickle-%{version}.tar.gz
Summary:	Lightweight userspace bandwidth shaper
Group:		Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD
BuildRequires:	libevent-devel
# patch from debian fix build
Patch0:		trickle-%{version}_debian.patch
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
%patch -p1

%build
%configure
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall

%files
%doc LICENSE TODO README
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}d
%{_libdir}/%{name}/%{name}-overload.so
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}d.conf.5.*
%{_mandir}/man8/%{name}d.8.*

