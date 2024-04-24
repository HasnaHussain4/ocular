## Eye Diseases Prediction

- first create a virtual environment

```
python3 -m venv eye
source  eye/bin/activate
```

- In next step  you have to install all the required packages. You can use pip for this task:

```
pip3 install -r  requirements.txt
```

> if u have multiple pip versions ensure to use version along with  command like : `pip3.11 install -r requirments.txt` instead of just `pip3 install -r requirments.txt`
This will install required packages

- in the final step run

```
streamlit run main.py
```