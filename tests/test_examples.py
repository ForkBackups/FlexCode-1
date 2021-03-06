import numpy as np
import flexcode
from flexcode.regression_models import NN

def test_example():
  # Generate data p(z | x) = N(x, 1)
  def generate_data(n_draws):
    x = np.random.normal(0, 1, n_draws)
    z = np.random.normal(x, 1, n_draws)
    return x.reshape((len(x), 1)), z.reshape((len(z), 1))

  x_train, z_train = generate_data(10000)
  x_validation, z_validation = generate_data(10000)
  x_test, z_test = generate_data(10000)

  # Parameterize model
  model = flexcode.FlexCodeModel(NN, max_basis=31, basis_system="cosine",
                                 regression_params={"k":20})

  # Fit and tune model
  model.fit(x_train, z_train)
  model.tune(x_validation, z_validation)

  # Estimate CDE loss
  model.estimate_error(x_test, z_test)

  cdes, z_grid = model.predict(x_test, n_grid=200)

  assert True
