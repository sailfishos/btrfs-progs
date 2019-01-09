Name:       btrfs-progs
Summary:    Btrfs helper utilities
Version:    0.19
Release:    1
Group:      System/Base
License:    GPLv2
URL:        http://www.kernel.org/pub/linux/kernel/people/mason/btrfs/
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-make-Fix-compilation-by-increasing-optimization-to-O.patch
Patch1:     0002-doc-remove-documentation-building.patch
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(blkid)
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
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary: Documentation for btrfs-progs
Group:   Documentation
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-make-Fix-compilation-by-increasing-optimization-to-O.patch
%patch0 -p1
# 0002-doc-remove-documentation-building.patch
%patch1 -p1

%build
prefix=%{_prefix} make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make bindir=%{buildroot}/%{_sbindir} mandir=%{buildroot}/%{_mandir} prefix=%{buildroot}/%{_prefix} install
rm %{buildroot}/%{_libdir}/libbtrfs.a

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        Documentation/*.txt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_sbindir}/btrfs
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-debug-tree
%{_sbindir}/btrfs-find-root
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-show-super
%{_sbindir}/btrfs-zero-log
%{_sbindir}/btrfsck
%{_sbindir}/btrfstune
%{_sbindir}/mkfs.btrfs
%{_sbindir}/fsck.btrfs
%{_libdir}/libbtrfs.so.0
%{_libdir}/libbtrfs.so.0.1

%files devel
%defattr(-,root,root,-)
%{_includedir}/btrfs/*.h
%{_libdir}/libbtrfs.so

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
