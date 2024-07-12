import rasterio
from rasterio.enums import Resampling

def saving(name):
    with rasterio.open(f'C:/Users/artem/OneDrive/Рабочий стол/frames/{name}') as src:
        data = src.read(
            out_shape=(src.count, int(src.height), int(src.width)),
            resampling=Resampling.bilinear
        )
        transform = src.transform

    with rasterio.open('test1_res.png', 'w', driver='PNG', height=data.shape[1], width=data.shape[2], count=src.count, dtype=data.dtype) as dst:
        dst.write(data)
    
    return 0