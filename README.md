# xfce4-screensaver-desktop-gen
This Python script generates .desktop entries from xscreensaver xml configuration files. It allows xfce4-screensaver (and likely MATE or GNOME screensaver) to discover installed xscreensaver screensavers.

## Dependencies
* Python 3
    * untangle
    * glob
    * argparse

## Usage

`./xfce4-screensaver-desktop-gen.py \[--inputfile «filename»\]`

If the tool is run without arguments it will parse each xml file in `/usr/share/xscreensaver/config` and generate a corresponding .desktop entry in `/usr/share/applications/screensavers/`

The `--inputfile` flag can be used to force the script to process a single specified xml file.

## Notes

It would be wise to confirm the location of the screensavers on your system; the script as configured is for a Gentoo AMD64 no-multilib system that stores them in `/usr/lib64/misc/xscreensaver/`. The XFCE Wiki suggests that `/usr/lib/xscreensaver/` may be a good place to start.

Once the location has been confirmed the script can be amended to suit your configuration. For example:

`sed 's/\/usr\/lib64\/misc\/xscreensaver\//\/usr\/lib\/xscreensaver\//' xfce4-screensaver-desktop-gen.py`