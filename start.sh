#!/bin/sh

GM_WORKSHOP_ID="" # ID of Workshop Collection that will force server to install it's content.
GM_GSLT="" # Game Server Account Token, mostly required for rating.
GM_MAP="gm_construct"
GM_PASSWORD=""
GM_TICKRATE=33
GM_PLAYERS=128
GM_GAMEMODE="sandbox"

# there is might be a way to make it look better
# but i'm just not that experienced in bash
if [ $(find . -name "srcds_run_x64") ]; then
  ./srcds_run_x64 -game garrysmod \
                  -maxplayers $GM_PLAYERS \
                  -port 27015 \
                  -condebug \
                  +map $GM_MAP \
                  +gamemode $GM_GAMEMODE \
                  +fps_max $GM_TICKRATE \
                  +host_workshop_collection $GM_WORKSHOP_ID \
                  +sv_setsteamaccount $GM_GSLT \
                  +sv_password $GM_PASSWORD
elif [ $(find . -name "srcds_run") ]; then
  ./srcds_run     -game garrysmod \
                  -maxplayers $GM_PLAYERS \
                  -port 27015 \
                  -condebug \
                  +map $GM_MAP \
                  +gamemode $GM_GAMEMODE \
                  +fps_max $GM_TICKRATE \
                  +host_workshop_collection $GM_WORKSHOP_ID \
                  +sv_setsteamaccount $GM_GSLT \
                  +sv_password $GM_PASSWORD
fi