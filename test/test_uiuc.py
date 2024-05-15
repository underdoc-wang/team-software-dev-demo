from shapely.geometry import Polygon
import sys
sys.path.insert(0, "./mycybergis")
import uiuc  # noqa


def test_uiuc_polygon_is_polygon():
    """Tests that the get_uiuc_polygon function returns a Polygon"""
    assert isinstance(uiuc.get_uiuc_polygon(), Polygon)

# uncomment if you want to see a test fail
# def test_if_1_equals_2():
#     assert 1 == 2
