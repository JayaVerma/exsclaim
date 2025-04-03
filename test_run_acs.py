# {
#     "name": "acs-nano",

#     "journal_family": "acs",

#     "maximum_scraped": 2,

#     "sortby": "relevant",

#     "query":
#     {
#         "search_field_1":
#         {
#             "term":"nano",
#             "synonyms":["nanoparticle"]
#         }
#     },

#     "open": true,

#     "save_format": ["boxes"],

#     "logging": ["print", "exsclaim.log"]
# }


test_json =  {
    "name": "acs-nano",

    "journal_family": "acs",

    "html_folder": "/home/j/jayaverma/exsclaim/exsclaim/html_files" ,

    "maximum_scraped": 2,

    "sortby": 'relevant',

    "query":

    {
        "search_field_1":
        {
            "term":"nano",
            "synonyms":["nanoparticle"]
        }
    },

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
