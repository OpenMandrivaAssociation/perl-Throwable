%define upstream_name    Throwable
%define upstream_version 0.100090

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An easy-to-use class for error objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Throwable/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Devel::StackTrace)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Throwable is a role for classes that are meant to be thrown as exceptions
to standard program flow. It is very simple and does only two things: saves
any previous value for '$@' and calls 'die $self'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


