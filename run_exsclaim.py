from exsclaim import journal
from exsclaim import pipeline
from exsclaim import tool
from exsclaim.pipeline import Pipeline

test_pipeline = Pipeline('./query/ecp-acs.json') #(test_json)
results = test_pipeline.run()