%define lname mspub
%define major 0
%define libname %mklibname %{lname} %{major}
%define develname %mklibname %{lname} -d

Summary:	A library providing ability to interpret and import Microsoft Publisher files
Name:		libmspub
Version:	0.0.1
Release:	1
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+ or MPLv1.1
URL:		http://www.freedesktop.org/wiki/Software/libmspub
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf automake libtool

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package -n	%{libname}
Summary:	Text categorization library
Group:		System/Libraries

%description -n	%{libname}
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package -n	%{develname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Provides:	mspub-devel = %{version}-%{release}

%description -n	%{develname}
Development files and headers for %{name}.

%package	doc
Summary:	Documentation of %{name} API
Group:		Documentation
BuildArch:	noarch

%description	doc
The %{name}-doc package contains documentation files for %{name}.

%package	tools
Summary:	Tools to transform Microsoft Publisher files into other formats
Group:		Applications/Publishing

%description tools
Tools to transform Microsoft Publisher files into other formats.
Currently supported: XHTML, raw.

%prep

%setup -q

%build
mkdir -p m4
autoreconf -fi

%configure2_5x \
    --disable-static

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool

%make

%install

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING.*
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}-0.0
%dir %{_includedir}/%{name}-0.0/%{name}
%{_includedir}/%{name}-0.0/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%{_docdir}/%{name}/html

%files tools
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml
