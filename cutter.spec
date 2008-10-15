Summary:	Aborts TCP/IP connections
Name:		cutter
Version:	1.03
Release:	0.9
License:	GPL v2
Group:		Applications/Networking
URL:		http://www.lowth.com/cutter
Source0:	http://www.lowth.com/cutter/software/%{name}-%{version}.tgz
# Source0-md5:	50093db9b64277643969ee75b83ebbd1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cutter is an open source program that allows Linux firewall
administrators to abort TCP/IP connections routed over the firewall or
router on which it is run.

%prep
%setup -q

%build
%{__cc} %{optflags} -o cutter cutter.c

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/%{name}
