import folium
import geopandas as gpd
from shapely.geometry import Polygon
from typing import List


def get_uiuc_polygon() -> Polygon:
    """
    Returns a shapely.geometry.Polygon surrounding UIUC.

    Returns:
        shapely.geometry.Polygon representing UIUC

    Todo:
        Add other places!
    """
    lats = [40.0837, 40.0835, 40.1163, 40.116, 40.098, 40.098, 40.0837]
    lons = [-88.2095, -88.2469, -88.24, -88.219, -88.219, -88.2096, -88.2095]
    return Polygon(zip(lons, lats))


def get_uiuc_gdf() -> gpd.GeoDataFrame:
    """
    Returns a gpd.GeoDataFrame representing UIUC. Uses :func:`mycybergis.uiuc.get_uiuc_polygon`.

    Returns:
        gpd.GeoDataFrame representing UIUC.

    See Also:
        :func:`mycybergis.uiuc.get_uiuc_polygon`
    """
    return gpd.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[get_uiuc_polygon()])


def get_map_of_uiuc(center: List[float] = [40.098, -88.219], zoom: int = 11) -> folium.Map:
    """
    Creates and returns a folium.Map instance of UIUC.

    Args:
        center (List[float]): the lon, lat for the center of the map.
        zoom (int): the starting level of zoom.

    Returns:
        folium.Map showing UIUC

    Tip:
        Maps are fun!
    """
    m = folium.Map(center, zoom_start=zoom)
    folium.GeoJson(get_uiuc_polygon()).add_to(m)
    return m


def get_uiuc_buffered_gdf(buffer: float = 1000, buffer_crs: str = "ESRI:102003",
                          output_crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
    """
    Returns a gpd.GeoDataFrame of UIUC with a buffer of size `buffer` in `buffer_crs` units
    and returns the GeoDataFrame in crs `output_crs`.

    Args:
        buffer (float): size of the buffer in `buffer_crs` units. Default is 1000.
        buffer_crs (str): authority string for Coordinate Reference System to calculate buffer on
        output_crs (str): authority string for return gpd.GeoDataFrame

    Returns:
        gpd.GeoDataFrame of UIUC with buffer
    """
    uiuc = get_uiuc_gdf()
    uiuc = uiuc.to_crs(buffer_crs)
    uiuc.geometry = uiuc.geometry.buffer(buffer)
    return uiuc.to_crs(output_crs)
