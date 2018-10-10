#
# IOT 2018LTS kernel
#  This kernel is an "enterprise style" kernel with a significant list of
#  backported features
#
# This package has a main package "standard" and a subpackage "sos"
#
# The "standard"  kernel  (the main package) is meant for running on
#  bare metal systems as well as running as a "normal" guest in
#  various hypervisors. This
#
# The "sos" kernel is specifically meant to run as DOM0 in an
#  ACRN hypervisor setup.
#

Name:           linux-iot-lts2018
Version:        4.19.0
Release:        2
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://git.kernel.org/torvalds/t/linux-4.19-rc6.tar.gz
Source1:        config-iot-lts2018
Source2:        config-iot-lts2018-sos
Source3:        cmdline-iot-lts2018
Source4:        cmdline-iot-lts2018-sos

# kernel-lts-quilt: a1de559d06d4a1856c936d996a32de5721716fe6
# kernel-config: mainline-tracking-v4.19-rc6-181002T220531Z

%define ktarget0 iot-lts2018
%define kversion0 %{version}-%{release}.%{ktarget0}
%define ktarget1 iot-lts2018-sos
%define kversion1 %{version}-%{release}.%{ktarget1}

BuildRequires:  buildreq-kernel

Requires: systemd-bin

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# PK XXXX: Series
Patch0001: 0001-greybus-Remove-android-make-file.patch
Patch0002: 0002-x86-mm-init32-Mark-text-and-rodata-RO-in-one-go.patch
Patch0003: 0003-x86-mm-cpa-Split-rename-and-clean-up-try_preserve_la.patch
Patch0004: 0004-x86-mm-cpa-Rework-static_protections.patch
Patch0005: 0005-x86-mm-cpa-Allow-range-check-for-static-protections.patch
Patch0006: 0006-x86-mm-cpa-Add-debug-mechanism.patch
Patch0007: 0007-x86-mm-cpa-Add-large-page-preservation-statistics.patch
Patch0008: 0008-x86-mm-cpa-Avoid-static-protection-checks-on-unmap.patch
Patch0009: 0009-x86-mm-cpa-Add-sanity-check-for-existing-mappings.patch
Patch0010: 0010-x86-mm-cpa-Optimize-same-protection-check.patch
Patch0011: 0011-x86-mm-cpa-Do-the-range-check-early.patch
Patch0012: 0012-x86-mm-cpa-Avoid-the-4k-pages-check-completely.patch
Patch0013: 0013-Integration-of-CBC-line-discipline-kernel-module.patch
Patch0014: 0014-cbc-Avoid-rx-sequence-counter-mismatch-warnings.patch
Patch0015: 0015-Fix-for-cbc-kernel-driver-crash-during-warm-reboot.patch
Patch0016: 0016-staging-Add-AVnu-based-Intel-IGB-driver.patch
Patch0017: 0017-the-igb_avb-direver-cannot-coexist-with-e1000-or-e10.patch
Patch0018: 0018-fix-some-likely-copy-paste-errors-with-some-if-block.patch
Patch0019: 0019-usb-xhci-pci-Only-create-Intel-mux-device-when-it-s-.patch
Patch0020: 0020-dwc3-setup-highspeed-to-USB3.0-on-bxtp-platform.patch
Patch0021: 0021-ACPI-battery-use-cache_time-as-cache-enabled.patch
Patch0022: 0022-PCI-add-pci_devices_ignore-cmdline-option.patch
Patch0023: 0023-x86-add-ACRN-hypervisor-guest.patch
Patch0024: 0024-VHM-add-vhm-char-device-driver.patch
Patch0025: 0025-VHM-add-guest-memory-management-support.patch
Patch0026: 0026-VHM-add-guest-memory-remote-mapping-support.patch
Patch0027: 0027-VHM-add-ioreq-service-support.patch
Patch0028: 0028-VHM-add-interrupt-injection-support.patch
Patch0029: 0029-VHM-add-API-to-get-vm-info.patch
Patch0030: 0030-VHM-add-API-to-do-guest-gpa2hpa-translation.patch
Patch0031: 0031-VHM-add-passthrough-device-support.patch
Patch0032: 0032-x86-acrn-add-write_msi-pv-ops-to-intercept-pci-msi-w.patch
Patch0033: 0033-sos-cleanup-hypercall-API.patch
Patch0034: 0034-vcpu-export-vcpu-create-interface-to-DM.patch
Patch0035: 0035-sos-clean-up-ptdev-msi-x-table-ioremap-operations.patch
Patch0036: 0036-sos-Update-the-common-head-file.patch
Patch0037: 0037-sos-cleanup-ptdev-irq-structure.patch
Patch0038: 0038-VBS-K-Virtio-Backend-Service-in-Kernel-a-kernel-leve.patch
Patch0039: 0039-VBS-K-virtqueue-initialization-API.patch
Patch0040: 0040-VBS-K-virtqueue-runtime-API.patch
Patch0041: 0041-VBS-K-added-a-VBS-K-reference-driver.patch
Patch0042: 0042-hypercall-refine-hypercall-interfaces.patch
Patch0043: 0043-vhm-refine-vm-related-hypercall-ioctrl.patch
Patch0044: 0044-hypercall-refine-HC-ID-and-parameter-number.patch
Patch0045: 0045-ioctl-cleanup-ioctl-structure.patch
Patch0046: 0046-Shared_buf-add-shared-buffer.patch
Patch0047: 0047-Shared_buf-added-hypercall-for-shared_buf-setup.patch
Patch0048: 0048-ACRNTrace-add-acrn-trace-module.patch
Patch0049: 0049-sos-fix-potential-bugs-in-ptdev-msi-x-access.patch
Patch0050: 0050-vhm-cleanup-ioctls.patch
Patch0051: 0051-VHM-check-HV-api-version-for-VHM-module-init.patch
Patch0052: 0052-VHM-add-VHM-api-version-support.patch
Patch0053: 0053-virtio-framework-support-ACRN-virtio-devices.patch
Patch0054: 0054-VHM-sync-public-header-file-acrn_common.h.patch
Patch0055: 0055-Check-x86_hyper-type-before-doing-hypercall.patch
Patch0056: 0056-VHM-replace-function-name-update_mmio_map-with-updat.patch
Patch0057: 0057-VHM-refine-memory-segment-interface.patch
Patch0058: 0058-VBS-K-added-VHM-wrapper-APIs.patch
Patch0059: 0059-api-doc-add-ACRN-VBS-API-docs.patch
Patch0060: 0060-HVLog-reserve-memory-for-ACRN-HVLog.patch
Patch0061: 0061-HVLog-add-HVLog-module.patch
Patch0062: 0062-update-MEM_ATTR_WRITE_PROT-with-WB-policy.patch
Patch0063: 0063-vhm-modify-mmio-memory-map-unmap-api.patch
Patch0064: 0064-vhm-cleanup-update-one-field-name-in-vhm.patch
Patch0065: 0065-sos-add-a-config-for-VHM.patch
Patch0066: 0066-api-doc-add-vhm-API-docs.patch
Patch0067: 0067-api-doc-update-ACRN-VBS-API-docs.patch
Patch0068: 0068-license-update-intel-license-for-ACRN-VBS.patch
Patch0069: 0069-VBS-K-fix-compilation-warnings-in-VBS-K-reference-dr.patch
Patch0070: 0070-Cleanup-Kconfig.patch
Patch0071: 0071-skip-sbuf-and-vhm-initialization-when-booting-native.patch
Patch0072: 0072-VHM-add-hugetlb-page-ept-mapping-support.patch
Patch0073: 0073-VHM-change-VM_SYSMEM-VM_MMIO-to-VM_MEMMAP_SYSMEM-VM_.patch
Patch0074: 0074-VHM-add-hash-table-support-for-huge-pages.patch
Patch0075: 0075-VHM-add-service-to-support-px-data-transition.patch
Patch0076: 0076-sos-sync-common-header-file.patch
Patch0077: 0077-sos_kernel-export-restart-vm-function-to-DM.patch
Patch0078: 0078-VHM-add-service-to-support-cx-data-transition.patch
Patch0079: 0079-vhm-add-set_memmaps-hypercall-support.patch
Patch0080: 0080-vhm-use-set-memmaps-hypercall-for-hugetlb.patch
Patch0081: 0081-vhm-prepare-future-update-for-struct-vm_set_memmap.patch
Patch0082: 0082-VHM-bug-fix-on-operating-multi-thread-synchronizatio.patch
Patch0083: 0083-vhm-add-hypercall-to-set-sstate-data.patch
Patch0084: 0084-VHM-Update-cpu-id-type-as-uint16_t-for-struct-acrn_c.patch
Patch0085: 0085-vhm-add-sos-offline-cpu-support.patch
Patch0086: 0086-vhm-Fix-kernel-doc-issues.patch
Patch0087: 0087-vhm-add-trusty-init-de-init-support.patch
Patch0088: 0088-vhm-Rename-the-restart_vm-to-reset_vm.patch
Patch0089: 0089-vhm-fix-kerneldoc-format.patch
Patch0090: 0090-sos-vhm-remove-set-guest-memory-map-by-CMA.patch
Patch0091: 0091-sos-vhm-remove-hugetlb_enabled-flag.patch
Patch0092: 0092-sos-vhm-remove-MAP_MMIO.patch
Patch0093: 0093-vhm-revisit-types-in-structure-parameters-of-hyperca.patch
Patch0094: 0094-sos-vhm-add-hcall_write_protect_page-hypercall.patch
Patch0095: 0095-sos-vhm-refine-set-memory-region-API.patch
Patch0096: 0096-vhm-remove-re-schedule-for-ioreq-tasklet.patch
Patch0097: 0097-vhm-Add-vcpu_num-to-record-vcpu-number-of-each-VM.patch
Patch0098: 0098-vhm-mark-pending-ioreqs-in-bitmap-then-dispatch-it-t.patch
Patch0099: 0099-vhm-use-correct-string-length.patch
Patch0100: 0100-vhm-adapt-to-the-new-state-transition-of-VHM-request.patch
Patch0101: 0101-vhm-Add-error-handling-for-IC_CREATE_VM-ioctl.patch
Patch0102: 0102-vhm-setup-ioreq-shared-buf-in-IC_CREATE_VM-ioctl.patch
Patch0103: 0103-VBS-K-add-virtio_dev_reset.patch
Patch0104: 0104-VBS-K-Check-whether-vhm_client_id-is-valid-before-de.patch
Patch0105: 0105-VBS-K-add-reset-support-for-vbs_rng.patch
Patch0106: 0106-VBS-K-fix-a-bug-due-to-incorrect-check-of-return-val.patch
Patch0107: 0107-VHM-remove-panic-action-when-ioreq-fails.patch
Patch0108: 0108-vbs-fix-virtio_vq_index_get-func-handling-of-multi-V.patch
Patch0109: 0109-vhm-init-client-kthread_exit-true.patch
Patch0110: 0110-vhm-fix-client-use-after-free.patch
Patch0111: 0111-Adds-new-API-for-unmap-memseg.patch
Patch0112: 0112-sos-vhm-add-HC_SETUP_HV_NPK_LOG-hypercall.patch
Patch0113: 0113-acrn-add-hv_npk_log-module.patch
Patch0114: 0114-Adding-kernel-parameter-for-forcing-xapic-in-physica.patch
Patch0115: 0115-VHM-Add-EXPORT_SYMBOL-for-VHM-API-function-so-that-i.patch
Patch0116: 0116-vhm-deinit-trusty-after-hcall_destroy_vm.patch
Patch0117: 0117-VHM-add-ioctl-hypercall-for-UOS-intr-data-monitor.patch
Patch0118: 0118-vhm-enable-Werror-while-compiling-vhm-vbs-hyper-dmab.patch
Patch0119: 0119-vhm-change-trace_printk-of-vhm_dev_ioctl-to-pr_debug.patch
Patch0120: 0120-vhm-add-ioeventfd-support-for-ACRN-hypervisor-servic.patch
Patch0121: 0121-vhm-add-irqfd-support-for-ACRN-hypervisor-service-mo.patch
Patch0122: 0122-vhm-add-ioctl-for-set-clear-IRQ-line.patch
Patch0123: 0123-sos-vhm-add-hypercall-to-set-guest-vcpu-registers.patch
Patch0124: 0124-Kernel-VHM-Rename-acpi_generic_address-in-acrn_commo.patch
Patch0125: 0125-drm-i915-gvt-some-changes-to-support-xengt-acrngt.patch
Patch0126: 0126-drm-i915-gvt-Refactored-BXT-plane-registers.patch
Patch0127: 0127-drm-i915-gvt-passthru-PIPE_DSL-regiser-to-guest.patch
Patch0128: 0128-drm-i915-gvt-local-display-support.patch
Patch0129: 0129-drm-i915-gvt-local-display-support-in-GVT-g-guest.patch
Patch0130: 0130-drm-i915-gvt-Change-DomU-to-support-3-HDMI-displays.patch
Patch0131: 0131-drm-i915-i915-changes-to-allow-DomU-to-support-3-HDM.patch
Patch0132: 0132-drm-i915-gvt-removed-save-store-registers.patch
Patch0133: 0133-drm-i915-gvt-ivi-lazy-shadow-context.patch
Patch0134: 0134-drm-i915-gvt-add-some-MMIO-value-initialization.patch
Patch0135: 0135-drm-i915-gvt-added-option-to-disable-wa_ctx-shadowin.patch
Patch0136: 0136-drm-i915-gvt-enable-ppgtt-oos-sync-by-default.patch
Patch0137: 0137-drm-i915-gvt-emit-shadow-ppgtt-root-in-LRI.patch
Patch0138: 0138-drm-i915-gvt-Raise-a-uevent-when-Dom-0-is-ready-for-.patch
Patch0139: 0139-drm-i915-gvt-Don-t-load-CSR-for-Dom-U.patch
Patch0140: 0140-drm-i915-gvt-add-acrngt-support.patch
Patch0141: 0141-drm-i915-gvt-hard-code-Pipe-B-plane-owner-to-UOS.patch
Patch0142: 0142-drm-i915-gvt-remove-some-initialization-of-ggtt-in-G.patch
Patch0143: 0143-drm-i915-gvt-avoid-unncessary-reset-in-GVT-g-guest.patch
Patch0144: 0144-drm-i915-gvt-add-param-disable_gvt_fw_loading-to-dis.patch
Patch0145: 0145-drm-i915-gvt-inject-error-interrupt-to-DomU-when-GPU.patch
Patch0146: 0146-drm-i915-gvt-Added-error-interrupt-handler-for-GVT-g.patch
Patch0147: 0147-drm-i915-gvt-Add-the-support-of-HUC_STATUS2-reg-emul.patch
Patch0148: 0148-drm-i915-gvt-Add-vgt-id-in-context-id.patch
Patch0149: 0149-drm-i915-gvt-show-pid-hw_id-of-current-DomU-process-.patch
Patch0150: 0150-drm-i915-gvt-Add-new-trace-point-to-output-per-domai.patch
Patch0151: 0151-drm-i915-gvt-preliminary-per-ring-scheduler.patch
Patch0152: 0152-drm-i915-gvt-Support-vGPU-guest-framebuffer-GEM-obje.patch
Patch0153: 0153-drm-i915-gvt-unset-DDI_BUF_CTL_ENABLE-during-port-em.patch
Patch0154: 0154-drm-i915-gvt-add-scaler-owner-to-support-guest-plane.patch
Patch0155: 0155-drm-i915-gvt-support-guest-plane-scaling.patch
Patch0156: 0156-drm-i915-gvt-add-module-parameter-enable_pvmmio.patch
Patch0157: 0157-drm-i915-gvt-get-ready-of-memory-for-pvmmio.patch
Patch0158: 0158-drm-i915-implement-pvmmio-in-guest-i915.patch
Patch0159: 0159-drm-i915-gvt-implement-pvmmio-in-GVTg.patch
Patch0160: 0160-drm-i915-gvt-add-pvmmio-support-in-preempt-context-s.patch
Patch0161: 0161-drm-i915-Use-64-bit-write-to-optimize-writing-fence_.patch
Patch0162: 0162-drm-i915-gvt-don-t-treat-EINVAL-if-trap-pci_command-.patch
Patch0163: 0163-drm-i915-gvt-pvmmio-optimization-for-plane-update.patch
Patch0164: 0164-drm-i915-gvt-handling-pvmmio-update-of-plane-registe.patch
Patch0165: 0165-drm-i915-gvt-enable-plane-update-pvmmio-through-enab.patch
Patch0166: 0166-drm-i915-gvt-implement-gfn_to_mfn-with-identical-1-1.patch
Patch0167: 0167-drm-i915-gvt-cached-read_gpa-optimization-in-shadow-.patch
Patch0168: 0168-drm-i915-gvt-add-a-fastpath-for-cmd-parsing-on-MI_NO.patch
Patch0169: 0169-drm-i915-gvt-notify-ppgtt-update-through-g2v.patch
Patch0170: 0170-drm-i915-gvt-handle-ppgtt-update-from-g2v.patch
Patch0171: 0171-drm-i915-gvt-enable-pv-ppgtt-update-by-default.patch
Patch0172: 0172-drm-i915-gvt-pvmmio-optimization-for-plane-wm-regist.patch
Patch0173: 0173-drm-i915-gvt-handling-pvmmio-update-of-plane-wm-regi.patch
Patch0174: 0174-drm-i915-gvt-enable-plane-wm-pvmmio-level-through-en.patch
Patch0175: 0175-drm-i915-gvt-notify-global-gtt-update-through-g2v.patch
Patch0176: 0176-drm-i915-gvt-handle-global-gtt-update-from-g2v.patch
Patch0177: 0177-drm-i915-gvt-enable-pv-global-gtt-update-by-default.patch
Patch0178: 0178-drm-i915-gvt-Check-the-state-of-PVMMIO-gtt-table-to-.patch
Patch0179: 0179-drm-i915-gvt-allocate-ddb-according-to-active-pipes.patch
Patch0180: 0180-drm-i915-to-limit-the-supported-modifiers-for-plane-.patch
Patch0181: 0181-REVERTME-IOTG-hyper_dmabuf-Introducing-the-hyper_dma.patch
Patch0182: 0182-hyper_dmabuf-Enable-hyper_dmabuf-only-on-x86-or-x86_.patch
Patch0183: 0183-hyper_dmabuf-Fix-array-length-check-issue-in-hyper_d.patch
Patch0184: 0184-kernel-hyper_dmabuf-disable-hyper_dmabuf-on-arch-arm.patch
Patch0185: 0185-hyper_dmabuf-Remove-void-cast-in-cpu_access-function.patch
Patch0186: 0186-hyper_dmabuf-Fix-incorrect-return-in-hyper_dmabuf_op.patch
Patch0187: 0187-hyper_dmabuf-Check-for-NULL-value-before-access-work.patch
Patch0188: 0188-hyper_dmabuf-Remove-unused-variable-warnings.patch
Patch0189: 0189-hyper_dmabuf-virtio-Protect-virtqueue-operations-wit.patch
Patch0190: 0190-hyper_dmabuf-virtio-Correctly-cleanup-front-end-conn.patch
Patch0191: 0191-hyper_dmabuf-virtio-bugfix-on-acrn_ioreq_add_iorange.patch
Patch0192: 0192-hyper_dmabuf-virtio-Add-support-for-VBS_RESET_DEV-io.patch
Patch0193: 0193-hyper_dmabuf-virtio-Handle-S3-resume-correctly-v2.patch
Patch0194: 0194-hyper_dmabuf-fix-map-failure-issue-when-assign-4G-me.patch
Patch0195: 0195-hyper_dmabuf-fix-compile-warnings-in-hyper_dmabuf.patch
Patch0196: 0196-hyper_dmabuf-virtio-Adapt-to-the-new-state-transitio.patch
Patch0197: 0197-hyper_dmabuf-virtio-Process-ioreq-according-to-bitma.patch
Patch0198: 0198-hyper_dmabuf-virtio-Fixed-compilation-warnings.patch
Patch0199: 0199-hyper_dmabuf-Align-with-dma_buf_ops-changes.patch
Patch0200: 0200-drm-i915-Sysfs-interface-to-get-GFX-shmem-usage-stat.patch
Patch0201: 0201-drm-i915-Async-work-for-hdcp-authentication.patch
Patch0202: 0202-drm-i915-Commit-CP-without-modeset.patch
Patch0203: 0203-drm-i915-Passing-the-intel_connector-to-HDCP-auth.patch
Patch0204: 0204-test-configs-use-for-clean-and-android-bare-metal-BA.patch
#END XXXX: PK Series

