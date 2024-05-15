Autodocs
========

The sphinx `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ extension helps us create documentation from our docstrings (comments on code for documenting functions). We will be using the `Napoleon <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_ extension and Google docstrings. 


#. **Basic Docstrings**

   Let's create and document a single function in ``mycybergis/uiuc.py``.

   An example of Google docstrings::

        Creates and returns a folium.Map instance of UIUC.

        Args:
            center (List[int]): the lon, lat for the center of the map.
            zoom (int): the starting level of zoom.

        Returns:
            folium.Map showing UIUC

   Create a basic function in the file and document it. If you can't think of anything, go super simple like ``add_two(number: int)`` which takes a number and returns the number plus two.

   .. tip::

        The ``Args/Arguments`` and ``Return/Returns`` sections take care of many use-cases, `but there are more options available <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstring-sections>`_. The include ``Raises`` (for errors), ``Warns`` (for warnings), ``Yield/Yields`` (for yielding values), but also stuff like ``Example``, ``Hint``, ``Tips``, and ``See Also``.

#. **Type Hinting**

   Python famously relies on `duck typing <https://en.wikipedia.org/wiki/Duck_typing>`_. This comes from the phrase "If it walks like a duck and it quacks like a duck, then it must be a duck" meaning that we generally don't care about the actual type of an object, but rather we care if the object acts the way we want (walking and quacking). This is very useful, but can make Python code hard to read. If you see a function signature ``do_the_thing(a, b, c)`` it's very difficult to understand what those arguments are supposed to be.
   
   `Type hinting <https://docs.python.org/3/library/typing.html>`_ can help us resolve those disambiguities and make our code more readable. Let's check an example from uiuc.py:

   .. code-block:: python

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

   It might be difficult to guess what ``center``, ``zoom``, and the return type might be without the docstrings and type hinting. Luckily, there is no guess work here, because it the type hints tell us exactly what we should be giving and getting! You can type hint built-in types (``int``, ``float``, ``str``, ``dict``, ...), but the built-in Python typing class also allows for more complex stuff like ``Any``, ``Union``, and ``Generic``. In the example above, we see a List of floats.

   Try adding type hints to your newly created function!

#. **Creating Autodocs with Autodoc and Napoleon**

   Now that we have our docstrings, we need to figure out how to generate documentation from it. Create a new page ("reference.rst") in the ``docs/`` and copy/paste the following into it::

        User Reference
        ==============

        User reference for mycybergis package.

        mycybergis.uiuc module
        ----------------------

        .. automodule:: mycybergis.uiuc
            :members:
    
   Let's break this down:

   * The heading of the page is "User Reference"
   * A short textual description
   * A subheading for the module within our package
   * The `autodoc directive <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives>`_ tells us to document the module ``mycybergis.uiuc`` and all of it's members (``:members:``).

#. **Add reference.rst to your TOC tree**

   Your toc tree on index.rst should include reference.rst::

        .. toctree::
           :maxdepth: 2
           :caption: Contents:

           tutorial
           reference

#. **Make HTML**

   Run ``make html`` in ``docs/`` and check the result! See if you can debug any formatting issues that come up!


   .. hint::

     One of the docstrings already in uiuc.py is intentially messed up so that it renders incorrectly. See if you can fix it.