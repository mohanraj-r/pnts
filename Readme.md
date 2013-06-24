Use `pip install -r requirements.txt` to use code coverage.

Code Coverage
-------------
Code coverage stats is obtained using the `coverage` module. 

To obtain code coverage run 

```
coverage run --omit test_vending_machine.py test_vending_machine.py 
coverage html
```

HTML report can be found in `htmlcov/index.html`

Current code coverage is `100%`