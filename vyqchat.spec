Summary:	real-time, text-based, serverless LAN chat program
Name:		vyqchat
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.gz
# Source0-md5:	f28b5698f82e3723ecf346439b8cf632
BuildRequires:	qt-devel >= 3.1.0
BuildRequires:	arts-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VyQChat is a real-time, text-based, serverless chat program dedicated to
LANs, that runs on Linux using Qt/X11 library. It is almost 100%
compatible with Vypress Chat(TM) for Windows. It allows you to chat with
friends on public or private channels, send and recieve messages etc.

%prep
%setup  -q

%build
%configure \
	--with-Qt-include-dir=%{_includedir}/qt \
	--with-Qt-lib-dir=%{_libdir} \
	--with-arts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
