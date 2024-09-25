from google.cloud import aiplatform

# To create a tabular dataset
my_dataset = aiplatform.TabularDataset.create(
    display_name="my-dataset", gcs_source=['gs://path/to/my/dataset.csv'])



# You can also create and import a dataset in separate steps:
my_dataset = aiplatform.TextDataset.create(
    display_name="my-dataset")

my_dataset.import_data(
    gcs_source=['gs://path/to/my/dataset.csv'],
    import_schema_uri=aiplatform.schema.dataset.ioformat.text.multi_label_classification
)

# To get a previously created Dataset:
dataset = aiplatform.ImageDataset('projects/my-project/location/us-central1/datasets/{DATASET_ID}')
