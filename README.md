Requirements
------------
 - Python 2.7.9 - 2.7.13

Disclaimer
----------

Pretty much all of these can be greatly improved. XKCD, for example, has a [JSON interface](https://xkcd.com/about/) to fetch comics, which would be far more reliable than clumsily scraping HTML with regex. On the plus side it's very beginner level Python so anyone should be able to figure out how to modify and improve it.

How to
------

 - If you haven't already [install Python](https://wiki.python.org/moin/BeginnersGuide/Download).
 - Set the necessary variables (DIRECTORY, USERNAME, PASSWORD, SUBS) for the comics you want to fetch. You can find the exchange servers for several popular cellular providers in carriers.xml
 - Set up a cron job(Linux/Mac) or Scheduled Task(windows) to execute the script as needed. Explosm is daily, XKCD is Mon, Wed, Fri (iirc), Sarah Scribbles is Wed, Sat.