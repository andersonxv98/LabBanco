create view compras_VIew
as 
select fornecedor.nome, Sum(compra.valor)
from fornecedor inner join compra 
on fornecedor.codigo = compra.codigo_for

select * from compras_view