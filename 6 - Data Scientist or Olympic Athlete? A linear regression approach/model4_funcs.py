import pandas as pd
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

os.chdir("/Users/alessandroquattrociocchi/Documents/Courses /FDS-Galasso/Final Project/olimpic/")

df_olympic = pd.read_csv('athlete_events.csv',index_col="ID")
df_noc = pd.read_csv('noc_regions.csv')
df = pd.merge(df_olympic, df_noc, on='NOC', how='left')
df = df_olympic.copy()
df_clean= df[df.Year >= 1960]
medal = ["Gold", "Silver","Bronze"]
df_clean = df_clean[df_clean['Medal'].isin(medal)]



df_clean['Age'] = df_clean.groupby(['Year', 'Sport'])['Age'].transform(lambda x: x.fillna(x.mean()))
df_clean['Height'] = df_clean.groupby(['Year', 'Sport'])['Height'].transform(lambda x: x.fillna(x.mean()))
df_clean['Weight'] = df_clean.groupby(['Year', 'Sport'])['Weight'].transform(lambda x: x.fillna(x.mean()))
df_clean.isna().sum()



def medal_feature(sport, event, sex, season, feature, data):

    if sport:
        data = data[data.Sport == sport]
    if event:
        data = data [data.Event == event]
    if sex:
        data = data [data.Sex == sex]
    if season:
        data = data [data.Season == season]

    return data, feature


def top_n_medalled_sport(sex,n,season,data):
    data = df_clean.loc[(df_clean['Sex'] == sex) & (df_clean['Season'] == season)]
    sports = data.groupby(['Sport']).size()
    top_medal_sports = pd.DataFrame({'Sports':sports.index, 'Count':sports.values})
    top_medal_sports.sort_values(['Count', 'Sports'], ascending=[False, True], inplace=True)
    plt.figure(figsize=(5,3))
    sns.barplot(x=top_medal_sports['Sports'][:n], y=top_medal_sports['Count'][:n])
    plt.xticks(rotation= 60)
    plt.title('Top Medalled Sports')
    plt.show()
    return list(top_medal_sports['Sports'][:n])


def top_n_events(sport, n, sex, data):
    data = data[df_clean.Sex == sex]
    z = []
    sports = data.groupby(['Sport']).size()
    top_medal_sports = pd.DataFrame({'Sports':sports.index, 'Count':sports.values})
    top_medal_sports.sort_values(['Count', 'Sports'], ascending=[False, True], inplace=True)
    top_sport = top_medal_sports['Sports'][:n].values.tolist()
    aux = data[ (data.Sport == sport)]
    disciplines  = aux['Event'].value_counts()[:n].index
    for x in disciplines:
        print(x)
        z.append(x)
    return  (z)



def regression_sport(data, feature):

    #start the calculation and the fitting
    Y = data.groupby('Year')[feature].mean()
    MSE = data.groupby('Year')[feature].var()
    Y_true = Y.values
    X = Y.index
    X = np.array(Y.index.tolist())
    X = X.reshape(-1,1)

    var = MSE.values
    var = np.where(np.isnan(var),0, var)
    mean_err = np.mean(var)
    var[var == 0] = mean_err

#make prediction
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y_true)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    slope = linear_regressor.coef_[0]
    intercept = linear_regressor.intercept_
    r2 = round(r2_score(Y_true, Y_pred),3)
    print('----------------------------------------')
    print('Regression features:')
    print("Slope: {:.2f}".format(round(slope, 2)))
    print("Intercept: {:.2f}".format(round(intercept, 2)))
    print("R_square: {:.2f}".format(round(r2, 3)))
    print('----------------------------------------')
    return (X,Y_true,Y_pred,var,r2)
    # plot the predict results


def regression_sport_visulization(data, feature):

    #start the calculation and the fitting
    Y = data.groupby('Year')[feature].mean()
    MSE = data.groupby('Year')[feature].var()
    Y_true = Y.values
    X = Y.index
    X = np.array(Y.index.tolist())
    X = X.reshape(-1,1)

    var = MSE.values
    var = np.where(np.isnan(var),0, var)
    mean_err = np.mean(var)
    var[var == 0] = mean_err

#make prediction
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y_true)  # perform linear regression
    Y_pred = linear_regressor.predict(X)  # make predictions
    slope = linear_regressor.coef_[0]
    intercept = linear_regressor.intercept_
    r2 = round(r2_score(Y_true, Y_pred),3)
    return (r2)
    # plot the predict results



def top_n_events_visulization(sport, n, sex, data):
    data = data[df_clean.Sex == sex]
    z = []
    sports = data.groupby(['Sport']).size()
    top_medal_sports = pd.DataFrame({'Sports':sports.index, 'Count':sports.values})
    top_medal_sports.sort_values(['Count', 'Sports'], ascending=[False, True], inplace=True)
    top_sport = top_medal_sports['Sports'][:n].values.tolist()
    aux = data[ (data.Sport == sport)]
    disciplines  = aux['Event'].value_counts()[:n].index
    for x in disciplines:
        z.append(x)
    return  (z)


def sports_overview(top_sports,n_events, sex, Season):
    res = {}
    feature = ["Height", "Weight", "Age"]
    for x in top_sports:
        top_events = top_n_events_visulization(sport = x, n = n_events, sex= sex, data = df_clean)
        for i in top_events:
            aux = []
            for y in feature:
                data, f = medal_feature(sport = x ,event = i  ,sex = sex ,season = Season ,feature = y  ,data = df_clean)
                r2 = regression_sport_visulization(data,f)
                aux.append(r2)
            res[i] = aux
    features_per_event = pd.DataFrame.from_dict(res, orient='index',columns=['Height', 'Weight', 'Age'])
    return features_per_event