# SEP and SoCWatch Series

# Clear Linux patch
# needs to add to PK series

%description
The Linux IOT LTS2018 kernel.

%package sos
License:        GPL-2.0
Summary:        The Linux kernel for Service OS
Group:          kernel

%description sos
The Linux kernel for Service OS

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%prep
%setup -q -n linux-4.19-rc6

#patchXXXX PK Series
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1
%patch0089 -p1
%patch0090 -p1
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
%patch0138 -p1
%patch0139 -p1
%patch0140 -p1
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1
%patch0144 -p1
%patch0145 -p1
%patch0146 -p1
%patch0147 -p1
%patch0148 -p1
%patch0149 -p1
%patch0150 -p1
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1
%patch0155 -p1
%patch0156 -p1
%patch0157 -p1
%patch0158 -p1
%patch0159 -p1
%patch0160 -p1
%patch0161 -p1
%patch0162 -p1
%patch0163 -p1
%patch0164 -p1
%patch0165 -p1
%patch0166 -p1
%patch0167 -p1
%patch0168 -p1
%patch0169 -p1
%patch0170 -p1
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1
%patch0180 -p1
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1
%patch0184 -p1
%patch0185 -p1
%patch0186 -p1
%patch0187 -p1
%patch0188 -p1
%patch0189 -p1
%patch0190 -p1
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1
%patch0195 -p1
%patch0196 -p1
%patch0197 -p1
%patch0198 -p1
%patch0199 -p1
%patch0200 -p1
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
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
/usr/lib/kernel/config-%{kversion0}
/usr/lib/kernel/cmdline-%{kversion0}
/usr/lib/kernel/org.clearlinux.%{ktarget0}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget0}
/usr/lib/modules/%{kversion0}/kernel
/usr/lib/modules/%{kversion0}/modules.*

%files sos
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
