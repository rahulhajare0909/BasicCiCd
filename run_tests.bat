pip install -r requirements.txt
pylint app --fail-under=6
pytest tests --html=report.html
