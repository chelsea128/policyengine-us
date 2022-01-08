from openfisca_us.model_api import *


class spm_unit_snap(Variable):
    value_type = float
    entity = SPMUnit
    label = u"SPM unit SNAP subsidy"
    definition_period = YEAR
    unit = "currency-USD"
