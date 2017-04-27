Name:	hello		
Version:	0.1	
Release:	1%{?dist}
Summary:	Say Hello World
		
License:	GPL
Source0:	hello	

BuildArch: noarch

%description

Simple hello world program


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}


%files
%{_bindir}/hello


%changelog

