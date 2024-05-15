Intro to RST
============

Sphinx can use markdown and ReSTructured Text. We will focus on ReSTructured text for now.

#. **Basic RST Syntax**


   Take a moment to go over these RST Resources:

   
   * `Quick reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
   * `Restructured Text (reST) and Sphinx CheatSheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_


#. **RST Hyperlink**

   There are `a variety of ways to link and reference in RST <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html>`_, but we will just quickly review making basic external links.

   The syntax for an external link is:

   .. code-block::

    `My Text <https://www.google.com/>`_


   The above link looks like this: `My Text <https://www.google.com/>`_ Try adding a link to your index.rst page.


#. **Brief Intro to TOC**

   When you open ``docs/index.rst`` you will see::

        .. toctree::
           :maxdepth: 2
           :caption: Contents:

   This is a toc (table of contents) tree directive. It links to other pages and defines the tree of pages within your site. `See the Sphinx "Directives" page for more info <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_. If you want to add pages to your site, you add them to a toctree somewhere.


#. **Adding a Page**

   Now, we will use the toctree to add a page. Within the ``docs/`` folder, create a file called "test.rst". Give it a title by copy/pasting::

        Test
        ====
    
   into it and then run ``make html``. What happens?

   .. raw:: html

        <details>
            <summary>Click after you've run make html</summary>
            <p>You should see a red warning stating "WARNING: document isn't included in any toctree".</p>
        </details>

   To fix the issue, you add "test" (or the name of your file without the extension) to the toctree in index.rst. So your index.rst should look like::

        .. mycybergis documentation master file, created by
        sphinx-quickstart on Thu Jun  2 21:31:49 2022.
        You can adapt this file completely to your liking, but it should at least
        contain the root `toctree` directive.

        Welcome to mycybergis's documentation!
        ======================================

        .. toctree::
           :maxdepth: 2
           :caption: Contents:
            
           test



        Indices and tables
        ==================

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`



   .. note::

        `RST is very specific about whitespaces <https://docutils.sourceforge.io/0.4/docs/ref/rst/restructuredtext.html#whitespace>`_. You want the "test" line to line up with the rest of the toctree directives! If you get errors about it still not being in the toctree, check that you've saved your file and that the "test" lines up with the other toctree directives.
  
   Now, run ``make html`` again, you should see "Test" in your contents. You may notice the sidebar change when click the Test page. Sometimes when you change the toctree, you need to wipe everything (``make clean``) and rebuild (``make html``) to fix the toctree/sidebar.


#. **Adding a Video**

  Let's embed a video! You can do this by adding raw HTML to RST! In our test.rst page, let's add::

        .. raw:: html

            <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The output above allows us to put raw HTML into our RST, including an iframe for a video! The output can be seen below:

   .. raw:: html

	    <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

   To embed a different video, find it on YouTube, click "Share", then "Embed", and copy the iframe.

**More Info:**

* `Use Lists <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/lists.html>`_