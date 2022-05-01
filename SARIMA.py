import statsmodels.api as sm


class SARIMA(object):

    def __init__(self, train, test):
        self.train = train
        self.test = test
        self.model = sm.tsa.statespace.SARIMAX(train,
                                               order=(1, 1, 1),
                                               seasonal_order=(1, 1, 1, 24),
                                               enforce_stationarity=False,
                                               enforce_invertibility=False).fit(disp=False)

    def predict(self):
        return self.model.predict(self.test)
