subroutine initial()

    use Simulation_data
    implicit none

    integer :: i, j
    real, parameter :: small = 1.e-99

    dx = (xmax - xmin)/imax
    dy = (ymax - ymin)/jmax

    ! initialize the x array
    do i = istart-ibuf, iend+ibuf
        x(i) = xmin + (i-0.5)*dx
    enddo
    ! initialize the y array
    do j = jstart-jbuf, jend+jbuf
        y(j) = ymin + (j-0.5)*dy
    enddo

    ! initialize u
    do j = jstart, jend
        do i = istart, iend

           ! (a)
           if ( ((x(i) .ge. 0.1) .and. (x(i) .le. 0.2)) .and. ((y(j) .ge. 0.1) .and. (y(j) .le. 0.2)) ) then
               u(i,j) = 1.0
           else
               u(i,j) = 0.01
           endif

        ! (b)
        !u(i) = max(exp(-1000.0*(x(i)-0.1)**2), small)
        enddo
    enddo

end subroutine initial
