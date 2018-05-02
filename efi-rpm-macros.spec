Summary: Common RPM Macros for building EFI-related packages
Name: efi-rpm-macros
Version: 2
Release: 5%{?dist}
Group: Development/System
License: GPLv3+
URL: https://github.com/rhboot/%{name}/
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86}
BuildRequires: git sed
Requires: efi-filesystem rpm
BuildArch: noarch

Source0: https://github.com/rhboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0001: 0001-Simplify-efi_arch_upper.patch
Patch0002: 0002-Add-a-changelog-entry-to-the-.spec-for-version-2.patch
Patch0003: 0003-efi-rpm-macros.spec.in-use-autosetup.patch
Patch0004: 0004-Add-efi_alt_arch-and-efi_alt_arch_upper.patch
Patch0005: 0005-Return-nil-instead-of-on-unsupported-arches.patch
Patch0006: 0006-efi_arch-turns-out-nil-is-definitely-not-what-we-wan.patch
Patch0007: 0007-Make-a-macros.efi-srpm-that-defines-efi.patch
Patch0008: 0008-Add-efi_has_alt_arch-0-or-1.patch
Patch0009: 0009-Add-efi-filesystem-subpackage.patch
Patch0010: 0010-efi-rpm-macros.spec-don-t-use-efi-rpm-macros-definit.patch

%global debug_package %{nil}
%global _efi_vendor_ %(eval sed -n -e 's/rhel/redhat/' -e 's/^ID=//p' /etc/os-release)

%description
%{name} provides a set of RPM macros for use in EFI-related packages.

%package -n efi-srpm-macros
Summary: Common SRPM Macros for building EFI-related packages
Group: Development/System
BuildArch: noarch
Requires: efi-filesystem rpm

%description -n efi-srpm-macros
efi-srpm-macros provides a set of SRPM macros for use in EFI-related packages.

%package -n efi-filesystem
Summary: The basic directory layout for EFI machines
Group: System Environment/Base
BuildArch: noarch
Requires: filesystem

%description -n efi-filesystem
The efi-filesystem package contains the basic directory layout for EFI
machine bootloaders and tools.

%prep
%autosetup -S git

%build
%make_build EFI_VENDOR=%{_efi_vendor_} clean all

%install
%make_install EFI_VENDOR=%{_efi_vendor_}

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%{_rpmmacrodir}/macros.efi

%files -n efi-srpm-macros
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README
%{_rpmmacrodir}/macros.efi-srpm

%files -n efi-filesystem
%defattr(0700,root,root,-)
%dir /boot/efi
%dir /boot/efi/EFI
%dir /boot/efi/EFI/BOOT
%dir /boot/efi/EFI/%{_efi_vendor_}

%changelog
* Wed May 02 2018 Peter Jones <pjones@redhat.com> - 2-5
- Add efi-filesystem subpackage

* Wed May 02 2018 Peter Jones <pjones@redhat.com> - 2-4
- Add %%{efi_has_alt_arch}

* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 2-3
- Make an efi-srpm-macros subpackage to pull in so %%{efi} works in
  ExclusiveArch in koji.

* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 2-2
- Fix the non-efi and non-efi-alt-arch cases, hopefully.

* Tue May 01 2018 Peter Jones <pjones@redhat.com> - 2-1
- Lots of rpmlint fixups and the like.

* Mon Apr 30 2018 Peter Jones <pjones@redhat.com> - 1-1
- First shot at building it.
