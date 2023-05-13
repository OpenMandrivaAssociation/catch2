%undefine _debugsource_packages

%define major 3
%define libname %mklibname catch2
%define devname %mklibname catch2 -d

Name: catch2
Version: 3.3.2
Release: 1
Source0: https://github.com/catchorg/Catch2/archive/refs/tags/v%{version}.tar.gz
Summary: C++ unit-test framework
URL: https://github.com/catchorg/Catch2
License: BSL-1.0
Group: System/Libraries
BuildRequires: cmake ninja

%description
A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14,
C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x
branch)

%package -n %{libname}
Summary: C++ unit-test framework
Group: System/Libraries

%description -n %{libname}
A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14,
C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x
branch)

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14,
C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x
branch)

%prep
%autosetup -p1 -n Catch2-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_datadir}/Catch2

%files -n %{devname}
%doc %{_docdir}/Catch2
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/pkgconfig/*
%{_libdir}/cmake/Catch2
