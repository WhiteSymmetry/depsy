heroku run --size=performance-l python update.py Person.set_scores --limit=1000000 --chunk=100
heroku run --size=performance-l python update.py Person.set_subscore_percentiles --limit=1000000 --chunk=100
heroku run --size=performance-l python update.py Person.set_impact --limit=1000000 --chunk=100
heroku run --size=performance-l python update.py Person.set_impact_percentiles --limit=1000000 --chunk=100
