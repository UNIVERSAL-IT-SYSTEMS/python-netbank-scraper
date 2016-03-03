# python-netbank-scraper
Export transactions from netbank account using python and selenium driver

Install Python requirements

```
pip install -r requirements.txt
```

Set Netbank ID and Password environment variables

```
export NETBANK_ID=123456789
export NETBANK_PASS=123455
```

Run.sh to start selenium container and start vnc viewer, once that's up and running run netbank script.

```
bash run.sh
python netbank.py
```


##Resources

[http://selenium-python.readthedocs.org/locating-elements.html](http://selenium-python.readthedocs.org/locating-elements.html)
[https://saucelabs.com/resources/selenium/css-selectors](https://saucelabs.com/resources/selenium/css-selectors)
