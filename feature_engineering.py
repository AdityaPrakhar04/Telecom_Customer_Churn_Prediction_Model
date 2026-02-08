class FeatureEngineering():
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X=X.copy()
        X['contract_x_tenure']=(X['tnf1__Contract']*X['remainder__Tenure in Months'])
        X['tenure_x_referrals']=(X['remainder__Tenure in Months']*X['remainder__Number of Referrals'])
        X['security_bundle']=(X['tnf2__Online Security_Yes']+X['tnf2__Online Backup_Yes']+X['tnf2__Premium Tech Support_Yes'])
        return X