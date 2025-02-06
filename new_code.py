import gdown

def download_file_from_google_drive(file_id, destination):
    """
    Downloads a file from Google Drive using its file ID.

    Args:
        file_id (str): The Google Drive file ID.
        destination (str): The path to save the downloaded file.
    """
    # Construct the download URL
    url = f"https://drive.google.com/uc?id={file_id}"
    
    # Use gdown to download the file
    gdown.download(url, destination, quiet=False)

    # Load the pretrained models

# download_file_from_google_drive('1ZodeH37Nd4ZbA0_1G_MkLKuuiyk7VUXR', '/home/j/jayaverma/exsclaim/exsclaim/figures/checkpoints/classifier_model.pt')
# download_file_from_google_drive('1Hh7IPTEc-oTWDGAxI9o0lKrv9MBgP4rm', '/home/j/jayaverma/exsclaim/exsclaim/figures/checkpoints/object_detection_model.pt')
# download_file_from_google_drive('1rZaxCPEWKGwvwYYa8jLINpUt20h0jo8y', '/home/j/jayaverma/exsclaim/exsclaim/figures/checkpoints/text_recognition_model.pt')
# download_file_from_google_drive('1B4_rMbP3a1XguHHX4EnJ6tSlyCCRIiy4', '/home/j/jayaverma/exsclaim/exsclaim/figures/checkpoints/scale_bar_detection_model.pt')
# download_file_from_google_drive('1oGjPG698LdSGvv3FhrLYh_1FhcmYYKpu', '/home/j/jayaverma/exsclaim/exsclaim/figures/checkpoints/scale_label_recognition_model.pt')

test_json =  {
    "name": "nature-nano",

    "journal_family": "nature",

    "maximum_scraped": 3,
     "html_folder": "/home/j/jayaverma/exsclaim/exsclaim/html_files" ,

    "sortby": 'relevant',

    "query":


    { "search_field_1":

        {   "term":"Ag nanoparticle",

            "synonyms":["Ag nanoparticles", "silver nanoparticle", "silver nanoparticle", "nanoparticles of silver", "AgNPs", "AgNP", "Ag NPs", "silver NPs", "silver NP"] } },

    "open": True,

    "save_format": ["boxes", "save_subfigures" ],

    "logging": ["print", "exsclaim.log"]
    }
#test_json = '/home/j/jayaverma/exsclaim/query/nature-nano.json'

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

# from exsclaim.visualize_dataset import *
# from itables import init_notebook_mode
# init_notebook_mode(all_interactive=True)

# df = read_jsons('/home/j/jayaverma/exsclaim/output/nature-nano/exsclaim.json')
# print(df)