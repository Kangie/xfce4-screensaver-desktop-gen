# xfce4-screensaver-desktop-gen.py
# Generates .desktop entries from xscreensaver xml config files. 
# Allows xfce4-screensaver (and probably MATE and GNOME screensavers) to use xscreensaver screensavers.

# Copyright (C) Matt J (Kangie@footclan.ninja), 2020.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# You may need to modify the exec path to suit your distribution.
# Gentoo amd64 no-multilib uses /usr/lib64/misc/xscreensaver/
# Xfce wiki suggests /usr/lib/xscreensaver/ might suit most distros.

import argparse 
import untangle
import glob

parser=argparse.ArgumentParser(description='Tool to generate .desktop entries from xscreensaver xml config files. Allows xfce4-screensaver (and probably MATE and GNOME screensavers) to use xscreensaver screensavers.', 
        epilog='If run without arguments will parse the whole /usr/share/xscreensaver/config/ directory')
parser.add_argument('--inputfile',metavar='Filename',
        type=str, help='input filename (xscreensaver xml)', required=False)
args=parser.parse_args()

if args.inputfile:
        # Parse xscreensaver config file
        obj = untangle.parse(args.inputfile)

        # Set output filename and open file.
        filename = '/usr/share/applications/screensavers/{}.desktop'.format(obj.screensaver['name'])
        file = open(filename,"w")

        # Write desktop entry.
        print("Writing {}".format(filename))
        file.write("[Desktop Entry]\n")
        file.write("Type=Application\n")
        file.write("Name={}\n".format(obj.screensaver['_label']))
        if obj.screensaver.command['arg']:
                file.write("Exec=/usr/lib64/misc/xscreensaver/{} {}\n".format(obj.screensaver['name'], obj.screensaver.command['arg']))
        else:
                file.write("Exec=/usr/lib64/misc/xscreensaver/{}\n".format(obj.screensaver['name']))
        file.write("TryExec=/usr/lib64/misc/xscreensaver/{}\n".format(obj.screensaver['name']))
        file.write("Categories=Screensaver;\n")
        file.write("NoDisplay=true\n")
        file.close()

else:
        path='/usr/share/xscreensaver/config'
        configs=glob.glob(path + '/*.xml')
        for st in configs:
                obj=untangle.parse(st)
                filename = '/usr/share/applications/screensavers/{}.desktop'.format(obj.screensaver['name'])
                file = open(filename,"w")
                # Write desktop entry.
                print("Writing {}".format(filename))
                file.write("[Desktop Entry]\n")
                file.write("Type=Application\n")
                file.write("Name={}\n".format(obj.screensaver['_label']))
                if obj.screensaver.command['arg']:
                        file.write("Exec=/usr/lib64/misc/xscreensaver/{} {}\n".format(obj.screensaver['name'], obj.screensaver.command['arg']))
                else:
                        file.write("Exec=/usr/lib64/misc/xscreensaver/{}\n".format(obj.screensaver['name']))
                file.write("TryExec=/usr/lib64/misc/xscreensaver/{}\n".format(obj.screensaver['name']))
                file.write("Categories=Screensaver;\n")
                file.write("NoDisplay=true\n")
                file.close()
