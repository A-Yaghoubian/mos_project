from mlcroissant import Dataset

ds = Dataset(jsonld="https://huggingface.co/api/datasets/hewliyang/nisqa-vcc-mos/croissant")
records = ds.records("default")