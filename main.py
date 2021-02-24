
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')
data = pd.read_csv('BedUtilization.csv')

plt.figure(figsize=(20,8))
plt.ylim(0, 8000)
overcapacity_prediction = sns.barplot(x='state',y='critical_staffing_shortage_anticipated_within_week_no',data = data)
plt.setp(overcapacity_prediction.get_xticklabels(), rotation=90)
overcapacity_prediction.tick_params(labelsize=10)
overcapacity_prediction.set_ylabel("Bed Shortage Prediction",fontsize=20)
overcapacity_prediction.set_xlabel("State",fontsize = 20)

# ICU Bed Occupancy

plt.figure(figsize=(20,8))
plt.ylim(0,8000)
bed_occupancy = sns.barplot(x='state',y='staffed_adult_icu_bed_occupancy', data = data)

plt.setp(bed_occupancy.get_xticklabels(), rotation=90)
bed_occupancy.tick_params(labelsize=10)
bed_occupancy.set_ylabel("ICU Bed Occupancy",fontsize=20)
bed_occupancy.set_xlabel("State",fontsize = 20)

# Overcapacity

Occupancy = data['staffed_adult_icu_bed_occupancy']
Coverage = data['staffed_adult_icu_bed_occupancy_coverage']
data['overcapacity'] = data['staffed_adult_icu_bed_occupancy'] - data['staffed_adult_icu_bed_occupancy_coverage']

plt.figure(figsize=(20,8))
plt.ylim(0,8000)
Overcapacity = sns.barplot(x='state',y='overcapacity', data = data)
plt.setp(bed_occupancy.get_xticklabels(), rotation=90)
Overcapacity.tick_params(labelsize=10)
Overcapacity.set_ylabel("Overcapacity",fontsize=20)
Overcapacity.set_xlabel("State",fontsize = 20)

# Anticipated ICU Bed shortage VS. Overcapacity

overcapacity_2 = dict(
        type='choropleth',
           locations = data['state'],
           locationmode = 'USA-states',
           z = data['overcapacity'],
            marker = dict(line = dict(color = 'rgb (255,255,255)', width =2)),
           colorbar = {'title' : 'Overcapacity'}
           )

layout = dict(title = 'Bed Overcapacity in USA States',
             geo = dict(scope = 'usa', showlakes = True))

Nationwide_overcapacity = go.Figure(data = [overcapacity_2],layout=layout)

Nationwide_overcapacity.show()



