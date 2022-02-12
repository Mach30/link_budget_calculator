import pint

# TODO -- remove this
# bad hacky way to include the calculator...
# must be modified to use __init__.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib', 'calculator'))
from link_budget_calculator import LinkBudgetCalculator

ureg = pint.UnitRegistry()
lcalc = LinkBudgetCalculator(ureg)

print(lcalc)