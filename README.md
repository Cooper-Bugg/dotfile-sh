# dotfilesh

Cyberpunk Arch rice. ThinkPad T480, Hyprland, cold dark palette — blue, gold, red.

```
cooper@arch-thinkpad
--------------------
  OS          Arch Linux (x86_64)
  Kernel      Linux 7.0.10-arch1-1
  Packages    ~800 (pacman)
--------------------
  Shell       zsh 5.9.1
  Terminal    Kitty
  WM          Hyprland 0.55.2 (Wayland)
  Resolution  2560x1440 @ 60Hz
--------------------
  CPU         Intel Core i7-8650U (8C/8T) @ 4.20 GHz
  GPU         UHD Graphics 620 [Integrated]
  RAM         ~2 GiB / 15.36 GiB
  Disk (/)    468 GiB [ext4]
--------------------
  Commands    ls/ll (eza)   cat (bat)    grep (rg)
              pacup (sync)  yayin (AUR)  v (vim)
              hyprconf      zshconf      aliasconf
```

## Stack

- **WM** — Hyprland (Lua config)
- **Bar** — Waybar, bottom, chunky (configured with native Hyprland workspace window icons, and a custom logo tooltip displaying system performance stats & top processes)
- **Launcher** — Rofi
- **Terminal** — Kitty
- **Editor** — Neovim (lazy.nvim, clangd, DAP, Treesitter, Kanagawa)
- **Shell** — ZSH, no framework, manual plugins
- **Screenshot** — `Super+Print` → broken screen shader + slurp region + swappy

## Install

```bash
git clone https://github.com/Cooper-Bugg/dotfilesh.git ~/.dotfiles
cd ~/.dotfiles
./install.sh   # requires stow
```

## OS State Capture & Restoration (Manual Backup Guide)

While these dotfiles capture your user-space configurations, they do not include system-level configurations, secrets, or installed binaries to avoid bloating the repository and leaking private info. 

If you want to capture or reconstruct this full OS environment manually, use the following guidelines:

### 1. Package Lists (Applications)
To capture all installed packages (native pacman and AUR via yay), run:
```bash
# Export package lists
pacman -Qqe > ~/.dotfiles/misc/pkglist.txt
```
To restore them on a fresh OS:
```bash
# Import package lists
sudo pacman -S --needed - < pkglist.txt
# For AUR packages (using yay/yayin)
yay -S --needed - < pkglist.txt
```

### 2. Enabled System Services
To see which system services must be enabled via `systemctl enable`:
```bash
systemctl list-unit-files --state=enabled
```
Key services on this system:
* **Display Manager**: `sddm.service`
* **Networking & VPN**: `NetworkManager.service`, `iwd.service`, `vpnagentd.service`
* **Power Management**: `tlp.service`
* **Security & Input**: `ufw.service`, `python3-validity.service` (fingerprint), `python3-validity-suspend-hotfix.service`
* **Local AI**: `ollama.service`
* **Bluetooth**: `bluetooth.service`
* **Printing**: `cups.service`, `avahi-daemon.service`

### 3. Critical System-Level Configurations (`/etc/`)
Some setups require manual configurations in system files (not managed by `stow` in your home directory):
* **Fingerprint PAM Authentication**: Configure `/etc/pam.d/system-local-login` and `/etc/pam.d/hyprlock` for `pam_fprintd.so` (refer to [setup-fingerprint.sh](file:///home/cooper/.dotfiles/bin/.local/bin/setup-fingerprint.sh)).
* **SDDM Configurations**: Copy or link the display manager configs from [misc/sddm-cyberpunk.conf](file:///home/cooper/.dotfiles/misc/sddm-cyberpunk.conf) to `/etc/sddm.conf.d/`.

### 4. Things NOT to capture (Backup separately)
Ensure these are backed up to secure, private storage and never committed to GitHub:
* **Secrets & Credentials**: Private keys (`~/.ssh/`), GPG keys (`~/.gnupg/`), passwords, and API tokens.
* **Hardware Drivers**: Graphics drivers and firmware (e.g., audio/SOF firmware).
