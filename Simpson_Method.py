#!/usr/bin/env python

'''
	-- Solução Computacional para o problema do Ponto de Fermat --

						Desenvolvido por:
						
		Lucas V. Araujo          <lucas.vieira.ar@disroot.org>
		Matheus F. Nascimento    <fernandes.matheuscp@gmail.com>
		Matheus H. Fontenele     <matheus.henriquefont@gmail.com>
		Odilon F. Damasceno Neto <odilondamasceno@protonmail.com>

Artigo: https://seer.ufrgs.br/reic/article/view/96282

'''

from math import acos, pi, sqrt

def distancia(a, b):
	#Retorna a distancia entre dois pontos atraves do teorema de Pitagoras
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def vertice_triangulo(a, b):
    Xa, Ya, Xb, Yb = a[0], a[1], b[0], b[1]
    #ax+by+c=0 (Equacao da reta que corta o triangulo ao meio)
    eq = [-2 * Xb + 2 * Xa, -2 * Yb + 2 * Ya, Yb ** 2 - Ya ** 2 + Xb ** 2 - Xa ** 2]
    ds = distancia(a, b)
    if eq[0] == 0:
    	#Se X for 0 (Xa=Xb), encontra-se o Y em uma equacao do 1ro grau
        Yc = -eq[2] / eq[1]
        Xc1 = Xb + (ds * sqrt(3)) / 2
        Xc2 = Xb - (ds * sqrt(3)) / 2
        return [Xc1, Yc],[ Xc2, Yc]
    elif eq[1] == 0:
        Xc = -eq[2] / eq[0]
        Yc1 = Yb + (ds * sqrt(3)) / 2
        Yc2 = Yb - (ds * sqrt(3)) / 2
        return [[Xc, Yc1],[Xc, Yc2]]
    else:
        try:
        	#X1 encontrado por equcao do 2ndo grau
            Xc1 = -((Yb-Ya)*sqrt(-Yb**4+4*Ya*Yb**3+(-6*Ya**2-2*Xb**2+4*Xa*Xb-2*Xa**2+4*ds**2)*Yb**2+(4*Ya**3+(4*Xb**2-8*Xa*Xb+4*Xa**2-8*ds**2)*Ya)*Yb-Ya**4+
(-2*Xb**2+4*Xa*Xb-2*Xa**2+4*ds**2)*Ya**2-Xb**4+4*Xa*Xb**3+(4*ds**2-6*Xa**2)*Xb**2+(4*Xa**3-8*ds**2*Xa)*Xb-Xa**4+4*ds**2*Xa**2)+(-Xb-Xa)*Yb**2+(2*Xb+2*Xa)*Ya*Yb+(-Xb-Xa)*Ya**2-
Xb**3+Xa*Xb**2+Xa**2*Xb-Xa**3)/(2*Yb**2-4*Ya*Yb+2*Ya**2+2*Xb**2-4*Xa*Xb+2*Xa**2)

			#X2 encontrado por equcao do 2ndo grau            
            Xc2 = ((Yb-Ya)*sqrt(-Yb**4+4*Ya*Yb**3+(-6*Ya**2-2*Xb**2+4*Xa*Xb-2*Xa**2+4*ds**2)*Yb**2+
(4*Ya**3+(4*Xb**2-8*Xa*Xb+4*Xa**2-8*ds**2)*Ya)*Yb-Ya**4+(-2*Xb**2+4*Xa*Xb-2*Xa**2+4*ds**2)*Ya**2-Xb**4+4*Xa*Xb**3+(4*ds**2-6*Xa**2)*Xb**2+(4*Xa**3-8*ds**2*Xa)*Xb-Xa**4+4*ds**2*Xa**2)+
(Xb+Xa)*Yb**2+(-2*Xb-2*Xa)*Ya*Yb+(Xb+Xa)*Ya**2+Xb**3-Xa*Xb**2-Xa**2*Xb+Xa**3)/(2*Yb**2-4*Ya*Yb+2*Ya**2+2*Xb**2-4*Xa*Xb+2*Xa**2)

            eq_y = lambda x: (-eq[0] * x - eq[2]) / eq[1]
            Yc1 = eq_y(Xc1)
            Yc2 = eq_y(Xc2)
            return [Xc1, Yc1], [Xc2, Yc2]
        except Exception, e:
            print e.message
    return []

def eq_reta(a, b):
	#Retorna a equacao da reta que passa pelos pontos a e b
	#ax+by+c=0
    return [(a[1] - b[1]), -(a[0] - b[0]), a[0] * b[1] - b[0] * a[1]]

def interseccao(r, s):
	#Retorna o ponto de interseccao entre as retas r e s
    Ar, Br, Cr = r
    As, Bs, Cs = s
    if As == 0:
        Y = -Cs / Bs
        X = (-Br * Y - Cr) / Ar
        return [X, Y]
    elif Ar == 0:
        Y = -Cr / Br
        X = (-Bs * Y - Cs) / As
        return [X, Y]
    elif Br == 0:
        X = -Cr / Ar
        Y = (-As * X - Cs) / Bs
        return [X, Y]
    elif Bs == 0:
        X = -Cs / As
        Y = (-Ar * X - Cr) / Br
        return [X, Y]
    X = (Br * Cs - Bs * Cr) / (Ar * Bs - As * Br)
    Y = (-Ar * X - Cr) / Br
    return [X, Y]

def angulo(r1, r2):
    prod = r1[0] * r2[0] + r1[1] * r2[1]
    md = sqrt(r1[0] ** 2 + r1[1] ** 2) * sqrt(r2[0] ** 2 + r2[1] ** 2)
    return acos(prod/md) * (180/pi)

def main():
    A = [float(input("X de A: ")), float(input("Y de A: "))]
    B = [float(input("X de B: ")), float(input("Y de B: "))]
    C = [float(input("X de C: ")), float(input("Y de C: "))]
    
    AB = [A[0]-B[0], A[1]-B[1]]
    AC = [A[0]-C[0], A[1]-C[1]]
    BA = [B[0]-A[0], B[1]-C[1]]
    BC = [B[0]-C[0], B[1]-C[1]]
    CA = [C[0]-A[0], C[1]-A[1]]
    CB = [C[0]-B[0], C[1]-B[1]]

    an0 = angulo(AB, AC)
    an2 = angulo(CA, CB)
    an1 = 180 - (an0+an2)
    if (an0 >= 120) or (an1 >= 120) or (an2 >= 120):
        print("Opa! Um dos angulos excede 120 graus!")
        return 0
    
    _V1 = vertice_triangulo(A, B)
    _V2 = vertice_triangulo(B, C)
    V1 = _V1[0] if distancia(C, _V1[0]) > distancia(C, _V1[1]) else _V1[1]
    V2 = _V2[0] if distancia(A, _V2[0]) > distancia(A, _V2[1]) else _V2[1]
    
    EQ1 = eq_reta(V1, C)
    EQ2 = eq_reta(V2, A)
    
    M = interseccao(EQ1, EQ2)
    
    print("O ponto de Fermat fica em: " + str(tuple(M)))
    return 0
quit(main())
