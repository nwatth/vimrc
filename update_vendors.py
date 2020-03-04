import zipfile
import shutil
import tempfile
import requests

from os import path


#--- Globals ----------------------------------------------
VENDORS = [
    # Analytics
    "wakatime/vim-wakatime",

    # Syntax
    "vim-ruby/vim-ruby",
    "kchmck/vim-coffee-script",
    "cakebaker/scss-syntax.vim",
    "tpope/vim-markdown",
    "posva/vim-vue",
    "isRuslan/vim-es6",

    # Linter
    "ngmy/vim-rubocop",
    "prettier/vim-prettier",
    "dgraham/vim-eslint",

    # Tools
    "bling/vim-airline",
    "vim-airline/vim-airline-themes",
    "scrooloose/nerdtree",
    "kien/ctrlp.vim",
    "chakrit/vim-thai-keys",
    "mileszs/ack.vim",
    "airblade/vim-gitgutter",
    "tpope/vim-commentary",
    "terryma/vim-expand-region",
    "gko/vim-coloresque",
    "corntrace/bufexplorer",
    "tpope/vim-repeat",
    "tpope/vim-surround",
    "scrooloose/syntastic",
    "garbas/vim-snipmate",
    "MarcWeber/vim-addon-mw-utils",
    "scrooloose/snipmate-snippets",
    "vim-scripts/tlib",
    "michaeljsmith/vim-indent-object",
    "vim-scripts/mru.vim",
    "vim-scripts/YankRing.vim",
    "mkitt/tabline.vim",
    "aklt/plantuml-syntax",
    "scrooloose/vim-slumlord",
]

GITHUB_ZIP = 'https://github.com/%s/archive/master.zip'

SOURCE_DIR = path.join(path.dirname(__file__), 'vendors')


def download_extract_replace(plugin_name, zip_path, temp_dir, source_dir):
    temp_zip_path = path.join(temp_dir, plugin_name)

    # Download and extract file in temp dir
    req = requests.get(zip_path)
    open(temp_zip_path, 'wb').write(req.content)

    zip_f = zipfile.ZipFile(temp_zip_path)
    zip_f.extractall(temp_dir)

    plugin_temp_path = path.join(temp_dir, path.join(temp_dir, '%s-master' % plugin_name))

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
        for vendor in VENDORS:
            owner, repo = vendor.split('/')
            zip_path = GITHUB_ZIP % vendor

            download_extract_replace(repo, zip_path,
                                     temp_directory, SOURCE_DIR)
    finally:
        shutil.rmtree(temp_directory)

