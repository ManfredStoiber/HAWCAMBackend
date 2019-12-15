USE `eidb` ;
DELIMITER $$
CREATE TRIGGER addAttribute
AFTER INSERT
ON attribues FOR EACH ROW
BEGIN
    call addattributef(new.Name,new.Datatype);
	#ALTER TABLE objects
    #ADD COLUMN new.Name new.Datatype;
END$$ 


CREATE TRIGGER removeAttribute
AFTER delete
ON attribues FOR EACH ROW
BEGIN
	call removeAttributef(old.name);
	#ALTER TABLE objects
	#DROP COLUMN old.Name;
END$$    

CREATE TRIGGER editAttribute
AFTER update
ON attribues FOR EACH ROW
BEGIN
	call editAttributef;
	#ALTER table objects
    #CHANGE old.Name new.Name new.Datatype;
END$$    
DELIMITER ;