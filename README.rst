.. contents::

Introduction
============

Bootstrap theme for Plone

Installation
============

Using Buildout
--------------

Add ``vs.bootstrap.plonetheme`` to eggs section of your instance::

 [instance]
 …
 eggs =
     …
     vs.bootstrap.plonetheme

Using zip
---------

#. Create a zip file::

    $ git clone git://github.com/veit/vs.bootstrap.plonetheme.git
    $ cd vs.bootstrap.plonetheme
    $ git archive --format=zip --prefix=bootstrap/ HEAD:src/vs/bootstrap/plonetheme/static/ > bootstrap.zip

#. Import this zip file in the *Import theme* tab of the *Theme Settings* view:
   ``@@theming-controlpanel``.
#. Activate theme in the *Basic settings* tab:

   #. Select the theme ``vs.bootstrap.plonetheme``
   #. Enable theme
   #. Save

