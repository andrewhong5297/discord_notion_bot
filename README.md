To get started:

- go through [discord developer portal](https://discordapp.com/developers/applications/me) and create a new bot, and get a invite link (could be oauth2 or not)
- make sure to go to "bot" and copy the discord bot token id, into config vars for "DISCORD_TOKEN"
- create a notion page with a full table, and store that table url in config vars of heroku for "NOTION_DATABASE_ID"
- get your token-v2 from your cookies (inspect -> applications -> cookies -> tokenv2) of your login that has edit access to this notion page. set this to "NOTION_TOKEN" in config vars
- host this on your own instance of heroku (with those above config vars within "settings"). Make sure to turn on the bot with "resources" and that little pen button next to the worker. If you're on the free version, the bot will shut off around the 22nd or 23rd of each month.
- right now the bot is set to 7 columns in lines 29-35 of the main.py script, those columns need to already exist in the notion page table. Feel free to change things around.
- Once everything above is ready, use that invite link to add the bot to your server, make sure to edit VALID_CHANNELS in line 21 to enable bug and feature requests for just that channel.
