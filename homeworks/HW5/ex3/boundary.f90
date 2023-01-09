subroutine boundary(v)
    !
    ! apply BC on array v
    !
    use Simulation_data
    implicit none
    real, dimension(istart-ibuf:iend+ibuf, jstart-jbuf:jend+jbuf), intent(inout) :: v
    integer :: i, j


    ! apply boundary condition

    ! left and right boundary (period)
    do j = jstart,jend
        do i = 1, ibuf
            v(istart-i, j) = v(iend-i+1, j)
            v(iend+i, j) = v(istart+i-1, j)
        enddo
    enddo

    ! top and down boundary (period)
    do j = 1, jbuf
        do i = istart, iend
            v(i, jstart-j) = v(i, jend-j+1)
            v(i, jend+j) = v(i, jstart+j-1)
        enddo
    enddo

end subroutine boundary
