#
# IOT 2018LTS kernel
#  This kernel is an "enterprise style" kernel with a significant list of
#  backported features
#
# There are two subpackages "sos" and "standard"
#
# The "sos" kernel is specifically meant to run as DOM0 in an
#  ACRN hypervisor setup.
# The "standard"  kernel is meant for running on bare metal systems as well
#  as running as a "normal" guest in various hypervisors
#

Name:           linux-iot-lts2018
Version:        4.14.73
Release:        113
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.14.73.tar.xz
Source1:        config-iot-lts2018-sos
Source2:        config-iot-lts2018-standard
Source3:        cmdline-iot-lts2018-sos
Source4:        cmdline-iot-lts2018-standard

# kernel-lts-quilt: lts-v4.14.73-base-181002T012100Z
# kernel-config: lts-v4.14.73-base-181002T012100Z

%define ktarget0 iot-lts2018-sos
%define kversion0 %{version}-%{release}.%{ktarget0}
%define ktarget1 iot-lts2018-standard
%define kversion1 %{version}-%{release}.%{ktarget1}

BuildRequires:  bash >= 2.03
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  elfutils-dev
BuildRequires:  kernel-config
BuildRequires:  make >= 3.78
BuildRequires:  openssl-dev
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  kmod
BuildRequires:  linux-firmware
BuildRequires:  lz4

Requires: systemd-bin
Requires: linux-iot-lts2018-sos
Requires: linux-iot-lts2018-standard

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# PK XXXX: Series
#END XXXX: PK Series

# SEP and SoCWatch Series

# Clear Linux patch
# needs to add to PK series

%description
The Linux kernel.

%package sos
License:        GPL-2.0
Summary:        The Linux kernel for Service OS
Group:          kernel

%description sos
The Linux kernel for Service OS

%package standard
License:        GPL-2.0
Summary:        The Linux kernel for Linux as a Guest
Group:          kernel

%description standard
The Linux kernel for Linux as a Guest

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%prep
%setup -q -n linux-4.14.73

#patchXXXX PK Series
# End XXXX PK Series

# SEP and SoCWatch Series

# Clear Linux patch

cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp -a /usr/lib/firmware/i915 firmware/
cp -a /usr/lib/firmware/intel-ucode firmware/
cp -a /usr/lib/firmware/intel firmware/

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config-${Target} ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget0}
BuildKernel %{ktarget1}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 cmdline-${Target}    ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

InstallKernel %{ktarget0} %{kversion0}
InstallKernel %{ktarget1} %{kversion1}

rm -rf %{buildroot}/usr/lib/firmware

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion0}
%dir /usr/lib/modules/%{kversion1}

%files sos
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion0}
/usr/lib/kernel/config-%{kversion0}
/usr/lib/kernel/cmdline-%{kversion0}
/usr/lib/kernel/org.clearlinux.%{ktarget0}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget0}
/usr/lib/modules/%{kversion0}/kernel
/usr/lib/modules/%{kversion0}/modules.*

%files standard
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion1}
/usr/lib/kernel/config-%{kversion1}
/usr/lib/kernel/cmdline-%{kversion1}
/usr/lib/kernel/org.clearlinux.%{ktarget1}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget1}
/usr/lib/modules/%{kversion1}/kernel
/usr/lib/modules/%{kversion1}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion0}
/usr/lib/kernel/System.map-%{kversion1}
/usr/lib/kernel/vmlinux-%{kversion0}
/usr/lib/kernel/vmlinux-%{kversion1}
