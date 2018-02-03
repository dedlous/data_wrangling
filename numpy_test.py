# # import numpy as np
# # #
# # # # Subway ridership for 5 stations on 10 different days
# # ridership = np.array([
# #     [0, 0, 2, 5, 0],
# #     [1478, 3877, 3674, 2328, 2539],
# #     [1613, 4088, 3991, 6461, 2691],
# #     [1560, 3392, 3826, 4787, 2613],
# #     [1608, 4802, 3932, 4477, 2705],
# #     [1576, 3933, 3909, 4979, 2685],
# #     [95, 229, 255, 496, 201],
# #     [2, 0, 1, 27, 0],
# #     [1438, 3785, 3589, 4174, 2215],
# #     [1342, 4043, 4009, 4665, 3033]
# # ])
# #
# # # # Change False to True for each block of code to see what it does
# # #
# # # # Accessing elements
# # if False:
# #     print  (ridership[1, 3])
# #     print   (ridership[1:3, 3:5])
# #     print   (ridership[1, :])
# #
# # # # Vectorized operations on rows or columns
# # if False:
# #     print    (ridership[0, :] + ridership[1, :])
# #     print    (ridership[:, 0] + ridership[:, 1])
# #
# # # # Vectorized operations on entire arrays
# # if False:
# #     a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# #     b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
# #     print (a + b)
# #
# #
# # def mean_riders_for_max_station(ridership):
# #     '''
# #     Fill in this function to find the station with the maximum riders on the
# #     first day, then return the mean riders per day for that station. Also
# #     return the mean ridership overall for comparsion.
# #
# #     Hint: NumPy's argmax() function might be useful:
# #     http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
# #     '''
# #     overall_mean = None  # Replace this with your code
# #     mean_for_max = None  # Replace this with your code
# #
# #     return (overall_mean, mean_for_max)
# #
# #
#
# import numpy as np
#
# # Change False to True for this block of code to see what it does
#
# # NumPy axis argument
# if True:
#     a = np.array([
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ])
#
#     print (a.sum())
#     print (a.sum(axis=0))
#     print  (a.sum(axis=1))
#
# # Subway ridership for 5 stations on 10 different days
# ridership = np.array([
#     [0, 0, 2, 5, 0],
#     [1478, 3877, 3674, 2328, 2539],
#     [1613, 4088, 3991, 6461, 2691],
#     [1560, 3392, 3826, 4787, 2613],
#     [1608, 4802, 3932, 4477, 2705],
#     [1576, 3933, 3909, 4979, 2685],
#     [95, 229, 255, 496, 201],
#     [2, 0, 1, 27, 0],
#     [1438, 3785, 3589, 4174, 2215],
#     [1342, 4043, 4009, 4665, 3033]
# ])
# print (ridership.mean(axis=0))
# print (ridership.mean(axis=1))
# def min_and_max_riders_per_day(ridership):
#     '''
#     Fill in this function. First, for each subway station, calculate the
#     mean ridership per day. Then, out of all the subway stations, return the
#     maximum and minimum of these values. That is, find the maximum
#     mean-ridership-per-day and the minimum mean-ridership-per-day for any
#     subway station.
#     '''
#     max_daily_ridership = None  # Replace this with your code
#     min_daily_ridership = None  # Replace this with your code
#
#     return (max_daily_ridership, min_daily_ridership)

import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[0, 0, 2, 5, 0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [95, 229, 255, 496, 201],
          [2, 0, 1, 27, 0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

# Change False to True for each block of code to see what it does

# DataFrame creation
if True:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print  (df_1)

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print (df_2)

    print (ridership_df.iloc[0])
    print (ridership_df.loc['05-05-11'])
    print   (ridership_df['R003'])
    print   (ridership_df.iloc[1, 3])

    print (ridership_df.iloc[1:4])

    print (ridership_df[['R003', 'R005']])


    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print (df)
    print (df.sum())
    print (df.sum(axis=1))
    print (df.values.sum())

    if 1:
        s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        df = pd.DataFrame({
            'a': [10, 20, 30, 40],
            'b': [50, 60, 70, 80],
            'c': [90, 100, 110, 120],
            'd': [130, 140, 150, 160]
        })
