nbsphinx
========

Often we create Jupyter Notebooks to demo the usage of our software and it's convenient for those notebooks to serve as examples on our sites. For example, `Geopandas example gallery does this <https://geopandas.org/en/stable/gallery/index.html>`_ (`see their conf.py <https://github.com/geopandas/geopandas/blob/460d9403a0942e67b3f4f5e73aa7589febef84b3/doc/source/conf.py>`_). This can be done with `nbsphinx <https://nbsphinx.readthedocs.io/en/0.8.8/>`_

#. **Notebooks within** ``docs/``

   When a notebook is within docs, you just have to add it's path to the toc tree or use ``:glob:`` like `in the Geopandas gallery <https://github.com/geopandas/geopandas/blob/460d9403a0942e67b3f4f5e73aa7589febef84b3/doc/source/gallery/index.rst>`_. A glob directive works like globs in Bash terminals (``ls *``).

   A "regular" toctree command would look just like if we added a new page. A glob directive might look like::

        .. nbgallery::
            :name: nbshpinx-gallery
            :glob:

            ./*
    
   This example is from the `geopandas gallery index.rst <https://github.com/geopandas/geopandas/blob/460d9403a0942e67b3f4f5e73aa7589febef84b3/doc/source/gallery/index.rst>`_.

#. **Notebooks Elsewhere**

   We will spend more time talking about including notebooks which are somewhere other than within ``docs/``. You can't just use "../" because the file must reside within your docs folder, but this can be done with `nbsphinx-link <https://github.com/vidartf/nbsphinx-link>`_.

   To use nbsphinx-link, you make a .nblink JSON file in the location where you want the notebook to be within your ``docs/`` directory. An example from the nbsphinx-link github is below::

        {
            "path": "relative/path/to/notebook"
        }


#. **Getting Test.ipynb in our Site**

   There is a sample notebook in ``notebooks/Test.ipynb`` which we want to include in our site.

   Make a folder "notebooks" in "docs" and create a file within ``docs/notebooks/`` called "Test.nblink". Copy/paste the following into it::

        {
            "path": "../../notebooks/Test.ipynb"
        }
   
#. **Creating An Example Page**
   
   You can link the notebook directly (by adding it to your index.rst toc tree), but we will create an Examples page and link it there.

   The first step then is to make an Examples page, ``docs/examples.rst`` and copy/paste the below into it::

        Examples
        ========

        .. toctree::
           :maxdepth: 2

           notebooks/Test
    
   Remember to also add your examples page to the main toctree (in index.rst)!

#. **Make HTML and Check it Out**

   In the terminal, from ``docs/`` run the ``make html`` command and check out the results.


.. tip::

    To see the widgets in your notebooks, you want to go "Settings" and select "Save Widget State Automatically". 


.. figure:: ../_static/img/SaveWidgetStateAutomatically.png

    Saving the widget state in JupyterLab