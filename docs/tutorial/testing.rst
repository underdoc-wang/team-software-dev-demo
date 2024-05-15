Testing Code
============

#. **Pytest** 

    For this section of the tutorial, we will use `Pytest <https://docs.pytest.org/en/8.2.x/>`_. You can install pytest using::

        pip install pytest

#. **Structuring Repo for Pytest**

    We recommend the following repo structure for testing:

        | test/
        | mycybergis/
        | ├── __init__.py
        | └── uiuc.py

    This allows us to keep all of our tests in a single directory for easily invoking pytest. It also allows us to easily point to our source directory (which will be useful later). However, there are also circumstances where placing tests elsewhere makes sense. Do what works best for you.

#. **Writing a Simple Test**

    Writing tests is hard. There are many edge-cases and bugs that can happen. We recommend test-first development, but we understand that science rarely follows that approach.

    Simple tests, even if they aren't comprehensive, can still be useful as sanity checks though. For example, for our simple package, we can make sure that our ``get_uiuc_polygon()`` function actually returns a polygon:

    .. code-block:: python

        def test_uiuc_polygon_is_polygon():
            """Tests that the get_uiuc_polygon function returns a Polygon"""
            assert isinstance(uiuc.get_uiuc_polygon(), Polygon)
    

#. **Running Pytest**

    You can run a simple test by simply pointing pytest to the directory with the tests::

        pytest test


#. **Code Coverage**

    Pytest can also be used to generate very simplistic coverage reports::

        pytest --cov-report=term --cov=mycybergis -s test

#. **Configuring Pytest**

    Pytest has a variety of options for configuration, allowing you to ignore or capture certain warnings. `See their documentation for future details <https://docs.pytest.org/en/stable/how-to/capture-warnings.html>`_.

