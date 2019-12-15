DELIMITER //
CREATE PROCEDURE addattributef(x varchar(20), y varchar(40))
BEGIN
	if y like "BOOL" THEN
	alter table objects
	add column x bool;
	end if;
	if y like "VARCHAR" THEN
	alter table objects
	add column x Varchar(400);
	end if;
	if y like "TEXT" THEN
	alter table objects
	add column x text;
	end if;
	if y like "DOUBLE" THEN
	alter table objects
	add column x double;
	end if;
	if y like "INT" THEN
	alter table objects
	add column x int;
	end if;
END //

CREATE PROCEDURE removeAttributef(x varchar(20))
BEGIN
	ALTER TABLE objects
	DROP COLUMN x;
END //

CREATE PROCEDURE editAttributef(x varchar(20), y varchar(20), z varchar(20))
BEGIN
	if y like "BOOL" THEN
	ALTER TABLE objects
    CHANGE x y bool;
	end if;
	if y like "VARCHAR" THEN
	ALTER TABLE objects
    CHANGE x y varchar(400);
	end if;
	if y like "TEXT" THEN
	ALTER TABLE objects
    CHANGE x y text;
	end if;
	if y like "DOUBLE" THEN
	ALTER TABLE objects
    CHANGE x y double;
	end if;
	if y like "INT" THEN
	ALTER TABLE objects
    CHANGE x y int;
	end if;
END //


DELIMITER ;