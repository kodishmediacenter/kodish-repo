# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/gsfvideos
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.velberantv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
#icon = local.getAddonInfo('icon')

icon =  "https://yt3.ggpht.com/-mKzPJMXBAxk/AAAAAAAAAAI/AAAAAAAAAAA/NfLHkdLbIGA/s100-c-k-no-rj-c0xffffff/photo.jpg"
icon2 = "https://yt3.ggpht.com/-oXl69oAacaQ/AAAAAAAAAAI/AAAAAAAAAAA/H43pPw8o8fo/s100-c-k-no-rj-c0xffffff/photo.jpg"
icon3 = "https://yt3.ggpht.com/-Q6yFRbPogCg/AAAAAAAAAAI/AAAAAAAAAAA/xmhIUUr5LLA/s100-c-k-no-rj-c0xffffff/photo.jpg"

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"
YOUTUBE_CHANNEL_ID  = "Velberan"
YOUTUBE_CHANNEL_ID2 = "velberan2"
YOUTUBE_CHANNEL_ID3 = "UCP-bdbQG7rkx5_w5x3QUiCg"
# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("velberantv.main_list "+repr(params))
	
	plugintools.log("velberantv.run")
	
	#plugintools.direct_play(str(entryurl))

plugintools.add_item(
		title = "Velberan Games",
		url = "plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
		
plugintools.add_item(
		title = "Velberan Adventures",
		url = "plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon2,
		folder = True )
		
plugintools.add_item(
		title = "Japão por Outro Olhos",
		url = "plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon3,
		folder = True )		
		
run()