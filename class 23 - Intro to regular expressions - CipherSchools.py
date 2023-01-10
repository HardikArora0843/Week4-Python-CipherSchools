SELECT * FROM [customers]
where ContactName LIKE '%a%'


SELECT * FROM [customers]
where city regexp "Md$"


SELECT * FROM [customers]
where city regexp "a|b|c"


SELECT * FROM [customers]
where city regexp "(a-b)*e"






