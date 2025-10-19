from netCDF4 import Dataset
import pandas as pd

def convert_netcdf_to_csv(nc_file, csv_file):
    ds = Dataset(nc_file, "r")
    data = {
        "temperature": ds.variables["TEMP"][:].flatten().tolist(),
        "salinity": ds.variables["PSAL"][:].flatten().tolist(),
        "depth": ds.variables["DEPH"][:].flatten().tolist(),
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    return csv_file
