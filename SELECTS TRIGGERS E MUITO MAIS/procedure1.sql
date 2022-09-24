CREATE DEFINER=`root`@`localhost` PROCEDURE `ToTalVendas`(in data1 date, in dataf date, out ValorTot float)
begin
select  sum(valor)  into ValorTot
from venda
where data>= data1 and data <=dataf;
end