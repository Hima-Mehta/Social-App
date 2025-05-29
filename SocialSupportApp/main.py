from datapipeline.data_preprocessing import create_data
from model_training import train_model
if __name__ == "__main__":
    create_data()
    train_model()