%define 	modulename pam_pop3
Summary:	PAM module for authenticating users against POP3 server
Summary(pl):	Modu³ PAM uwierzytelniaj±cy u¿ytkowników wzglêdem serwera POP3
Name:		pam-%{modulename}
Version:	1.0
Release:	1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://shum.huji.ac.il/~schapiro/linux/%{modulename}/%{modulename}-%{version}.tar.gz
# Source0-md5:	e9bfebe349f79e308ff8d329e5b25f91
URL:		http://shum.huji.ac.il/~schapiro/linux/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_pop3 aims to provide a authenticating users against an POP3
server.

%description -l pl
pam_pop3 to modu³ PAM maj±cy na celu uwierzytelnianie u¿ytkowników
wzglêdem serwera POP3.

%prep
%setup -q -n %{modulename}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_pop3.so $RPM_BUILD_ROOT/%{_lib}/security/pam_pop3.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /%{_lib}/security/pam_pop3.so
