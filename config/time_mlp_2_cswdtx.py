from blocks.initialization import IsotropicGaussian, Constant

import data
from model.time_mlp import Model, Stream


n_begin_end_pts = 5     # how many points we consider at the beginning and end of the known trajectory

dim_embeddings = [
    ('origin_call', data.origin_call_train_size, 10),
    ('origin_stand', data.stands_size, 10),
    ('week_of_year', 52, 10),
    ('day_of_week', 7, 10),
    ('qhour_of_day', 24 * 4, 10),
    ('day_type', 3, 10),
    ('taxi_id', 448, 10),
]

dim_input = n_begin_end_pts * 2 * 2 + sum(x for (_, _, x) in dim_embeddings)
dim_hidden = [500, 100]
dim_output = 1

embed_weights_init = IsotropicGaussian(0.001)
mlp_weights_init = IsotropicGaussian(0.01)
mlp_biases_init = Constant(0.001)

exp_base = 1.5

learning_rate = 0.00001
momentum = 0.99
batch_size = 32

max_splits = 100
