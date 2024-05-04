{{ config(materialized='table' )}}

select
    *
from
    trajectories
where
    speed > 40