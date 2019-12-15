SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `eidb` DEFAULT CHARACTER SET utf8;
USE `eidb` ;

-- -----------------------------------------------------
-- Table `eidb`.`Objects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Objects` (
  `idObjects` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(300) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  `description` VARCHAR(400) NULL,
  PRIMARY KEY (`idObjects`),
  UNIQUE INDEX `idObjects_UNIQUE` (`idObjects` ASC),
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC));


-- -----------------------------------------------------
-- Table `eidb`.`Object_to_Object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Object_to_Object` (
  `prim_idObject` INT NOT NULL,
  `sec_idObject` INT NOT NULL,
  `Obligated` TINYINT NOT NULL,
  PRIMARY KEY (`prim_idObject`, `sec_idObject`),
  INDEX `secObjectid_idx` (`sec_idObject` ASC),
  CONSTRAINT `primObjectid`
    FOREIGN KEY (`prim_idObject`)
    REFERENCES `eidb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid`
    FOREIGN KEY (`sec_idObject`)
    REFERENCES `eidb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Categories` (
  `Category_name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`Category_name`));


-- -----------------------------------------------------
-- Table `eidb`.`Object_to_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Object_to_category` (
  `idObject` INT NOT NULL,
  `idcategorie` INT NOT NULL,
  PRIMARY KEY (`idObject`, `idcategorie`),
  INDEX `idCategorie_object_toCathegorie_idx` (`idcategorie` ASC),
  CONSTRAINT `idObject_object_to_categorie`
    FOREIGN KEY (`idObject`)
    REFERENCES `eidb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCategorie_object_toCathegorie`
    FOREIGN KEY (`idcategorie`)
    REFERENCES `eidb`.`Categories` (`idCategories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Attribues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Attribues` (
  `idAttribues` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  `Datatype` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAttribues`),
  UNIQUE INDEX `idAttribues_UNIQUE` (`idAttribues` ASC),
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE);


-- -----------------------------------------------------
-- Table `eidb`.`Categorie_to_Attributes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Categorie_to_Attributes` (
  `idCategorie` INT NOT NULL,
  `idAttribute` INT NOT NULL,
  `mandatory` TINYINT NULL,
  PRIMARY KEY (`idCategorie`, `idAttribute`),
  INDEX `idAttribute_Categorie_to_Attributes_idx` (`idAttribute` ASC),
  CONSTRAINT `idCategorie_Categorie_to_Attributes`
    FOREIGN KEY (`idCategorie`)
    REFERENCES `eidb`.`Categories` (`idCategories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idAttribute_Categorie_to_Attributes`
    FOREIGN KEY (`idAttribute`)
    REFERENCES `eidb`.`Attribues` (`idAttribues`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Objectentity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Objectentity` (
  `idObject` INT NOT NULL,
  `idObjectentity` INT NOT NULL AUTO_INCREMENT,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  INDEX `idObject_Objectentity_idx` (`idObject` ASC),
  PRIMARY KEY (`idObjectentity`, `idObject`),
  CONSTRAINT `idObject_Objectentity`
    FOREIGN KEY (`idObject`)
    REFERENCES `eidb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Usergroup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Usergroup` (
  `idUsergroup` INT NOT NULL AUTO_INCREMENT,
  `Usergroupname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsergroup`));


-- -----------------------------------------------------
-- Table `eidb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `userpassword` VARCHAR(45) NOT NULL,
  `idusergroup` INT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC),
  UNIQUE INDEX `idusers_UNIQUE` (`idusers` ASC),
  INDEX `idusergroup_users_idx` (`idusergroup` ASC),
  CONSTRAINT `idusergroup_users`
    FOREIGN KEY (`idusergroup`)
    REFERENCES `eidb`.`Usergroup` (`idUsergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`permissions` (
  `idpermissions` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(400) NOT NULL,
  PRIMARY KEY (`idpermissions`));


-- -----------------------------------------------------
-- Table `eidb`.`usergroup_to_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`usergroup_to_permissions` (
  `idusergroup` INT NOT NULL,
  `idpermission` INT NOT NULL,
  PRIMARY KEY (`idusergroup`, `idpermission`),
  INDEX `idpermission_usergroup_to_permissions_idx` (`idpermission` ASC),
  CONSTRAINT `idusergroup_usergroup_to_permissions`
    FOREIGN KEY (`idusergroup`)
    REFERENCES `eidb`.`Usergroup` (`idUsergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpermission_usergroup_to_permissions`
    FOREIGN KEY (`idpermission`)
    REFERENCES `eidb`.`permissions` (`idpermissions`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Comments` (
  `idComments` INT NOT NULL AUTO_INCREMENT,
  `idobjectentity` INT NOT NULL,
  `comment` VARCHAR(400) NOT NULL,
  `date` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idComments`),
  INDEX `idobjectentity_Comments_idx` (`idobjectentity` ASC),
  CONSTRAINT `idobjectentity_Comments`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `eidb`.`Objectentity` (`idObject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`organisations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`organisations` (
  `idorganisations` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `kostenstelle` VARCHAR(45) NULL,
  PRIMARY KEY (`idorganisations`));


-- -----------------------------------------------------
-- Table `eidb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`customer` (
  `idcustomer` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(60) NOT NULL,
  `tel` VARCHAR(15) NULL,
  `fristname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `idorganisation` INT NULL,
  PRIMARY KEY (`idcustomer`),
  INDEX `idorganisation_customer_idx` (`idorganisation` ASC),
  CONSTRAINT `idorganisation_customer`
    FOREIGN KEY (`idorganisation`)
    REFERENCES `eidb`.`organisations` (`idorganisations`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`reservations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`reservations` (
  `idobjectentity` INT NOT NULL,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `idcustomer` INT NOT NULL,
  `comment` VARCHAR(400) NULL,
  `active` TINYINT NOT NULL,
  PRIMARY KEY (`idobjectentity`, `startdate`),
  INDEX `idcustomer_reservations_idx` (`idcustomer` ASC),
  CONSTRAINT `idcustomer_reservations`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `eidb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idobjectentitiy_reservations`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `eidb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`loans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`loans` (
  `idcustomer` INT NOT NULL,
  `idobjectentity` INT NOT NULL,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `returndate` DATE NULL,
  PRIMARY KEY (`idobjectentity`, `startdate`),
  INDEX `idonjectetity_loans_idx` (`idobjectentity` ASC),
  CONSTRAINT `idcustomer_loans`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `eidb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idonjectetity_loans`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `eidb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`Objectenitiy_to_Objectentity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`Objectenitiy_to_Objectentity` (
  `prim_idObjectentity` INT NOT NULL,
  `sec_idObjectentity` INT NOT NULL,
  `Obligated` TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (`prim_idObjectentity`, `sec_idObjectentity`),
  INDEX `secObjectid_idx` (`sec_idObjectentity` ASC),
  CONSTRAINT `primObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`prim_idObjectentity`)
    REFERENCES `eidb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`sec_idObjectentity`)
    REFERENCES `eidb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `eidb`.`detetion_reason`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eidb`.`detetion_reason` (
  `objectentityid` INT NOT NULL,
  `reason` VARCHAR(400) NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`objectentityid`, `date`),
  CONSTRAINT `objektentityid_detetion_reason`
    FOREIGN KEY (`objectentityid`)
    REFERENCES `eidb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
