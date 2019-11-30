-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Objects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Objects` (
  `idObjects` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(300) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  `description` VARCHAR(400) NULL,
  PRIMARY KEY (`idObjects`),
  UNIQUE INDEX `idObjects_UNIQUE` (`idObjects` ASC) VISIBLE,
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Object_to_Object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Object_to_Object` (
  `prim_idObject` INT NOT NULL,
  `sec_idObject` INT NOT NULL,
  `Obligated` TINYINT NOT NULL,
  PRIMARY KEY (`prim_idObject`, `sec_idObject`),
  INDEX `secObjectid_idx` (`sec_idObject` ASC) VISIBLE,
  CONSTRAINT `primObjectid`
    FOREIGN KEY (`prim_idObject`)
    REFERENCES `mydb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid`
    FOREIGN KEY (`sec_idObject`)
    REFERENCES `mydb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Categories` (
  `idCategories` INT NOT NULL AUTO_INCREMENT,
  `Category_name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idCategories`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Object_to_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Object_to_category` (
  `idObject` INT NOT NULL,
  `idcategorie` INT NOT NULL,
  PRIMARY KEY (`idObject`, `idcategorie`),
  INDEX `idCategorie_object_toCathegorie_idx` (`idcategorie` ASC) VISIBLE,
  CONSTRAINT `idObject_object_to_categorie`
    FOREIGN KEY (`idObject`)
    REFERENCES `mydb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCategorie_object_toCathegorie`
    FOREIGN KEY (`idcategorie`)
    REFERENCES `mydb`.`Categories` (`idCategories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Attribues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Attribues` (
  `idAttribues` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  `Datatype` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAttribues`),
  UNIQUE INDEX `idAttribues_UNIQUE` (`idAttribues` ASC) VISIBLE,
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Categorie_to_Attributes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Categorie_to_Attributes` (
  `idCategorie` INT NOT NULL,
  `idAttribute` INT NOT NULL,
  `mandatory` TINYINT NULL,
  PRIMARY KEY (`idCategorie`, `idAttribute`),
  INDEX `idAttribute_Categorie_to_Attributes_idx` (`idAttribute` ASC) VISIBLE,
  CONSTRAINT `idCategorie_Categorie_to_Attributes`
    FOREIGN KEY (`idCategorie`)
    REFERENCES `mydb`.`Categories` (`idCategories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idAttribute_Categorie_to_Attributes`
    FOREIGN KEY (`idAttribute`)
    REFERENCES `mydb`.`Attribues` (`idAttribues`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Objectentity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Objectentity` (
  `idObject` INT NOT NULL,
  `idObjectentity` INT NOT NULL AUTO_INCREMENT,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  INDEX `idObject_Objectentity_idx` (`idObject` ASC) VISIBLE,
  PRIMARY KEY (`idObjectentity`, `idObject`),
  CONSTRAINT `idObject_Objectentity`
    FOREIGN KEY (`idObject`)
    REFERENCES `mydb`.`Objects` (`idObjects`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usergroup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usergroup` (
  `idUsergroup` INT NOT NULL AUTO_INCREMENT,
  `Usergroupname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsergroup`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `userpassword` VARCHAR(45) NOT NULL,
  `idusergroup` INT NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `idusers_UNIQUE` (`idusers` ASC) VISIBLE,
  INDEX `idusergroup_users_idx` (`idusergroup` ASC) VISIBLE,
  CONSTRAINT `idusergroup_users`
    FOREIGN KEY (`idusergroup`)
    REFERENCES `mydb`.`Usergroup` (`idUsergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`permissions` (
  `idpermissions` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(400) NOT NULL,
  PRIMARY KEY (`idpermissions`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usergroup_to_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usergroup_to_permissions` (
  `idusergroup` INT NOT NULL,
  `idpermission` INT NOT NULL,
  PRIMARY KEY (`idusergroup`, `idpermission`),
  INDEX `idpermission_usergroup_to_permissions_idx` (`idpermission` ASC) VISIBLE,
  CONSTRAINT `idusergroup_usergroup_to_permissions`
    FOREIGN KEY (`idusergroup`)
    REFERENCES `mydb`.`Usergroup` (`idUsergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpermission_usergroup_to_permissions`
    FOREIGN KEY (`idpermission`)
    REFERENCES `mydb`.`permissions` (`idpermissions`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Comments` (
  `idComments` INT NOT NULL AUTO_INCREMENT,
  `idobjectentity` INT NOT NULL,
  `comment` VARCHAR(400) NOT NULL,
  `date` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idComments`),
  INDEX `idobjectentity_Comments_idx` (`idobjectentity` ASC) VISIBLE,
  CONSTRAINT `idobjectentity_Comments`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `mydb`.`Objectentity` (`idObject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`organisations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`organisations` (
  `idorganisations` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `kostenstelle` VARCHAR(45) NULL,
  PRIMARY KEY (`idorganisations`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `idcustomer` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(60) NOT NULL,
  `tel` VARCHAR(15) NULL,
  `fristname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `idorganisation` INT NULL,
  PRIMARY KEY (`idcustomer`),
  INDEX `idorganisation_customer_idx` (`idorganisation` ASC) VISIBLE,
  CONSTRAINT `idorganisation_customer`
    FOREIGN KEY (`idorganisation`)
    REFERENCES `mydb`.`organisations` (`idorganisations`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`reservations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reservations` (
  `idobjectentity` INT NOT NULL,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `idcustomer` INT NOT NULL,
  `comment` VARCHAR(400) NULL,
  `active` TINYINT NOT NULL,
  PRIMARY KEY (`idobjectentity`, `startdate`),
  INDEX `idcustomer_reservations_idx` (`idcustomer` ASC) VISIBLE,
  CONSTRAINT `idcustomer_reservations`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `mydb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idobjectentitiy_reservations`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `mydb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`loans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`loans` (
  `idcustomer` INT NOT NULL,
  `idobjectentity` INT NOT NULL,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `returndate` DATE NULL,
  PRIMARY KEY (`idobjectentity`, `startdate`),
  INDEX `idonjectetity_loans_idx` (`idobjectentity` ASC) VISIBLE,
  CONSTRAINT `idcustomer_loans`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `mydb`.`customer` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idonjectetity_loans`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `mydb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Objectenitiy_to_Objectentity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Objectenitiy_to_Objectentity` (
  `prim_idObjectentity` INT NOT NULL,
  `sec_idObjectentity` INT NOT NULL,
  `Obligated` TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (`prim_idObjectentity`, `sec_idObjectentity`),
  INDEX `secObjectid_idx` (`sec_idObjectentity` ASC) VISIBLE,
  CONSTRAINT `primObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`prim_idObjectentity`)
    REFERENCES `mydb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`sec_idObjectentity`)
    REFERENCES `mydb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`detetion_reason`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`detetion_reason` (
  `objectentityid` INT NOT NULL,
  `reason` VARCHAR(400) NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`objectentityid`, `date`),
  CONSTRAINT `objektentityid_detetion_reason`
    FOREIGN KEY (`objectentityid`)
    REFERENCES `mydb`.`Objectentity` (`idObjectentity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
