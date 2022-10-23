!
! A simple program to calculate pi
!
program calculate_pi

    implicit none

    real            :: area, error
    integer           :: i, n
    real, parameter :: pi = 4.0*atan(1.0)
    real            :: t1, t2

    integer, parameter :: MAXN = 7
    integer, dimension(MAXN) :: numbers

    !--- setup numbers
    numbers = (/10, 100, 1000, 10000, 100000, 1000000, 10000000/)

    !--- open a file to store the error
    open(unit=11, file="error-Simp-2.dat")
    write(11,100) "# ", "N", "Error", "Compute time [s]"

    !--- measure the compute time
    call cpu_time(t1)
    ! do integral
    do i=1, MAXN
        area = 0. ! Reset the area number everytime
        
        n = numbers(i)
        call calculate_function_integral(n, area)
        print *, "N = ",n, " PI = ", 2.*area
        error = abs(2.*area - pi)/pi 

        call cpu_time(t2)
        write(11,200) numbers(i), error, (t2-t1)
        t1 = t2
    enddo

    100 format(a2, a9, 2a24)
    200 format(2x, i9, 2e24.14)

    close(11)

end program calculate_pi

subroutine calculate_function_integral(N, A)
    implicit none
    integer, intent(in)  :: N
    real,  intent(out) :: A
    integer :: i
    real    :: my_func
    real    :: x, h, dx, dA, x1, x2, h1, h2, h3

    !-- initialize values
    dx = 2./dble(N)

    !-- calculate each rectangle and sum the area
    do i = 1, N
        ! This is for midpoint method
        ! x = -1.d0 + (real(i)-0.5d0)*dx
        ! h = my_func(x)
        ! dA = h*dx
        
        ! This is for trapezoid method
        !x1 = -1.d0 + (i-1)*dx
        !x2 = -1.d0 + i*dx
        !h1 = my_func(x1)
        !h2 = my_func(x2)
        !dA = (h1 + h2)*dx/2.

        ! This is for Simpson's method
        x1 = -1.d0 + (i-1)*dx
        x2 = -1.d0 + i*dx
        h1 = my_func(x1)
        h2 = my_func((x1+x2)/2.)
        h3 = my_func(x2)
        dA = (h1 + 4.*h2 + h3)*dx/6.
        
        A = A + dA
    enddo

    return 
end subroutine calculate_function_integral

real function my_func(x)
    ! the function return the y values of a half circle with radius = 1
    real :: x
    my_func = sqrt(1. - x**2)
    return
end function
