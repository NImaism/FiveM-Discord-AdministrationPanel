<p align="center">
  <h1 align="center">
      FiveM Discord Administration Panel
  </h1>
  <h3 align="center">
     Version 1.0.0.
  </h3>
  <h4 align="center">
      If you would like to report an issue or request a feature. Join our <a href="https://discord.com/DAwe3J75bD">Discord</a> or create an issue.
  </h4>
</p>

<br/>
<br/>

# 
Control Server Fivem From Discord
-----------------------------------------------------------



 
  
-----------------------------------------------------------
How to use: 
+ execute the sql file in your server database
+ then put start HR_BanSystem in server.cfg
+ *Note: You Have To Put Your Steam Hex In server/main.lua - Admins then you can use commands(/tokenban, /reloadtk...)

-----------------------------------------------------------
What are the features of this resource?
  
  + Anti Multiple Accounts : players information such as(steam hex, license, tokens) will be save in database after first login.
   so they cant connect to server with a diffrent steam hex or license(new account).
   
  + Anti Unban: if you ban a player, the player can not connect to server or unban himself(Even if Steam, license, discordid, ip,... has changed) :}
  
  + You Can WhiteList Players From (Anti Multiple Account System) with /multiacc [steamhex]

-----------------------------------------------------------
How Is This Possible? Are Using HWID?
 + not exactly HWID but 
 + im using a new native called GetPlayerToken() : 
 + {Gets a player's token. Tokens can be used to enhance banning logic, however are specific to a server.}
 + players token will not change if they change their information such as(discord id, ip, steamhex, license...)
 + *Note: for now i recommend you to ban cheaters(Permanent), because there is no ban duration in script.(you have to unban players manually.)
 ----------------------------------------------------------
 Will I make any changes in the future?
  probably yes 
  + Discord Log
  + Ban Duration
  + etc
-----------------------------------------------------------  
