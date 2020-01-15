select c.id, c.name
from CUSTOMER as c
order by
c.name DESC,
(min(c.id) over (partition by c.name))
