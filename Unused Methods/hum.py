from sklearn.neural_network import MLPRegressor
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPRegressor(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(7, ), random_state=1)

clf.fit(X, y)                         
print(clf.predict([[2., 2.], [-1., -2.]]))