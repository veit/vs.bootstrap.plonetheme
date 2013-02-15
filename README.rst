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

#. Activate *Diazo theme support* in the Plone control panel *Add-ons*.
#. Import this zip file in the *Import theme* tab of the *Theme Settings* view:
   ``@@theming-controlpanel``.
#. Activate theme in the *Basic settings* tab:

   #. Select the theme ``vs.bootstrap.plonetheme``
   #. Enable theme
   #. Save

Customization
=============

You can customize the generated bootstrap files using the `Diazo Bootstrap
Framework <https://github.com/veit/diazo_bootstrap>`_.

Bug tracker
===========

Have a bug? Please create an issue here on GitHub that conforms with
`necolass guidelines <https://github.com/necolas/issue-guidelines>`_:

`Issues <https://github.com/veit/vs.bootstrap.plonetheme/issues>`_

Author
======

Veit Schiele

- `github <https://github.com/veit>`_
- `Twitter <https://twitter.com/VeitSchiele>`_

Copyrights and licenses
=======================

vs.bootstrap.plonetheme
 Copyright 2012 Veit Schiele

 Licensed under GPL version 2.

Diazo
 Copyright Plone Foundation

 Licensed under a BSD-like License.
 
Bootstrap
 Copyright 2012 Twitter, Inc.

 Licensed under the `Apache License v2.0
 <http://www.apache.org/licenses/LICENSE-2.0>`_.

Font Awesome
 Font licensed under the `SIL Open Font License
 <http://scripts.sil.org/OFL>`_.

 CSS, LESS, and SASS files licensed under the
 `MIT License
 <http://opensource.org/licenses/mit-license.html>`_.

 Pictograms licensed under the `CC BY 3.0 License
 <http://creativecommons.org/licenses/by/3.0/>`_.

