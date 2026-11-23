Name:           locklet
Version:        0.1.0
Release:        1%{?dist}
Summary:        Lock screen for river and rivermonad (ext-session-lock-v1)

License:        BSD-3-Clause
URL:            https://github.com/prietus/locklet
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       python3
Requires:       python3-gobject
Requires:       gtk4
# Gtk4LayerShell and Gtk4SessionLock (>= 1.1), loaded with gi and ctypes.
Requires:       gtk4-layer-shell >= 1.1
# The password is checked with libpam through ctypes.
Requires:       pam
Recommends:     python3-pillow
Recommends:     grim
Recommends:     bgmonad

%description
locklet is a lock screen for river and rivermonad (or any compositor with
ext-session-lock-v1). The screen keeps looking the same for an instant and
then crossfades to the wallpaper bgmonad shows on that output, blurred and
darkened, drifting slowly. The password is checked with PAM. It also has an
idle daemon that locks after a while without input and before suspending.


%prep
%autosetup -n %{name}-%{version}
%py3_shebang_fix locklet


%build
# Nothing to build: locklet is a single Python script.


%install
install -Dpm 0755 locklet %{buildroot}%{_bindir}/locklet
install -Dpm 0644 pam/locklet %{buildroot}%{_sysconfdir}/pam.d/locklet


%files
%license LICENSE
%doc README.md
%{_bindir}/locklet
%config(noreplace) %{_sysconfdir}/pam.d/locklet


%changelog
* Mon Nov 23 2026 Carlos Prieto Ortiz <prietus@live.com> - 0.1.0-1
- First release
