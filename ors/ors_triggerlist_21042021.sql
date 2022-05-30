* ORS Schema Trigger 

(1) 

CREATE DEFINER=`ors`@`%` TRIGGER `customer_BEFORE_DELETE` 
BEFORE DELETE ON `customer` 
FOR EACH ROW BEGIN
delete from ors.bill where customerId = OLD.customer_id ;
delete from ors.order where customerId = OLD.customer_id ;
END

(2)

CREATE DEFINER=`ors`@`%` TRIGGER `item_BEFORE_DELETE` 
BEFORE DELETE ON `item` 
FOR EACH ROW BEGIN
delete from ors.order where itemid = OLD.itemno ;
END



(3)

CREATE DEFINER=`ors`@`%` TRIGGER `manager_BEFORE_DELETE` 
BEFORE DELETE ON `manager` 
FOR EACH ROW BEGIN
delete from ors.order where managerid = OLD.idno ;
END

(4)

CREATE DEFINER=`ors`@`%` TRIGGER `order_BEFORE_INSERT` 
BEFORE INSERT ON `order` 
FOR EACH ROW BEGIN
Declare
v_price float;
begin
set NEW.orderdate=curdate();
set @v_price := (select price from item where itemno=new.itemid);
set NEW.price = NEW.quantity * @v_price ;
END;
END

(5)

CREATE DEFINER=`ors`@`%` TRIGGER `waiter_BEFORE_DELETE` 
BEFORE DELETE ON `waiter` 
FOR EACH ROW BEGIN
delete from ors.order where waiterid = OLD.idno ;
END

(6)

