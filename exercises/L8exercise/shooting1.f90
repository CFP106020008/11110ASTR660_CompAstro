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
    real :: try_y2, tolerance, yend
    real :: yend1, yend2
    real :: error1, error2, errormid
    real :: guess1, guess2, guessmid
    real :: initial_y, expected_y

    !! tolerance
    tolerance = 1.e-3

    ! Boundary condition
    initial_y  = 1.0
    expected_y = 1.0
    
    guess1 = -1000.0
    guess2 = 1000.0

    ! Some random value
    errormid = 1.e99

    do while (abs(errormid) .ge. tolerance) 
        guessmid = (guess1 + guess2)/2.
        call get_final(guess1,   initial_y, expected_y, error1)
        call get_final(guess2,   initial_y, expected_y, error2)
        call get_final(guessmid, initial_y, expected_y, errormid)
        if ((error1*errormid) .gt. 0) then
            guess1 = guessmid
        else
            guess2 = guessmid
        endif
        print *, 'Try y(1) = ', guessmid, ', got error = ', errormid
    enddo
    print *, 'y1(0) is', guessmid
        

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
    k(1) = yin(2)   ! TODO
    k(2) = 6.*t   ! TODO
    return
end subroutine my_func

subroutine get_final(y2, initial_y1, expected_y1, error)
    
    use Solver , only : rk2
    implicit none
    
    external :: my_func

    real :: h,t,tend
    integer :: i,n
    real :: try_y2, tolerance, yend
    real, dimension(2) :: y, ynext
    real, intent(in) :: y2, expected_y1, initial_y1 
    real, intent(out) :: error

    h    = 0.01  ! step size
    t    = 0.0   ! initial t
    tend = 1.0   ! final   t

    n    =  2   ! number of ODEs

    ! initial conditions
    y(1) =  initial_y1  ! y(1) = u
    y(2) =  y2          ! y(2) = u' 
    do while(t .lt. tend)
        if ((t+h) .ge. tend) then
            h = tend - t
        endif
        call rk2(n, y, ynext, t, h, my_func)
        y = ynext
        t = t + h
    enddo
    yend = ynext(1)
    error = yend - expected_y1
end subroutine get_final





