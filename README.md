**First Activate the virtual environment**
```
source /blockchain_env/bin/activate
```

**Install all the required packages**
```
pip3 install -r requierements.txt
```
**Run the test**

Make sure to activate virtual environment.

```
python3 -m pytest backend/tests
```