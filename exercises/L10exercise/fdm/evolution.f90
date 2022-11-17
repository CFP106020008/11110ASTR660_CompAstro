subroutine evolution()
    use Simulation_data
    use IO, only : output
    implicit none

    integer :: n
    real    :: dt, time

    n        = 0
    time     = 0.0

    dt = abs(dx/c)*cfl

    do while(time .le. tend)

        ! reset boundary condition
        call boundary(u)

        ! dump output times with frequency set by io_interval
        if (mod(n,io_interval) .eq. 0) then
            print *, "n =", n ," Time =", time
            call output(n,time)
        endif

        ! update the solution
        call update(time, dt)
        
        n    = n + 1
        time = time + dt
    enddo

end subroutine evolution


subroutine update(time, dt)
    use Simulation_data
    implicit none
    real, intent(in) :: time ,dt
    real :: cp, cm, uxp, uxm
    integer :: i

    uold = u
    cp = max(c, 0.) ! c in positive direction
    cm = min(c, 0.) ! c in negative direction

    do i = istart, iend

        ! TODO: implement the upwind or FTCS methods here

        ! Upwind:
        !uxp = (uold(i) - uold(i-1))/dx ! c in positive direction
        !uxm = (uold(i+1) - uold(i))/dx ! c in negative direction
        !u(i) = uold(i) - dt*(cp*uxp+cm*uxm)

        ! FTCS
        u(i) = uold(i) - c*dt/dx/2.*(uold(i+1) - u(i-1))

    enddo

end subroutine update
