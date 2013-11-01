mean_stationary = LOAD '/user/shared/white_noise_shocks' USING PigStorage(' ') AS (atTime:int, obs:float);
shocks = FILTER mean_stationary BY (obs >= 244.2) OR (obs <= -236.2);
shocks = ORDER shocks BY atTime;
DUMP shocks;
