with accounts as
  (
	select
	[from_id] as acc,
	[tdate] as dt_from,
	[tdate],
	[amount]
	from [transfers]

	union

	select
	[to_id],
	[tdate] as dt_from,
	[tdate],
	[amount]
	from [transfers]
    )

 SELECT
    acc,
	MIN(dt_from) AS dt_from,
   LEAD([tdate], 1, '3000-01-01') OVER (PARTITION BY acc ORDER BY [tdate]) AS dt_to,
	SUM([amount]) OVER (PARTITION BY acc ORDER BY [tdate]) AS balance

FROM  accounts  a
GROUP BY acc, [tdate], [amount]
ORDER BY acc, [tdate];
