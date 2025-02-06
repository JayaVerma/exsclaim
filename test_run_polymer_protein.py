test_json =  {
    "name": "nature_polymer_protein_complex",

    "journal_family": "nature",

    "html_folder": "/home/j/jayaverma/exsclaim/exsclaim/html_files" ,

    "maximum_scraped": 5,

    "sortby": 'relevant',

    "query":

    { "search_field_1":

        {   "term":"polymer protein complex",

            "synonyms":["protein-polymer complex", "polymeric protein complex", "polymer-protein interaction", "polymer-protein assembly", "protein complex with polymer", "polymeric protein assembly"] } },

    "open": True,

    "save_format": ["boxes", "save_subfigures" ],

    "logging": ["print", "exsclaim.log"]
    }

from exsclaim import journal
print("journal imported successfully")
from exsclaim import pipeline
print("pipeline imported successfully")
from exsclaim import tool
print("tool imported successfully")

from exsclaim.pipeline import Pipeline
print("Pipeline imported successfully")
test_pipeline = Pipeline(test_json)
results = test_pipeline.run()

