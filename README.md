#Mini PC Scraper

So I made this python tool ( that you can host on a VPS ) that can be used to scrape all the local (local = south african) online shops for raspberry pi's and arduinos. PLEASE NOTE: This does not scrape all the products and there might be some false positives.

## How it works

I am using Python Flask Server to host the whole project so users can view all the results scraped from the sites. It scrapes those sites every hour ( delay can be set to any value ) and then stores them neatly in an excel document which can be retrieved from a certain endpoint or viewed online. It also allows easy integration with other tools its using JSON format responses for endpoints.

## Progress

- [x] Finished Scraping for Takealot
- [ ] Finished Scraping for BotShop
- [ ] Finished Scraping for RoboFactory (Still not sure if trusted or not) 
- [ ] Packed .exe file for easy installation + usage
- [ ] Added automatic syncing to google sheets (Planned)

## Installation

There's two options for running this program.
- Using Python on the local machine
- Using the packed .exe file built with python pre-installed

#### 1) Using Python ( Skip if done already )

Installing python is really simple just head to the official hosting site: [Official Python Download Site](https://www.python.org/downloads/) and then download the latest stable version of Python. After donwloaded you can open the wizard and finish up the installation (please note: You need to select `Add Python to PATH` since you need to access it from anywhere on the pc) 

After installing Python you can download the repo and save it somewhere after that open command prompt and go to the directory of the program using `cd` and then install the requirements:

```bash
pip3 install -r requirements.txt
```
This will install all the libraries you need for it to work.

#### 2) Using packed .exe

Just donwload the zip folder [here](https://google.com) and run the main.exe file.

## Hosting

**PLEASE NOTE: I will add the hosting setups once done with program**

I've listed some free hosting options and reverse proxies you can use to test this out.

- Render
- Deta Space
- PythonAnywhere
- Google Cloud Platform ( Free tier )

I will also include ways to host this as Functions on some BaaS's

- Appwrite
- Firebase
- Supabase
