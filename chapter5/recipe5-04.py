# 5.4 欠損クラス値の補完

# 問題
# カテゴリ特徴量に欠損値があり、予測した値で置き換えたい。

# k-最近傍法(KNN)クラス分類器を用いて、欠損値を予測する。

import numpy as  np
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.preprocessing import Imputer

# カテゴリ特徴量を持つ特徴量行列を作成
X = np.array([
  [0, 2.10, 1.45],
  [1, 1.18, 1.33],
  [0, 1.22, 1.27],
  [1, -0.21, -1.19]
])

# カテゴリ特徴量に欠損値を持つ特徴量行列を作成
X_with_nan = np.array([
  [np.nan, 0.87, 1.31],
  [np.nan, -0.67, -0.22]
])

# KNNクラス分類器を訓練
clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(X[:,1:], X[:,0])

# 欠損値のクラスを予測
imputed_values = trained_model.predict(X_with_nan[:,1:])

# 予測されたクラス値と他の特徴量を結合
X_with_imputed = np.hstack((imputed_values.reshape(-1, 1), X_with_nan[:,1:]))

# 2つの特徴量行列を結合
print(np.vstack((X_with_imputed, X)))

# 欠損値をその特徴量の最頻値で置き換える方法

# X_complete = np.vstack((X_with_nan, X))

# imputer = Imputer(strategy='most_frequent', axis=0)

# print(imputer.fit_transform(X_complete))
