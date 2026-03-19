from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score


def train_regression(df, features):
    df = df.dropna()

    train = df[df["Year"] <= 2022]
    test = df[df["Year"] > 2022]

    X_train = train[features]
    y_train = train["Production_tonnes"]

    X_test = test[features]
    y_test = test["Production_tonnes"]

    model = RandomForestRegressor(n_estimators=300, max_depth=6, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    return model, {
        "MAE": mean_absolute_error(y_test, preds),
        "R2": r2_score(y_test, preds)
    }


def train_classifier(df, features):
    df = df.dropna()

    train = df[df["Year"] <= 2022]
    test = df[df["Year"] > 2022]

    X_train = train[features]
    y_train = train["Disease_Risk"]

    X_test = test[features]
    y_test = test["Disease_Risk"]

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    return model, {
        "Accuracy": accuracy_score(y_test, preds)
    }