Sets
T periodos /1*12/;

Parameters
Demand(T)
/
1  2600
2  3400
3  3900
4  5300
5  4250
6  4200
7  3800
8  4500
9  4300
10 3800
11 3600
12 3000
/;

scalar
c costo de produccion /80/
h /2.7/
CF /10000/
CR /12/
CO /18/
CWplus /10/
CWminus /37/
Cutso /95/;

Positive Variables
P(T) produccion en el periodo t
I(T) inventario a la mano en el periodo t
S(T) faltantes en el periodo T
LR(T) horas de trabajo en tiempo regular en el periodo T
LO(T) horas de trabajo extra en el periodo T
Wplus(T) aumento en la fuerza de trabajo en el periodo T
Wminus(T) reduccion en la fuerza de trabajo en el periodo T
OUTSOURCE(T) unidades subcontratadas en el periodo T
;

free variables
z valor de la funcion objetivo
NI(T) inventario neto
;

equations
FO definicion de la funcion objetivo para minimizar
INVNETO1(T) definicion 1 del inventario neto
INVNETO2(T) definicion 2 del inventario neto
WORKFORCE(T) conservacion de la fuerza de trabajo
PRODUCTION(T) relacion de la produccion y fuerza de trabajo
INVINICIAL inventario neto inicial
INVINICIALHAND inventario a la mano inicial
WFINICIAL fuerza de trabajo inicial
;

FO..                        z =e= SUM(T, c*P(T) + h*I(T) + CF*S(T) + CR*LR(T) + CO*LO(T) + CWplus*Wplus(T) + CWminus*Wminus(T) + Cutso*OUTSOURCE(T));
INVNETO1(T)$(ORD(T)>1)..    NI(T) =e= NI(T-1) + P(T) + OUTSOURCE(T) - Demand(T);
INVNETO2(T)$(ORD(T)>1)..    NI(T) =e= I(T) - S(T);
WORKFORCE(T)$(ORD(T)>1)..   LR(T) =e= LR(T-1) + Wplus(T) - Wminus(T);
PRODUCTION(T)..             P(T) =e= LR(T) + LO(T);
INVINICIAL..                NI("1") =e= 3000 + P("1") + OUTSOURCE("1") - Demand("1");
INVINICIALHAND..            NI("1") =e= I("1") - S("1");
WFINICIAL..                 LR("1") =e= 2880;

model planeacionAgregada /all/;
solve planeacionAgregada using LP minimizing z;
display z.l, P.l, I.l, NI.l, LR.l, LO.l, S.l, Wplus.l, Wminus.l, OUTSOURCE.l;