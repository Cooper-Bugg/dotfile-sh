# eza replaces ls
alias eza='eza --icons'
alias ls='eza --icons'
alias ll='eza -lh --icons --git'
alias la='eza -lah --icons --git'
alias tree='eza --tree --icons'
alias tree-dirs='eza --tree --only-dirs --icons -I ".git|.cache|.npm|.gemini|.thunderbird|node_modules"'
alias tree-all='eza --tree --icons -I ".git|.cache|.npm|.gemini|.thunderbird|node_modules"'

# navigation
alias ..='cd ..'
alias ...='cd ../..'
alias -- -='cd -'

# git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline --graph'

# editor
alias v='nvim'
alias bvim='nvim'

# system shortcuts
alias pacup='sudo pacman -Syu'
alias pacin='sudo pacman -S'
alias pacre='sudo pacman -Rns'
alias pacse='pacman -Ss'
alias yayup='yay -Syu'
alias yayin='yay -S'

# quick config edits
alias hyprconf='vim ~/.config/hypr/hyprland.lua'
alias zshconf='vim ~/.config/zsh/.zshrc'
alias aliasconf='vim ~/.config/zsh/aliases.zsh'

# AI
alias deepseek='~/.local/bin/bugg-os'
alias deepseek-raw='ollama run deepseek-r1:1.5b'
alias bugg-os='~/.local/bin/bugg-os'
alias prime='ollama run agy-prime'
alias tactician='ollama run command-r'


