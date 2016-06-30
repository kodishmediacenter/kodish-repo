# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.kodiescorpaio'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'


def run():
    plugintools.log("kodiescorpaio.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("kodiescorpaio ===> " + repr(params))

                icon2 = "http://kodish.esy.es/imgs/icon2.png"


		plugintools.add_item(title = "Dicas do Alex"              , url = base + "channel/UCe0K_VF6Wz16fHVWKwIuSqQ/", thumbnail = icon, folder = True)
                plugintools.add_item(title = "House Geek   "              , url = base + "channel/UCy1VTBxKIp4QrbCwsQcOI4A/", thumbnail = icon2, folder = True)
                
		

		
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
