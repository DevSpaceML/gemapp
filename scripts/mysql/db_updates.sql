use tiyeni;

 alter table accomz RENAME TO stays;

alter table stays change column name bizname varchar(255) NOT NULL;
alter table stays change column email email varchar(255) NOT NULL UNIQUE;
alter table stays change column type stay_type  varchar(255);

alter table eats change column name bizname varchar(255) NOT NULL;
alter table eats change column email email varchar(255) NOT NULL;
alter table eats change column type eats_type varchar(255);

alter table events change column type evnt_type varchar(100) NOT NULL;

alter table transport change column name bizname varchar(255) NOT NULL 
alter table transport change column hireType hire_type varchar(100);