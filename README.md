## Indus Valley Font

The area of encoding is U+E000 onwards, comprising of most interchangeable glyphs found in the Indus Valley.

### Programmer Font

To install fonts, follow instructions below for the folder ``IndusProgrammer``

Installing
==========

Windows
-------

In the ttf folder, double-click each font file, click “Install font”; to install all at once, select all files, right-click, and choose “Install”

macOS
-----

In the downloaded TTF folder:

1.  Select all font files
2.  Right click and select `Open` (alternatively `Open With Font Book`)
3.  Select "Install Font"

Linux Manual Installation
-------------------------

With most desktop-oriented distributions, double-clicking each font file in the ttf folder and selecting “Install font” should be enough. If it isn’t, create and run `download_and_install.sh` script:

    #!/usr/bin/env bash

    fonts_dir="${HOME}/.local/share/fonts"
    if [ ! -d "${fonts_dir}" ]; then
        echo "mkdir -p $fonts_dir"
        mkdir -p "${fonts_dir}"
    else
        echo "Found fonts dir $fonts_dir"
    fi

    for type in Bold Light Medium Regular Retina; do
        file_path="${HOME}/.local/share/fonts/IndusProgrammer-${type}.ttf"
        file_url="https://github.com/decipher-indus/font/blob/programmer/distr/IndusProgrammer/IndusProgrammer-${type}.ttf?raw=true"
        if [ ! -e "${file_path}" ]; then
            echo "wget -O $file_path $file_url"
            wget -O "${file_path}" "${file_url}"
        else
      echo "Found existing file $file_path"
        fi;
    done

    echo "fc-cache -f"
    fc-cache -f
    
Enabling ligatures
==================

Atom
----

To change your font to Fira Code, open Atom's preferences (`cmd + ,` on a Mac, `ctrl + ,` on PC), make sure the "Settings" tab is selected, or the "Editor" in Atom 1.10+, and scroll down to "Editor Settings". In the "Font Family" field, enter `Indus Programmer`.

If you wish to specify a font weight, for example, Light, use `Indus Programmer Light` as a font name (Windows) or `IndusProgrammer-Light` (macOS).

Ligatures are enabled by default in Atom 1.9 and above.


VS Code
-------

To open the settings editor, first from the File menu choose Preferences, Settings or use keyboard shortcut `Ctrl + ,` (Windows) or `Cmd + ,` (macOS).

To enable FiraCode in the settings editor, under "Commonly Used", expand the "Text Editor" settings and then click on "Font". In the "Font Family" input box type `IndusProgrammer`, replacing any content. Tick the check box "Enables/Disables font ligatures" under "Font Ligatures" to enable the special ligatures.

If you wish to specify a font weight, for example, Light, use `Indus Programmer Light` as a font name (Windows) or `IndusProgrammer-Light` (macOS).


IntelliJ products
-----------------

1. Enable in Settings → Editor → Font → Enable Font Ligatures
2. Select `IndusProgrammer` as "Primary font" under Settings → Editor → Font

Additionally, if a Color Scheme is selected:

3. Enable in Settings → Editor → Color Scheme → Color Scheme Font → Enable Font Ligatures
4. Select Indus Programmer as "Primary font" under Settings → Editor → Color Scheme → Color Scheme Font


Sublime Text
------------

Preferences --> Settings

Add before "ignored_packages":

    "font_face": "Indus Programmer",
    "font_options": ["subpixel_antialias"],

If you want enable antialias, add in font_options: "gray_antialias"


Visual Studio
-------------

1. Launch Visual Studio (2015 or later).
2. Launch the Options dialog by opening the "Tools" menu and selecting "Options". 
3. In the Options dialog, under the "Environment" category, you'll find "Fonts and Colors". Click on that. You'll see a combo-box on the right hand side of the dialog labelled "Font". Select "Indus Programmer" from that combo-box. 
4. Click "OK" to dismiss.
5. Restart Visual Studio.

Now, most ligatures will work.
