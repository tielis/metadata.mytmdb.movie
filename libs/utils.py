# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# pylint: disable=missing-docstring

"""Misc utils"""

import xbmc, unicodedata
from os import path, makedirs
from xbmcaddon import Addon


ID = 'metadata.mytmdb.movies'

def trailer_log(source, msg, title):      
    addonDataDir = xbmc.translatePath(Addon(ID).getAddonInfo('profile'))    
    Logtxt = path.join(addonDataDir, "Trailer_log.txt")
    lines =  []
    found = False        
    txt_msg = unicodedata.normalize('NFC',str(source + msg + title + '\n'))
    try:
        makedirs(addonDataDir)
        f = open(Logtxt, "r")
        lines = f.readlines()
        f.close()
    except:
        pass
    if lines:
        for i, line in enumerate(lines):        
            if title in line:
                found = True
                if not msg in line:                    
                    lines[i] = txt_msg
                    f = open(Logtxt, "w")
                    f.write("".join(lines))
                    f.close()
                break        
    if not found:
        f = open(Logtxt, "a", encoding='utf-8')        
        f.write(txt_msg)
        f.close()        
    return