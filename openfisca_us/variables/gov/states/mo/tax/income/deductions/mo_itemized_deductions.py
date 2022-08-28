from openfisca_us.model_api import *


class mo_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Sum of Federal itemized deductions applicable to MO taxable income calculation"
    unit = USD
    definition_period = YEAR
    reference = "https://dor.mo.gov/forms/4711_2021.pdf"

    def formula(tax_unit, period, parameters):
        total_itemized_federal_deductions = add(tax_unit, period, ["casualty_loss_deduction", "charitable_deduction", "interest_deduction", "itemized_taxable_income_deductions", "medical_expense_deduction", "misc_deduction"])
        person = tax_unit.members
        social_security_tax = person("employee_social_security_tax", period)
        medicare_tax = person("employee_medicare_tax", period)
        self_employment_tax = person("self_employment_tax", period)
        net_state_income_taxes = tax_unit("mo_net_state_income_taxes", period)
        return (total_itemized_federal_deductions + social_security_tax + medicare_tax + self_employment_tax) - net_state_income_taxes