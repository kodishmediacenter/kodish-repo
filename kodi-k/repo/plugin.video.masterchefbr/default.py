import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.masterchefbr'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = "https://yt3.ggpht.com/-DjeJJy9xWR4/AAAAAAAAAAI/AAAAAAAAAAA/TGAuenmyFz8/s100-c-k-no-rj-c0xffffff/photo.jpg"

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID = "UC2EWGw-KBjEReUbXMJEiaCA"

# Ponto de Entrada
def run():
	# Pega Parametros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("masterchefbr.main_list "+repr(params))
	
	plugintools.log("masterchefbr.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Master Chef Br",
		url = "plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
		

run()