cd ~/.vim_runtime
echo 'set runtimepath+=~/.vim_runtime' > ~/.vimrc

cat ~/.vim_runtime/vimrcs/basic.vim >> ~/.vimrc

echo '

source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim

try
source ~/.vim_runtime/my_configs.vim
catch
endtry' >> ~/.vimrc

echo "Installed the Ultimate Vim configuration successfully! Enjoy :-)"
