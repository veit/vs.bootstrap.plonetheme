from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import vs.bootstrap.plonetheme


VS_BOOTSTRAP_PLONETHEME = PloneWithPackageLayer(
    zcml_package=vs.bootstrap.plonetheme,
    zcml_filename='testing.zcml',
    gs_profile_id='vs.bootstrap.plonetheme:testing',
    name="VS_BOOTSTRAP_PLONETHEME")

VS_BOOTSTRAP_PLONETHEME_INTEGRATION = IntegrationTesting(
    bases=(VS_BOOTSTRAP_PLONETHEME, ),
    name="VS_BOOTSTRAP_PLONETHEME_INTEGRATION")

VS_BOOTSTRAP_PLONETHEME_FUNCTIONAL = FunctionalTesting(
    bases=(VS_BOOTSTRAP_PLONETHEME, ),
    name="VS_BOOTSTRAP_PLONETHEME_FUNCTIONAL")
