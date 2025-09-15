import numpy as np

#Functions to perform task as required
list2d=lambda r,c: [list([0 for x in range (c)]) for y in range(r)]
def mdisp(m,name="Output",msg=""):
    print(" _ "*25)
    print(f"\n\r[ Matrix ({name}) {msg}]")
    for r in m:
        print("[\t"+"\t".join(f"{x:5}" for x in r)+"\t    ]")
    print(" _ "*25)
def matsqchk(m):
    if len(m)==len(m[0]):
        return True
    return False
def add(a,b):
    r,c=len(a),len(a[0])
    res=list2d(r,c)
    for i in range(r):
        for j in range(c):
            res[i][j]=a[i][j]+b[i][j]
    mdisp(res)
def sub(a,b):
    r,c=len(a),len(a[0])
    res=list2d(r,c)
    for i in range(r):
        for j in range(c):
            res[i][j]=a[i][j]-b[i][j]
    mdisp(res)
def mul(a,b):
    r1,c1,r2,c2=len(a),len(a[0]),len(b),len(b[0])
    res=list2d(r1,c2)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j]+=a[i][k]*b[k][j]
    mdisp(res)
def trace(a):
    res=0
    for i in range(len(a)):
        res+=a[i][i]
    return res
def det(a):
    return np.linalg.det(a)
def minor(a,x,y):
    r,c=len(a),len(a[0])
    res=list2d(r-1,c-1)
    r_offst, c_offst = 0, 0
    for i in range(r):
        if i == x-1:
            r_offst = -1
            continue
        c_offst = 0
        for j in range(c):
            if j == y-1:
                c_offst = -1
                continue
            res[i + r_offst][j + c_offst] = a[i][j]
    return res
def cofac(a):
    r,c=len(a),len(a[0])
    res=list2d(r,c)
    for i in range(r):
        for j in range(c):
            p=(-1)**(i+j+2)
            res[i][j]=round(p*det(minor(a,i+1,j+1)),2)
    return res
def transpose(a):
    r,c=len(a),len(a[0])
    res=list2d(c,r)
    for i in range(c):
        for j in range(r):
            res[i][j]=a[j][i]
    return res
def adjoint(a):
    res=transpose(cofac(a))
    return res
def inv(a):
    r,c=len(a),len(a[0])
    res=list2d(r,c)
    m=adjoint(a)
    for i in range(r):
        for j in range(c):
            res[i][j]=round(m[i][j]/det(a),2)
    return res

#Taking Inputs
mat_data={}
def make_matrix():
    nm=input("Give Matrix Name : ")
    print(f"--------Insert Data for Matrix {nm.title()}")
    r=int(input("Enter number of rows : "))
    c=int(input("Enter number of columns : "))
    mat=list2d(r,c)

    for i in range(1,r+1):
        for j in range(1,c+1):
            mat[i-1][j-1]=int(input(f"Enter {i},{j} :"))
    mat_data[nm]=mat
    mdisp(mat,nm,"added successfully !! ")


#Menu
def Menu():
    print(f"\n{'-'*12} MENU {'-'*12}\n")
    print("\n\r{am} to add new matrix,\n\r{d} to display all matrices,\n\r{tr} for trace of matrix,\n\r{dt} for determinant of matrix")
    print("\n\r{a} to add matrices,\n\r{sb} for subtraction,\n\r{m} for multiplication")
    print("\n\r{t} for transpose,\n\r{c} for cofactor,\n\r{ad} for adjoint of matrix,\n\r{i} for inverse of matrix")
    inp=input('\n\rEnter task : ')
    if inp=='am':#add new matrix
        print(f"\n{'-'*12} ADD NEW MATRIX {'-'*12}\n")
        make_matrix()
    elif inp=='d':#display saved matrices
        print(f"\n{'-'*12} DISPLAY SAVED MATRICES {'-'*12}\n")
        if mat_data!={}:
            for x,y in mat_data.items():
                mdisp(y,x)
        else:
            print("No Matrix Found !!")
    elif inp=='tr':#trace of the matrix
        print(f"\n{'-'*12} TRACE OF MATRIX {'-'*12}\n")
        x=input("Enter Matrix Name : ")
        if matsqchk(mat_data[x]):
            print(f'Trace  : {trace(mat_data[x])}')
        else:
            print("Trace of given Matrix can't be calculated !!")
    elif inp=='dt':#determinant of matrix
        print(f"\n{'-'*12} DETERMINANT OF MATRIX {'-'*12}\n")
        x=input("Enter Matrix Name : ")
        if matsqchk(mat_data[x]):
            print(f'Determinant : {round(det(mat_data[x]),2)}')
    elif inp=='a':#add two matrices
        print(f"\n{'-'*12} PERFORM MATRIX ADDITION {'-'*12}\n")
        try:
            x=input("Enter the Matrix 1 Name : ")
            y=input("Enter the Matrix 2 Name : ")
            if len(mat_data[x])==len(mat_data[y]) and len(mat_data[x][0])==len(mat_data[y][0]):
                add(mat_data[x],mat_data[y])
            else:
                print("Matrices Order Not Matched !!")
        except:
            print("Something Went Wrong !!")
    elif inp=='sb':#subtract two matrices
        print(f"\n{'-'*12} PERFORM MATRIX SUBTRACTION {'-'*12}\n")
        try:
            x=input("Enter the Matrix 1 Name : ")
            y=input("Enter the Matrix 2 Name : ")
            if len(mat_data[x])==len(mat_data[y]) and len(mat_data[x][0])==len(mat_data[y][0]):
                sub(mat_data[x],mat_data[y])
            else:
                print("Matrices Order Not Matched !!")
        except:
            print("Something Went Wrong !!")
    elif inp=='m':#multiply two matrices
        print(f"\n{'-'*12} PERFORM MATRIX MULTIPLICATION {'-'*12}\n")
        try:
            x=input("Enter the Matrix 1 Name : ")
            y=input("Enter the Matrix 2 Name : ")
            if len(mat_data[x][0])==len(mat_data[y]):
                mul(mat_data[x],mat_data[y])
            else:
                print("Matrices can't be multiplied !!")
        except:
            print("Something Went Wrong !!")
    elif inp=='t':#transpose of matrix
        print(f"\n{'-'*12} TRANSPOSE OF MATRIX {'-'*12}\n")
        x=input("Enter Matrix Name : ")
        mdisp(transpose(mat_data[x]))
    elif inp=='c':#find cofactor matrix
        print(f"\n{'-'*12} COFACTOR MATRIX {'-'*12}\n")
        x=input("Enter the Matrix Name : ")
        try:
            mdisp(cofac(mat_data[x]),x,"Cofactor Matrix")
        except:
            print("Something Went Wrong !!")
    elif inp=='ad':#adjoint of matrix
        print(f"\n{'-'*12} ADJOINT OF MATRIX {'-'*12}\n")
        x=input("Enter Matrix Name : ")
        try:
            mdisp(adjoint(mat_data[x]))
        except:
            print("Something Went Wrong !!")
    elif inp=='i':#inverse of matrix
        print(f"\n{'-'*12} INVERSE OF MATRIX {'-'*12}\n")
        x=input("Enter Matrix Name : ")
        try:
            mdisp(inv(mat_data[x]))
        except:
            print("Something Went Wrong !!")
#check whether user wants to continue ?
contnue=True
while contnue:
    Menu()
    print(f"\n{'-'*12} CONTINUE ? {'-'*12}\n")
    if (input("Want to Continue (Y/N)? ")).lower()=='n':
        contnue=False
