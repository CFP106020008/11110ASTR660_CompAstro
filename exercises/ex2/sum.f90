program summation
    
    implicit none
    integer :: i, N
    integer, parameter :: amin = 1
    integer, parameter :: amax = 100
    real :: result
    double precision, dimension(amax-amin+1) :: series
    
    series(1) = amin
    do i = 2, amax-amin+1
        series(i) = series(i-1) + 1
    end do
    
    result = sum(series)
    
    print *, 'Summing from ', amin, 'to ', amax, 'is ', result

end program summation
