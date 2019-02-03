import pandas as pd
import statsmodels.formula.api as sm

def regression_test(a, b, reg_name):
  {
    'a': [i.result for i in a],
    'b': [i.result for i in b]
  }
  normal_ols = sm.ols(formula='a ~ b',
                          data=df).fit()
  yield PipelineSuccess(reg_name, normal_ols.summary())


