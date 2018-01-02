# Insta-Liker
>An autoliker script for Instagram.

### Tech Stack  
- Selenium Webdriver
- Gecko Driver (included in the repository)

### Python libraries used:
1. os
2. time
3. getpass
4. sys

## How to Use:
- Make sure selenium and Mozilla Firefox are installed on your system.
  - Selenium Installation(from command line): pip install selenium 
  - You probably know how to install Firefox
- Clone this repository, get to the directory. 
- Create a file named keys.txt in the directory of this repository.
  - Add your Instagram account username in the first line of the keys.txt file.
  - Add your Instagram account password in the second line of the keys.txt file.
  - Save the changes of the file.
- Run using 'python3 automation.py'.  
- Provide the number of posts you wish to like.
- The script searches for number of unliked posts you wish to like from your feed and likes them.
- ENJOY!

### Future Plans:
1. Use headless browser. I tried to use chrome-headless but its quite slow.
2. Add functionality of liking all the posts of a particular person that you are following.
3. Improve scrolling and error checking.
