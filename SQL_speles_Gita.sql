insert or ignore into invertars values("S_003", "Standoff", "PC", "RPG", 8, 2017, 38.99);
insert or ignore into invertars values("S_004", "Warzone", "PC", "RPG", 16, 2015, 46.99);

select * from invertars;


select sum(Cena) from invertars; 
select max(Cena) from invertars; 
select avg(Vecuma_ierobezojums) from invertars; 
select min(Izdosanas_gads) from invertars; 
select Nosaukums, Platforma, Cena from invertars; 