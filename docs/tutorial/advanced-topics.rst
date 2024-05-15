Advanced Topics
===============


Sphinx Themes
-------------

For more themes, check out the `Sphinx Themes Gallery <https://sphinx-themes.org/>`_.

Sphinx Alternatives
-------------------

There are many other alternatives to Sphinx for creating documentation.

* `MkDocs <https://www.mkdocs.org/>`_
* `pydoc <https://docs.python.org/3/library/pydoc.html>`_
* `Doxygen <https://www.doxygen.nl/>`_

Checking Workflows Locally
--------------------------

You may run into issues where workflows break and debugging them by pushing little changes can be a pain. I highly recommend the `act <https://github.com/nektos/act>`_ tool for running Github Actions locally. `act can be installed a variety of ways <https://github.com/nektos/act#installation>`_ and using it is as simple as::

    > act  # runs all of your workflows

Other Workflows
---------------

This Github doc on `Building and testing Python <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>`_ is very helpful!

Other useful workflows:

* `py-actions/flake8 <https://github.com/py-actions/flake8>`_ for checking the PEP style of your code.
