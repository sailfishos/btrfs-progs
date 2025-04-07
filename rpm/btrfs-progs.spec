Name:       btrfs-progs
Summary:    Btrfs helper utilities
Version:    6.14
Release:    1
License:    GPLv2
URL:        https://github.com/sailfishos/btrfs-progs
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  lzo-devel
BuildRequires:  libacl-devel
BuildRequires:  zlib-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libattr-devel
BuildRequires:  e2fsprogs-devel

%description
Btrfs userspace utilities, include btrfs, btrfs-debug-tree and etc.

%package devel
Summary: Btrfs filesystem-specific libraries and headers
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure \
  --bindir=%{_sbindir} \
  --disable-documentation\
  --disable-libudev \
  --disable-static

%make_build

%install

%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_sbindir}/btrfs
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-find-root
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-select-super
%{_sbindir}/btrfsck
%{_sbindir}/btrfstune
%{_sbindir}/mkfs.btrfs
%{_sbindir}/fsck.btrfs
%{_libdir}/libbtrfs.so.*
%{_libdir}/libbtrfsutil.so.*

%files devel
%{_includedir}/btrfs/*.h
%{_includedir}/btrfsutil.h
%{_libdir}/libbtrfs.so
%{_libdir}/libbtrfsutil.so
%{_libdir}/pkgconfig/*.pc
