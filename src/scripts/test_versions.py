import pandas as pd
import geopandas as gpd
from osgeo import gdal
import earthaccess
import openpyxl
import pystac_client

pandas_v = pd.__version__
geopandas_v = gpd.__version__
gdal_v = gdal.__version__
earthaccess_v = earthaccess.__version__
openpyxl_v = openpyxl.__version__
pystac_v = pystac_client.__version__

print (f'Pandas {pandas_v}, GeoPandas {geopandas_v}, GDAL {gdal_v}, Earthaccess {earthaccess_v}, OpenPyXl {openpyxl_v}, pySTAC {pystac_v}')