import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#load dataset
data = fetch_movielens(min_rating=4.0)
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)

def recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape
    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        score = model.predict(user_id, np.arange(n_items))
        recommendations = data['item_labels'][np.argsort(-score)]
        print('recommendations for user %s \n', user_id)
        for recom in recommendations[:3]:
            print(recom)

recommendation(model, data, [3, 35, 23])