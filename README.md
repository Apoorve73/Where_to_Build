![Where_to_Build](https://socialify.git.ci/Apoorve73/Where_to_Build/image?description=1&forks=1&language=1&owner=1&pattern=Brick%20Wall&pulls=1&stargazers=1&theme=Dark)
# Where_to_Build
In this project we **aim** to build **new health centers** at places where there is a **lack of medical services** using a **dynamic mapping** system. The ***tools*** that we have used so far are **web scraping** , **python3**(for making our base code run).Website is constructed using **HTML, CSS, Bootstrap, Javascript, Flask(_WTForms,_Bootstrap,etc.), SQLAlchemy and Sqlite(as database for login information)**. 
The **coronavirus pandemic** has shown us all in just a few days how fragile our way of life really is. Basic certainties about our health, that of our loved ones and our normal way of life can no longer be taken for granted.Opening temporary or permanent **medical centers at the right place** for now is the basic aim so that for any sort of treatment no one has to travel long distances and can be cured at nearby places itself and medical services can reach a large number of people at same time.

**CHECK ```Demo.mp4``` for quick demonstration.** 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites Installation

Install [python3(latest version)](https://www.python.org/downloads/).

In the project directory, open Terminal(Mac/Linux) or Command Prompt(Windows)

``` 
    pip install flask   
    pip install flask_bootstrap 
    pip install flask_wtf 
    pip install flask_sqlalchemy 
```
   
 ### Usage

Once done with the project setup, open the project in an [**IDE**](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments); for example - [**PyCharm**](https://www.jetbrains.com/pycharm/), [**Visual Studio Code**](https://code.visualstudio.com/), etc.


**NOTE** : ***Be sure to select appropriate interpreter. Sometimes it may get deselected.***

### From Command Line Interface

* Create Virtual Environment
```
pip install virtualenv

virtualenv myenv
```
### Mac / Linux User
```
source myenv/bin/activate
```
### Windows Users
```
myenv\Scripts\activate
```

* Head to the project directory containing ```main.py```

* Open Terminal(Mac/Linux)/Command Prompt (Windows) there.

* Follow accordingly :arrow_down:

  1. **Unix Bash (Linux, Mac, etc.):**
  ```
  $ export FLASK_APP=main/py
  $ flask run
  ```
  2. **Windows CMD:**
  ```
  > set FLASK_APP=main.py
  > flask run
  ```
  3. **Windows PowerShell:**
   ```
  > $env:FLASK_APP = "1"
  > flask run
  ```
* ### Output:
```
 $ flask run
 Serving Flask app "hello"
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

 * Copy `http://127.0.0.1:5000/` and open it in a browser and Voila!
 
 * For Quick Demo, click on `Get Demo Here` tab.
![Best among 2000 registered properties mapped for building new hospitals](https://github.com/Apoorve73/Where_to_Build/blob/master/Map_Dallas.png)

> ***Without using shell***
> 1. Open `main.py`
> 2. Hit `Run`, if using any IDE as mentioned above.

## Contribution
Pleas read [Contribution.md](https://github.com/Apoorve73/Where_to_Build/blob/master/contribution.md) :point_up_2: for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

**Initial Work**
1. [Apoorve Goyal](https://github.com/Apoorve73)
2. [Sanjana Maheshwari](https://github.com/sanjana-302)
3. [Saloni Gupta](https://github.com/salonigupta1)
 
