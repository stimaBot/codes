pA=80000
pB=200000

cresc_A = pA*0.03
cresc_B = pB*0.0015

ano=0

tA = pA+ano*cresc_A
tB = pB+ano*cresc_B

while(tA!=tB):
    print("iteração", ano)
    tA = pA+ano*cresc_A
    tB = pB+ano*cresc_B
    if(tA==tB):
        print("Terão a mesma população no ano: ", ano)
    else:
        if(tA>tB):
            print("A população de A será maior que a população de B no ano: ", ano)
            break
        ano=ano+1
    
