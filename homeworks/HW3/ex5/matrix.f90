!
! National Tsing Hua University
!
! ASTR 660 Computational Astrophysics
!
! Created:  Kuo-Chuan Pan 2020
! Modified: Karen Yang 2022.10.15
!
! Problem:
!
!        Solving non-linear equations
!
program linear
    use linalg
    implicit none
    integer, parameter  :: N = 3
    real,dimension(N,N) :: lower, upper, A, P, Ainv, L, U
    real,dimension(N) :: b
    real,dimension(N) :: x
    real,dimension(4,4) :: aa,ll,uu,pp
    integer :: i,j

    ! lower triangle
    lower(1,1) = -1.0
    lower(1,2) =  0.0
    lower(1,3) =  0.0
    lower(2,1) = -6.0
    lower(2,2) = -4.0
    lower(2,3) =  0.0
    lower(3,1) =  1.0
    lower(3,2) =  2.0
    lower(3,3) =  2.0

    ! upper triangle
    upper(1,1) = 1.0
    upper(1,2) = 2.0
    upper(1,3) = 2.0
    upper(2,1) = 0.
    upper(2,2) = -4.
    upper(2,3) = -6
    upper(3,1) = 0.
    upper(3,2) = 0.
    upper(3,3) = -1.0

    ! the vectore b for lower
   ! b(1) =  1.0
   ! b(2) = -6.0
   ! b(3) =  3.0
        
    ! the vectore b for upper
   ! b(1) =  3.0
   ! b(2) = -6.0
   ! b(3) =  1.0
   
    ! matrix A in lecture 
    !A(1,1) = 2
    !A(1,2) = 4
    !A(1,3) = -2
    !A(2,1) = 4
    !A(2,2) = 9
    !A(2,3) = -3
    !A(3,1) = -2
    !A(3,2) = -3
    !A(3,3) = 7

    ! matrix A in HW3
    A(1,1) = 1
    A(1,2) = 2
    A(1,3) = 2
    A(2,1) = 4
    A(2,2) = 6
    A(2,3) = 8
    A(3,1) = 4
    A(3,2) = 8
    A(3,3) = 10

    ! vector b in ex4 of HW3
    b(1) = 4
    b(2) = 6
    b(3) = 10
    
    !call solve_lower_triangular_matrix(N,lower,b,x)
    !call solve_upper_triangular_matrix(N,upper,b,x)
    call LU_decomposition(N,A,L,U)
    call solve_lu(N,A,b,x)

    !call mat_print("L",lower)
    !call mat_print("U",upper)
    call mat_print("A",A)
    call mat_print("L",L)
    call mat_print("U",U)
    

    print *, "vector   b = ",b
    print *, "solution x = ",x
    
end program linear 


