import os
import xarray as xr
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def netcdf_to_text_chunks(nc_file, output_csv="data/processed_argo_data.csv"):
    ds = xr.open_dataset(nc_file)

    # Convert to pandas DataFrame
    df = ds.to_dataframe().reset_index()

    # Create descriptive text for each timestamp
    df["text"] = df.apply(
        lambda row: f"On {row['time'].strftime('%Y-%m-%d')}, temperature was {row['temperature']:.2f}°C and salinity was {row['salinity']:.2f} PSU.",
        axis=1,
    )

    # Save to CSV with text column for embedding
    df[["text"]].to_csv(output_csv, index=False)
    print(f"✅ Text chunks saved to {output_csv}")

def build_faiss_index(data_path="data/processed_argo_data.csv", index_path="vector_store"):
    df = pd.read_csv(data_path)
    texts = df["text"].tolist()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(texts, embeddings)

    os.makedirs(index_path, exist_ok=True)
    vector_store.save_local(index_path)
    print(f"✅ FAISS index saved at {index_path}")

if __name__ == "__main__":
    netcdf_to_text_chunks("data/sample_data.nc")
    build_faiss_index()
