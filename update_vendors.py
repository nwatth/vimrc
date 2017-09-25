import zipfile
import shutil
import tempfile
import requests

from os import path


#--- Globals ----------------------------------------------
VENDORS = """
vim-airline https://github.com/bling/vim-airline
vim-airline-themes https://github.com/vim-airline/vim-airline-themes
nerdtree https://github.com/scrooloose/nerdtree
ctrlp.vim https://github.com/kien/ctrlp.vim
vim-thai-keys https://github.com/chakrit/vim-thai-keys
ack.vim https://github.com/mileszs/ack.vim
vim-gitgutter https://github.com/airblade/vim-gitgutter
vim-commentary https://github.com/tpope/vim-commentary
vim-expand-region https://github.com/terryma/vim-expand-region
vim-coloresque https://github.com/gko/vim-coloresque
bufexplorer https://github.com/corntrace/bufexplorer
vim-repeat https://github.com/tpope/vim-repeat
vim-surround https://github.com/tpope/vim-surround
syntastic https://github.com/scrooloose/syntastic
vim-snipmate https://github.com/garbas/vim-snipmate
vim-addon-mw-utils https://github.com/MarcWeber/vim-addon-mw-utils
snipmate-snippets https://github.com/scrooloose/snipmate-snippets
tlib https://github.com/vim-scripts/tlib
vim-indent-object https://github.com/michaeljsmith/vim-indent-object
mru.vim https://github.com/vim-scripts/mru.vim
YankRing.vim https://github.com/vim-scripts/YankRing.vim
vim-ruby https://github.com/vim-ruby/vim-ruby
vim-coffee-script https://github.com/kchmck/vim-coffee-script
scss-syntax.vim https://github.com/cakebaker/scss-syntax.vim
vim-markdown https://github.com/tpope/vim-markdown
""".strip()

GITHUB_ZIP = '%s/archive/master.zip'

SOURCE_DIR = path.join(path.dirname(__file__), 'vendors')


def download_extract_replace(plugin_name, zip_path, temp_dir, source_dir):
    temp_zip_path = path.join(temp_dir, plugin_name)

    # Download and extract file in temp dir
    req = requests.get(zip_path)
    open(temp_zip_path, 'wb').write(req.content)

    zip_f = zipfile.ZipFile(temp_zip_path)
    zip_f.extractall(temp_dir)

    plugin_temp_path = path.join(temp_dir,
                                 path.join(temp_dir, '%s-master' % plugin_name))

    # Remove the current plugin and replace it with the extracted
    plugin_dest_path = path.join(source_dir, plugin_name)

    try:
        shutil.rmtree(plugin_dest_path)
    except OSError:
        pass

    shutil.move(plugin_temp_path, plugin_dest_path)

    print('Updated {0}'.format(plugin_name))


if __name__ == '__main__':
    temp_directory = tempfile.mkdtemp()

    try:
        for line in VENDORS.splitlines():
            name, github_url = line.split(' ')
            zip_path = GITHUB_ZIP % github_url

            download_extract_replace(name, zip_path,
                                     temp_directory, SOURCE_DIR)
    finally:
        shutil.rmtree(temp_directory)
