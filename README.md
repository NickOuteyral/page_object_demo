# Page Object Automation Demo

In order to be able to run this script you'll need the latest version of Python, as well as Google Chrome v79. 
Also, there's an implementation of Selenium in this script that should be downloaded automatically if you use a dev 
environment such as PyCharm but if you don't you'll need to download it manually. The easiest way to do so is with the
pip3 packet manager which comes bundled with python. Simply open a console and type `pip3 install selenium`. If you get
a message saying that pip3 isn't recognized as a console command you might need to add python and pip3 to the System's path.
You do that by editing the environment variables, for Windows you can find the proper how to in the following link: 
`https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/`. This tutorial uses python 34 in the 
path, you should use whichever version of python and pip that you have downloaded. The default directory for python and 
pip in Windows is something like `C:\Users\YourUser\AppData\Local\Programs\Python\Python38-32` for python and
`C:\Users\YourUser\AppData\Local\Programs\Python\Python38-32\Scripts` for pip. AppData is a hidden folder so you might 
need to enable hidden folders to be visible

You have two main ways of executing these tests. The first is by console commands, for which you'll need to open a console
terminal, navigate to the download location of the repository and type `py test_aliexpress.py` in Windows. In MacOS and
Linux it should be `python3 test_aliexpress.py`. The test result will be shown in the same console. Speaking of which, if 
the scripts fails to run due to some chromedriver issues you should update the selenium on your pc with the `pip install
 -U selenium` line

The other option is to run it from a dev environment, such as PyCharm. If you want to edit the code and do things such as
debugging, it's recommended. You can download a free edition of PyCharm at `https://www.jetbrains.com/pycharm/`

-------------------------------

## test_aliexpress

In this file we can find the test for this occasion. The TestClass itself uses the unittest framework which allows for 
a clear test status at the end of the run. Should there be multiple tests it will inform how many tests passed and how 
many failed. Furthermore it's divided into 3 parts, those being the setUp, test_ and tearDown methods

### setUp

This method fires up the browser and has a few variables that allow for quick parameter changes in case you want to assert
a different element, a different result page, a different search query or all of the above

### test_elements_sold

This method is the main logic of the TestClass. It takes advantage of the page object structure implemented for the site
structure so that most of the logic consists in calling methods that already do the work for you. This allows for someone
with little experience to write their own tests, assuming that the current pre-built tools are enough for the tests

### tearDown

It simply closes the WebDriver after all tests are run