import matplotlib.pyplot as pl

data_names = ["Renault", "Toyota", "KIA", "Skoda", "Nissan", "Hyundai", "Volkswagen", "Peugeot", "Suzuki", "Mazda", "BMW", "Mitsubishi"]
data_values = [14642, 12618, 7599, 6211, 5317, 5118, 4698, 2780, 2618, 2547, 2408, 2356]

pl.pie(data_values, autopct="%.1f", radius=1.1, explode=[0.15] + [0 for _ in range(len(data_names)-1)])
pl.legend(bbox_to_anchor=(-0.2, 0.4, 0.2, 0.2),loc=0, labels=data_names)
pl.show()