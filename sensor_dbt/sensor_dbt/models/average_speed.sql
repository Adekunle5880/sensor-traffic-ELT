{{ config(materialized='table') }}

with source_data as (

    select
        type,
        AVG(avg_speed) as average_speed
    from
        vehicle
    GROUP BY
        type

)

select *
from source_data