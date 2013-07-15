
Name:       btrfs-progs
Summary:    Btrfs helper utilities
Version:    0.19
Release:    1
Group:      System/Base
License:    GPLv2
URL:        http://www.kernel.org/pub/linux/kernel/people/mason/btrfs/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  lzo-devel
BuildRequires:  libacl-devel

%description
Btrfs userspace utilities, include btrfs, btrfs-debug-tree and etc.

%package devel
Summary: Btrfs filesystem-specific libraries and headers
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package docs
Summary: Documentation for btrfs-progs
Group:   Documenation
Requires: %{name} = %{version}-%{release}

%description docs
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
cd btrfs-progs
prefix=%{_prefix} make %{?jobs:-j%jobs}

%install
cd btrfs-progs
rm -rf %{buildroot}
make mandir=%{buildroot}/%{_mandir} prefix=%{buildroot}/%{_prefix} install
rm %{buildroot}/%{_libdir}/libbtrfs.a


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/btrfs
%{_bindir}/btrfs-convert
%{_bindir}/btrfs-debug-tree
%{_bindir}/btrfs-find-root
%{_bindir}/btrfs-image
%{_bindir}/btrfs-map-logical
%{_bindir}/btrfs-show-super
%{_bindir}/btrfs-zero-log
%{_bindir}/btrfsck
%{_bindir}/btrfstune
%{_bindir}/mkfs.btrfs
%{_libdir}/libbtrfs.so.0
%{_libdir}/libbtrfs.so.0.1

%files devel
%defattr(-,root,root,-)
%{_includedir}/btrfs/*.h
%{_libdir}/libbtrfs.so

%files docs
%defattr(-,root,root,-)
%doc %{_mandir}/man8/btrfs-image.8.gz
%doc %{_mandir}/man8/btrfs.8.gz
%doc %{_mandir}/man8/btrfsck.8.gz
%doc %{_mandir}/man8/mkfs.btrfs.8.gz

