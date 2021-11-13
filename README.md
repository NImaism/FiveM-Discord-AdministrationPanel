<p align="center">
  <h1 align="center">
      FiveM Discord Administration Panel
  </h1>
  <h3 align="center">
     Version 1.0.0
  </h3>
  <h4 align="center">
      If you would like to report an issue or request a feature. Join our <a href="https://discord.com/invite/DAwe3J75bD">Discord</a> or create an issue.
  </h4>
</p>

<br/>
<br/>


Control Server Fivem From Discord
-----------------------------------------------------------


### Features
* Set Time
* Stop Resource
* Start Resource
* Set Admin Level
* Set Weather
* Custom Command
* With Show Count Of Player In Server
* Server Build
* .....


-----------------------------------------------------------

### Upcoming Features
* Have an idea? Suggest it in our [Discord](https://discord.com/invite/DAwe3J75bD) or Issues page.


-----------------------------------------------------------

### Requirements
Python Libraries
* Discord
* request
* discord_components

 ----------------------------------------------------------
 
 ### Installation

 First :
 * 1 Create Bot & Get Token Bot From https://discord.com/developers/applications
 * 2 Install Python Libraries
 * 3 put folder in resource folder in your fivem server
 * 4 in server.cfg write add_ace resource.IsM Panel command allow  
 * 5 config your bot in config.json
 * 6 run cmd in folder & type python main.py
 * 7 and start resource
 * 8 Enjoy !
 ---------------------------------------------------------
### Custom Command 
In Admin-Cmd.py Write:

```py
@commands.command()
@has_permissions(administrator=True)
async def CommandName(self, ctx, id, perm):
	if cheakadmin(ctx.author.id):
		request(f"CommandName {arguments} {arguments}")
		await ctx.send(">>> CommandName Has Ben Successful")
```      
In You Script For Command Write:
```lua
RegisterCommand("CommandName", function(source, args)
    if source == 0 then
        print(args[1])
        -- ....
    end   
end)

```

--------------------------------------------------------
### Example Config

```json
{
    "Token":"OTA2ND2kxMjcyNsjQ1MTkzNzQ5.YY6ZZyQ.vOXIKk7NMm5VVg5GxWyRBIHm1fUo", // Token Bot Discord
    "Perfix":"-", // Perfix Bot
    "Status": ["IsM Company", "By NImaism"], // Status
    "Users": [
        {
            "Server": "Sosis Land", // Server Name
            "Owner": "NImaism", // Server Owner Name
            "Admins":[841250866895781918], // Discord User Id For Use Command
            "Ip":"5.63.10.232:30120", // Ip:Port Server
            "Site":"https://servers.fivem.net/servers/detail/a89pf49" // Link Server In Fivem Server List Site

        }
    ]
}

```



 ---------------------------------------------------------
 
 ### Media
 
<p align="left">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_114933_7zfh.png" width="350" alt="accessibility text">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_110131_ylot.png" width="350" alt="accessibility text">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_105911_20pg.png" width="350" alt="accessibility text">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_113245_qhlu.png" width="350" alt="accessibility text">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_110052_wt2s.png" width="350" alt="accessibility text">
  <img src="https://s4.uupload.ir/files/screenshot_2021-11-13_110107_dok.png" width="350" alt="accessibility text">

</p>
 
-----------------------------------------------------------  


### Support
* Join our [Discord](https://discord.com/invite/DAwe3J75bD) Server for Support or open an issue via GitHub.
