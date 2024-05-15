Deploying to Github Pages
=========================

We are going to deploy our site to Github Pages using Github Actions. 


#. **Actions and Workflows**

   Github has created a good video covering Github Actions (I promise this one isn't a rickroll):

   .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/cP0I9w2coGU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

   .. seealso::

        The Github Docs `Understanding Github Actions <https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions>`_ page is helpful, as is the `Using workflows <https://docs.github.com/en/actions/using-workflows>`_ page. For a hands-on tutorial, checkout `Quickstart for Github Action <https://docs.github.com/en/actions/quickstart>`_
   

#. **Workflow for Building Site and Pushing**

   The workflow below can be used for building a sphinx site and pushing it to Github::

        name: Sphinx build

        on: push

        jobs:
          sphinx-build:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v2
            - name: Build HTML
              with:
                pre-build-command: "apt install -y pandoc"
              uses: ammaraskar/sphinx-action@0.4
            - name: Upload artifacts
              uses: actions/upload-artifact@v1
              with:
                name: html-docs
                path: docs/_build/html/
            - name: Deploy
              uses: peaceiris/actions-gh-pages@v3
              if: github.ref == 'refs/heads/main'
              with:
                github_token: ${{ secrets.GITHUB_TOKEN }}
                publish_dir: docs/_build/html

   Let's break down the steps:

   #. First, we checkout the repo.
   #. Next, we build the sphinx page. By default, it will install packages within ``docs/requirements.txt``, but we also need the container to install pandocs for everything to work.
   #. Next, we upload the built site.
   #. Deploy the site. 

#. **Adding This Workflow to Your Repo**

   Let's create a folder (in ``github-pages-demo``, not ``docs``) called ".github" and then a folder within that called "workflows". Within that folder, create a file called "SphinxBuild.yml" and copy/paste the above code into.

#. **Pushing The Repo**

   Add and commit your changes, then push it!::

        git add .
        git commit -a
        git push origin main

   Let's check on our repo to see if the action ran. Go to Github and find your fork of the repo. You should see an "Actions" tab. We can see our Actions here:

   .. figure:: ../_static/img/GithubActionsPage.png

        The Github Actions page for the repo.
    

   You can also click on workflow runs to get details and logs on your workflows as shown below:

   .. figure:: ../_static/img/CheckingJobLogs.png

        Workflow details


#. **Github Pages**

   Let's see if our page is up! Go to ``https://<your github username>.github.io/github-pages-demo``. You should see a 404 eror. That's because we have to enable Github pages first. However, you go to the repo's page, you'll notice a new branch: ``gh-pages``. This is our built site!

   So how do we get this working? On the Github Repo's page, go to the "Settings" tab, then in the menu select "Pages". This should bring you to the page below:

   .. figure:: ../_static/img/SettingsGithubPages.png

        Github Pages page in the Settings of your repo.

   Under the "Source" heading you will see a dropdown that says "None". Click on the dropdown and select "gh-pages" (this is where our workflow uploads the built site). For the folder dropdown, we can leave it as "/ (root)". When in doubt, you could check that branch to look for where your built site went. Click save. It will take a couple of minutes for the 404 error to go away, but your page should eventually show up!
