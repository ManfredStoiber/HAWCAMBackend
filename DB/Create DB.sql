SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SwE_IV_DB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SwE_IV_DB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SwE_IV_DB` DEFAULT CHARACTER SET utf8 ;
USE `SwE_IV_DB` ;

-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`object` (
  `id_object` INT NOT NULL AUTO_INCREMENT,
  `object_name` VARCHAR(300) NOT NULL,
  `object_deleted` TINYINT NOT NULL DEFAULT 0,
  `object_description` VARCHAR(400) NULL,
  PRIMARY KEY (`id_object`),
  UNIQUE INDEX `idObjects_UNIQUE` (`id_object` ASC) ,
  UNIQUE INDEX `Name_UNIQUE` (`object_name` ASC) )
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`object_to_object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`object_to_object` (
  `prim_id_object` INT NOT NULL,
  `sec_id_object` INT NOT NULL,
  `mandatory` TINYINT NOT NULL,
  PRIMARY KEY (`prim_id_object`, `sec_id_object`),
  INDEX `secObjectid_idx` (`sec_id_object` ASC) ,
  CONSTRAINT `primObjectid`
    FOREIGN KEY (`prim_id_object`)
    REFERENCES `SwE_IV_DB`.`object` (`id_object`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid`
    FOREIGN KEY (`sec_id_object`)
    REFERENCES `SwE_IV_DB`.`object` (`id_object`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`category` (
  `Category_name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`Category_name`))
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`object_to_category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`object_to_category` (
  `id_object` INT NOT NULL,
  `categorie_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_object`, `categorie_name`),
  INDEX `IdCategory_object_to_cathegory_idx` (`categorie_name` ASC) ,
  CONSTRAINT `idObject_object_to_categorie`
    FOREIGN KEY (`id_object`)
    REFERENCES `SwE_IV_DB`.`object` (`id_object`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `IdCategory_object_to_cathegory`
    FOREIGN KEY (`categorie_name`)
    REFERENCES `SwE_IV_DB`.`category` (`Category_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`attribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`attribute` (
  `id_attribute` INT NOT NULL AUTO_INCREMENT,
  `attribute_name` VARCHAR(45) NOT NULL,
  `deleted` TINYINT NOT NULL DEFAULT 0,
  `attribute_datatype` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_attribute`),
  UNIQUE INDEX `idAttribues_UNIQUE` (`id_attribute` ASC) ,
  UNIQUE INDEX `Name_UNIQUE` (`attribute_name` ASC) )
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`category_to_attribute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`category_to_attribute` (
  `category_name` VARCHAR(45) NOT NULL,
  `id_attribute` INT NOT NULL,
  `mandatory` TINYINT NULL,
  PRIMARY KEY (`category_name`, `id_attribute`),
  INDEX `idAttribute_Categorie_to_Attributes_idx` (`id_attribute` ASC) ,
  CONSTRAINT `idAttribute_Categorie_to_Attributes`
    FOREIGN KEY (`id_attribute`)
    REFERENCES `SwE_IV_DB`.`attribute` (`id_attribute`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Categorie_name_Categorie_to_Attributes`
    FOREIGN KEY (`category_name`)
    REFERENCES `SwE_IV_DB`.`category` (`Category_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`object_entity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`object_entity` (
  `id_object` INT NOT NULL,
  `id_object_entity` INT NOT NULL AUTO_INCREMENT,
  `object_entity_deleted` TINYINT NOT NULL DEFAULT 0,
  INDEX `idObject_Objectentity_idx` (`id_object` ASC) ,
  PRIMARY KEY (`id_object_entity`, `id_object`),
  CONSTRAINT `idObject_Objectentity`
    FOREIGN KEY (`id_object`)
    REFERENCES `SwE_IV_DB`.`object` (`id_object`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`usergroup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`usergroup` (
  `id_usergroup` INT NOT NULL AUTO_INCREMENT,
  `usergroup_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_usergroup`))
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`user` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `user_password` VARCHAR(45) NOT NULL,
  `id_usergroup` INT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `username_UNIQUE` (`user_name` ASC) ,
  UNIQUE INDEX `idusers_UNIQUE` (`id_user` ASC) ,
  INDEX `idusergroup_users_idx` (`id_usergroup` ASC) ,
  CONSTRAINT `idusergroup_users`
    FOREIGN KEY (`id_usergroup`)
    REFERENCES `SwE_IV_DB`.`usergroup` (`id_usergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`permission` (
  `id_permissions` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(400) NOT NULL,
  PRIMARY KEY (`id_permissions`))
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`usergroup_to_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`usergroup_to_permission` (
  `idusergroup` INT NOT NULL,
  `idpermission` INT NOT NULL,
  PRIMARY KEY (`idusergroup`, `idpermission`),
  INDEX `idpermission_usergroup_to_permissions_idx` (`idpermission` ASC) ,
  CONSTRAINT `idusergroup_usergroup_to_permission`
    FOREIGN KEY (`idusergroup`)
    REFERENCES `SwE_IV_DB`.`usergroup` (`id_usergroup`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idpermission_usergroup_to_permission`
    FOREIGN KEY (`idpermission`)
    REFERENCES `SwE_IV_DB`.`permission` (`id_permissions`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`comment` (
  `id_comment` INT NOT NULL AUTO_INCREMENT,
  `id_object_entity` INT NOT NULL,
  `comment_text` VARCHAR(400) NOT NULL,
  `comment_date` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id_comment`),
  INDEX `idobjectentity_Comments_idx` (`id_object_entity` ASC) ,
  CONSTRAINT `idobjectentity_Comments`
    FOREIGN KEY (`id_object_entity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`organisation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`organisation` (
  `id_organisation` INT NOT NULL AUTO_INCREMENT,
  `organisation_name` VARCHAR(45) NOT NULL,
  `kostenstelle` VARCHAR(45) NULL,
  PRIMARY KEY (`id_organisation`))
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`customer` (
  `id_customer` INT NOT NULL AUTO_INCREMENT,
  `customer_email` VARCHAR(60) NOT NULL,
  `customer_tel` VARCHAR(15) NULL,
  `customer_fristname` VARCHAR(45) NULL,
  `lcustomer_astname` VARCHAR(45) NULL,
  `idorganisation` INT NULL,
  PRIMARY KEY (`id_customer`),
  INDEX `idorganisation_customer_idx` (`idorganisation` ASC) ,
  CONSTRAINT `idorganisation_customer`
    FOREIGN KEY (`idorganisation`)
    REFERENCES `SwE_IV_DB`.`organisation` (`id_organisation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`reservation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`reservation` (
  `id_object_entity` INT NOT NULL,
  `reservation_startdate` DATE NOT NULL,
  `reservation_enddate` DATE NOT NULL,
  `idcustomer` INT NOT NULL,
  `reservation_comment` VARCHAR(400) NULL,
  `reservation_active` TINYINT NOT NULL,
  PRIMARY KEY (`id_object_entity`, `reservation_startdate`),
  INDEX `idcustomer_reservations_idx` (`idcustomer` ASC) ,
  CONSTRAINT `idcustomer_reservations`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `SwE_IV_DB`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idobjectentitiy_reservations`
    FOREIGN KEY (`id_object_entity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object_entity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`loans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`loans` (
  `idcustomer` INT NOT NULL,
  `idobjectentity` INT NOT NULL,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `returndate` DATE NULL,
  PRIMARY KEY (`idobjectentity`, `startdate`),
  INDEX `idonjectetity_loans_idx` (`idobjectentity` ASC) ,
  CONSTRAINT `idcustomer_loans`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `SwE_IV_DB`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idonjectetity_loans`
    FOREIGN KEY (`idobjectentity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object_entity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`object_enitiy_to_object_entity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`object_enitiy_to_object_entity` (
  `prim_id_object_entity` INT NOT NULL,
  `sec_id_object_entity` INT NOT NULL,
  `mandatory` TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (`prim_id_object_entity`, `sec_id_object_entity`),
  INDEX `secObjectid_idx` (`sec_id_object_entity` ASC) ,
  CONSTRAINT `primObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`prim_id_object_entity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object_entity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `secObjectid_Objectenitiy_to_Objectentity`
    FOREIGN KEY (`sec_id_object_entity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object_entity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `SwE_IV_DB`.`deletion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SwE_IV_DB`.`deletion` (
  `id_object_entity` INT NOT NULL,
  `deletion_reason` VARCHAR(400) NULL,
  `deletion_date` DATETIME NOT NULL,
  PRIMARY KEY (`id_object_entity`, `deletion_date`),
  CONSTRAINT `objektentityid_detetion_reason`
    FOREIGN KEY (`id_object_entity`)
    REFERENCES `SwE_IV_DB`.`object_entity` (`id_object_entity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
