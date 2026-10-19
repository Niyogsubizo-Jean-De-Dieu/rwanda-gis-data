# Rwanda Area Profile – Physical, Social & Environmental GIS Toolkit

Open training notebooks that turn free data into a clear profile of an area: its **land, climate, people, livelihoods and environmental risks**.
They run in **Google Colab** (free, works on a phone browser). No GIS software, no account sign-in and no powerful laptop needed – the data for each area is stored in this repository.

**Who it is for:** students and trainers, planners and local-government staff, NGOs and community groups, researchers.

## Quick start

1. Open the notebook in Colab:
   [**Open Rwanda_Area_Profile_GIS.ipynb in Colab**](https://colab.research.google.com/github/Niyogsubizo-Jean-De-Dieu/rwanda-gis-data/blob/main/Rwanda_Area_Profile_GIS.ipynb)
2. Run **Cell 1** and **Cell 2** (setup, about 1 minute).
3. Run **Cell 3** (it already points to this repository and to `data/gicumbi`).
4. Run the remaining cells **top to bottom** (tap ▶). Each cell prints the maps, charts and tables it creates.
5. Run the **last cell** to download a Word report with everything.

Tip on a phone: if the page looks cramped, switch the browser to "Desktop site".

## What you get

| Theme | Outputs |
|---|---|
| 1. Physical environment | elevation, slope classes, rainfall and temperature, soil texture and pH, land cover, surface water |
| 2. People and settlements | sectors, population size / density / growth, built-up area growth |
| 3. Livelihoods and economy | night-time lights, mapped services and enterprises (where available), your own data from a CSV |
| 4. Environment and risks | forest cover and tree-cover loss, cropland on steep slopes (erosion hot-spots), vegetation health trend |
| 5. Area snapshot | headline indicators and a Word report with every map, chart and table plus data sources |

## Repository contents

```
Rwanda_Area_Profile_GIS.ipynb      Notebook for everyone (reads the data from this repo)
00_Export_Study_Area_Data.ipynb    For maintainers: creates a data folder for a new area
data/
  gicumbi/                         Data for Gicumbi District (clipped to the district)
    boundary_district.geojson, boundary_sectors.geojson, rwanda_districts.geojson
    dem.tif, worldcover.tif, water_occurrence.tif, treecover2000.tif, lossyear.tif
    soil_texture.tif, soil_ph_x10.tif, pop_2020.tif, built_2020.tif, ntl_latest.tif
    climate_monthly.csv, rain_annual.csv, pop_timeseries.csv,
    built_timeseries.csv, ntl_timeseries.csv, ndvi_timeseries.csv
    meta.json                      Area name, map projection, years, export date
```

All rasters share the same map projection (see `meta.json`). Elevation, land cover, water and forest layers are at 30 m, population and built-up at 100 m, soils at 250 m and night lights at 500 m.

## Add another area (for maintainers)

1. Open [`00_Export_Study_Area_Data.ipynb`](https://colab.research.google.com/github/Niyogsubizo-Jean-De-Dieu/rwanda-gis-data/blob/main/00_Export_Study_Area_Data.ipynb) in Colab. It needs a free [Google Earth Engine](https://earthengine.google.com/) project, but only the maintainer needs this.
2. Enter the district name and a folder name (for example `musanze`), then run the cells. It downloads a zip.
3. Unzip it into `data/<area>/` in this repository, then commit and push.
4. Users change the folder in Cell 3 of the main notebook (for example `data/musanze`).

Use the UTM zone **EPSG:32735** for districts west of about 30°E (for example Rusizi or Rubavu) and **EPSG:32736** for districts east of it.

## Using your own local data

Cell **3C** creates a CSV template (indicator, category, value, year, source). Fill it in with local figures (for example employment by sector, crops, services) and upload it – the notebook turns it into charts and tables for your report.

## Data sources

| Layer | Source |
|---|---|
| Administrative boundaries | geoBoundaries (Runfola et al., 2020) |
| Elevation | NASA SRTM 30 m |
| Rainfall | CHIRPS (Funk et al., 2015) |
| Temperature | ERA5-Land (Muñoz Sabater, 2019) |
| Soils | OpenLandMap (texture and pH, 250 m) |
| Land cover | ESA WorldCover 2021 (10 m, resampled to 30 m) |
| Surface water | JRC Global Surface Water (Pekel et al., 2016) |
| Population | WorldPop (modelled, 100 m) |
| Built-up area | GHSL GHS-BUILT-S (JRC) |
| Night lights | VIIRS annual night-time lights |
| Forest change | Hansen et al. global forest change |
| Vegetation | MODIS NDVI |
| Services and enterprises | OpenStreetMap contributors (where available) |

The notebook adds full references to the report it generates. Each dataset has its own terms of use – check them before reusing the data outside training.

## Limitations – please read

- These are **open global datasets**, modelled or satellite-derived. They are good for a consistent first look but have limited accuracy at local scale.
- Population figures are **modelled estimates** and can differ from the national census.
- OpenStreetMap coverage is incomplete and uneven.
- Always **validate key numbers with local and national sources** (for example NISR, REMA, RWB, RAB, MINALOC) before taking decisions.

## Troubleshooting

- **"Could not clone the repository"** – the repository must be public.
- **A cell fails after a restart** – use *Runtime → Run all* from Cell 1, or run the cells again from the top.
- **File not found in Cell 3** – check that the folder name matches an existing folder under `data/`.

## Licence and contact

Add a licence for the notebooks (for example MIT) in a `LICENSE` file and your contact details here.
