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
- **Bar** — Waybar, bottom, chunky
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
