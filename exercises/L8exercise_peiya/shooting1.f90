!---------------------------------------------------
!
! National Tsing Hua University
!
! ASTR 660 Computational Astrophysics
!
! Created:  Kuo-Chuan Pan 2020
! Modified: Karen Yang 2022.10.25
!
! Problem:
!
!        Solving boundary value problems

program shooting1

    use Solver , only : rk2

    implicit none

    external :: my_func

    real :: h,t,tend
    integer :: i,n
    real :: try_y2
    real, dimension(2) :: y, ynext

    real, save :: a = -1.5        ! bracking interval [a,b]
    real, save :: b = 2.0         ! bracking interval [a,b] 
    real       :: err = 1.0
    integer       :: iter = 1

    h    = 0.01  ! step size
    tend = 1.0   ! final   t
    
    n    =  2   ! number of ODEs
    
    do while (err .ge. 1.0e-4)
        print *, "Iteration time = ", iter
        
        ! a trial value
        try_y2 = (a+b)/2.0

        ! initial conditions
        y(1) =  1.0      ! y(1) = u
        y(2) =  try_y2   ! y(2) = u' 

        t = 0.    
        do while(t .lt. tend)
            !if ((t+h) .ge. tend) then
            !    h = tend - t
            !endif
            call rk2(n, y, ynext, t, h, my_func)
            y = ynext
            t = t + h
            print *, t, ynext(1)
        enddo
        err = abs(ynext(1)-1.0)
        
        if (ynext(1) .ge. 1.0) then
            b = try_y2
        else
            a = try_y2
        endif
        iter = iter + 1

    enddo

    print *, "y1(1) = ", ynext(1)
    print *, "The desired value is 1."
    print *, "dydt(t=0) = ", try_y2

end program shooting1

!-----------------------------------------------
!
!  Solving Boundary Value problem
!
!  u'' = 6t      0 < t < 1
!
!  with BC
!
!         u(t=0) = 1 and
!         u(t=1) = 1
!
!-----------------------------------------------

subroutine my_func(n, t, yin, k)
    implicit none
    integer, intent(in) :: n  ! number of ODEs
    real, intent(in)    :: t
    real, dimension(n), intent(in)  :: yin
    real, dimension(n), intent(out) :: k    ! dydt

    ! in this example  n = 2
    k(1) = yin(2) ! TODO
    k(2) = 6.*t   ! TODO
    return
end subroutine my_func


