from classe_no import no
from busca_largura import busca

b=no("b")
a=no("a")
f=no("f")
d=no("d")
c=no("c")
e=no("e")
h=no("h")
i=no("i")
l=no("l")
j=no("k")
g=no("g")
k=no("k")

b.set_adjacente([a,f,d])
a.set_adjacente([b,h,i])
f.set_adjacente([b,c,e])
d.set_adjacente([g])
c.set_adjacente([f])
e.set_adjacente([f,j,k])
h.set_adjacente([a])
i.set_adjacente([a,l])
j.set_adjacente([e])
k.set_adjacente([e])
l.set_adjacente([i])
g.set_adjacente([d])

buscar = busca()
buscar.executar(b)
buscar.percorrrer_caminho(g)
print(buscar.percorrrer_caminho(g))