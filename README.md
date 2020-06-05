# BirthdayBot
This Discord bot is a tool to help Discord users keep track of birthdays in their servers. If you like this bot and would like to support me you can
donate [here](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=FV3CH35QBDSAJ&currency_code=USD&source=url)

<p>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_donations" />
<input type="hidden" name="business" value="FV3CH35QBDSAJ" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>
</p>

## Getting Started
Follow the instructions below to invite this bot onto your discord server. 
You need to be an admin of a server to install. 

### Installing
1. Click this [link](https://discord.com/api/oauth2/authorize?client_id=701412155853111317&permissions=8&scope=bot)
2. Select what discord server you want to add the bot too.

### Using birthdayBot!

Once you have the bot up and running, you can use the following commands to add, edit, delete, or view someone's birthday.

#### b!add
 ```
 b!add name mm/dd will add someone's name and birthday to the system.

Example: 
b!add test 04/24
```
<p align="center">
  <img src="images/add.png" height="50%">
</p>

#### b!all
 ```
 b!all will list all birthdays in the system.

Example: 
b!all
```

#### b!delete
 ```
 b!delete name will remove someone's birthday from the system.

Example: 
b!delete test
```
<p align="center">
  <img src="images/delete.png" height="100">
</p>

#### b!edit
 ```
b!edit name will allow you to edit a birthday in the system with that corresponding name.

Example: 
b!edit test 05/24
```
<p align="center">
  <img src="images/edit.png" height="100">
</p>

#### b!month
 ```
b!month monthoftheyear will allow you to view all birthdays for that month.

Example: 
b!month may 
```

#### b!today
 ```
 b!today will print a happy birthday message for birthdays on that day if none, it wil print nothing.

Example: 
b!today 
```
<p align="center">
  <img src="images/today.png" height="100">
</p>

#### b!thisMonth
 ```
b!thisMonth will allow you to view all birthdays for the current month.

Example: 
b!thisMonth
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Prerequisites

* Python
* Mongodb
* Discord.py 
