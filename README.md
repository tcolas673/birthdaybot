# BirthdayBot
This Discord bot is a tool to help Discord users keep track of birthdays in their servers. If you like this bot and would like to support me you can
donate here
[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=FV3CH35QBDSAJ&currency_code=USD&source=url)

## Getting Started
Follow the instructions below to invite this bot onto your discord server. 
You need to be an admin of a server to install. 

### Installing
1. Click this [link](https://discord.com/api/oauth2/authorize?client_id=701412155853111317&permissions=8&scope=bot)
2. Select what discord server you want to add the bot to

### Using birthdayBot!

Once you have the bot up and running on your server, you can use the following commands to add, edit, delete, or view someone's birthday.

#### b!add
 ```
 b!add name mm/dd will add someone's name and birthday to the system.

Example: b!add Test 04/24
Output: Test's birthday was added
```

#### b!all
 ```
 b!all will list all birthdays in the system.

Example: b!all
Output: Test 04/24
        Troy 05/25
```

#### b!delete
 ```
 b!delete name will remove someone's birthday from the system.

Example: b!delete Test
Output: Birthday was deleted
```

#### b!deleteAll
 ```
 b!deleteAll will remove all birthday's added. Only Administrator's can run this command.

Example: b!deleteAll
Output: All Birthday's have been deleted
```

#### b!edit
 ```
b!edit name will allow you to edit a birthday in the system with that corresponding name.

Example: b!edit test 05/24
Output: Birthday updated
```

#### b!help
 ```
 b!help will list all bot commands.
```

#### b!here
 ```
 b!here will make bot send all Happy birthday messages
 in corresponding channel.

Example: b!here
Output: All Happy Birthday notices will appear here
```

#### b!month
 ```
b!month monthoftheyear will allow you to view all birthdays for that month.

Example: b!month may 
Output: Troy 05/25
```

#### b!name
 ```
 b!name username will show birthdate of user if they are in the system

Example: b!name Test
Output: 04/24
```

#### b!thisMonth
 ```
b!thisMonth will allow you to view all birthdays for the current month.

Example: b!thisMonth
Output: Test 04/24
```

#### b!today
 ```
 b!today will print a happy birthday message for birthdays on that day if none, it wil print nothing.

Example: b!today 
Output: Happy Birthday Test!
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Prerequisites

* Python
* Mongodb
* Discord.py 
