# birthdayBot
This Discord bot is a tool to help Discord users keep track of birthdays in their servers. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes. 

### Prerequisites

* Python
* Pip
* Discord 

### Installing
1. ```git clone https://github.com/tcolas673/birthdaybot.git ```
2. Start up Command Prompt or Terminal and navigate to this directory: ```cd <clone directory>```
3. Install Discord.py by running the following command
```
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```
4. Invite the bot to your server [(more instructions here)](https://stackoverflow.com/questions/37689289/how-to-join-a-server) and input your Discord bot key in config.json
5. type python3 birthdaybot.py in your terminal

### Using birthdayBot!

Once you have the bot up and running, you can type b!add to add someone's name and birthday.

###### b!add
 ```
 b!add name mm/dd will add someone's name and birthday to the system.

Example: 
b!add test 04/24
```
<p align="center">
  <img src="">
</p>


###### b!all
 ```
 b!all will list all birthdays in the system.

Example: 
b!all
```
<p align="center">
  <img src="">
</p>

###### b!delete
 ```
 b!delete name will remove someone's birthday from the system.

Example: 
b!delete test
```
<p align="center">
  <img src="">
</p>

###### b!edit
 ```
b!edit name will allow you to edit a birthday in the system with that corresponding name.

Example: 
b!edit test 05/24
```
<p align="center">
  <img src="">
</p>

###### b!month
 ```
b!month monthoftheyear will allow you to view all birthdays for that month.

Example: 
b!month may 
```
<p align="center">
  <img src="">
</p>

###### b!today
 ```
 b!today will print a happy birthday message for birthdays on that day if none, it wil print nothing.

Example: 
b!today 
```
<p align="center">
  <img src="">
</p>

###### b!thisMonth
 ```
b!thisMonth will allow you to view all birthdays for the current month.

Example: 
b!thisMonth
```
<p align="center">
  <img src="">
</p>

## Built With

* [Node.js](https://nodejs.org/en/) - Javascript runtime
* [Request](https://www.npmjs.com/package/request) - HTTP client for node.js

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Testers on Discord server (special thanks to Akira, Asano, Christopher, Nodar, Trevor, and Yui)
