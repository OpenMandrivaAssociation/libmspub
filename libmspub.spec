%define lname	mspub
%define api	0.1
%define major	1
%define libname %mklibname %{lname} %{api} %{major}
%define devname %mklibname %{lname} -d

Summary:	A library providing ability to interpret and import Microsoft Publisher files
Name:		libmspub
Version:	0.1.1
Release:	1
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+ or MPLv1.1
Url:		http://www.freedesktop.org/wiki/Software/libmspub
Source0:	http://dev-www.libreoffice.org/src/libmspub/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(zlib)

%track
prog %{name} = {
	url = http://cgit.freedesktop.org/libreoffice/libmspub/
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.gz
}

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package	tools
Summary:	Tools to transform Microsoft Publisher files into other formats
Group:		Publishing

%description tools
Tools to transform Microsoft Publisher files into other formats.
Currently supported: XHTML, raw.

%package -n	%{libname}
Summary:	Text categorization library
Group:		System/Libraries
Obsoletes:	%{_lib}mspub0 < 0.0.4-1

%description -n	%{libname}
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package -n	%{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{lname}-devel = %{version}-%{release}
Obsoletes:	%{name}-doc < %{version}-%{release}

%description -n	%{devname}
Development files and headers for %{name}.

%prep
%setup -q
%apply_patches
mkdir -p m4
autoreconf -fi

%build
%configure2_5x \
	--disable-static

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool

%make

%install
%makeinstall_std

%files tools
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml

%files -n %{libname}
%{_libdir}/libmspub-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.*
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_includedir}/%{name}-%{api}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

