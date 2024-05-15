Ensuring Code Quality
=====================

It is very useful when working in a team that your code is well written. You may remember what your code does, but your teammate who didn't write it should also be able to figure out what you're doing. To accomplish this, we will talk about using linting tools (with a focus on Python's Flake8) to ensure consistent code quality.

#. **Flake8**

    Flake8 is a tool for checking Python code quality. `The documentation can be found here <https://flake8.pycqa.org/en/latest/>`_ and it can be installed using::

        python -m pip install flake8

#. **Using Flake8**

    To use Flake8, within a shell you can run::

        flake8 path/to/code.py

    alternatively, to test multiple files you can use::

        flake path/to/code/

    to check the files within the directory. Using our example code::

        > flake8 mycybergis/uiuc.py 
            mycybergis/uiuc.py:24:80: E501 line too long (96 > 79 characters)
            mycybergis/uiuc.py:32:80: E501 line too long (86 > 79 characters)
            mycybergis/uiuc.py:35:80: E501 line too long (91 > 79 characters)
            mycybergis/uiuc.py:54:80: E501 line too long (80 > 79 characters)
            mycybergis/uiuc.py:57:80: E501 line too long (91 > 79 characters)
            mycybergis/uiuc.py:61:80: E501 line too long (82 > 79 characters)
            mycybergis/uiuc.py:62:80: E501 line too long (97 > 79 characters)

#. **Customizing Your Errors/Warnings**

    Flake8 enforces the `PEP8 code standards <https://peps.python.org/pep-0008/>`_ which are mostly intuitive after you've spent a bit of time with them.

    A list of the Flake8 error codes `can be found on this page of their documentation <https://flake8.pycqa.org/en/latest/user/error-codes.html>`_. If there are certain issues that you are fine ignoring, you can use the ``--ignore`` flag. For example::

        flake8 --ignore E501 mycybergis/uiuc.py
    
    You can also ignore a list of errors like::

        flake8 --ignore=E501,E722,F403,F405 mycybergis/uiuc.py

    Check out their `page on configuration <https://flake8.pycqa.org/en/latest/user/configuration.html>`_ for additional customization options.

#. **Breaking the Rules Occasionally**

    There are occasionally good reasons to break the rules and Flake8 allows you to include these kinds of exceptions. The ``# noqa`` statement at the end of a line of code will exclude that line from code quality assurance (NO Quality Assurance = NOQA). For example::

        import numpy as np  # noqa

#. **Linting in VSCode**

    Many (most?) of us work within VSCode which has it's own linting extensions for keeping your code quality consistent. `See their page on Linting <https://code.visualstudio.com/docs/python/linting>`_.


#. **Additional Recommendations**  

    We also recommend using good docstrings to help explain what each funciton/class is doing. `Our Github Pages tutorial covers this along with how you can turn your docstrings into documentation <https://cybergis.github.io/github-pages-demo/tutorial/autodocs.html>`_.