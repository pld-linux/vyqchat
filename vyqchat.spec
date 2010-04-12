Summary:	Real-time, text-based, serverless LAN chat program
Summary(pl.UTF-8):	Działający w czasie rzeczywistym, tekstowy, bezserwerowy program do pogawędek sieciowych
Name:		vyqchat
Version:	0.2.8
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.gz
# Source0-md5:	67974bc5df1ed0d63785d04325444d4f
Source1:	%{name}.desktop
URL:		http://linux.bydg.org/~yogin/
Patch0:		%{name}-gcc4.patch
BuildRequires:	artsc-devel
BuildRequires:	libao-devel
BuildRequires:	libsndfile-devel
BuildRequires:	openssl-devel >= 0.9.6
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.1.0
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VyQChat is a real-time, text-based, serverless chat program dedicated
to LANs, that runs on Linux using Qt/X11 library. It is almost 100%
compatible with Vypress Chat(TM) for Windows. It allows you to chat
with friends on public or private channels, send and recieve messages
etc.

%description -l pl.UTF-8
VyQChat jest działającym w czasie rzeczywistym, tekstowym, nie
wymagającym serwera program do pogawędek przeznaczonym dla sieci
lokalnych, który działa w Linuksie korzystając z biblioteki Qt/X11.
Jest on niemal w 100% zgodny z programem Vypress Chat(TM) dla Windows.
Pozwala on na rozmowy z przyjaciółmi na kanałach publicznych lub
prywatnych, wysyłanie i otrzymywanie wiadomości itp.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%{__autoheader}

%configure \
	--with-Qt-include-dir=%{_includedir}/qt \
	--with-Qt-lib-dir=%{_libdir} \
	--with-arts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/
cp -f gfx/default/user.png $RPM_BUILD_ROOT%{_pixmapsdir}/vyqchat.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
